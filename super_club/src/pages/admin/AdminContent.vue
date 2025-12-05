<template>
  <div class="admin-content">
    <!-- 页面头部 -->
    <div class="page-header">
      <div class="header-left">
        <h2>内容管理</h2>
        <p>管理系统中的所有内容</p>
      </div>
      <div class="header-right">
        <button @click="openAddModal" class="btn-primary">
          <span>📝</span>
          添加内容
        </button>
      </div>
    </div>

    <!-- 统计卡片 -->
    <div class="stats-row">
      <div class="stat-card">
        <div class="stat-icon" style="background-color: #3498db;">📄</div>
        <div class="stat-info">
          <div class="stat-value">{{ stats.total }}</div>
          <div class="stat-label">总内容数</div>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon" style="background-color: #27ae60;">✅</div>
        <div class="stat-info">
          <div class="stat-value">{{ stats.published }}</div>
          <div class="stat-label">已发布</div>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon" style="background-color: #f39c12;">📝</div>
        <div class="stat-info">
          <div class="stat-value">{{ stats.draft }}</div>
          <div class="stat-label">草稿</div>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon" style="background-color: #e74c3c;">⭐</div>
        <div class="stat-info">
          <div class="stat-value">{{ stats.featured }}</div>
          <div class="stat-label">精选</div>
        </div>
      </div>
    </div>

    <!-- 筛选和搜索 -->
    <div class="filter-bar">
      <div class="filter-left">
        <input 
          v-model="filters.search" 
          type="text" 
          placeholder="搜索内容标题..." 
          class="search-input"
          @input="debouncedSearch"
        />
        <select v-model="filters.type" @change="loadContent" class="filter-select">
          <option value="">全部类型</option>
          <option value="article">文章</option>
          <option value="video">视频</option>
          <option value="course">课程</option>
        </select>
        <select v-model="filters.department" @change="loadContent" class="filter-select">
          <option value="">全部分类</option>
          <option value="技术">技术</option>
          <option value="产品">产品</option>
          <option value="设计">设计</option>
          <option value="运营">运营</option>
          <option value="创业">创业</option>
        </select>
        <select v-model="filters.isPublished" @change="loadContent" class="filter-select">
          <option value="">全部状态</option>
          <option value="true">已发布</option>
          <option value="false">草稿</option>
        </select>
      </div>
      <div class="filter-right">
        <button @click="loadContent" class="btn-secondary">
          🔄 刷新
        </button>
      </div>
    </div>

    <!-- 内容列表 -->
    <div class="content-table-container">
      <div v-if="loading" class="loading-state">
        <div class="spinner"></div>
        <p>加载中...</p>
      </div>
      
      <div v-else-if="contentList.length === 0" class="empty-state">
        <div class="empty-icon">📭</div>
        <p>暂无内容数据</p>
        <button @click="openAddModal" class="btn-primary">创建第一篇内容</button>
      </div>
      
      <table v-else class="content-table">
        <thead>
          <tr>
            <th>内容信息</th>
            <th>类型</th>
            <th>分类</th>
            <th>状态</th>
            <th>数据</th>
            <th>创建时间</th>
            <th>操作</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="content in contentList" :key="content.id">
            <td class="content-info-cell">
              <div class="content-info">
                <img 
                  v-if="content.coverImage" 
                  :src="content.coverImage" 
                  :alt="content.title"
                  class="content-cover"
                />
                <div v-else class="content-cover-placeholder">📄</div>
                <div class="content-details">
                  <div class="content-title">{{ content.title }}</div>
                  <div class="content-author">
                    作者：{{ content.author?.name || '未知' }}
                  </div>
                </div>
              </div>
            </td>
            <td>
              <span class="type-badge" :class="content.type">
                {{ getTypeLabel(content.type) }}
              </span>
            </td>
            <td>{{ content.department || '-' }}</td>
            <td>
              <span class="status-badge" :class="content.isPublished ? 'published' : 'draft'">
                {{ content.isPublished ? '已发布' : '草稿' }}
              </span>
              <span v-if="content.isFeatured" class="featured-badge">⭐ 精选</span>
            </td>
            <td class="stats-cell">
              <div class="content-stats">
                <span title="浏览量">👁 {{ content.viewCount || 0 }}</span>
                <span title="点赞数">❤️ {{ content.likeCount || 0 }}</span>
                <span title="评论数">💬 {{ content.commentCount || 0 }}</span>
              </div>
            </td>
            <td>{{ formatDate(content.createdAt) }}</td>
            <td class="actions-cell">
              <div class="action-buttons">
                <button @click="viewContentDetail(content)" class="action-btn view" title="查看详情">
                  👁
                </button>
                <button @click="editContent(content)" class="action-btn edit" title="编辑">
                  ✏️
                </button>
                <button 
                  @click="togglePublish(content)" 
                  class="action-btn" 
                  :class="content.isPublished ? 'unpublish' : 'publish'"
                  :title="content.isPublished ? '取消发布' : '发布'"
                >
                  {{ content.isPublished ? '📤' : '📥' }}
                </button>
                <button 
                  @click="toggleFeatured(content)" 
                  class="action-btn featured"
                  :class="{ active: content.isFeatured }"
                  title="切换精选"
                >
                  ⭐
                </button>
                <button @click="confirmDelete(content)" class="action-btn delete" title="删除">
                  🗑️
                </button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- 分页 -->
    <div v-if="pagination.total > pagination.limit" class="pagination">
      <button 
        @click="changePage(pagination.page - 1)" 
        :disabled="pagination.page <= 1"
        class="page-btn"
      >
        上一页
      </button>
      <span class="page-info">
        第 {{ pagination.page }} / {{ Math.ceil(pagination.total / pagination.limit) }} 页
        （共 {{ pagination.total }} 条）
      </span>
      <button 
        @click="changePage(pagination.page + 1)" 
        :disabled="pagination.page >= Math.ceil(pagination.total / pagination.limit)"
        class="page-btn"
      >
        下一页
      </button>
    </div>

    <!-- 添加/编辑内容弹窗 -->
    <div v-if="showModal" class="modal-overlay" @click="closeModal">
      <div class="modal-content large" @click.stop>
        <div class="modal-header">
          <h3>{{ editingContent ? '编辑内容' : '添加内容' }}</h3>
          <button @click="closeModal" class="close-btn">✕</button>
        </div>
        <div class="modal-body">
          <form @submit.prevent="saveContent" class="content-form">
            <div class="form-row">
              <div class="form-group">
                <label>标题 <span class="required">*</span></label>
                <input 
                  v-model="formData.title" 
                  type="text" 
                  placeholder="请输入内容标题"
                  required
                />
              </div>
            </div>
            
            <div class="form-row two-columns">
              <div class="form-group">
                <label>类型</label>
                <select v-model="formData.type">
                  <option value="article">文章</option>
                  <option value="video">视频</option>
                  <option value="course">课程</option>
                </select>
              </div>
              <div class="form-group">
                <label>分类</label>
                <select v-model="formData.department">
                  <option value="">请选择分类</option>
                  <option value="技术">技术</option>
                  <option value="产品">产品</option>
                  <option value="设计">设计</option>
                  <option value="运营">运营</option>
                  <option value="创业">创业</option>
                </select>
              </div>
            </div>
            
            <div class="form-group">
              <label>封面图片URL</label>
              <input 
                v-model="formData.coverImage" 
                type="url" 
                placeholder="请输入封面图片URL"
              />
            </div>
            
            <div class="form-group">
              <label>摘要</label>
              <textarea 
                v-model="formData.excerpt" 
                placeholder="请输入内容摘要（可选）"
                rows="2"
              ></textarea>
            </div>
            
            <div class="form-group">
              <label>正文内容 <span class="required">*</span></label>
              <textarea 
                v-model="formData.content" 
                placeholder="请输入正文内容（支持Markdown格式）"
                rows="10"
                required
              ></textarea>
            </div>
            
            <div class="form-group">
              <label>标签（用逗号分隔）</label>
              <input 
                v-model="formData.tagsInput" 
                type="text" 
                placeholder="例如：Vue, JavaScript, 前端"
              />
            </div>
            
            <div class="form-row two-columns">
              <div class="form-group">
                <label>阅读时间（分钟）</label>
                <input 
                  v-model.number="formData.readingTime" 
                  type="number" 
                  min="1"
                  placeholder="5"
                />
              </div>
              <div class="form-group checkbox-group">
                <label class="checkbox-label">
                  <input type="checkbox" v-model="formData.isPublished" />
                  <span>立即发布</span>
                </label>
                <label class="checkbox-label">
                  <input type="checkbox" v-model="formData.isFeatured" />
                  <span>设为精选</span>
                </label>
              </div>
            </div>
            
            <div class="form-actions">
              <button type="button" @click="closeModal" class="btn-secondary">取消</button>
              <button type="submit" class="btn-primary" :disabled="saving">
                {{ saving ? '保存中...' : (editingContent ? '保存修改' : '创建内容') }}
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>

    <!-- 内容详情弹窗（使用可复用组件） -->
    <ContentDetailModal
      :visible="showDetailModal"
      :content="detailContent"
      :loading="loadingDetail"
      :is-admin="true"
      @close="closeDetailModal"
      @edit="editFromDetail"
      @toggle-publish="togglePublishFromDetail"
    />

    <!-- 删除确认弹窗 -->
    <div v-if="showDeleteConfirm" class="modal-overlay" @click="showDeleteConfirm = false">
      <div class="modal-content small" @click.stop>
        <div class="modal-header">
          <h3>确认删除</h3>
          <button @click="showDeleteConfirm = false" class="close-btn">✕</button>
        </div>
        <div class="modal-body">
          <p class="confirm-text">
            确定要删除内容 <strong>"{{ deletingContent?.title }}"</strong> 吗？
          </p>
          <p class="warning-text">此操作不可恢复！</p>
        </div>
        <div class="modal-footer">
          <button @click="showDeleteConfirm = false" class="btn-secondary">取消</button>
          <button @click="deleteContent" class="btn-danger" :disabled="deleting">
            {{ deleting ? '删除中...' : '确认删除' }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, reactive, onMounted } from 'vue'
import { API_CONFIG } from '@/config/api'
import { adminAPI } from '../../api/admin.js'
import ContentDetailModal from '../../components/ContentDetailModal.vue'

export default {
  name: 'AdminContent',
  components: {
    ContentDetailModal
  },
  setup() {
    const loading = ref(false)
    const saving = ref(false)
    const deleting = ref(false)
    const loadingDetail = ref(false)
    const showModal = ref(false)
    const showDeleteConfirm = ref(false)
    const showDetailModal = ref(false)
    const editingContent = ref(null)
    const deletingContent = ref(null)
    const detailContent = ref(null)
    const contentList = ref([])
    
    const stats = ref({
      total: 0,
      published: 0,
      draft: 0,
      featured: 0
    })
    
    const pagination = ref({
      page: 1,
      limit: 10,
      total: 0
    })
    
    const filters = reactive({
      search: '',
      type: '',
      department: '',
      isPublished: ''
    })
    
    const formData = reactive({
      title: '',
      type: 'article',
      department: '',
      coverImage: '',
      excerpt: '',
      content: '',
      tagsInput: '',
      readingTime: 5,
      isPublished: false,
      isFeatured: false
    })
    
    // 防抖搜索
    let searchTimeout = null
    const debouncedSearch = () => {
      if (searchTimeout) clearTimeout(searchTimeout)
      searchTimeout = setTimeout(() => {
        pagination.value.page = 1
        loadContent()
      }, 300)
    }
    
    // 加载内容列表
    const loadContent = async () => {
      loading.value = true
      try {
        const token = localStorage.getItem('admin_token')
        const params = new URLSearchParams({
          page: pagination.value.page,
          limit: pagination.value.limit
        })
        
        if (filters.search) params.append('search', filters.search)
        if (filters.type) params.append('type', filters.type)
        if (filters.department) params.append('department', filters.department)
        if (filters.isPublished !== '') params.append('is_published', filters.isPublished)
        
        const response = await fetch(`${API_CONFIG.baseURL}/admin/content?${params}`, {
          headers: {
            'Authorization': `Bearer ${token}`
          }
        })
        
        const data = await response.json()
        
        if (data.success) {
          contentList.value = data.data?.items || []
          if (data.data?.pagination) {
            pagination.value.total = data.data.pagination.total
          }
        }
      } catch (error) {
        console.error('加载内容失败:', error)
      } finally {
        loading.value = false
      }
    }
    
    // 加载统计数据
    const loadStats = async () => {
      try {
        const token = localStorage.getItem('admin_token')
        const response = await fetch(`${API_CONFIG.baseURL}/admin/content/stats/overview`, {
          headers: {
            'Authorization': `Bearer ${token}`
          }
        })
        
        const data = await response.json()
        
        if (data.success) {
          stats.value = {
            total: data.data.total || 0,
            published: data.data.published || 0,
            draft: data.data.draft || 0,
            featured: data.data.featured || 0
          }
        }
      } catch (error) {
        console.error('加载统计数据失败:', error)
      }
    }
    
    // 打开添加弹窗
    const openAddModal = () => {
      editingContent.value = null
      resetForm()
      showModal.value = true
    }
    
    // 编辑内容
    const editContent = (content) => {
      editingContent.value = content
      formData.title = content.title || ''
      formData.type = content.type || 'article'
      formData.department = content.department || ''
      formData.coverImage = content.coverImage || ''
      formData.excerpt = content.excerpt || ''
      formData.content = content.content || ''
      formData.tagsInput = (content.tags || []).join(', ')
      formData.readingTime = content.readingTime || 5
      formData.isPublished = content.isPublished || false
      formData.isFeatured = content.isFeatured || false
      showModal.value = true
    }
    
    // 重置表单
    const resetForm = () => {
      formData.title = ''
      formData.type = 'article'
      formData.department = ''
      formData.coverImage = ''
      formData.excerpt = ''
      formData.content = ''
      formData.tagsInput = ''
      formData.readingTime = 5
      formData.isPublished = false
      formData.isFeatured = false
    }
    
    // 关闭弹窗
    const closeModal = () => {
      showModal.value = false
      editingContent.value = null
      resetForm()
    }
    
    // 保存内容
    const saveContent = async () => {
      saving.value = true
      try {
        const token = localStorage.getItem('admin_token')
        const tags = formData.tagsInput
          .split(',')
          .map(t => t.trim())
          .filter(t => t)
        
        const payload = {
          title: formData.title,
          type: formData.type,
          department: formData.department,
          coverImage: formData.coverImage,
          excerpt: formData.excerpt,
          content: formData.content,
          tags: tags,
          readingTime: formData.readingTime,
          isPublished: formData.isPublished,
          isFeatured: formData.isFeatured
        }
        
        const url = editingContent.value 
          ? `${API_CONFIG.baseURL}/admin/content/${editingContent.value.id}`
          : `${API_CONFIG.baseURL}/admin/content`
        
        const response = await fetch(url, {
          method: editingContent.value ? 'PUT' : 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
          },
          body: JSON.stringify(payload)
        })
        
        const data = await response.json()
        
        if (data.success) {
          closeModal()
          loadContent()
          loadStats()
        } else {
          alert(data.message || '保存失败')
        }
      } catch (error) {
        console.error('保存内容失败:', error)
        alert('保存失败，请重试')
      } finally {
        saving.value = false
      }
    }
    
    // 切换发布状态
    const togglePublish = async (content) => {
      try {
        const token = localStorage.getItem('admin_token')
        const newStatus = !content.isPublished
        
        const response = await fetch(
          `${API_CONFIG.baseURL}/admin/content/${content.id}/publish?is_published=${newStatus}`,
          {
            method: 'PUT',
            headers: {
              'Authorization': `Bearer ${token}`
            }
          }
        )
        
        const data = await response.json()
        
        if (data.success) {
          content.isPublished = newStatus
          loadStats()
        }
      } catch (error) {
        console.error('切换发布状态失败:', error)
      }
    }
    
    // 切换精选状态
    const toggleFeatured = async (content) => {
      try {
        const token = localStorage.getItem('admin_token')
        const newStatus = !content.isFeatured
        
        const response = await fetch(
          `${API_CONFIG.baseURL}/admin/content/${content.id}/featured?is_featured=${newStatus}`,
          {
            method: 'PUT',
            headers: {
              'Authorization': `Bearer ${token}`
            }
          }
        )
        
        const data = await response.json()
        
        if (data.success) {
          content.isFeatured = newStatus
          loadStats()
        }
      } catch (error) {
        console.error('切换精选状态失败:', error)
      }
    }
    
    // 确认删除
    const confirmDelete = (content) => {
      deletingContent.value = content
      showDeleteConfirm.value = true
    }
    
    // 删除内容
    const deleteContent = async () => {
      if (!deletingContent.value) return
      
      deleting.value = true
      try {
        const token = localStorage.getItem('admin_token')
        
        const response = await fetch(
          `${API_CONFIG.baseURL}/admin/content/${deletingContent.value.id}`,
          {
            method: 'DELETE',
            headers: {
              'Authorization': `Bearer ${token}`
            }
          }
        )
        
        const data = await response.json()
        
        if (data.success) {
          showDeleteConfirm.value = false
          deletingContent.value = null
          loadContent()
          loadStats()
        } else {
          alert(data.message || '删除失败')
        }
      } catch (error) {
        console.error('删除内容失败:', error)
        alert('删除失败，请重试')
      } finally {
        deleting.value = false
      }
    }
    
    // 分页
    const changePage = (page) => {
      pagination.value.page = page
      loadContent()
    }
    
    // 格式化日期
    const formatDate = (dateStr) => {
      if (!dateStr) return '-'
      const date = new Date(dateStr)
      return date.toLocaleDateString('zh-CN', {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit'
      })
    }
    
    // 获取类型标签
    const getTypeLabel = (type) => {
      const labels = {
        article: '文章',
        video: '视频',
        course: '课程'
      }
      return labels[type] || type
    }
    
    // 查看内容详情
    const viewContentDetail = async (content) => {
      showDetailModal.value = true
      loadingDetail.value = true
      detailContent.value = null
      
      try {
        const token = localStorage.getItem('admin_token')
        const response = await fetch(`${API_CONFIG.baseURL}/admin/content/${content.id}`, {
          headers: {
            'Authorization': `Bearer ${token}`
          }
        })
        
        const data = await response.json()
        
        if (data.success) {
          detailContent.value = data.data
        } else {
          alert('加载详情失败')
          showDetailModal.value = false
        }
      } catch (error) {
        console.error('加载内容详情失败:', error)
        alert('加载详情失败，请重试')
        showDetailModal.value = false
      } finally {
        loadingDetail.value = false
      }
    }
    
    // 关闭详情弹窗
    const closeDetailModal = () => {
      showDetailModal.value = false
      detailContent.value = null
    }
    
    // 从详情页编辑
    const editFromDetail = (content) => {
      closeDetailModal()
      editContent(content || detailContent.value)
    }
    
    // 从详情页切换发布状态
    const togglePublishFromDetail = async (content) => {
      const targetContent = content || detailContent.value
      if (!targetContent) return
      
      try {
        const token = localStorage.getItem('admin_token')
        const newStatus = !targetContent.isPublished
        
        const response = await fetch(
          `${API_CONFIG.baseURL}/admin/content/${targetContent.id}/publish?is_published=${newStatus}`,
          {
            method: 'PUT',
            headers: {
              'Authorization': `Bearer ${token}`
            }
          }
        )
        
        const data = await response.json()
        
        if (data.success) {
          // 更新详情内容状态
          if (detailContent.value && detailContent.value.id === targetContent.id) {
            detailContent.value.isPublished = newStatus
          }
          // 更新列表中的状态
          const item = contentList.value.find(c => c.id === targetContent.id)
          if (item) {
            item.isPublished = newStatus
          }
          loadStats()
        }
      } catch (error) {
        console.error('切换发布状态失败:', error)
      }
    }
    
    // 格式化日期时间
    const formatDateTime = (dateStr) => {
      if (!dateStr) return '-'
      const date = new Date(dateStr)
      return date.toLocaleString('zh-CN', {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit'
      })
    }
    
    // 格式化内容（简单的Markdown转HTML）
    const formatContent = (content) => {
      if (!content) return ''
      // 简单的Markdown处理
      let html = content
        // 转义HTML
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        // 标题
        .replace(/^### (.+)$/gm, '<h4>$1</h4>')
        .replace(/^## (.+)$/gm, '<h3>$1</h3>')
        .replace(/^# (.+)$/gm, '<h2>$1</h2>')
        // 粗体和斜体
        .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
        .replace(/\*(.+?)\*/g, '<em>$1</em>')
        // 代码块
        .replace(/`(.+?)`/g, '<code>$1</code>')
        // 换行
        .replace(/\n/g, '<br>')
      return html
    }
    
    onMounted(() => {
      loadContent()
      loadStats()
    })
    
    return {
      loading,
      saving,
      deleting,
      loadingDetail,
      showModal,
      showDeleteConfirm,
      showDetailModal,
      editingContent,
      deletingContent,
      detailContent,
      contentList,
      stats,
      pagination,
      filters,
      formData,
      debouncedSearch,
      loadContent,
      openAddModal,
      editContent,
      closeModal,
      saveContent,
      togglePublish,
      toggleFeatured,
      confirmDelete,
      deleteContent,
      changePage,
      formatDate,
      formatDateTime,
      getTypeLabel,
      viewContentDetail,
      closeDetailModal,
      editFromDetail,
      togglePublishFromDetail,
      formatContent
    }
  }
}
</script>

<style scoped>
.admin-content {
  max-width: 1400px;
  margin: 0 auto;
}

/* 页面头部 */
.page-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 24px;
}

.header-left h2 {
  margin: 0 0 8px 0;
  font-size: 28px;
  font-weight: 600;
  color: #2c3e50;
}

.header-left p {
  margin: 0;
  color: #666;
  font-size: 16px;
}

/* 统计卡片 */
.stats-row {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 16px;
  margin-bottom: 24px;
}

.stat-card {
  background: white;
  border-radius: 12px;
  padding: 20px;
  display: flex;
  align-items: center;
  gap: 16px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.stat-icon {
  width: 48px;
  height: 48px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
  color: white;
}

.stat-value {
  font-size: 24px;
  font-weight: 700;
  color: #2c3e50;
}

.stat-label {
  font-size: 14px;
  color: #666;
}

/* 筛选栏 */
.filter-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
  gap: 16px;
  flex-wrap: wrap;
}

.filter-left {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
}

.search-input {
  padding: 10px 16px;
  border: 1px solid #ddd;
  border-radius: 8px;
  font-size: 14px;
  width: 240px;
}

.filter-select {
  padding: 10px 16px;
  border: 1px solid #ddd;
  border-radius: 8px;
  font-size: 14px;
  background: white;
  cursor: pointer;
}

/* 按钮样式 */
.btn-primary {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  padding: 12px 20px;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 8px;
  transition: transform 0.2s, box-shadow 0.2s;
}

.btn-primary:hover:not(:disabled) {
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
}

.btn-primary:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.btn-secondary {
  background: #f0f0f0;
  color: #333;
  border: none;
  padding: 10px 16px;
  border-radius: 8px;
  font-size: 14px;
  cursor: pointer;
  transition: background-color 0.2s;
}

.btn-secondary:hover {
  background: #e0e0e0;
}

.btn-danger {
  background: #e74c3c;
  color: white;
  border: none;
  padding: 10px 16px;
  border-radius: 8px;
  font-size: 14px;
  cursor: pointer;
  transition: background-color 0.2s;
}

.btn-danger:hover:not(:disabled) {
  background: #c0392b;
}

.btn-danger:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

/* 内容表格 */
.content-table-container {
  background: white;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  overflow: hidden;
}

.content-table {
  width: 100%;
  border-collapse: collapse;
}

.content-table th,
.content-table td {
  padding: 16px;
  text-align: left;
  border-bottom: 1px solid #f0f0f0;
}

.content-table th {
  background: #f8f9fa;
  font-weight: 600;
  color: #2c3e50;
  font-size: 14px;
}

.content-table tr:hover {
  background-color: #f8f9fa;
}

/* 内容信息单元格 */
.content-info-cell {
  min-width: 280px;
}

.content-info {
  display: flex;
  align-items: center;
  gap: 12px;
}

.content-cover {
  width: 60px;
  height: 40px;
  border-radius: 6px;
  object-fit: cover;
}

.content-cover-placeholder {
  width: 60px;
  height: 40px;
  border-radius: 6px;
  background: #f0f0f0;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
}

.content-title {
  font-weight: 500;
  color: #2c3e50;
  margin-bottom: 4px;
  max-width: 200px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.content-author {
  font-size: 12px;
  color: #666;
}

/* 徽章样式 */
.type-badge {
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 500;
}

.type-badge.article {
  background: #e3f2fd;
  color: #1976d2;
}

.type-badge.video {
  background: #fce4ec;
  color: #c2185b;
}

.type-badge.course {
  background: #fff3e0;
  color: #f57c00;
}

.status-badge {
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 500;
}

.status-badge.published {
  background: #d5f4e6;
  color: #27ae60;
}

.status-badge.draft {
  background: #fef9e7;
  color: #f39c12;
}

.featured-badge {
  margin-left: 8px;
  font-size: 12px;
  color: #f39c12;
}

/* 统计数据单元格 */
.stats-cell {
  min-width: 140px;
}

.content-stats {
  display: flex;
  gap: 12px;
  font-size: 12px;
  color: #666;
}

/* 操作按钮 */
.actions-cell {
  min-width: 140px;
}

.action-buttons {
  display: flex;
  gap: 8px;
}

.action-btn {
  width: 32px;
  height: 32px;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 14px;
  transition: all 0.2s;
}

.action-btn.edit {
  background: #e3f2fd;
}

.action-btn.edit:hover {
  background: #bbdefb;
}

.action-btn.publish {
  background: #d5f4e6;
}

.action-btn.publish:hover {
  background: #a8e6cf;
}

.action-btn.unpublish {
  background: #fef9e7;
}

.action-btn.unpublish:hover {
  background: #ffeaa7;
}

.action-btn.featured {
  background: #f0f0f0;
}

.action-btn.featured.active {
  background: #fff3e0;
}

.action-btn.featured:hover {
  background: #ffeaa7;
}

.action-btn.delete {
  background: #fdf2f2;
}

.action-btn.delete:hover {
  background: #fecaca;
}

/* 加载和空状态 */
.loading-state,
.empty-state {
  padding: 60px;
  text-align: center;
  color: #666;
}

.spinner {
  width: 40px;
  height: 40px;
  border: 3px solid #f0f0f0;
  border-top-color: #667eea;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 0 auto 16px;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.empty-icon {
  font-size: 48px;
  margin-bottom: 16px;
}

/* 分页 */
.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 16px;
  margin-top: 24px;
  padding: 16px;
}

.page-btn {
  padding: 8px 16px;
  border: 1px solid #ddd;
  border-radius: 6px;
  background: white;
  cursor: pointer;
  transition: all 0.2s;
}

.page-btn:hover:not(:disabled) {
  background: #f0f0f0;
  border-color: #bbb;
}

.page-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.page-info {
  color: #666;
  font-size: 14px;
}

/* 弹窗样式 */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  padding: 20px;
}

.modal-content {
  background: white;
  border-radius: 12px;
  max-height: 90vh;
  overflow-y: auto;
}

.modal-content.large {
  width: 100%;
  max-width: 700px;
}

.modal-content.small {
  width: 100%;
  max-width: 400px;
}


.modal-header {
  padding: 24px 24px 0 24px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid #f0f0f0;
  padding-bottom: 16px;
}

.modal-header h3 {
  margin: 0;
  font-size: 20px;
  font-weight: 600;
  color: #2c3e50;
}

.close-btn {
  background: none;
  border: none;
  font-size: 20px;
  cursor: pointer;
  color: #666;
  padding: 4px;
  border-radius: 4px;
  transition: background-color 0.2s;
}

.close-btn:hover {
  background-color: #f0f0f0;
}

.modal-body {
  padding: 24px;
}

.modal-footer {
  padding: 16px 24px 24px;
  display: flex;
  justify-content: flex-end;
  gap: 12px;
}

/* 表单样式 */
.content-form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.form-row {
  display: flex;
  gap: 16px;
}

.form-row.two-columns {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
  flex: 1;
}

.form-group label {
  font-weight: 500;
  color: #333;
  font-size: 14px;
}

.required {
  color: #e74c3c;
}

.form-group input,
.form-group select,
.form-group textarea {
  padding: 12px 16px;
  border: 1px solid #ddd;
  border-radius: 8px;
  font-size: 14px;
  transition: border-color 0.2s;
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
  outline: none;
  border-color: #667eea;
  box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

.form-group textarea {
  resize: vertical;
  font-family: inherit;
}

.checkbox-group {
  flex-direction: row;
  align-items: center;
  gap: 16px;
  padding-top: 28px;
}

.checkbox-label {
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
  font-weight: normal;
}

.checkbox-label input[type="checkbox"] {
  width: 18px;
  height: 18px;
  cursor: pointer;
}

.form-actions {
  display: flex;
  justify-content: flex-end;
  gap: 12px;
  margin-top: 12px;
  padding-top: 20px;
  border-top: 1px solid #f0f0f0;
}

/* 确认弹窗 */
.confirm-text {
  margin: 0 0 12px 0;
  color: #333;
  font-size: 16px;
}

.warning-text {
  margin: 0;
  color: #e74c3c;
  font-size: 14px;
}

/* 查看按钮样式 */
.action-btn.view {
  background: #e8f5e9;
}

.action-btn.view:hover {
  background: #c8e6c9;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .page-header {
    flex-direction: column;
    gap: 16px;
  }
  
  .filter-bar {
    flex-direction: column;
    align-items: stretch;
  }
  
  .filter-left {
    flex-direction: column;
  }
  
  .search-input {
    width: 100%;
  }
  
  .stats-row {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .content-table-container {
    overflow-x: auto;
  }
  
  .form-row.two-columns {
    grid-template-columns: 1fr;
  }
  
  .checkbox-group {
    flex-direction: column;
    align-items: flex-start;
    padding-top: 0;
  }
}
</style>
