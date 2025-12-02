<template>
  <div class="admin-layout">
    <!-- 侧边栏 -->
    <aside class="sidebar" :class="{ collapsed: sidebarCollapsed }">
      <div class="sidebar-header">
        <div class="logo">
          <h2 v-if="!sidebarCollapsed">Super Club</h2>
          <h2 v-else>SC</h2>
        </div>
        <button @click="toggleSidebar" class="toggle-btn">
          <span>{{ sidebarCollapsed ? '→' : '←' }}</span>
        </button>
      </div>
      
      <nav class="sidebar-nav">
        <router-link 
          v-for="item in menuItems" 
          :key="item.name"
          :to="item.path" 
          class="nav-item"
          :class="{ active: $route.name === item.name }"
        >
          <span class="nav-icon">{{ item.icon }}</span>
          <span v-if="!sidebarCollapsed" class="nav-text">{{ item.label }}</span>
        </router-link>
      </nav>
      
      <div class="sidebar-footer">
        <button @click="handleLogout" class="logout-btn">
          <span class="nav-icon">🚪</span>
          <span v-if="!sidebarCollapsed" class="nav-text">退出登录</span>
        </button>
      </div>
    </aside>
    
    <!-- 主内容区 -->
    <main class="main-content">
      <!-- 顶部导航栏 -->
      <header class="top-header">
        <div class="header-left">
          <h1 class="page-title">{{ currentPageTitle }}</h1>
        </div>
        <div class="header-right">
          <div class="user-info">
            <span class="user-name">{{ adminUser?.name || '管理员' }}</span>
            <div class="user-avatar">{{ (adminUser?.name || 'A')[0] }}</div>
          </div>
        </div>
      </header>
      
      <!-- 页面内容 -->
      <div class="page-content">
        <router-view />
      </div>
    </main>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'

export default {
  name: 'AdminLayout',
  setup() {
    const router = useRouter()
    const route = useRoute()
    const sidebarCollapsed = ref(false)
    const adminUser = ref(null)
    
    const menuItems = [
      { name: 'admin-dashboard', path: '/admin', label: '仪表板', icon: '📊' },
      { name: 'admin-users', path: '/admin/users', label: '用户管理', icon: '👥' },
      { name: 'admin-projects', path: '/admin/projects', label: '项目管理', icon: '🚀' },
      { name: 'admin-events', path: '/admin/events', label: '活动管理', icon: '📅' },
      { name: 'admin-content', path: '/admin/content', label: '内容管理', icon: '📝' },
      { name: 'admin-carousel', path: '/admin/carousel', label: '轮播管理', icon: '🖼️' }
    ]
    
    const currentPageTitle = computed(() => {
      const currentItem = menuItems.find(item => item.name === route.name)
      return currentItem?.label || '管理后台'
    })
    
    const toggleSidebar = () => {
      sidebarCollapsed.value = !sidebarCollapsed.value
    }
    
    const handleLogout = () => {
      localStorage.removeItem('admin_token')
      localStorage.removeItem('admin_refresh_token')
      localStorage.removeItem('admin_user')
      router.push('/admin/login')
    }
    
    onMounted(() => {
      // 检查登录状态
      const token = localStorage.getItem('admin_token')
      const userStr = localStorage.getItem('admin_user')
      
      if (!token) {
        router.push('/admin/login')
        return
      }
      
      if (userStr) {
        try {
          adminUser.value = JSON.parse(userStr)
        } catch (e) {
          console.error('Failed to parse admin user:', e)
        }
      }
    })
    
    return {
      sidebarCollapsed,
      menuItems,
      currentPageTitle,
      adminUser,
      toggleSidebar,
      handleLogout
    }
  }
}
</script>

<style scoped>
.admin-layout {
  display: flex;
  height: 100vh;
  background-color: #f5f6fa;
}

/* 侧边栏样式 */
.sidebar {
  width: 250px;
  background: white;
  border-right: 1px solid #e1e5e9;
  display: flex;
  flex-direction: column;
  transition: width 0.3s ease;
  box-shadow: 2px 0 8px rgba(0, 0, 0, 0.1);
}

.sidebar.collapsed {
  width: 70px;
}

.sidebar-header {
  padding: 20px;
  border-bottom: 1px solid #e1e5e9;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.logo h2 {
  color: #2c3e50;
  margin: 0;
  font-size: 18px;
  font-weight: 600;
}

.toggle-btn {
  background: none;
  border: none;
  cursor: pointer;
  padding: 5px;
  border-radius: 4px;
  color: #666;
  transition: background-color 0.2s;
}

.toggle-btn:hover {
  background-color: #f0f0f0;
}

.sidebar-nav {
  flex: 1;
  padding: 20px 0;
}

.nav-item {
  display: flex;
  align-items: center;
  padding: 12px 20px;
  color: #666;
  text-decoration: none;
  transition: all 0.2s;
  border-left: 3px solid transparent;
}

.nav-item:hover {
  background-color: #f8f9fa;
  color: #2c3e50;
}

.nav-item.active {
  background-color: #e3f2fd;
  color: #1976d2;
  border-left-color: #1976d2;
}

.nav-icon {
  font-size: 18px;
  margin-right: 12px;
  width: 20px;
  text-align: center;
}

.nav-text {
  font-size: 14px;
  font-weight: 500;
}

.sidebar-footer {
  padding: 20px;
  border-top: 1px solid #e1e5e9;
}

.logout-btn {
  display: flex;
  align-items: center;
  width: 100%;
  padding: 12px 0;
  background: none;
  border: none;
  color: #e74c3c;
  cursor: pointer;
  transition: color 0.2s;
}

.logout-btn:hover {
  color: #c0392b;
}

/* 主内容区样式 */
.main-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.top-header {
  background: white;
  padding: 0 30px;
  height: 70px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid #e1e5e9;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
}

.page-title {
  color: #2c3e50;
  margin: 0;
  font-size: 20px;
  font-weight: 600;
}

.header-right {
  display: flex;
  align-items: center;
}

.user-info {
  display: flex;
  align-items: center;
  gap: 12px;
}

.user-name {
  color: #666;
  font-size: 14px;
}

.user-avatar {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  font-size: 14px;
}

.page-content {
  flex: 1;
  padding: 30px;
  overflow-y: auto;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .sidebar {
    position: fixed;
    left: -250px;
    z-index: 1000;
    height: 100vh;
  }
  
  .sidebar.collapsed {
    left: -70px;
  }
  
  .main-content {
    margin-left: 0;
  }
  
  .page-content {
    padding: 20px;
  }
}
</style>
