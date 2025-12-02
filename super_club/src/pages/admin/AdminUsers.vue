<template>
  <div class="admin-users">
    <!-- 页面头部 -->
    <div class="page-header">
      <div class="header-left">
        <h2>用户管理</h2>
        <p>管理系统中的所有用户账户</p>
      </div>
      <div class="header-right">
        <button @click="showAddModal = true" class="btn-primary">
          <span>➕</span>
          添加用户
        </button>
      </div>
    </div>
    
    <!-- 筛选和搜索 -->
    <div class="filters-section">
      <div class="filters">
        <div class="filter-group">
          <label>状态筛选</label>
          <select v-model="filters.status" @change="loadUsers">
            <option value="">全部状态</option>
            <option value="active">活跃</option>
            <option value="inactive">非活跃</option>
            <option value="banned">已封禁</option>
          </select>
        </div>
        
        <div class="filter-group">
          <label>会员等级</label>
          <select v-model="filters.membershipLevel" @change="loadUsers">
            <option value="">全部等级</option>
            <option value="free">免费用户</option>
            <option value="premium">高级用户</option>
            <option value="vip">VIP用户</option>
          </select>
        </div>
        
        <div class="filter-group">
          <label>搜索用户</label>
          <input
            v-model="filters.search"
            @input="debounceSearch"
            type="text"
            placeholder="搜索姓名、邮箱..."
            class="search-input"
          />
        </div>
      </div>
    </div>
    
    <!-- 用户列表 -->
    <div class="users-table-container">
      <div v-if="loading" class="loading-state">
        <div class="loading-spinner"></div>
        <p>加载中...</p>
      </div>
      
      <div v-else-if="users.length === 0" class="empty-state">
        <div class="empty-icon">👥</div>
        <h3>暂无用户数据</h3>
        <p>还没有用户注册，或者当前筛选条件下没有匹配的用户</p>
      </div>
      
      <div v-else class="table-wrapper">
        <table class="users-table">
          <thead>
            <tr>
              <th>用户信息</th>
              <th>邮箱</th>
              <th>角色</th>
              <th>会员等级</th>
              <th>状态</th>
              <th>注册时间</th>
              <th>操作</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="user in users" :key="user.id" class="user-row">
              <td class="user-info">
                <div class="user-avatar">
                  <img v-if="user.avatar" :src="user.avatar" :alt="user.name" />
                  <div v-else class="avatar-placeholder">
                    {{ user.name ? user.name[0] : '?' }}
                  </div>
                </div>
                <div class="user-details">
                  <div class="user-name">{{ user.name }}</div>
                  <div class="user-company" v-if="user.company">
                    {{ user.company }}
                  </div>
                </div>
              </td>
              <td class="user-email">{{ user.email }}</td>
              <td class="user-role">
                <span 
                  class="role-badge" 
                  :class="getRoleClass(user.role)"
                >
                  {{ getRoleText(user.role) }}
                </span>
              </td>
              <td class="user-membership">
                <span 
                  class="membership-badge" 
                  :class="getMembershipClass(user.membershipLevel)"
                >
                  {{ getMembershipText(user.membershipLevel) }}
                </span>
              </td>
              <td class="user-status">
                <span 
                  class="status-badge" 
                  :class="getStatusClass(user.isActive)"
                >
                  {{ user.isActive ? '活跃' : '非活跃' }}
                </span>
              </td>
              <td class="user-created">
                {{ formatDate(user.createdAt) }}
              </td>
              <td class="user-actions">
                <div class="action-buttons">
                  <button 
                    @click="editUser(user)" 
                    class="btn-edit"
                    title="编辑用户"
                  >
                    ✏️
                  </button>
                  <button 
                    @click="toggleUserStatus(user)" 
                    class="btn-toggle"
                    :class="{ 'btn-activate': !user.isActive, 'btn-deactivate': user.isActive }"
                    :title="user.isActive ? '禁用用户' : '启用用户'"
                  >
                    {{ user.isActive ? '🚫' : '✅' }}
                  </button>
                  <button 
                    @click="deleteUser(user)" 
                    class="btn-delete"
                    title="删除用户"
                  >
                    🗑️
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
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
    
    <!-- 添加/编辑用户模态框 -->
    <div v-if="showAddModal || showEditModal" class="modal-overlay" @click="closeModals">
      <div class="modal-content" @click.stop>
        <div class="modal-header">
          <h3>{{ showAddModal ? '添加用户' : '编辑用户' }}</h3>
          <button @click="closeModals" class="close-btn">✕</button>
        </div>
        
        <form @submit.prevent="saveUser" class="user-form">
          <div class="form-row">
            <div class="form-group">
              <label>姓名 *</label>
              <input 
                v-model="userForm.name" 
                type="text" 
                required 
                placeholder="请输入姓名"
              />
            </div>
            <div class="form-group">
              <label>邮箱 *</label>
              <input 
                v-model="userForm.email" 
                type="email" 
                required 
                placeholder="请输入邮箱"
                :disabled="showEditModal"
              />
            </div>
          </div>
          
          <div class="form-row" v-if="showAddModal">
            <div class="form-group">
              <label>密码 *</label>
              <input 
                v-model="userForm.password" 
                type="password" 
                required 
                placeholder="请输入密码"
              />
            </div>
            <div class="form-group">
              <label>确认密码 *</label>
              <input 
                v-model="userForm.confirmPassword" 
                type="password" 
                required 
                placeholder="请再次输入密码"
              />
            </div>
          </div>
          
          <div class="form-row">
            <div class="form-group">
              <label>手机号</label>
              <input 
                v-model="userForm.phone" 
                type="tel" 
                placeholder="请输入手机号"
              />
            </div>
            <div class="form-group">
              <label>公司</label>
              <input 
                v-model="userForm.company" 
                type="text" 
                placeholder="请输入公司名称"
              />
            </div>
          </div>
          
          <div class="form-row">
            <div class="form-group">
              <label>职位</label>
              <input 
                v-model="userForm.position" 
                type="text" 
                placeholder="请输入职位"
              />
            </div>
            <div class="form-group">
              <label>会员等级</label>
              <select v-model="userForm.membershipLevel">
                <option value="free">免费用户</option>
                <option value="premium">高级用户</option>
                <option value="vip">VIP用户</option>
              </select>
            </div>
          </div>
          
          <div class="form-row">
            <div class="form-group">
              <label>用户角色</label>
              <select v-model="userForm.role">
                <option value="user">普通用户</option>
                <option value="admin">管理员</option>
                <option value="super_admin">超级管理员</option>
              </select>
            </div>
            <div class="form-group">
              <!-- 占位 -->
            </div>
          </div>
          
          <div class="form-group">
            <label>个人简介</label>
            <textarea 
              v-model="userForm.bio" 
              rows="3" 
              placeholder="请输入个人简介"
            ></textarea>
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
import { ref, computed, onMounted } from 'vue'

export default {
  name: 'AdminUsers',
  setup() {
    const loading = ref(false)
    const saving = ref(false)
    const users = ref([])
    const currentPage = ref(1)
    const pageSize = ref(10)
    const totalUsers = ref(0)
    const showAddModal = ref(false)
    const showEditModal = ref(false)
    const editingUser = ref(null)
    
    // 筛选条件
    const filters = ref({
      status: '',
      membershipLevel: '',
      search: ''
    })
    
    // 用户表单
    const userForm = ref({
      name: '',
      email: '',
      password: '',
      confirmPassword: '',
      phone: '',
      company: '',
      position: '',
      membershipLevel: 'free',
      role: 'user',
      bio: ''
    })
    
    // 计算属性
    const totalPages = computed(() => {
      return Math.ceil(totalUsers.value / pageSize.value)
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
    
    // 方法
    const loadUsers = async () => {
      loading.value = true
      try {
        // 获取admin_token
        const token = localStorage.getItem('admin_token')
        if (!token) {
          // 没有token，跳转到登录页
          window.location.href = '/admin/login'
          return
        }
        
        // 构建查询参数
        const params = new URLSearchParams({
          page: currentPage.value.toString(),
          limit: pageSize.value.toString()
        })
        
        if (filters.value.status) {
          params.append('status', filters.value.status)
        }
        if (filters.value.membershipLevel) {
          params.append('membership_level', filters.value.membershipLevel)
        }
        if (filters.value.search) {
          params.append('search', filters.value.search)
        }
        
        const response = await fetch(`http://127.0.0.1:8001/api/admin/users?${params}`, {
          headers: {
            'Authorization': `Bearer ${token}`
          }
        })
        
        if (response.status === 401) {
          // Token无效，清除并跳转到登录页
          localStorage.removeItem('admin_token')
          localStorage.removeItem('admin_user')
          window.location.href = '/admin/login'
          return
        }
        
        const result = await response.json()
        
        if (result.success && result.data) {
          users.value = result.data.items || []
          totalUsers.value = result.data.pagination?.total || 0
        }
      } catch (error) {
        console.error('加载用户失败:', error)
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
          loadUsers()
        }, 500)
      }
    })()
    
    const changePage = (page) => {
      if (page >= 1 && page <= totalPages.value) {
        currentPage.value = page
        loadUsers()
      }
    }
    
    const getMembershipClass = (level) => {
      const classes = {
        free: 'membership-free',
        premium: 'membership-premium',
        vip: 'membership-vip'
      }
      return classes[level] || 'membership-free'
    }
    
    const getMembershipText = (level) => {
      const texts = {
        free: '免费用户',
        premium: '高级用户',
        vip: 'VIP用户'
      }
      return texts[level] || '免费用户'
    }
    
    const getStatusClass = (isActive) => {
      return isActive ? 'status-active' : 'status-inactive'
    }
    
    const getRoleText = (role) => {
      const texts = {
        user: '普通用户',
        admin: '管理员',
        super_admin: '超级管理员'
      }
      return texts[role] || '普通用户'
    }
    
    const getRoleClass = (role) => {
      const classes = {
        user: 'role-user',
        admin: 'role-admin',
        super_admin: 'role-super-admin'
      }
      return classes[role] || 'role-user'
    }
    
    const formatDate = (dateString) => {
      if (!dateString) return '-'
      const date = new Date(dateString)
      return date.toLocaleDateString('zh-CN', {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit'
      })
    }
    
    const resetUserForm = () => {
      userForm.value = {
        name: '',
        email: '',
        password: '',
        confirmPassword: '',
        phone: '',
        company: '',
        position: '',
        membershipLevel: 'free',
        role: 'user',
        bio: ''
      }
    }
    
    const editUser = (user) => {
      editingUser.value = user
      userForm.value = {
        name: user.name,
        email: user.email,
        password: '',
        confirmPassword: '',
        phone: user.phone || '',
        company: user.company || '',
        position: user.position || '',
        membershipLevel: user.membershipLevel || 'free',
        role: user.role || 'user',
        bio: user.bio || ''
      }
      showEditModal.value = true
    }
    
    const closeModals = () => {
      showAddModal.value = false
      showEditModal.value = false
      editingUser.value = null
      resetUserForm()
    }
    
    const saveUser = async () => {
      saving.value = true
      try {
        const token = localStorage.getItem('admin_token')
        if (!token) {
          window.location.href = '/admin/login'
          return
        }
        
        // 验证表单
        if (showAddModal.value) {
          if (!userForm.value.name || !userForm.value.email || !userForm.value.password) {
            alert('请填写必填字段')
            saving.value = false
            return
          }
          if (userForm.value.password !== userForm.value.confirmPassword) {
            alert('两次输入的密码不一致')
            saving.value = false
            return
          }
          if (userForm.value.password.length < 6) {
            alert('密码长度至少6位')
            saving.value = false
            return
          }
          
          // 创建用户
          const response = await fetch('http://127.0.0.1:8001/api/admin/users', {
            method: 'POST',
            headers: {
              'Authorization': `Bearer ${token}`,
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({
              name: userForm.value.name,
              email: userForm.value.email,
              password: userForm.value.password,
              phone: userForm.value.phone,
              company: userForm.value.company,
              position: userForm.value.position,
              membershipLevel: userForm.value.membershipLevel,
              role: userForm.value.role,
              bio: userForm.value.bio
            })
          })
          
          const result = await response.json()
          if (result.success) {
            alert('用户创建成功')
          } else {
            alert(result.detail || '创建失败')
            saving.value = false
            return
          }
        } else {
          // 更新用户
          const response = await fetch(`http://127.0.0.1:8001/api/admin/users/${editingUser.value.id}`, {
            method: 'PUT',
            headers: {
              'Authorization': `Bearer ${token}`,
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({
              name: userForm.value.name,
              phone: userForm.value.phone,
              company: userForm.value.company,
              position: userForm.value.position,
              membershipLevel: userForm.value.membershipLevel,
              role: userForm.value.role,
              bio: userForm.value.bio
            })
          })
          
          const result = await response.json()
          if (result.success) {
            alert('用户信息已更新')
          } else {
            alert(result.detail || '更新失败')
            saving.value = false
            return
          }
        }
        
        closeModals()
        loadUsers()
      } catch (error) {
        console.error('保存用户失败:', error)
        alert('保存用户失败')
      } finally {
        saving.value = false
      }
    }
    
    const toggleUserStatus = async (user) => {
      try {
        const token = localStorage.getItem('admin_token')
        if (!token) {
          window.location.href = '/admin/login'
          return
        }
        
        const newStatus = !user.isActive
        const response = await fetch(`http://127.0.0.1:8001/api/admin/users/${user.id}/status?is_active=${newStatus}`, {
          method: 'PUT',
          headers: {
            'Authorization': `Bearer ${token}`
          }
        })
        
        const result = await response.json()
        if (result.success) {
          user.isActive = newStatus
          alert(`用户已${newStatus ? '启用' : '禁用'}`)
        } else {
          alert(result.detail || '操作失败')
        }
      } catch (error) {
        console.error('切换用户状态失败:', error)
        alert('操作失败')
      }
    }
    
    const deleteUser = async (user) => {
      if (!confirm(`确定要删除用户 "${user.name}" 吗？此操作不可恢复。`)) {
        return
      }
      
      try {
        const token = localStorage.getItem('admin_token')
        if (!token) {
          window.location.href = '/admin/login'
          return
        }
        
        const response = await fetch(`http://127.0.0.1:8001/api/admin/users/${user.id}`, {
          method: 'DELETE',
          headers: {
            'Authorization': `Bearer ${token}`
          }
        })
        
        const result = await response.json()
        if (result.success) {
          alert('用户已删除')
          loadUsers()
        } else {
          alert(result.detail || '删除失败')
        }
      } catch (error) {
        console.error('删除用户失败:', error)
        alert('删除失败')
      }
    }
    
    onMounted(() => {
      loadUsers()
    })
    
    return {
      loading,
      saving,
      users,
      currentPage,
      totalPages,
      visiblePages,
      filters,
      userForm,
      showAddModal,
      showEditModal,
      loadUsers,
      debounceSearch,
      changePage,
      getMembershipClass,
      getMembershipText,
      getStatusClass,
      getRoleText,
      getRoleClass,
      formatDate,
      editUser,
      closeModals,
      saveUser,
      toggleUserStatus,
      deleteUser
    }
  }
}
</script>

<style scoped>
.admin-users {
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

/* 表格容器 */
.users-table-container {
  background: white;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  margin-bottom: 24px;
}

.table-wrapper {
  overflow-x: auto;
}

.users-table {
  width: 100%;
  border-collapse: collapse;
}

.users-table th {
  background-color: #f8f9fa;
  padding: 16px 12px;
  text-align: left;
  font-weight: 600;
  color: #2c3e50;
  border-bottom: 1px solid #e1e5e9;
  font-size: 14px;
}

.users-table td {
  padding: 16px 12px;
  border-bottom: 1px solid #f0f0f0;
  vertical-align: middle;
}

.user-row:hover {
  background-color: #f8f9fa;
}

/* 用户信息列 */
.user-info {
  display: flex;
  align-items: center;
  gap: 12px;
  min-width: 200px;
}

.user-avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  overflow: hidden;
  flex-shrink: 0;
}

.user-avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.avatar-placeholder {
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  font-size: 16px;
}

.user-details {
  flex: 1;
  min-width: 0;
}

.user-name {
  font-weight: 500;
  color: #2c3e50;
  margin-bottom: 2px;
}

.user-company {
  font-size: 12px;
  color: #666;
}

/* 邮箱列 */
.user-email {
  color: #666;
  font-size: 14px;
  min-width: 200px;
}

/* 会员等级徽章 */
.membership-badge {
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 500;
  text-align: center;
  display: inline-block;
  min-width: 60px;
}

.membership-free {
  background-color: #f0f0f0;
  color: #666;
}

.membership-premium {
  background-color: #e3f2fd;
  color: #1976d2;
}

.membership-vip {
  background-color: #fff3e0;
  color: #f57c00;
}

/* 角色徽章 */
.role-badge {
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 500;
  text-align: center;
  display: inline-block;
  min-width: 70px;
}

.role-user {
  background-color: #f0f0f0;
  color: #666;
}

.role-admin {
  background-color: #e8f5e9;
  color: #2e7d32;
}

.role-super-admin {
  background-color: #fce4ec;
  color: #c2185b;
}

/* 状态徽章 */
.status-badge {
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 500;
  text-align: center;
  display: inline-block;
  min-width: 50px;
}

.status-active {
  background-color: #d5f4e6;
  color: #27ae60;
}

.status-inactive {
  background-color: #fdf2f2;
  color: #e74c3c;
}

/* 操作按钮 */
.action-buttons {
  display: flex;
  gap: 8px;
}

.action-buttons button {
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

.btn-toggle.btn-activate {
  background-color: #d5f4e6;
  color: #27ae60;
}

.btn-toggle.btn-deactivate {
  background-color: #fff3e0;
  color: #f57c00;
}

.btn-toggle:hover {
  opacity: 0.8;
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
  max-width: 600px;
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
.user-form {
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

.form-group input:disabled {
  background-color: #f5f5f5;
  cursor: not-allowed;
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
  
  .form-row {
    grid-template-columns: 1fr;
  }
  
  .users-table {
    font-size: 12px;
  }
  
  .users-table th,
  .users-table td {
    padding: 8px 6px;
  }
  
  .action-buttons {
    flex-direction: column;
    gap: 4px;
  }
  
  .action-buttons button {
    width: 28px;
    height: 28px;
    font-size: 12px;
  }
}
</style>
