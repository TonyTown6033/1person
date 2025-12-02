<template>
  <!-- 桌面端侧边栏 -->
  <aside class="sidebar desktop-sidebar">
    <RouterLink to="/" class="logo">Pitch.</RouterLink>
    
    <nav class="nav-menu">
      <RouterLink to="/" class="nav-item" :class="{ active: route.name === 'home' }">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path>
          <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path>
        </svg>
        <span>学习</span>
      </RouterLink>
      <RouterLink to="/talents" class="nav-item" :class="{ active: route.name === 'talents' }">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
          <circle cx="12" cy="7" r="4"></circle>
        </svg>
        <span>牛人</span>
      </RouterLink>
      <RouterLink to="/links" class="nav-item" :class="{ active: route.name === 'links' }">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path>
          <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path>
        </svg>
        <span>链接</span>
      </RouterLink>
      <RouterLink to="/projects" class="nav-item" :class="{ active: route.name === 'projects' }">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <circle cx="12" cy="12" r="10"></circle>
          <path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path>
          <path d="M12 17h.01"></path>
        </svg>
        <span>项目</span>
      </RouterLink>
      <RouterLink to="/events" class="nav-item" :class="{ active: route.name === 'events' }">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
          <circle cx="12" cy="10" r="3"></circle>
        </svg>
        <span>活动</span>
      </RouterLink>
      <RouterLink to="/profile" class="nav-item" :class="{ active: route.name === 'profile' }">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
          <circle cx="12" cy="7" r="4"></circle>
        </svg>
        <span>我的</span>
      </RouterLink>
    </nav>

    <div class="sidebar-footer">
      <div class="footer-buttons">
        <button class="footer-btn active">首页</button>
        <button class="footer-btn">名片</button>
      </div>
      <div class="user-profile">
        <div class="avatar">
          <img src="https://api.dicebear.com/7.x/avataaars/svg?seed=greta" alt="greta" />
        </div>
        <span class="username">greta</span>
        <svg class="bell-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path>
          <path d="M13.73 21a2 2 0 0 1-3.46 0"></path>
        </svg>
      </div>
    </div>
  </aside>

  <!-- 移动端顶部导航栏 -->
  <header class="mobile-header">
    <RouterLink to="/" class="mobile-logo">Pitch.</RouterLink>
    <div class="mobile-header-actions">
      <button class="mobile-header-btn">首页</button>
      <button class="mobile-header-btn">名片</button>
      <button class="mobile-header-btn mobile-login-btn">登录</button>
    </div>
  </header>

  <!-- 移动端底部导航栏 -->
  <nav class="mobile-bottom-nav">
    <RouterLink to="/" class="mobile-nav-item" :class="{ active: route.name === 'home' }">
      <svg class="mobile-nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path>
        <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path>
      </svg>
      <span>学习</span>
    </RouterLink>
    <RouterLink to="/talents" class="mobile-nav-item" :class="{ active: route.name === 'talents' }">
      <svg class="mobile-nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
        <circle cx="12" cy="7" r="4"></circle>
      </svg>
      <span>牛人</span>
    </RouterLink>
    <RouterLink to="/links" class="mobile-nav-item" :class="{ active: route.name === 'links' }">
      <svg class="mobile-nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path>
        <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path>
      </svg>
      <span>链接</span>
    </RouterLink>
    <RouterLink to="/projects" class="mobile-nav-item" :class="{ active: route.name === 'projects' }">
      <svg class="mobile-nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <circle cx="12" cy="12" r="10"></circle>
        <path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path>
        <path d="M12 17h.01"></path>
      </svg>
      <span>项目</span>
    </RouterLink>
    <RouterLink to="/events" class="mobile-nav-item" :class="{ active: route.name === 'events' }">
      <svg class="mobile-nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
        <circle cx="12" cy="10" r="3"></circle>
      </svg>
      <span>活动</span>
    </RouterLink>
    <RouterLink to="/profile" class="mobile-nav-item" :class="{ active: route.name === 'profile' }">
      <svg class="mobile-nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
        <circle cx="12" cy="7" r="4"></circle>
      </svg>
      <span>我的</span>
    </RouterLink>
  </nav>
</template>

<script setup>
import { useRoute } from 'vue-router'

const route = useRoute()
</script>

<style scoped>
/* 桌面端侧边栏样式 */
.desktop-sidebar {
  width: 240px;
  background-color: #f5f5f5;
  display: flex;
  flex-direction: column;
  padding: 32px 16px;
  height: 100vh;
  flex-shrink: 0;
  position: sticky;
  top: 0;
}

.logo {
  font-size: 24px;
  font-weight: 700;
  text-align: center;
  color: #ffffff;
  background-color: #000000;
  padding: 16px;
  border-radius: 8px;
  margin-bottom: 32px;
  display: block;
  text-decoration: none;
}

.nav-menu {
  display: flex;
  flex-direction: column;
  gap: 4px;
  flex: 1;
}

.nav-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 16px;
  color: #000000;
  text-decoration: none;
  border-radius: 8px;
  transition: background-color 0.2s;
}

.nav-item:hover {
  background-color: #e8e8e8;
}

.nav-item.active {
  background-color: #e5e5e5;
}

.nav-icon {
  width: 20px;
  height: 20px;
  stroke: currentColor;
}

.sidebar-footer {
  margin-top: auto;
  padding-top: 24px;
}

.footer-buttons {
  display: flex;
  gap: 8px;
  margin-bottom: 24px;
}

.footer-btn {
  flex: 1;
  padding: 10px 16px;
  background-color: #ffffff;
  border: 1px solid #e0e0e0;
  border-radius: 6px;
  color: #000000;
  cursor: pointer;
  font-size: 14px;
  transition: all 0.2s;
}

.footer-btn:hover {
  background-color: #f5f5f5;
}

.footer-btn.active {
  background-color: #000000;
  color: #ffffff;
  border-color: #000000;
}

.user-profile {
  display: flex;
  align-items: center;
  gap: 12px;
}

.avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  overflow: hidden;
  background-color: #e0e0e0;
}

.avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.username {
  flex: 1;
  color: #000000;
  font-size: 14px;
}

.bell-icon {
  width: 20px;
  height: 20px;
  color: #000000;
  cursor: pointer;
}

/* 移动端顶部导航栏 */
.mobile-header {
  display: none;
  align-items: center;
  justify-content: space-between;
  padding: 12px 16px;
  background-color: #ffffff;
  border-bottom: 1px solid #e0e0e0;
  position: sticky;
  top: 0;
  z-index: 100;
}

.mobile-logo {
  font-size: 20px;
  font-weight: 700;
  color: #ffffff;
  background-color: #000000;
  padding: 8px 16px;
  border-radius: 6px;
  text-decoration: none;
}

.mobile-header-actions {
  display: flex;
  align-items: center;
  gap: 8px;
}

.mobile-header-btn {
  padding: 6px 12px;
  background-color: #ffffff;
  border: 1px solid #e0e0e0;
  border-radius: 6px;
  color: #000000;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.2s;
}

.mobile-header-btn:hover {
  background-color: #f5f5f5;
}

.mobile-login-btn {
  background-color: #000000;
  color: #ffffff;
  border-color: #000000;
}

.mobile-login-btn:hover {
  background-color: #333333;
}

/* 移动端底部导航栏 */
.mobile-bottom-nav {
  display: none;
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  background-color: #ffffff;
  border-top: 1px solid #e0e0e0;
  padding: 8px 0 calc(8px + env(safe-area-inset-bottom));
  z-index: 100;
  box-shadow: 0 -2px 8px rgba(0, 0, 0, 0.05);
  max-width: 100%;
  overflow-x: hidden;
}

.mobile-nav-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 4px;
  padding: 8px 4px;
  color: #666666;
  text-decoration: none;
  flex: 1;
  transition: color 0.2s;
  font-size: 11px;
  min-width: 0;
  position: relative;
}

.mobile-nav-item.active {
  color: #000000;
  font-weight: 500;
}

.mobile-nav-item.active::before {
  content: '';
  position: absolute;
  top: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 40px;
  height: 2px;
  background-color: #000000;
  border-radius: 0 0 2px 2px;
}

.mobile-nav-icon {
  width: 22px;
  height: 22px;
  stroke: currentColor;
  flex-shrink: 0;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .desktop-sidebar {
    display: none;
  }

  .mobile-header {
    display: flex;
  }

  .mobile-bottom-nav {
    display: flex;
  }
}

@media (min-width: 769px) {
  .mobile-header {
    display: none;
  }

  .mobile-bottom-nav {
    display: none;
  }
}
</style>

