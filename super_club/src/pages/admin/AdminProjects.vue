<template>
  <div class="admin-projects">
    <!-- 页面头部 -->
    <div class="page-header">
      <div class="header-left">
        <h2>项目管理</h2>
        <p>管理系统中的所有项目</p>
      </div>
      <div class="header-right">
        <button @click="showAddModal = true" class="btn-primary">
          <span>🚀</span>
          添加项目
        </button>
      </div>
    </div>
    
    <!-- 筛选和搜索 -->
    <div class="filters-section">
      <div class="filters">
        <div class="filter-group">
          <label>项目状态</label>
          <select v-model="filters.status" @change="loadProjects">
            <option value="">全部状态</option>
            <option value="active">进行中</option>
            <option value="recruiting">招募中</option>
            <option value="paused">暂停</option>
            <option value="completed">已完成</option>
          </select>
        </div>
        
        <div class="filter-group">
          <label>项目分类</label>
          <select v-model="filters.category" @change="loadProjects">
            <option value="">全部分类</option>
            <option value="tech">技术开发</option>
            <option value="design">设计创意</option>
            <option value="business">商业项目</option>
            <option value="education">教育培训</option>
            <option value="other">其他</option>
          </select>
        </div>
        
        <div class="filter-group">
          <label>是否精选</label>
          <select v-model="filters.featured" @change="loadProjects">
            <option value="">全部</option>
            <option value="true">精选项目</option>
            <option value="false">普通项目</option>
          </select>
        </div>
        
        <div class="filter-group">
          <label>搜索项目</label>
          <input
            v-model="filters.search"
            @input="debounceSearch"
            type="text"
            placeholder="搜索项目名称、描述..."
            class="search-input"
          />
        </div>
      </div>
    </div>
    
    <!-- 项目列表 -->
    <div class="projects-container">
      <div v-if="loading" class="loading-state">
        <div class="loading-spinner"></div>
        <p>加载中...</p>
      </div>
      
      <div v-else-if="projects.length === 0" class="empty-state">
        <div class="empty-icon">🚀</div>
        <h3>暂无项目数据</h3>
        <p>还没有项目发布，或者当前筛选条件下没有匹配的项目</p>
      </div>
      
      <div v-else class="projects-grid">
        <div v-for="project in projects" :key="project.id" class="project-card">
          <!-- 项目头部 -->
          <div class="project-header">
            <div class="project-logo">
              <img v-if="project.logo" :src="project.logo" :alt="project.name" />
              <div v-else class="logo-placeholder">
                {{ project.name[0] }}
              </div>
            </div>
            <div class="project-info">
              <h3 class="project-name">{{ project.name }}</h3>
              <div class="project-meta">
                <span class="project-owner">{{ project.ownerName }}</span>
                <span class="project-date">{{ formatDate(project.createdAt) }}</span>
              </div>
            </div>
            <div class="project-actions">
              <button 
                @click="toggleFeatured(project)" 
                class="btn-feature"
                :class="{ active: project.isFeatured }"
                :title="project.isFeatured ? '取消精选' : '设为精选'"
              >
                ⭐
              </button>
            </div>
          </div>
          
          <!-- 项目内容 -->
          <div class="project-content">
            <p class="project-description">{{ project.description }}</p>
            
            <div class="project-tags" v-if="project.tags && project.tags.length">
              <span 
                v-for="tag in project.tags.slice(0, 3)" 
                :key="tag" 
                class="tag"
              >
                {{ tag }}
              </span>
              <span v-if="project.tags.length > 3" class="tag-more">
                +{{ project.tags.length - 3 }}
              </span>
            </div>
            
            <div class="project-stats">
              <div class="stat-item">
                <span class="stat-icon">👁️</span>
                <span class="stat-value">{{ project.viewCount }}</span>
              </div>
              <div class="stat-item">
                <span class="stat-icon">❤️</span>
                <span class="stat-value">{{ project.interestCount }}</span>
              </div>
              <div class="stat-item">
                <span class="stat-icon">🤝</span>
                <span class="stat-value">{{ project.collaborationCount }}</span>
              </div>
            </div>
          </div>
          
          <!-- 项目底部 -->
          <div class="project-footer">
            <div class="project-status">
              <span 
                class="status-badge" 
                :class="getStatusClass(project.status)"
              >
                {{ getStatusText(project.status) }}
              </span>
              <span 
                class="category-badge"
                :class="getCategoryClass(project.category)"
              >
                {{ getCategoryText(project.category) }}
              </span>
            </div>
            
            <div class="project-controls">
              <button 
                @click="editProject(project)" 
                class="btn-edit"
                title="编辑项目"
              >
                ✏️
              </button>
              <button 
                @click="toggleProjectStatus(project)" 
                class="btn-toggle"
                :title="getToggleTitle(project.status)"
              >
                {{ getToggleIcon(project.status) }}
              </button>
              <button 
                @click="deleteProject(project)" 
                class="btn-delete"
                title="删除项目"
              >
                🗑️
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
    
    <!-- 分页 -->
    <div class="pagination" v-if="totalPages > 1">
      <button 
        @click="changePage(currentPage - 1)" 
        :disabled="currentPage === 1"
        class="page-btn"
      >
        上一页
      </button>
      
      <div class="page-numbers">
        <button
          v-for="page in visiblePages"
          :key="page"
          @click="changePage(page)"
          class="page-btn"
          :class="{ active: page === currentPage }"
        >
          {{ page }}
        </button>
      </div>
      
      <button 
        @click="changePage(currentPage + 1)" 
        :disabled="currentPage === totalPages"
        class="page-btn"
      >
        下一页
      </button>
    </div>
    
    <!-- 添加/编辑项目模态框 -->
    <div v-if="showAddModal || showEditModal" class="modal-overlay" @click="closeModals">
      <div class="modal-content" @click.stop>
        <div class="modal-header">
          <h3>{{ showAddModal ? '添加项目' : '编辑项目' }}</h3>
          <button @click="closeModals" class="close-btn">✕</button>
        </div>
        
        <form @submit.prevent="saveProject" class="project-form">
          <div class="form-row">
            <div class="form-group">
              <label>项目名称 *</label>
              <input 
                v-model="projectForm.name" 
                type="text" 
                required 
                placeholder="请输入项目名称"
              />
            </div>
            <div class="form-group">
              <label>项目类型</label>
              <input 
                v-model="projectForm.type" 
                type="text" 
                placeholder="请输入项目类型"
              />
            </div>
          </div>
          
          <div class="form-group">
            <label>项目描述 *</label>
            <textarea 
              v-model="projectForm.description" 
              rows="3" 
              required
              placeholder="请输入项目简短描述"
            ></textarea>
          </div>
          
          <div class="form-group">
            <label>详细描述</label>
            <textarea 
              v-model="projectForm.fullDescription" 
              rows="5" 
              placeholder="请输入项目详细描述"
            ></textarea>
          </div>
          
          <div class="form-row">
            <div class="form-group">
              <label>项目分类</label>
              <select v-model="projectForm.category">
                <option value="">请选择分类</option>
                <option value="tech">技术开发</option>
                <option value="design">设计创意</option>
                <option value="business">商业项目</option>
                <option value="education">教育培训</option>
                <option value="other">其他</option>
              </select>
            </div>
            <div class="form-group">
              <label>项目状态</label>
              <select v-model="projectForm.status">
                <option value="active">进行中</option>
                <option value="recruiting">招募中</option>
                <option value="paused">暂停</option>
                <option value="completed">已完成</option>
              </select>
            </div>
          </div>
          
          <div class="form-row">
            <div class="form-group">
              <label>项目标签</label>
              <input 
                v-model="tagsInput" 
                type="text" 
                placeholder="请输入标签，用逗号分隔"
              />
            </div>
            <div class="form-group">
              <label>是否精选</label>
              <div class="checkbox-group">
                <input 
                  v-model="projectForm.isFeatured" 
                  type="checkbox" 
                  id="featured"
                />
                <label for="featured">设为精选项目</label>
              </div>
            </div>
          </div>
          
          <div class="form-actions">
            <button type="button" @click="closeModals" class="btn-cancel">
              取消
            </button>
            <button type="submit" class="btn-save" :disabled="saving">
              {{ saving ? '保存中...' : '保存' }}
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted, watch } from 'vue'

export default {
  name: 'AdminProjects',
  setup() {
    const loading = ref(false)
    const saving = ref(false)
    const projects = ref([])
    const currentPage = ref(1)
    const pageSize = ref(12)
    const totalProjects = ref(0)
    const showAddModal = ref(false)
    const showEditModal = ref(false)
    const editingProject = ref(null)
    const tagsInput = ref('')
    
    // 筛选条件
    const filters = ref({
      status: '',
      category: '',
      featured: '',
      search: ''
    })
    
    // 项目表单
    const projectForm = ref({
      name: '',
      type: '',
      description: '',
      fullDescription: '',
      category: '',
      status: 'active',
      tags: [],
      isFeatured: false
    })
    
    // 计算属性
    const totalPages = computed(() => {
      return Math.ceil(totalProjects.value / pageSize.value)
    })
    
    const visiblePages = computed(() => {
      const pages = []
      const start = Math.max(1, currentPage.value - 2)
      const end = Math.min(totalPages.value, currentPage.value + 2)
      
      for (let i = start; i <= end; i++) {
        pages.push(i)
      }
      return pages
    })
    
    // 监听标签输入
    watch(tagsInput, (newValue) => {
      projectForm.value.tags = newValue.split(',').map(tag => tag.trim()).filter(tag => tag)
    })
    
    // 模拟项目数据
    const mockProjects = [
      {
        id: '1',
        name: 'AI智能助手',
        type: '人工智能',
        description: '基于GPT的智能对话助手，支持多种场景应用',
        fullDescription: '这是一个基于最新GPT技术的智能对话助手项目...',
        category: 'tech',
        status: 'active',
        tags: ['AI', 'GPT', '对话系统', '自然语言处理'],
        isFeatured: true,
        logo: null,
        ownerName: '张三',
        viewCount: 1250,
        interestCount: 89,
        collaborationCount: 12,
        createdAt: '2024-01-15T10:30:00Z',
        updatedAt: '2024-12-01T15:20:00Z'
      },
      {
        id: '2',
        name: '在线教育平台',
        type: '教育科技',
        description: '面向K12学生的在线学习平台，提供个性化学习体验',
        fullDescription: '这是一个专为K12学生设计的在线教育平台...',
        category: 'education',
        status: 'recruiting',
        tags: ['教育', '在线学习', 'K12', '个性化'],
        isFeatured: false,
        logo: null,
        ownerName: '李四',
        viewCount: 890,
        interestCount: 67,
        collaborationCount: 8,
        createdAt: '2024-02-20T14:15:00Z',
        updatedAt: '2024-11-30T09:45:00Z'
      },
      {
        id: '3',
        name: '品牌视觉设计',
        type: '品牌设计',
        description: '为初创公司提供完整的品牌视觉识别系统设计',
        fullDescription: '这是一个专业的品牌视觉设计项目...',
        category: 'design',
        status: 'completed',
        tags: ['品牌设计', 'VI设计', 'Logo', '视觉识别'],
        isFeatured: true,
        logo: null,
        ownerName: '王五',
        viewCount: 567,
        interestCount: 45,
        collaborationCount: 5,
        createdAt: '2024-03-10T16:45:00Z',
        updatedAt: '2024-11-25T11:30:00Z'
      }
    ]
    
    // 方法
    const loadProjects = async () => {
      loading.value = true
      try {
        // 模拟API调用
        await new Promise(resolve => setTimeout(resolve, 1000))
        
        let filteredProjects = [...mockProjects]
        
        // 应用筛选条件
        if (filters.value.status) {
          filteredProjects = filteredProjects.filter(project => 
            project.status === filters.value.status
          )
        }
        
        if (filters.value.category) {
          filteredProjects = filteredProjects.filter(project => 
            project.category === filters.value.category
          )
        }
        
        if (filters.value.featured) {
          const isFeatured = filters.value.featured === 'true'
          filteredProjects = filteredProjects.filter(project => 
            project.isFeatured === isFeatured
          )
        }
        
        if (filters.value.search) {
          const searchTerm = filters.value.search.toLowerCase()
          filteredProjects = filteredProjects.filter(project =>
            project.name.toLowerCase().includes(searchTerm) ||
            project.description.toLowerCase().includes(searchTerm) ||
            project.ownerName.toLowerCase().includes(searchTerm)
          )
        }
        
        totalProjects.value = filteredProjects.length
        projects.value = filteredProjects.slice(
          (currentPage.value - 1) * pageSize.value,
          currentPage.value * pageSize.value
        )
      } catch (error) {
        console.error('加载项目失败:', error)
      } finally {
        loading.value = false
      }
    }
    
    const debounceSearch = (() => {
      let timeout
      return () => {
        clearTimeout(timeout)
        timeout = setTimeout(() => {
          currentPage.value = 1
          loadProjects()
        }, 500)
      }
    })()
    
    const changePage = (page) => {
      if (page >= 1 && page <= totalPages.value) {
        currentPage.value = page
        loadProjects()
      }
    }
    
    const getStatusClass = (status) => {
      const classes = {
        active: 'status-active',
        recruiting: 'status-recruiting',
        paused: 'status-paused',
        completed: 'status-completed'
      }
      return classes[status] || 'status-active'
    }
    
    const getStatusText = (status) => {
      const texts = {
        active: '进行中',
        recruiting: '招募中',
        paused: '暂停',
        completed: '已完成'
      }
      return texts[status] || '进行中'
    }
    
    const getCategoryClass = (category) => {
      const classes = {
        tech: 'category-tech',
        design: 'category-design',
        business: 'category-business',
        education: 'category-education',
        other: 'category-other'
      }
      return classes[category] || 'category-other'
    }
    
    const getCategoryText = (category) => {
      const texts = {
        tech: '技术开发',
        design: '设计创意',
        business: '商业项目',
        education: '教育培训',
        other: '其他'
      }
      return texts[category] || '其他'
    }
    
    const getToggleIcon = (status) => {
      return status === 'paused' ? '▶️' : '⏸️'
    }
    
    const getToggleTitle = (status) => {
      return status === 'paused' ? '恢复项目' : '暂停项目'
    }
    
    const formatDate = (dateString) => {
      const date = new Date(dateString)
      return date.toLocaleDateString('zh-CN', {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit'
      })
    }
    
    const resetProjectForm = () => {
      projectForm.value = {
        name: '',
        type: '',
        description: '',
        fullDescription: '',
        category: '',
        status: 'active',
        tags: [],
        isFeatured: false
      }
      tagsInput.value = ''
    }
    
    const editProject = (project) => {
      editingProject.value = project
      projectForm.value = {
        name: project.name,
        type: project.type || '',
        description: project.description,
        fullDescription: project.fullDescription || '',
        category: project.category,
        status: project.status,
        tags: [...project.tags],
        isFeatured: project.isFeatured
      }
      tagsInput.value = project.tags.join(', ')
      showEditModal.value = true
    }
    
    const closeModals = () => {
      showAddModal.value = false
      showEditModal.value = false
      editingProject.value = null
      resetProjectForm()
    }
    
    const saveProject = async () => {
      saving.value = true
      try {
        // 模拟API调用
        await new Promise(resolve => setTimeout(resolve, 1000))
        
        if (showAddModal.value) {
          console.log('添加项目:', projectForm.value)
        } else {
          console.log('编辑项目:', editingProject.value.id, projectForm.value)
        }
        
        closeModals()
        loadProjects()
      } catch (error) {
        console.error('保存项目失败:', error)
      } finally {
        saving.value = false
      }
    }
    
    const toggleFeatured = async (project) => {
      try {
        // 模拟API调用
        await new Promise(resolve => setTimeout(resolve, 300))
        
        project.isFeatured = !project.isFeatured
        console.log('切换精选状态:', project.id, project.isFeatured)
      } catch (error) {
        console.error('切换精选状态失败:', error)
      }
    }
    
    const toggleProjectStatus = async (project) => {
      try {
        // 模拟API调用
        await new Promise(resolve => setTimeout(resolve, 300))
        
        project.status = project.status === 'paused' ? 'active' : 'paused'
        console.log('切换项目状态:', project.id, project.status)
      } catch (error) {
        console.error('切换项目状态失败:', error)
      }
    }
    
    const deleteProject = async (project) => {
      if (!confirm(`确定要删除项目 "${project.name}" 吗？此操作不可恢复。`)) {
        return
      }
      
      try {
        // 模拟API调用
        await new Promise(resolve => setTimeout(resolve, 500))
        
        console.log('删除项目:', project.id)
        loadProjects()
      } catch (error) {
        console.error('删除项目失败:', error)
      }
    }
    
    onMounted(() => {
      loadProjects()
    })
    
    return {
      loading,
      saving,
      projects,
      currentPage,
      totalPages,
      visiblePages,
      filters,
      projectForm,
      tagsInput,
      showAddModal,
      showEditModal,
      loadProjects,
      debounceSearch,
      changePage,
      getStatusClass,
      getStatusText,
      getCategoryClass,
      getCategoryText,
      getToggleIcon,
      getToggleTitle,
      formatDate,
      editProject,
      closeModals,
      saveProject,
      toggleFeatured,
      toggleProjectStatus,
      deleteProject
    }
  }
}
</script>

<style scoped>
.admin-projects {
  max-width: 1400px;
  margin: 0 auto;
}

/* 页面头部 */
.page-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 30px;
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

.btn-primary:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
}

/* 筛选区域 */
.filters-section {
  background: white;
  border-radius: 12px;
  padding: 24px;
  margin-bottom: 24px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.filters {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
}

.filter-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.filter-group label {
  font-size: 14px;
  font-weight: 500;
  color: #333;
}

.filter-group select,
.search-input {
  padding: 10px 12px;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-size: 14px;
  transition: border-color 0.2s;
}

.filter-group select:focus,
.search-input:focus {
  outline: none;
  border-color: #667eea;
  box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

/* 项目网格 */
.projects-container {
  margin-bottom: 24px;
}

.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 24px;
}

.project-card {
  background: white;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  transition: transform 0.2s, box-shadow 0.2s;
}

.project-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
}

/* 项目头部 */
.project-header {
  padding: 20px;
  display: flex;
  align-items: flex-start;
  gap: 12px;
  border-bottom: 1px solid #f0f0f0;
}

.project-logo {
  width: 48px;
  height: 48px;
  border-radius: 8px;
  overflow: hidden;
  flex-shrink: 0;
}

.project-logo img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.logo-placeholder {
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  font-size: 18px;
}

.project-info {
  flex: 1;
  min-width: 0;
}

.project-name {
  margin: 0 0 6px 0;
  font-size: 16px;
  font-weight: 600;
  color: #2c3e50;
  line-height: 1.3;
}

.project-meta {
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 12px;
  color: #666;
}

.project-actions {
  flex-shrink: 0;
}

.btn-feature {
  width: 32px;
  height: 32px;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 16px;
  transition: all 0.2s;
  background-color: #f8f9fa;
  color: #666;
}

.btn-feature.active {
  background-color: #fff3e0;
  color: #f57c00;
}

.btn-feature:hover {
  transform: scale(1.1);
}

/* 项目内容 */
.project-content {
  padding: 20px;
}

.project-description {
  margin: 0 0 16px 0;
  color: #666;
  font-size: 14px;
  line-height: 1.5;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.project-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-bottom: 16px;
}

.tag {
  padding: 4px 8px;
  background-color: #e3f2fd;
  color: #1976d2;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 500;
}

.tag-more {
  padding: 4px 8px;
  background-color: #f0f0f0;
  color: #666;
  border-radius: 4px;
  font-size: 12px;
}

.project-stats {
  display: flex;
  gap: 16px;
}

.stat-item {
  display: flex;
  align-items: center;
  gap: 4px;
  font-size: 12px;
  color: #666;
}

.stat-icon {
  font-size: 14px;
}

/* 项目底部 */
.project-footer {
  padding: 16px 20px;
  background-color: #f8f9fa;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.project-status {
  display: flex;
  gap: 8px;
}

.status-badge,
.category-badge {
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 500;
}

.status-active {
  background-color: #d5f4e6;
  color: #27ae60;
}

.status-recruiting {
  background-color: #e3f2fd;
  color: #1976d2;
}

.status-paused {
  background-color: #fff3e0;
  color: #f57c00;
}

.status-completed {
  background-color: #f0f0f0;
  color: #666;
}

.category-tech {
  background-color: #e8f5e8;
  color: #2e7d32;
}

.category-design {
  background-color: #fce4ec;
  color: #c2185b;
}

.category-business {
  background-color: #e0f2f1;
  color: #00695c;
}

.category-education {
  background-color: #f3e5f5;
  color: #7b1fa2;
}

.category-other {
  background-color: #f0f0f0;
  color: #666;
}

.project-controls {
  display: flex;
  gap: 8px;
}

.project-controls button {
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

.btn-edit {
  background-color: #e3f2fd;
  color: #1976d2;
}

.btn-edit:hover {
  background-color: #bbdefb;
}

.btn-toggle {
  background-color: #fff3e0;
  color: #f57c00;
}

.btn-toggle:hover {
  background-color: #ffe0b2;
}

.btn-delete {
  background-color: #fdf2f2;
  color: #e74c3c;
}

.btn-delete:hover {
  background-color: #fecaca;
}

/* 分页 */
.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 8px;
  margin-top: 24px;
}

.page-btn {
  padding: 8px 12px;
  border: 1px solid #ddd;
  background: white;
  border-radius: 6px;
  cursor: pointer;
  font-size: 14px;
  transition: all 0.2s;
}

.page-btn:hover:not(:disabled) {
  background-color: #f8f9fa;
  border-color: #bbb;
}

.page-btn.active {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border-color: #667eea;
}

.page-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.page-numbers {
  display: flex;
  gap: 4px;
}

/* 模态框 */
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
  width: 100%;
  max-width: 700px;
  max-height: 90vh;
  overflow-y: auto;
}

.modal-header {
  padding: 24px 24px 0 24px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
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

/* 表单 */
.project-form {
  padding: 0 24px 24px 24px;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
  margin-bottom: 16px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.form-group label {
  font-size: 14px;
  font-weight: 500;
  color: #333;
}

.form-group input,
.form-group select,
.form-group textarea {
  padding: 10px 12px;
  border: 1px solid #ddd;
  border-radius: 6px;
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

.checkbox-group {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-top: 8px;
}

.checkbox-group input[type="checkbox"] {
  width: auto;
  margin: 0;
}

.form-actions {
  display: flex;
  justify-content: flex-end;
  gap: 12px;
  margin-top: 24px;
  padding-top: 24px;
  border-top: 1px solid #e1e5e9;
}

.btn-cancel {
  padding: 10px 20px;
  border: 1px solid #ddd;
  background: white;
  border-radius: 6px;
  cursor: pointer;
  font-size: 14px;
  transition: all 0.2s;
}

.btn-cancel:hover {
  background-color: #f8f9fa;
  border-color: #bbb;
}

.btn-save {
  padding: 10px 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 14px;
  font-weight: 500;
  transition: all 0.2s;
}

.btn-save:hover:not(:disabled) {
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
}

.btn-save:disabled {
  opacity: 0.6;
  cursor: not-allowed;
  transform: none;
}

/* 加载和空状态 */
.loading-state,
.empty-state {
  text-align: center;
  padding: 60px 20px;
  color: #666;
}

.loading-spinner {
  width: 40px;
  height: 40px;
  border: 3px solid #f0f0f0;
  border-top: 3px solid #667eea;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 0 auto 16px;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.empty-icon {
  font-size: 48px;
  margin-bottom: 16px;
}

.empty-state h3 {
  margin: 0 0 8px 0;
  font-size: 18px;
  color: #2c3e50;
}

.empty-state p {
  margin: 0;
  font-size: 14px;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .page-header {
    flex-direction: column;
    gap: 16px;
    align-items: stretch;
  }
  
  .filters {
    grid-template-columns: 1fr;
  }
  
  .projects-grid {
    grid-template-columns: 1fr;
  }
  
  .form-row {
    grid-template-columns: 1fr;
  }
  
  .project-header {
    padding: 16px;
  }
  
  .project-content {
    padding: 16px;
  }
  
  .project-footer {
    padding: 12px 16px;
    flex-direction: column;
    gap: 12px;
    align-items: stretch;
  }
  
  .project-status {
    justify-content: center;
  }
  
  .project-controls {
    justify-content: center;
  }
}
</style>
