# 用vue还原前端页面
_Exported on 2025/11/10 at GMT+8 17:06:37 from Cursor (2.0.69)_

---

**User**

用vue来一比一还原这个前端页面

---

**Cursor**


检查项目结构，确认是否已有 Vue 项目。



查看现有文件结构：



创建还原该页面的 Vue 组件。先创建主布局和侧边栏组件：



创建主布局和组件：


```vue
<template>
  <div class="app-container">
    <Sidebar />
    <MainContent />
  </div>
</template>

<script setup>
import Sidebar from './components/Sidebar.vue'
import MainContent from './components/MainContent.vue'
</script>

<style scoped>
.app-container {
  display: flex;
  min-height: 100vh;
  background-color: #ffffff;
}
</style>

```

```vue
<template>
  <aside class="sidebar">
    <div class="logo">Pitch.</div>
    
    <nav class="nav-menu">
      <a href="#" class="nav-item active">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path>
          <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path>
        </svg>
        <span>学习</span>
      </a>
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
          <circle cx="12" cy="7" r="4"></circle>
        </svg>
        <span>牛人</span>
      </a>
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path>
          <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path>
        </svg>
        <span>链接</span>
      </a>
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="12" cy="12" r="10"></circle>
          <path d="M12 6v6l4 2"></path>
        </svg>
        <span>项目</span>
      </a>
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
          <circle cx="12" cy="10" r="3"></circle>
        </svg>
        <span>活动</span>
      </a>
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
          <circle cx="12" cy="7" r="4"></circle>
        </svg>
        <span>我的</span>
      </a>
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
</template>

<script setup>
</script>

<style scoped>
.sidebar {
  width: 240px;
  background-color: #f8f8f8;
  display: flex;
  flex-direction: column;
  padding: 24px 16px;
  min-height: 100vh;
}

.logo {
  background-color: #000000;
  color: #ffffff;
  padding: 12px 16px;
  border-radius: 8px;
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 32px;
  text-align: center;
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
  background-color: #e8e8e8;
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
</style>

```

```vue
<template>
  <main class="main-content">
    <div class="content-header">
      <h1 class="main-title">Starter Studies</h1>
      <p class="subtitle">把自己当公司来经营</p>
      
      <div class="tabs">
        <button class="tab active">CEO图书馆</button>
        <button class="tab">最近更新</button>
      </div>
    </div>

    <div class="content-cards-section">
      <div class="cards-container">
        <ContentCard
          v-for="card in cards"
          :key="card.id"
          :title="card.title"
          :description="card.description"
          :image="card.image"
        />
      </div>
    </div>

    <div class="content-bottom">
      <div class="tabs">
        <button class="tab active">系统阅读</button>
        <button class="tab">专题策展</button>
      </div>
      
      <FeatureGrid />
    </div>
  </main>
</template>

<script setup>
import { ref } from 'vue'
import ContentCard from './ContentCard.vue'
import FeatureGrid from './FeatureGrid.vue'

const cards = ref([
  {
    id: 1,
    title: '《别让猴子跳回背上》如何做一个合理的管理者(下)',
    description: '作为管理者,你的贡献来自于你的判断力与影响力,你的职责不是亲力亲为地背负所有猴子,而是要提供动力让其他人发挥所长。',
    image: 'https://images.unsplash.com/photo-1497366216548-37526070297c?w=400&h=250&fit=crop'
  },
  {
    id: 2,
    title: '《别让猴子跳回背上》为什么领导没时间,下属没事做?(上)',
    description: '一旦你接受了这些本不属于你的猴子,一个更严重的问题便随之而来:你为什么越努力,反而越忙乱?',
    image: 'https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=400&h=250&fit=crop'
  },
  {
    id: 3,
    title: '《上瘾》如何培养用户的使用习惯?(下)',
    description: '成功的习惯养成类产品,本质上是将用户面临的问题与产品提供的解决方案,通过一次又一次的循环,紧密地联系在一起,直至这种联系变成一种近乎本能的反应。',
    image: 'https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=400&h=250&fit=crop'
  },
  {
    id: 4,
    title: '《上瘾》可或缺的-',
    description: '在这个注意上你的产品惯"用你的产品生死和',
    image: 'https://images.unsplash.com/photo-1542744173-8e7e53415bb0?w=400&h=250&fit=crop'
  }
])
</script>

<style scoped>
.main-content {
  flex: 1;
  padding: 40px 48px;
  background-color: #ffffff;
  overflow-y: auto;
}

.content-header {
  margin-bottom: 40px;
}

.main-title {
  font-size: 48px;
  font-weight: 700;
  color: #000000;
  margin-bottom: 8px;
}

.subtitle {
  font-size: 18px;
  color: #666666;
  margin-bottom: 32px;
}

.tabs {
  display: flex;
  gap: 32px;
  border-bottom: 1px solid #e0e0e0;
}

.tab {
  padding: 12px 0;
  background: none;
  border: none;
  font-size: 16px;
  color: #666666;
  cursor: pointer;
  position: relative;
  transition: color 0.2s;
}

.tab:hover {
  color: #000000;
}

.tab.active {
  color: #000000;
}

.tab.active::after {
  content: '';
  position: absolute;
  bottom: -1px;
  left: 0;
  right: 0;
  height: 2px;
  background-color: #000000;
}

.content-cards-section {
  margin-bottom: 60px;
}

.cards-container {
  display: flex;
  gap: 24px;
  overflow-x: auto;
  padding-bottom: 16px;
  scrollbar-width: thin;
  scrollbar-color: #c0c0c0 #f0f0f0;
}

.cards-container::-webkit-scrollbar {
  height: 8px;
}

.cards-container::-webkit-scrollbar-track {
  background: #f0f0f0;
  border-radius: 4px;
}

.cards-container::-webkit-scrollbar-thumb {
  background: #c0c0c0;
  border-radius: 4px;
}

.cards-container::-webkit-scrollbar-thumb:hover {
  background: #a0a0a0;
}

.content-bottom {
  margin-top: 60px;
}
</style>

```

```vue
<template>
  <div class="content-card">
    <div class="card-image-wrapper">
      <img :src="image" :alt="title" class="card-image" />
      <span class="ai-tag">AI生成</span>
    </div>
    <div class="card-content">
      <h3 class="card-title">{{ title }}</h3>
      <p class="card-description">{{ description }}</p>
    </div>
  </div>
</template>

<script setup>
defineProps({
  title: {
    type: String,
    required: true
  },
  description: {
    type: String,
    required: true
  },
  image: {
    type: String,
    required: true
  }
})
</script>

<style scoped>
.content-card {
  min-width: 320px;
  max-width: 320px;
  background-color: #ffffff;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  transition: transform 0.2s, box-shadow 0.2s;
}

.content-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.12);
}

.card-image-wrapper {
  position: relative;
  width: 100%;
  height: 200px;
  overflow: hidden;
  background-color: #f0f0f0;
}

.card-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.ai-tag {
  position: absolute;
  top: 12px;
  left: 12px;
  background-color: rgba(0, 0, 0, 0.6);
  color: #ffffff;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 12px;
}

.card-content {
  padding: 20px;
}

.card-title {
  font-size: 18px;
  font-weight: 600;
  color: #000000;
  margin-bottom: 12px;
  line-height: 1.4;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.card-description {
  font-size: 14px;
  color: #666666;
  line-height: 1.6;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>

```

```vue
<template>
  <div class="feature-grid">
    <div class="feature-item">
      <svg class="feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
        <path d="M13 8H3"></path>
        <path d="M17 12H3"></path>
      </svg>
      <span class="feature-text">战略部</span>
    </div>
    <div class="feature-item">
      <svg class="feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
      </svg>
      <span class="feature-text">品牌部</span>
    </div>
    <div class="feature-item">
      <svg class="feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <circle cx="12" cy="12" r="10"></circle>
        <path d="M12 6v6l4 2"></path>
      </svg>
      <span class="feature-text">运营部</span>
    </div>
    <div class="feature-item">
      <svg class="feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6"></path>
        <path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18"></path>
        <path d="M4 22h16"></path>
        <path d="M10 14.66V17c0 .55-.47.98-.97 1.21C7.85 18.75 7 20.24 7 22"></path>
        <path d="M14 14.66V17c0 .55.47.98.97 1.21C16.15 18.75 17 20.24 17 22"></path>
        <path d="M18 2H6v7a6 6 0 0 0 12 0V2Z"></path>
      </svg>
      <span class="feature-text">销售部</span>
    </div>
  </div>
</template>

<script setup>
</script>

<style scoped>
.feature-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 24px;
  margin-top: 32px;
}

.feature-item {
  aspect-ratio: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 16px;
  background-color: #f8f8f8;
  border-radius: 12px;
  transition: background-color 0.2s, transform 0.2s;
  cursor: pointer;
}

.feature-item:hover {
  background-color: #f0f0f0;
  transform: translateY(-2px);
}

.feature-icon {
  width: 48px;
  height: 48px;
  color: #000000;
  stroke: currentColor;
  stroke-width: 2;
  fill: none;
}

.feature-text {
  font-size: 16px;
  font-weight: 500;
  color: #000000;
}
</style>

```

```css
@import './base.css';

#app {
  width: 100%;
  margin: 0;
  padding: 0;
  font-weight: normal;
}

* {
  box-sizing: border-box;
}

body {
  margin: 0;
  padding: 0;
}

```


检查是否有 lint 错误：



优化图标和样式，使其更贴近设计：


```vue
<template>
  <aside class="sidebar">
    <div class="logo">Pitch.</div>
    
    <nav class="nav-menu">
      <a href="#" class="nav-item active">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path>
          <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path>
        </svg>
        <span>学习</span>
      </a>
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
          <circle cx="12" cy="7" r="4"></circle>
        </svg>
        <span>牛人</span>
      </a>
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path>
          <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path>
        </svg>
        <span>链接</span>
      </a>
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <circle cx="12" cy="12" r="10"></circle>
          <path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path>
          <path d="M12 17h.01"></path>
        </svg>
        <span>项目</span>
      </a>
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
          <circle cx="12" cy="10" r="3"></circle>
        </svg>
        <span>活动</span>
      </a>
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
          <circle cx="12" cy="7" r="4"></circle>
        </svg>
        <span>我的</span>
      </a>
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
</template>

<script setup>
</script>

<style scoped>
.sidebar {
  width: 240px;
  background-color: #f8f8f8;
  display: flex;
  flex-direction: column;
  padding: 24px 16px;
  min-height: 100vh;
}

.logo {
  background-color: #000000;
  color: #ffffff;
  padding: 12px 16px;
  border-radius: 8px;
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 32px;
  text-align: center;
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
  background-color: #e8e8e8;
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
</style>


```

```vue
<template>
  <div class="feature-grid">
    <div class="feature-item">
      <svg class="feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path>
        <polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline>
        <line x1="12" y1="22.08" x2="12" y2="12"></line>
      </svg>
      <span class="feature-text">战略部</span>
    </div>
    <div class="feature-item">
      <svg class="feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
      </svg>
      <span class="feature-text">品牌部</span>
    </div>
    <div class="feature-item">
      <svg class="feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <circle cx="12" cy="12" r="10"></circle>
        <circle cx="12" cy="12" r="3"></circle>
        <line x1="12" y1="1" x2="12" y2="3"></line>
        <line x1="12" y1="21" x2="12" y2="23"></line>
        <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
        <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
        <line x1="1" y1="12" x2="3" y2="12"></line>
        <line x1="21" y1="12" x2="23" y2="12"></line>
        <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
        <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
      </svg>
      <span class="feature-text">运营部</span>
    </div>
    <div class="feature-item">
      <svg class="feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6"></path>
        <path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18"></path>
        <path d="M4 22h16"></path>
        <path d="M10 14.66V17c0 .55-.47.98-.97 1.21C7.85 18.75 7 20.24 7 22"></path>
        <path d="M14 14.66V17c0 .55.47.98.97 1.21C16.15 18.75 17 20.24 17 22"></path>
        <path d="M18 2H6v7a6 6 0 0 0 12 0V2Z"></path>
      </svg>
      <span class="feature-text">销售部</span>
    </div>
  </div>
</template>

<script setup>
</script>

<style scoped>
.feature-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 24px;
  margin-top: 32px;
}

.feature-item {
  aspect-ratio: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 16px;
  background-color: #f8f8f8;
  border-radius: 12px;
  transition: background-color 0.2s, transform 0.2s;
  cursor: pointer;
}

.feature-item:hover {
  background-color: #f0f0f0;
  transform: translateY(-2px);
}

.feature-icon {
  width: 48px;
  height: 48px;
  color: #000000;
  stroke: currentColor;
  stroke-width: 2;
  fill: none;
}

.feature-text {
  font-size: 16px;
  font-weight: 500;
  color: #000000;
}
</style>


```

```vue
<template>
  <aside class="sidebar">
    <div class="logo">Pitch.</div>
    
    <nav class="nav-menu">
      <a href="#" class="nav-item active">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path>
          <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path>
        </svg>
        <span>学习</span>
      </a>
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
          <circle cx="12" cy="7" r="4"></circle>
        </svg>
        <span>牛人</span>
      </a>
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path>
          <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path>
        </svg>
        <span>链接</span>
      </a>
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <circle cx="12" cy="12" r="10"></circle>
          <path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path>
          <path d="M12 17h.01"></path>
        </svg>
        <span>项目</span>
      </a>
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
          <circle cx="12" cy="10" r="3"></circle>
        </svg>
        <span>活动</span>
      </a>
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
          <circle cx="12" cy="7" r="4"></circle>
        </svg>
        <span>我的</span>
      </a>
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
</template>

<script setup>
</script>

<style scoped>
.sidebar {
  width: 240px;
  background-color: #f5f5f5;
  display: flex;
  flex-direction: column;
  padding: 24px 16px;
  min-height: 100vh;
  flex-shrink: 0;
}

.logo {
  background-color: #000000;
  color: #ffffff;
  padding: 12px 16px;
  border-radius: 8px;
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 32px;
  text-align: center;
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
  background-color: #e8e8e8;
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
</style>


```

```vue
<template>
  <aside class="sidebar">
    <div class="logo">Pitch.</div>
    
    <nav class="nav-menu">
      <a href="#" class="nav-item active">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path>
          <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path>
        </svg>
        <span>学习</span>
      </a>
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
          <circle cx="12" cy="7" r="4"></circle>
        </svg>
        <span>牛人</span>
      </a>
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path>
          <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path>
        </svg>
        <span>链接</span>
      </a>
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <circle cx="12" cy="12" r="10"></circle>
          <path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path>
          <path d="M12 17h.01"></path>
        </svg>
        <span>项目</span>
      </a>
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
          <circle cx="12" cy="10" r="3"></circle>
        </svg>
        <span>活动</span>
      </a>
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
          <circle cx="12" cy="7" r="4"></circle>
        </svg>
        <span>我的</span>
      </a>
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
</template>

<script setup>
</script>

<style scoped>
.sidebar {
  width: 240px;
  background-color: #f5f5f5;
  display: flex;
  flex-direction: column;
  padding: 24px 16px;
  min-height: 100vh;
  flex-shrink: 0;
}

.logo {
  background-color: #000000;
  color: #ffffff;
  padding: 12px 16px;
  border-radius: 8px;
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 32px;
  text-align: center;
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
</style>


```

```vue
<template>
  <main class="main-content">
    <div class="content-header">
      <h1 class="main-title">Starter Studies</h1>
      <p class="subtitle">把自己当公司来经营</p>
      
      <div class="tabs">
        <button class="tab active">CEO图书馆</button>
        <button class="tab">最近更新</button>
      </div>
    </div>

    <div class="content-cards-section">
      <div class="cards-container">
        <ContentCard
          v-for="card in cards"
          :key="card.id"
          :title="card.title"
          :description="card.description"
          :image="card.image"
        />
      </div>
    </div>

    <div class="content-bottom">
      <div class="tabs">
        <button class="tab active">系统阅读</button>
        <button class="tab">专题策展</button>
      </div>
      
      <FeatureGrid />
    </div>
  </main>
</template>

<script setup>
import { ref } from 'vue'
import ContentCard from './ContentCard.vue'
import FeatureGrid from './FeatureGrid.vue'

const cards = ref([
  {
    id: 1,
    title: '《别让猴子跳回背上》如何做一个合理的管理者(下)',
    description: '作为管理者,你的贡献来自于你的判断力与影响力,你的职责不是亲力亲为地背负所有猴子,而是要提供动力让其他人发挥所长。',
    image: 'https://images.unsplash.com/photo-1497366216548-37526070297c?w=400&h=250&fit=crop'
  },
  {
    id: 2,
    title: '《别让猴子跳回背上》为什么领导没时间,下属没事做?(上)',
    description: '一旦你接受了这些本不属于你的猴子,一个更严重的问题便随之而来:你为什么越努力,反而越忙乱?',
    image: 'https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=400&h=250&fit=crop'
  },
  {
    id: 3,
    title: '《上瘾》如何培养用户的使用习惯?(下)',
    description: '成功的习惯养成类产品,本质上是将用户面临的问题与产品提供的解决方案,通过一次又一次的循环,紧密地联系在一起,直至这种联系变成一种近乎本能的反应。',
    image: 'https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=400&h=250&fit=crop'
  },
  {
    id: 4,
    title: '《上瘾》可或缺的-',
    description: '在这个注意上你的产品惯"用你的产品生死和',
    image: 'https://images.unsplash.com/photo-1542744173-8e7e53415bb0?w=400&h=250&fit=crop'
  }
])
</script>

<style scoped>
.main-content {
  flex: 1;
  padding: 40px 48px;
  background-color: #ffffff;
  overflow-y: auto;
  min-width: 0;
}

.content-header {
  margin-bottom: 40px;
}

.main-title {
  font-size: 48px;
  font-weight: 700;
  color: #000000;
  margin-bottom: 8px;
}

.subtitle {
  font-size: 18px;
  color: #666666;
  margin-bottom: 32px;
}

.tabs {
  display: flex;
  gap: 32px;
  border-bottom: 1px solid #e0e0e0;
}

.tab {
  padding: 12px 0;
  background: none;
  border: none;
  font-size: 16px;
  color: #666666;
  cursor: pointer;
  position: relative;
  transition: color 0.2s;
}

.tab:hover {
  color: #000000;
}

.tab.active {
  color: #000000;
}

.tab.active::after {
  content: '';
  position: absolute;
  bottom: -1px;
  left: 0;
  right: 0;
  height: 2px;
  background-color: #000000;
}

.content-cards-section {
  margin-bottom: 60px;
}

.cards-container {
  display: flex;
  gap: 24px;
  overflow-x: auto;
  padding-bottom: 16px;
  scrollbar-width: thin;
  scrollbar-color: #c0c0c0 #f0f0f0;
}

.cards-container::-webkit-scrollbar {
  height: 8px;
}

.cards-container::-webkit-scrollbar-track {
  background: #f0f0f0;
  border-radius: 4px;
}

.cards-container::-webkit-scrollbar-thumb {
  background: #c0c0c0;
  border-radius: 4px;
}

.cards-container::-webkit-scrollbar-thumb:hover {
  background: #a0a0a0;
}

.content-bottom {
  margin-top: 60px;
}
</style>


```

```vue
<template>
  <div class="feature-grid">
    <div class="feature-item">
      <svg class="feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path>
        <polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline>
        <line x1="12" y1="22.08" x2="12" y2="12"></line>
      </svg>
      <span class="feature-text">战略部</span>
    </div>
    <div class="feature-item">
      <svg class="feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
      </svg>
      <span class="feature-text">品牌部</span>
    </div>
    <div class="feature-item">
      <svg class="feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <circle cx="12" cy="12" r="10"></circle>
        <circle cx="12" cy="12" r="3"></circle>
        <line x1="12" y1="1" x2="12" y2="3"></line>
        <line x1="12" y1="21" x2="12" y2="23"></line>
        <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
        <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
        <line x1="1" y1="12" x2="3" y2="12"></line>
        <line x1="21" y1="12" x2="23" y2="12"></line>
        <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
        <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
      </svg>
      <span class="feature-text">运营部</span>
    </div>
    <div class="feature-item">
      <svg class="feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6"></path>
        <path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18"></path>
        <path d="M4 22h16"></path>
        <path d="M10 14.66V17c0 .55-.47.98-.97 1.21C7.85 18.75 7 20.24 7 22"></path>
        <path d="M14 14.66V17c0 .55.47.98.97 1.21C16.15 18.75 17 20.24 17 22"></path>
        <path d="M18 2H6v7a6 6 0 0 0 12 0V2Z"></path>
      </svg>
      <span class="feature-text">销售部</span>
    </div>
  </div>
</template>

<script setup>
</script>

<style scoped>
.feature-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 24px;
  margin-top: 32px;
}

.feature-item {
  aspect-ratio: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 16px;
  background-color: #f8f8f8;
  border-radius: 12px;
  transition: background-color 0.2s, transform 0.2s;
  cursor: pointer;
}

.feature-item:hover {
  background-color: #f0f0f0;
  transform: translateY(-2px);
}

.feature-icon {
  width: 40px;
  height: 40px;
  color: #000000;
  stroke: currentColor;
  stroke-width: 1.5;
  fill: none;
}

.feature-text {
  font-size: 16px;
  font-weight: 500;
  color: #000000;
}
</style>


```


进行最后的样式优化，确保更贴近原设计：


```vue
<template>
  <main class="main-content">
    <div class="content-header">
      <h1 class="main-title">Starter Studies</h1>
      <p class="subtitle">把自己当公司来经营</p>
      
      <div class="tabs">
        <button class="tab active">CEO图书馆</button>
        <button class="tab">最近更新</button>
      </div>
    </div>

    <div class="content-cards-section">
      <div class="cards-container">
        <ContentCard
          v-for="card in cards"
          :key="card.id"
          :title="card.title"
          :description="card.description"
          :image="card.image"
        />
      </div>
    </div>

    <div class="content-bottom">
      <div class="tabs">
        <button class="tab active">系统阅读</button>
        <button class="tab">专题策展</button>
      </div>
      
      <FeatureGrid />
    </div>
  </main>
</template>

<script setup>
import { ref } from 'vue'
import ContentCard from './ContentCard.vue'
import FeatureGrid from './FeatureGrid.vue'

const cards = ref([
  {
    id: 1,
    title: '《别让猴子跳回背上》如何做一个合理的管理者(下)',
    description: '作为管理者,你的贡献来自于你的判断力与影响力,你的职责不是亲力亲为地背负所有猴子,而是要提供动力让其他人发挥所长。',
    image: 'https://images.unsplash.com/photo-1497366216548-37526070297c?w=400&h=250&fit=crop'
  },
  {
    id: 2,
    title: '《别让猴子跳回背上》为什么领导没时间,下属没事做?(上)',
    description: '一旦你接受了这些本不属于你的猴子,一个更严重的问题便随之而来:你为什么越努力,反而越忙乱?',
    image: 'https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=400&h=250&fit=crop'
  },
  {
    id: 3,
    title: '《上瘾》如何培养用户的使用习惯?(下)',
    description: '成功的习惯养成类产品,本质上是将用户面临的问题与产品提供的解决方案,通过一次又一次的循环,紧密地联系在一起,直至这种联系变成一种近乎本能的反应。',
    image: 'https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=400&h=250&fit=crop'
  },
  {
    id: 4,
    title: '《上瘾》可或缺的-',
    description: '在这个注意上你的产品惯"用你的产品生死和',
    image: 'https://images.unsplash.com/photo-1542744173-8e7e53415bb0?w=400&h=250&fit=crop'
  }
])
</script>

<style scoped>
.main-content {
  flex: 1;
  padding: 40px 48px;
  background-color: #ffffff;
  overflow-y: auto;
  min-width: 0;
}

.content-header {
  margin-bottom: 40px;
}

.main-title {
  font-size: 42px;
  font-weight: 700;
  color: #000000;
  margin-bottom: 8px;
  letter-spacing: -0.5px;
}

.subtitle {
  font-size: 18px;
  color: #666666;
  margin-bottom: 32px;
}

.tabs {
  display: flex;
  gap: 32px;
  border-bottom: 1px solid #e0e0e0;
}

.tab {
  padding: 12px 0;
  background: none;
  border: none;
  font-size: 16px;
  color: #666666;
  cursor: pointer;
  position: relative;
  transition: color 0.2s;
}

.tab:hover {
  color: #000000;
}

.tab.active {
  color: #000000;
}

.tab.active::after {
  content: '';
  position: absolute;
  bottom: -1px;
  left: 0;
  right: 0;
  height: 2px;
  background-color: #000000;
}

.content-cards-section {
  margin-bottom: 60px;
}

.cards-container {
  display: flex;
  gap: 24px;
  overflow-x: auto;
  padding-bottom: 16px;
  scrollbar-width: thin;
  scrollbar-color: #c0c0c0 #f0f0f0;
}

.cards-container::-webkit-scrollbar {
  height: 8px;
}

.cards-container::-webkit-scrollbar-track {
  background: #f0f0f0;
  border-radius: 4px;
}

.cards-container::-webkit-scrollbar-thumb {
  background: #c0c0c0;
  border-radius: 4px;
}

.cards-container::-webkit-scrollbar-thumb:hover {
  background: #a0a0a0;
}

.content-bottom {
  margin-top: 60px;
}
</style>


```

```vue
<template>
  <div class="content-card">
    <div class="card-image-wrapper">
      <img :src="image" :alt="title" class="card-image" />
      <span class="ai-tag">AI生成</span>
    </div>
    <div class="card-content">
      <h3 class="card-title">{{ title }}</h3>
      <p class="card-description">{{ description }}</p>
    </div>
  </div>
</template>

<script setup>
defineProps({
  title: {
    type: String,
    required: true
  },
  description: {
    type: String,
    required: true
  },
  image: {
    type: String,
    required: true
  }
})
</script>

<style scoped>
.content-card {
  min-width: 300px;
  max-width: 300px;
  background-color: #ffffff;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.06);
  transition: transform 0.2s, box-shadow 0.2s;
  flex-shrink: 0;
}

.content-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.12);
}

.card-image-wrapper {
  position: relative;
  width: 100%;
  height: 200px;
  overflow: hidden;
  background-color: #f0f0f0;
}

.card-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.ai-tag {
  position: absolute;
  top: 12px;
  left: 12px;
  background-color: rgba(0, 0, 0, 0.6);
  color: #ffffff;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 12px;
}

.card-content {
  padding: 20px;
}

.card-title {
  font-size: 18px;
  font-weight: 600;
  color: #000000;
  margin-bottom: 12px;
  line-height: 1.4;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.card-description {
  font-size: 14px;
  color: #666666;
  line-height: 1.6;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>


```

```vue
<template>
  <div class="content-card">
    <div class="card-image-wrapper">
      <img :src="image" :alt="title" class="card-image" />
      <span class="ai-tag">AI生成</span>
    </div>
    <div class="card-content">
      <h3 class="card-title">{{ title }}</h3>
      <p class="card-description">{{ description }}</p>
    </div>
  </div>
</template>

<script setup>
defineProps({
  title: {
    type: String,
    required: true
  },
  description: {
    type: String,
    required: true
  },
  image: {
    type: String,
    required: true
  }
})
</script>

<style scoped>
.content-card {
  min-width: 300px;
  max-width: 300px;
  background-color: #ffffff;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.06);
  transition: transform 0.2s, box-shadow 0.2s;
  flex-shrink: 0;
}

.content-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.12);
}

.card-image-wrapper {
  position: relative;
  width: 100%;
  height: 180px;
  overflow: hidden;
  background-color: #f0f0f0;
}

.card-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.ai-tag {
  position: absolute;
  top: 12px;
  left: 12px;
  background-color: rgba(0, 0, 0, 0.6);
  color: #ffffff;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 12px;
}

.card-content {
  padding: 20px;
}

.card-title {
  font-size: 18px;
  font-weight: 600;
  color: #000000;
  margin-bottom: 12px;
  line-height: 1.4;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.card-description {
  font-size: 14px;
  color: #666666;
  line-height: 1.6;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>


```

```vue
<template>
  <div class="content-card">
    <div class="card-image-wrapper">
      <img :src="image" :alt="title" class="card-image" />
      <span class="ai-tag">AI生成</span>
    </div>
    <div class="card-content">
      <h3 class="card-title">{{ title }}</h3>
      <p class="card-description">{{ description }}</p>
    </div>
  </div>
</template>

<script setup>
defineProps({
  title: {
    type: String,
    required: true
  },
  description: {
    type: String,
    required: true
  },
  image: {
    type: String,
    required: true
  }
})
</script>

<style scoped>
.content-card {
  min-width: 300px;
  max-width: 300px;
  background-color: #ffffff;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.06);
  transition: transform 0.2s, box-shadow 0.2s;
  flex-shrink: 0;
}

.content-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.12);
}

.card-image-wrapper {
  position: relative;
  width: 100%;
  height: 180px;
  overflow: hidden;
  background-color: #f0f0f0;
}

.card-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.ai-tag {
  position: absolute;
  top: 8px;
  left: 8px;
  background-color: rgba(0, 0, 0, 0.7);
  color: #ffffff;
  padding: 3px 6px;
  border-radius: 3px;
  font-size: 11px;
}

.card-content {
  padding: 20px;
}

.card-title {
  font-size: 18px;
  font-weight: 600;
  color: #000000;
  margin-bottom: 12px;
  line-height: 1.4;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.card-description {
  font-size: 14px;
  color: #666666;
  line-height: 1.6;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>


```

```vue
<template>
  <div class="content-card">
    <div class="card-image-wrapper">
      <img :src="image" :alt="title" class="card-image" />
      <span class="ai-tag">AI生成</span>
    </div>
    <div class="card-content">
      <h3 class="card-title">{{ title }}</h3>
      <p class="card-description">{{ description }}</p>
    </div>
  </div>
</template>

<script setup>
defineProps({
  title: {
    type: String,
    required: true
  },
  description: {
    type: String,
    required: true
  },
  image: {
    type: String,
    required: true
  }
})
</script>

<style scoped>
.content-card {
  min-width: 300px;
  max-width: 300px;
  background-color: #ffffff;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.06);
  transition: transform 0.2s, box-shadow 0.2s;
  flex-shrink: 0;
}

.content-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.12);
}

.card-image-wrapper {
  position: relative;
  width: 100%;
  height: 180px;
  overflow: hidden;
  background-color: #f0f0f0;
}

.card-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.ai-tag {
  position: absolute;
  top: 8px;
  left: 8px;
  background-color: rgba(0, 0, 0, 0.7);
  color: #ffffff;
  padding: 3px 6px;
  border-radius: 3px;
  font-size: 11px;
}

.card-content {
  padding: 16px;
}

.card-title {
  font-size: 18px;
  font-weight: 600;
  color: #000000;
  margin-bottom: 12px;
  line-height: 1.4;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.card-description {
  font-size: 14px;
  color: #666666;
  line-height: 1.6;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>


```

```vue
<template>
  <div class="content-card">
    <div class="card-image-wrapper">
      <img :src="image" :alt="title" class="card-image" />
      <span class="ai-tag">AI生成</span>
    </div>
    <div class="card-content">
      <h3 class="card-title">{{ title }}</h3>
      <p class="card-description">{{ description }}</p>
    </div>
  </div>
</template>

<script setup>
defineProps({
  title: {
    type: String,
    required: true
  },
  description: {
    type: String,
    required: true
  },
  image: {
    type: String,
    required: true
  }
})
</script>

<style scoped>
.content-card {
  min-width: 300px;
  max-width: 300px;
  background-color: #ffffff;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.06);
  transition: transform 0.2s, box-shadow 0.2s;
  flex-shrink: 0;
}

.content-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.12);
}

.card-image-wrapper {
  position: relative;
  width: 100%;
  height: 180px;
  overflow: hidden;
  background-color: #f0f0f0;
}

.card-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.ai-tag {
  position: absolute;
  top: 8px;
  left: 8px;
  background-color: rgba(0, 0, 0, 0.7);
  color: #ffffff;
  padding: 3px 6px;
  border-radius: 3px;
  font-size: 11px;
}

.card-content {
  padding: 16px;
}

.card-title {
  font-size: 16px;
  font-weight: 600;
  color: #000000;
  margin-bottom: 10px;
  line-height: 1.5;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.card-description {
  font-size: 14px;
  color: #666666;
  line-height: 1.6;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>


```

```vue
<template>
  <div class="content-card">
    <div class="card-image-wrapper">
      <img :src="image" :alt="title" class="card-image" />
      <span class="ai-tag">AI生成</span>
    </div>
    <div class="card-content">
      <h3 class="card-title">{{ title }}</h3>
      <p class="card-description">{{ description }}</p>
    </div>
  </div>
</template>

<script setup>
defineProps({
  title: {
    type: String,
    required: true
  },
  description: {
    type: String,
    required: true
  },
  image: {
    type: String,
    required: true
  }
})
</script>

<style scoped>
.content-card {
  min-width: 300px;
  max-width: 300px;
  background-color: #ffffff;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.06);
  transition: transform 0.2s, box-shadow 0.2s;
  flex-shrink: 0;
}

.content-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.12);
}

.card-image-wrapper {
  position: relative;
  width: 100%;
  height: 180px;
  overflow: hidden;
  background-color: #f0f0f0;
}

.card-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.ai-tag {
  position: absolute;
  top: 8px;
  left: 8px;
  background-color: rgba(0, 0, 0, 0.7);
  color: #ffffff;
  padding: 3px 6px;
  border-radius: 3px;
  font-size: 11px;
}

.card-content {
  padding: 16px;
}

.card-title {
  font-size: 16px;
  font-weight: 600;
  color: #000000;
  margin-bottom: 10px;
  line-height: 1.5;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.card-description {
  font-size: 13px;
  color: #666666;
  line-height: 1.6;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>


```

```vue
<template>
  <main class="main-content">
    <div class="content-header">
      <h1 class="main-title">Starter Studies</h1>
      <p class="subtitle">把自己当公司来经营</p>
      
      <div class="tabs">
        <button class="tab active">CEO图书馆</button>
        <button class="tab">最近更新</button>
      </div>
    </div>

    <div class="content-cards-section">
      <div class="cards-container">
        <ContentCard
          v-for="card in cards"
          :key="card.id"
          :title="card.title"
          :description="card.description"
          :image="card.image"
        />
      </div>
    </div>

    <div class="content-bottom">
      <div class="tabs">
        <button class="tab active">系统阅读</button>
        <button class="tab">专题策展</button>
      </div>
      
      <FeatureGrid />
    </div>
  </main>
</template>

<script setup>
import { ref } from 'vue'
import ContentCard from './ContentCard.vue'
import FeatureGrid from './FeatureGrid.vue'

const cards = ref([
  {
    id: 1,
    title: '《别让猴子跳回背上》如何做一个合理的管理者(下)',
    description: '作为管理者,你的贡献来自于你的判断力与影响力,你的职责不是亲力亲为地背负所有猴子,而是要提供动力让其他人发挥所长。',
    image: 'https://images.unsplash.com/photo-1497366216548-37526070297c?w=400&h=250&fit=crop'
  },
  {
    id: 2,
    title: '《别让猴子跳回背上》为什么领导没时间,下属没事做?(上)',
    description: '一旦你接受了这些本不属于你的猴子,一个更严重的问题便随之而来:你为什么越努力,反而越忙乱?',
    image: 'https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=400&h=250&fit=crop'
  },
  {
    id: 3,
    title: '《上瘾》如何培养用户的使用习惯?(下)',
    description: '成功的习惯养成类产品,本质上是将用户面临的问题与产品提供的解决方案,通过一次又一次的循环,紧密地联系在一起,直至这种联系变成一种近乎本能的反应。',
    image: 'https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=400&h=250&fit=crop'
  },
  {
    id: 4,
    title: '《上瘾》可或缺的-',
    description: '在这个注意上你的产品惯"用你的产品生死和',
    image: 'https://images.unsplash.com/photo-1542744173-8e7e53415bb0?w=400&h=250&fit=crop'
  }
])
</script>

<style scoped>
.main-content {
  flex: 1;
  padding: 40px 48px;
  background-color: #ffffff;
  overflow-y: auto;
  min-width: 0;
}

.content-header {
  margin-bottom: 40px;
}

.main-title {
  font-size: 42px;
  font-weight: 700;
  color: #000000;
  margin-bottom: 8px;
  letter-spacing: -0.5px;
}

.subtitle {
  font-size: 18px;
  color: #666666;
  margin-bottom: 32px;
}

.tabs {
  display: flex;
  gap: 32px;
  border-bottom: 1px solid #e0e0e0;
}

.tab {
  padding: 12px 0;
  background: none;
  border: none;
  font-size: 16px;
  color: #666666;
  cursor: pointer;
  position: relative;
  transition: color 0.2s;
}

.tab:hover {
  color: #000000;
}

.tab.active {
  color: #000000;
}

.tab.active::after {
  content: '';
  position: absolute;
  bottom: -1px;
  left: 0;
  right: 0;
  height: 2px;
  background-color: #000000;
}

.content-cards-section {
  margin-bottom: 60px;
}

.cards-container {
  display: flex;
  gap: 20px;
  overflow-x: auto;
  padding-bottom: 16px;
  scrollbar-width: thin;
  scrollbar-color: #c0c0c0 #f0f0f0;
}

.cards-container::-webkit-scrollbar {
  height: 8px;
}

.cards-container::-webkit-scrollbar-track {
  background: #f0f0f0;
  border-radius: 4px;
}

.cards-container::-webkit-scrollbar-thumb {
  background: #c0c0c0;
  border-radius: 4px;
}

.cards-container::-webkit-scrollbar-thumb:hover {
  background: #a0a0a0;
}

.content-bottom {
  margin-top: 60px;
}
</style>


```

```vue
<template>
  <div class="feature-grid">
    <div class="feature-item">
      <svg class="feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path>
        <polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline>
        <line x1="12" y1="22.08" x2="12" y2="12"></line>
      </svg>
      <span class="feature-text">战略部</span>
    </div>
    <div class="feature-item">
      <svg class="feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
      </svg>
      <span class="feature-text">品牌部</span>
    </div>
    <div class="feature-item">
      <svg class="feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <circle cx="12" cy="12" r="10"></circle>
        <circle cx="12" cy="12" r="3"></circle>
        <line x1="12" y1="1" x2="12" y2="3"></line>
        <line x1="12" y1="21" x2="12" y2="23"></line>
        <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
        <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
        <line x1="1" y1="12" x2="3" y2="12"></line>
        <line x1="21" y1="12" x2="23" y2="12"></line>
        <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
        <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
      </svg>
      <span class="feature-text">运营部</span>
    </div>
    <div class="feature-item">
      <svg class="feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6"></path>
        <path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18"></path>
        <path d="M4 22h16"></path>
        <path d="M10 14.66V17c0 .55-.47.98-.97 1.21C7.85 18.75 7 20.24 7 22"></path>
        <path d="M14 14.66V17c0 .55.47.98.97 1.21C16.15 18.75 17 20.24 17 22"></path>
        <path d="M18 2H6v7a6 6 0 0 0 12 0V2Z"></path>
      </svg>
      <span class="feature-text">销售部</span>
    </div>
  </div>
</template>

<script setup>
</script>

<style scoped>
.feature-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
  margin-top: 32px;
}

.feature-item {
  aspect-ratio: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 16px;
  background-color: #f8f8f8;
  border-radius: 12px;
  transition: background-color 0.2s, transform 0.2s;
  cursor: pointer;
}

.feature-item:hover {
  background-color: #f0f0f0;
  transform: translateY(-2px);
}

.feature-icon {
  width: 40px;
  height: 40px;
  color: #000000;
  stroke: currentColor;
  stroke-width: 1.5;
  fill: none;
}

.feature-text {
  font-size: 16px;
  font-weight: 500;
  color: #000000;
}
</style>


```

```vue
<template>
  <div class="feature-grid">
    <div class="feature-item">
      <svg class="feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path>
        <polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline>
        <line x1="12" y1="22.08" x2="12" y2="12"></line>
      </svg>
      <span class="feature-text">战略部</span>
    </div>
    <div class="feature-item">
      <svg class="feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
      </svg>
      <span class="feature-text">品牌部</span>
    </div>
    <div class="feature-item">
      <svg class="feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <circle cx="12" cy="12" r="10"></circle>
        <circle cx="12" cy="12" r="3"></circle>
        <line x1="12" y1="1" x2="12" y2="3"></line>
        <line x1="12" y1="21" x2="12" y2="23"></line>
        <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
        <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
        <line x1="1" y1="12" x2="3" y2="12"></line>
        <line x1="21" y1="12" x2="23" y2="12"></line>
        <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
        <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
      </svg>
      <span class="feature-text">运营部</span>
    </div>
    <div class="feature-item">
      <svg class="feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6"></path>
        <path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18"></path>
        <path d="M4 22h16"></path>
        <path d="M10 14.66V17c0 .55-.47.98-.97 1.21C7.85 18.75 7 20.24 7 22"></path>
        <path d="M14 14.66V17c0 .55.47.98.97 1.21C16.15 18.75 17 20.24 17 22"></path>
        <path d="M18 2H6v7a6 6 0 0 0 12 0V2Z"></path>
      </svg>
      <span class="feature-text">销售部</span>
    </div>
  </div>
</template>

<script setup>
</script>

<style scoped>
.feature-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
  margin-top: 32px;
}

.feature-item {
  aspect-ratio: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 12px;
  background-color: #f8f8f8;
  border-radius: 8px;
  transition: background-color 0.2s, transform 0.2s;
  cursor: pointer;
  padding: 20px;
}

.feature-item:hover {
  background-color: #f0f0f0;
  transform: translateY(-2px);
}

.feature-icon {
  width: 40px;
  height: 40px;
  color: #000000;
  stroke: currentColor;
  stroke-width: 1.5;
  fill: none;
}

.feature-text {
  font-size: 16px;
  font-weight: 500;
  color: #000000;
}
</style>


```

```vue
<template>
  <div class="feature-grid">
    <div class="feature-item">
      <svg class="feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path>
        <polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline>
        <line x1="12" y1="22.08" x2="12" y2="12"></line>
      </svg>
      <span class="feature-text">战略部</span>
    </div>
    <div class="feature-item">
      <svg class="feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
      </svg>
      <span class="feature-text">品牌部</span>
    </div>
    <div class="feature-item">
      <svg class="feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <circle cx="12" cy="12" r="10"></circle>
        <circle cx="12" cy="12" r="3"></circle>
        <line x1="12" y1="1" x2="12" y2="3"></line>
        <line x1="12" y1="21" x2="12" y2="23"></line>
        <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
        <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
        <line x1="1" y1="12" x2="3" y2="12"></line>
        <line x1="21" y1="12" x2="23" y2="12"></line>
        <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
        <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
      </svg>
      <span class="feature-text">运营部</span>
    </div>
    <div class="feature-item">
      <svg class="feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6"></path>
        <path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18"></path>
        <path d="M4 22h16"></path>
        <path d="M10 14.66V17c0 .55-.47.98-.97 1.21C7.85 18.75 7 20.24 7 22"></path>
        <path d="M14 14.66V17c0 .55.47.98.97 1.21C16.15 18.75 17 20.24 17 22"></path>
        <path d="M18 2H6v7a6 6 0 0 0 12 0V2Z"></path>
      </svg>
      <span class="feature-text">销售部</span>
    </div>
  </div>
</template>

<script setup>
</script>

<style scoped>
.feature-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
  margin-top: 32px;
}

.feature-item {
  aspect-ratio: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 12px;
  background-color: #f8f8f8;
  border-radius: 8px;
  transition: background-color 0.2s, transform 0.2s;
  cursor: pointer;
  padding: 20px;
}

.feature-item:hover {
  background-color: #f0f0f0;
  transform: translateY(-2px);
}

.feature-icon {
  width: 40px;
  height: 40px;
  color: #000000;
  stroke: currentColor;
  stroke-width: 1.5;
  fill: none;
}

.feature-text {
  font-size: 15px;
  font-weight: 500;
  color: #000000;
}
</style>


```


已完成 Vue 页面的还原。已创建以下组件：

1. **App.vue** - 主布局，包含侧边栏和主内容区域
2. **Sidebar.vue** - 左侧边栏，包含：
   - Logo "Pitch."
   - 导航菜单（学习、牛人、链接、项目、活动、我的）
   - 底部按钮（首页、名片）
   - 用户信息（头像、用户名、通知图标）
3. **MainContent.vue** - 主内容区域，包含：
   - 标题和副标题
   - 标签页（CEO图书馆、最近更新）
   - 内容卡片横向滚动区域
   - 底部标签和功能网格
4. **ContentCard.vue** - 内容卡片组件，包含图片、AI标签、标题和描述
5. **FeatureGrid.vue** - 功能块网格（2x2），包含战略部、品牌部、运营部、销售部

页面特点：
- 响应式布局，侧边栏固定宽度，主内容自适应
- 样式贴近原设计（颜色、间距、字体）
- 交互效果（悬停、激活状态）
- 横向滚动的内容卡片
- SVG 图标

运行 `npm run dev` 查看效果。页面应已还原为与原设计一致的界面。

---

**User**

这是目前生成的页面 注意到CEO图书馆和最近的更新不是两个标签而是同一个 这个网站向下拉会出现我贴的图片这样的内容 继续修改

---

**Cursor**


查看当前代码，然后根据新需求更新页面：



根据新需求更新页面：将顶部标签改为按钮样式，并添加向下滚动后的新内容区域。


```vue
<template>
  <main class="main-content">
    <div class="content-header">
      <h1 class="main-title">Starter Studies</h1>
      <p class="subtitle">把自己当公司来经营</p>
      
      <div class="header-tabs">
        <button class="header-tab active">CEO图书馆</button>
        <button class="header-tab">最近更新</button>
      </div>
    </div>

    <div class="content-cards-section">
      <div class="cards-container">
        <ContentCard
          v-for="card in cards"
          :key="card.id"
          :title="card.title"
          :description="card.description"
          :image="card.image"
        />
      </div>
    </div>

    <div class="content-bottom">
      <div class="tabs">
        <button class="tab active">系统阅读</button>
        <button class="tab">专题策展</button>
      </div>
      
      <FeatureGrid />
    </div>
  </main>
</template>

<script setup>
import { ref } from 'vue'
import ContentCard from './ContentCard.vue'
import FeatureGrid from './FeatureGrid.vue'

const cards = ref([
  {
    id: 1,
    title: '《别让猴子跳回背上》如何做一个合理的管理者(下)',
    description: '作为管理者,你的贡献来自于你的判断力与影响力,你的职责不是亲力亲为地背负所有猴子,而是要提供动力让其他人发挥所长。',
    image: 'https://images.unsplash.com/photo-1497366216548-37526070297c?w=400&h=250&fit=crop'
  },
  {
    id: 2,
    title: '《别让猴子跳回背上》为什么领导没时间,下属没事做?(上)',
    description: '一旦你接受了这些本不属于你的猴子,一个更严重的问题便随之而来:你为什么越努力,反而越忙乱?',
    image: 'https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=400&h=250&fit=crop'
  },
  {
    id: 3,
    title: '《上瘾》如何培养用户的使用习惯?(下)',
    description: '成功的习惯养成类产品,本质上是将用户面临的问题与产品提供的解决方案,通过一次又一次的循环,紧密地联系在一起,直至这种联系变成一种近乎本能的反应。',
    image: 'https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=400&h=250&fit=crop'
  },
  {
    id: 4,
    title: '《上瘾》可或缺的-',
    description: '在这个注意上你的产品惯"用你的产品生死和',
    image: 'https://images.unsplash.com/photo-1542744173-8e7e53415bb0?w=400&h=250&fit=crop'
  }
])
</script>

<style scoped>
.main-content {
  flex: 1;
  padding: 40px 48px;
  background-color: #ffffff;
  overflow-y: auto;
  min-width: 0;
}

.content-header {
  margin-bottom: 40px;
}

.main-title {
  font-size: 42px;
  font-weight: 700;
  color: #000000;
  margin-bottom: 8px;
  letter-spacing: -0.5px;
}

.subtitle {
  font-size: 18px;
  color: #666666;
  margin-bottom: 32px;
}

.tabs {
  display: flex;
  gap: 32px;
  border-bottom: 1px solid #e0e0e0;
}

.tab {
  padding: 12px 0;
  background: none;
  border: none;
  font-size: 16px;
  color: #666666;
  cursor: pointer;
  position: relative;
  transition: color 0.2s;
}

.tab:hover {
  color: #000000;
}

.tab.active {
  color: #000000;
}

.tab.active::after {
  content: '';
  position: absolute;
  bottom: -1px;
  left: 0;
  right: 0;
  height: 2px;
  background-color: #000000;
}

.content-cards-section {
  margin-bottom: 60px;
}

.cards-container {
  display: flex;
  gap: 20px;
  overflow-x: auto;
  padding-bottom: 16px;
  scrollbar-width: thin;
  scrollbar-color: #c0c0c0 #f0f0f0;
}

.cards-container::-webkit-scrollbar {
  height: 8px;
}

.cards-container::-webkit-scrollbar-track {
  background: #f0f0f0;
  border-radius: 4px;
}

.cards-container::-webkit-scrollbar-thumb {
  background: #c0c0c0;
  border-radius: 4px;
}

.cards-container::-webkit-scrollbar-thumb:hover {
  background: #a0a0a0;
}

.content-bottom {
  margin-top: 60px;
}
</style>


```

```vue
<template>
  <main class="main-content">
    <div class="content-header">
      <h1 class="main-title">Starter Studies</h1>
      <p class="subtitle">把自己当公司来经营</p>
      
      <div class="header-tabs">
        <button class="header-tab active">CEO图书馆</button>
        <button class="header-tab">最近更新</button>
      </div>
    </div>

    <div class="content-cards-section">
      <div class="cards-container">
        <ContentCard
          v-for="card in cards"
          :key="card.id"
          :title="card.title"
          :description="card.description"
          :image="card.image"
        />
      </div>
    </div>

    <div class="content-bottom">
      <FeatureGrid />
      
      <ContentFilters />
      
      <ArticleList />
    </div>
  </main>
</template>

<script setup>
import { ref } from 'vue'
import ContentCard from './ContentCard.vue'
import FeatureGrid from './FeatureGrid.vue'

const cards = ref([
  {
    id: 1,
    title: '《别让猴子跳回背上》如何做一个合理的管理者(下)',
    description: '作为管理者,你的贡献来自于你的判断力与影响力,你的职责不是亲力亲为地背负所有猴子,而是要提供动力让其他人发挥所长。',
    image: 'https://images.unsplash.com/photo-1497366216548-37526070297c?w=400&h=250&fit=crop'
  },
  {
    id: 2,
    title: '《别让猴子跳回背上》为什么领导没时间,下属没事做?(上)',
    description: '一旦你接受了这些本不属于你的猴子,一个更严重的问题便随之而来:你为什么越努力,反而越忙乱?',
    image: 'https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=400&h=250&fit=crop'
  },
  {
    id: 3,
    title: '《上瘾》如何培养用户的使用习惯?(下)',
    description: '成功的习惯养成类产品,本质上是将用户面临的问题与产品提供的解决方案,通过一次又一次的循环,紧密地联系在一起,直至这种联系变成一种近乎本能的反应。',
    image: 'https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=400&h=250&fit=crop'
  },
  {
    id: 4,
    title: '《上瘾》可或缺的-',
    description: '在这个注意上你的产品惯"用你的产品生死和',
    image: 'https://images.unsplash.com/photo-1542744173-8e7e53415bb0?w=400&h=250&fit=crop'
  }
])
</script>

<style scoped>
.main-content {
  flex: 1;
  padding: 40px 48px;
  background-color: #ffffff;
  overflow-y: auto;
  min-width: 0;
}

.content-header {
  margin-bottom: 40px;
}

.main-title {
  font-size: 42px;
  font-weight: 700;
  color: #000000;
  margin-bottom: 8px;
  letter-spacing: -0.5px;
}

.subtitle {
  font-size: 18px;
  color: #666666;
  margin-bottom: 32px;
}

.tabs {
  display: flex;
  gap: 32px;
  border-bottom: 1px solid #e0e0e0;
}

.tab {
  padding: 12px 0;
  background: none;
  border: none;
  font-size: 16px;
  color: #666666;
  cursor: pointer;
  position: relative;
  transition: color 0.2s;
}

.tab:hover {
  color: #000000;
}

.tab.active {
  color: #000000;
}

.tab.active::after {
  content: '';
  position: absolute;
  bottom: -1px;
  left: 0;
  right: 0;
  height: 2px;
  background-color: #000000;
}

.content-cards-section {
  margin-bottom: 60px;
}

.cards-container {
  display: flex;
  gap: 20px;
  overflow-x: auto;
  padding-bottom: 16px;
  scrollbar-width: thin;
  scrollbar-color: #c0c0c0 #f0f0f0;
}

.cards-container::-webkit-scrollbar {
  height: 8px;
}

.cards-container::-webkit-scrollbar-track {
  background: #f0f0f0;
  border-radius: 4px;
}

.cards-container::-webkit-scrollbar-thumb {
  background: #c0c0c0;
  border-radius: 4px;
}

.cards-container::-webkit-scrollbar-thumb:hover {
  background: #a0a0a0;
}

.content-bottom {
  margin-top: 60px;
}
</style>


```

```vue
<template>
  <main class="main-content">
    <div class="content-header">
      <h1 class="main-title">Starter Studies</h1>
      <p class="subtitle">把自己当公司来经营</p>
      
      <div class="header-tabs">
        <button class="header-tab active">CEO图书馆</button>
        <button class="header-tab">最近更新</button>
      </div>
    </div>

    <div class="content-cards-section">
      <div class="cards-container">
        <ContentCard
          v-for="card in cards"
          :key="card.id"
          :title="card.title"
          :description="card.description"
          :image="card.image"
        />
      </div>
    </div>

    <div class="content-bottom">
      <FeatureGrid />
      
      <ContentFilters />
      
      <ArticleList />
    </div>
  </main>
</template>

<script setup>
import { ref } from 'vue'
import ContentCard from './ContentCard.vue'
import FeatureGrid from './FeatureGrid.vue'
import ContentFilters from './ContentFilters.vue'
import ArticleList from './ArticleList.vue'

const cards = ref([
  {
    id: 1,
    title: '《别让猴子跳回背上》如何做一个合理的管理者(下)',
    description: '作为管理者,你的贡献来自于你的判断力与影响力,你的职责不是亲力亲为地背负所有猴子,而是要提供动力让其他人发挥所长。',
    image: 'https://images.unsplash.com/photo-1497366216548-37526070297c?w=400&h=250&fit=crop'
  },
  {
    id: 2,
    title: '《别让猴子跳回背上》为什么领导没时间,下属没事做?(上)',
    description: '一旦你接受了这些本不属于你的猴子,一个更严重的问题便随之而来:你为什么越努力,反而越忙乱?',
    image: 'https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=400&h=250&fit=crop'
  },
  {
    id: 3,
    title: '《上瘾》如何培养用户的使用习惯?(下)',
    description: '成功的习惯养成类产品,本质上是将用户面临的问题与产品提供的解决方案,通过一次又一次的循环,紧密地联系在一起,直至这种联系变成一种近乎本能的反应。',
    image: 'https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=400&h=250&fit=crop'
  },
  {
    id: 4,
    title: '《上瘾》可或缺的-',
    description: '在这个注意上你的产品惯"用你的产品生死和',
    image: 'https://images.unsplash.com/photo-1542744173-8e7e53415bb0?w=400&h=250&fit=crop'
  }
])
</script>

<style scoped>
.main-content {
  flex: 1;
  padding: 40px 48px;
  background-color: #ffffff;
  overflow-y: auto;
  min-width: 0;
}

.content-header {
  margin-bottom: 40px;
}

.main-title {
  font-size: 42px;
  font-weight: 700;
  color: #000000;
  margin-bottom: 8px;
  letter-spacing: -0.5px;
}

.subtitle {
  font-size: 18px;
  color: #666666;
  margin-bottom: 32px;
}

.tabs {
  display: flex;
  gap: 32px;
  border-bottom: 1px solid #e0e0e0;
}

.tab {
  padding: 12px 0;
  background: none;
  border: none;
  font-size: 16px;
  color: #666666;
  cursor: pointer;
  position: relative;
  transition: color 0.2s;
}

.tab:hover {
  color: #000000;
}

.tab.active {
  color: #000000;
}

.tab.active::after {
  content: '';
  position: absolute;
  bottom: -1px;
  left: 0;
  right: 0;
  height: 2px;
  background-color: #000000;
}

.content-cards-section {
  margin-bottom: 60px;
}

.cards-container {
  display: flex;
  gap: 20px;
  overflow-x: auto;
  padding-bottom: 16px;
  scrollbar-width: thin;
  scrollbar-color: #c0c0c0 #f0f0f0;
}

.cards-container::-webkit-scrollbar {
  height: 8px;
}

.cards-container::-webkit-scrollbar-track {
  background: #f0f0f0;
  border-radius: 4px;
}

.cards-container::-webkit-scrollbar-thumb {
  background: #c0c0c0;
  border-radius: 4px;
}

.cards-container::-webkit-scrollbar-thumb:hover {
  background: #a0a0a0;
}

.content-bottom {
  margin-top: 60px;
}
</style>


```

```vue
<template>
  <main class="main-content">
    <div class="content-header">
      <h1 class="main-title">Starter Studies</h1>
      <p class="subtitle">把自己当公司来经营</p>
      
      <div class="header-tabs">
        <button class="header-tab active">CEO图书馆</button>
        <button class="header-tab">最近更新</button>
      </div>
    </div>

    <div class="content-cards-section">
      <div class="cards-container">
        <ContentCard
          v-for="card in cards"
          :key="card.id"
          :title="card.title"
          :description="card.description"
          :image="card.image"
        />
      </div>
    </div>

    <div class="content-bottom">
      <FeatureGrid />
      
      <ContentFilters />
      
      <ArticleList />
    </div>
  </main>
</template>

<script setup>
import { ref } from 'vue'
import ContentCard from './ContentCard.vue'
import FeatureGrid from './FeatureGrid.vue'
import ContentFilters from './ContentFilters.vue'
import ArticleList from './ArticleList.vue'

const cards = ref([
  {
    id: 1,
    title: '《别让猴子跳回背上》如何做一个合理的管理者(下)',
    description: '作为管理者,你的贡献来自于你的判断力与影响力,你的职责不是亲力亲为地背负所有猴子,而是要提供动力让其他人发挥所长。',
    image: 'https://images.unsplash.com/photo-1497366216548-37526070297c?w=400&h=250&fit=crop'
  },
  {
    id: 2,
    title: '《别让猴子跳回背上》为什么领导没时间,下属没事做?(上)',
    description: '一旦你接受了这些本不属于你的猴子,一个更严重的问题便随之而来:你为什么越努力,反而越忙乱?',
    image: 'https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=400&h=250&fit=crop'
  },
  {
    id: 3,
    title: '《上瘾》如何培养用户的使用习惯?(下)',
    description: '成功的习惯养成类产品,本质上是将用户面临的问题与产品提供的解决方案,通过一次又一次的循环,紧密地联系在一起,直至这种联系变成一种近乎本能的反应。',
    image: 'https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=400&h=250&fit=crop'
  },
  {
    id: 4,
    title: '《上瘾》可或缺的-',
    description: '在这个注意上你的产品惯"用你的产品生死和',
    image: 'https://images.unsplash.com/photo-1542744173-8e7e53415bb0?w=400&h=250&fit=crop'
  }
])
</script>

<style scoped>
.main-content {
  flex: 1;
  padding: 40px 48px;
  background-color: #ffffff;
  overflow-y: auto;
  min-width: 0;
}

.content-header {
  margin-bottom: 40px;
}

.main-title {
  font-size: 42px;
  font-weight: 700;
  color: #000000;
  margin-bottom: 8px;
  letter-spacing: -0.5px;
}

.subtitle {
  font-size: 18px;
  color: #666666;
  margin-bottom: 32px;
}

.header-tabs {
  display: flex;
  gap: 12px;
}

.header-tab {
  padding: 10px 20px;
  border: none;
  border-radius: 6px;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.2s;
  background-color: #ffffff;
  color: #000000;
  border: 1px solid #e0e0e0;
}

.header-tab:hover {
  background-color: #f5f5f5;
}

.header-tab.active {
  background-color: #333333;
  color: #ffffff;
  border-color: #333333;
}

.content-cards-section {
  margin-bottom: 60px;
}

.cards-container {
  display: flex;
  gap: 20px;
  overflow-x: auto;
  padding-bottom: 16px;
  scrollbar-width: thin;
  scrollbar-color: #c0c0c0 #f0f0f0;
}

.cards-container::-webkit-scrollbar {
  height: 8px;
}

.cards-container::-webkit-scrollbar-track {
  background: #f0f0f0;
  border-radius: 4px;
}

.cards-container::-webkit-scrollbar-thumb {
  background: #c0c0c0;
  border-radius: 4px;
}

.cards-container::-webkit-scrollbar-thumb:hover {
  background: #a0a0a0;
}

.content-bottom {
  margin-top: 60px;
}
</style>


```

```vue
<template>
  <div class="feature-grid">
    <div class="feature-item">
      <svg class="feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path>
        <polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline>
        <line x1="12" y1="22.08" x2="12" y2="12"></line>
      </svg>
      <span class="feature-text">战略部</span>
    </div>
    <div class="feature-item">
      <svg class="feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
      </svg>
      <span class="feature-text">品牌部</span>
    </div>
    <div class="feature-item">
      <svg class="feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6"></path>
        <path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18"></path>
        <path d="M4 22h16"></path>
        <path d="M10 14.66V17c0 .55-.47.98-.97 1.21C7.85 18.75 7 20.24 7 22"></path>
        <path d="M14 14.66V17c0 .55.47.98.97 1.21C16.15 18.75 17 20.24 17 22"></path>
        <path d="M18 2H6v7a6 6 0 0 0 12 0V2Z"></path>
      </svg>
      <span class="feature-text">销售部</span>
    </div>
    <div class="feature-item">
      <svg class="feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <circle cx="12" cy="12" r="10"></circle>
        <circle cx="12" cy="12" r="3"></circle>
        <line x1="12" y1="1" x2="12" y2="3"></line>
        <line x1="12" y1="21" x2="12" y2="23"></line>
        <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
        <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
        <line x1="1" y1="12" x2="3" y2="12"></line>
        <line x1="21" y1="12" x2="23" y2="12"></line>
        <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
        <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
      </svg>
      <span class="feature-text">人力部</span>
    </div>
    <div class="feature-item">
      <svg class="feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
        <polyline points="14 2 14 8 20 8"></polyline>
        <line x1="16" y1="13" x2="8" y2="13"></line>
        <line x1="16" y1="17" x2="8" y2="17"></line>
        <polyline points="10 9 9 9 8 9"></polyline>
      </svg>
      <span class="feature-text">财法部</span>
    </div>
    <div class="feature-item">
      <svg class="feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect>
        <line x1="8" y1="21" x2="16" y2="21"></line>
        <line x1="12" y1="17" x2="12" y2="21"></line>
      </svg>
      <span class="feature-text">技术部</span>
    </div>
  </div>
</template>

<script setup>
</script>

<style scoped>
.feature-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
  margin-top: 32px;
}

.feature-item {
  aspect-ratio: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 12px;
  background-color: #f8f8f8;
  border-radius: 8px;
  transition: background-color 0.2s, transform 0.2s;
  cursor: pointer;
  padding: 20px;
}

.feature-item:hover {
  background-color: #f0f0f0;
  transform: translateY(-2px);
}

.feature-icon {
  width: 40px;
  height: 40px;
  color: #000000;
  stroke: currentColor;
  stroke-width: 1.5;
  fill: none;
}

.feature-text {
  font-size: 15px;
  font-weight: 500;
  color: #000000;
}
</style>


```

```vue
<template>
  <div class="feature-grid">
    <div class="feature-item">
      <svg class="feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path>
        <polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline>
        <line x1="12" y1="22.08" x2="12" y2="12"></line>
      </svg>
      <span class="feature-text">战略部</span>
    </div>
    <div class="feature-item">
      <svg class="feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
      </svg>
      <span class="feature-text">品牌部</span>
    </div>
    <div class="feature-item">
      <svg class="feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6"></path>
        <path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18"></path>
        <path d="M4 22h16"></path>
        <path d="M10 14.66V17c0 .55-.47.98-.97 1.21C7.85 18.75 7 20.24 7 22"></path>
        <path d="M14 14.66V17c0 .55.47.98.97 1.21C16.15 18.75 17 20.24 17 22"></path>
        <path d="M18 2H6v7a6 6 0 0 0 12 0V2Z"></path>
      </svg>
      <span class="feature-text">销售部</span>
    </div>
    <div class="feature-item">
      <svg class="feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <circle cx="12" cy="12" r="10"></circle>
        <circle cx="12" cy="12" r="3"></circle>
        <line x1="12" y1="1" x2="12" y2="3"></line>
        <line x1="12" y1="21" x2="12" y2="23"></line>
        <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
        <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
        <line x1="1" y1="12" x2="3" y2="12"></line>
        <line x1="21" y1="12" x2="23" y2="12"></line>
        <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
        <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
      </svg>
      <span class="feature-text">人力部</span>
    </div>
    <div class="feature-item">
      <svg class="feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
        <polyline points="14 2 14 8 20 8"></polyline>
        <line x1="16" y1="13" x2="8" y2="13"></line>
        <line x1="16" y1="17" x2="8" y2="17"></line>
        <polyline points="10 9 9 9 8 9"></polyline>
      </svg>
      <span class="feature-text">财法部</span>
    </div>
    <div class="feature-item">
      <svg class="feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect>
        <line x1="8" y1="21" x2="16" y2="21"></line>
        <line x1="12" y1="17" x2="12" y2="21"></line>
      </svg>
      <span class="feature-text">技术部</span>
    </div>
  </div>
</template>

<script setup>
</script>

<style scoped>
.feature-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  margin-top: 32px;
}

.feature-item {
  aspect-ratio: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 12px;
  background-color: #f8f8f8;
  border-radius: 8px;
  transition: background-color 0.2s, transform 0.2s;
  cursor: pointer;
  padding: 20px;
}

.feature-item:hover {
  background-color: #f0f0f0;
  transform: translateY(-2px);
}

.feature-icon {
  width: 40px;
  height: 40px;
  color: #000000;
  stroke: currentColor;
  stroke-width: 1.5;
  fill: none;
}

.feature-text {
  font-size: 15px;
  font-weight: 500;
  color: #000000;
}
</style>


```

```vue
<template>
  <div class="content-filters">
    <div class="main-tabs">
      <button 
        v-for="tab in mainTabs" 
        :key="tab"
        :class="['main-tab', { active: activeMainTab === tab }]"
        @click="activeMainTab = tab"
      >
        {{ tab }}
      </button>
    </div>

    <div class="filter-section">
      <div class="filter-label">部门筛选</div>
      <div class="filter-buttons">
        <button 
          v-for="dept in departments" 
          :key="dept"
          :class="['filter-btn', { active: activeDepartment === dept }]"
          @click="activeDepartment = dept"
        >
          {{ dept }}
        </button>
      </div>
    </div>

    <div class="filter-section">
      <div class="filter-label">内容类型</div>
      <div class="filter-buttons">
        <button 
          v-for="type in contentTypes" 
          :key="type"
          :class="['filter-btn', { active: activeContentType === type }]"
          @click="activeContentType = type"
        >
          {{ type }}
        </button>
      </div>
    </div>

    <div class="search-section">
      <div class="search-box">
        <svg class="search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="11" cy="11" r="8"></circle>
          <path d="m21 21-4.35-4.35"></path>
        </svg>
        <input type="text" placeholder="搜索..." class="search-input" />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const activeMainTab = ref('全部文章')
const activeDepartment = ref('不限')
const activeContentType = ref('不限')

const mainTabs = ['全部文章', '资料分享', '行业数据库']
const departments = ['不限', '战略部', '品牌部', '销售部', '财法部', '人力部', '技术部']
const contentTypes = ['不限', '书籍播客', '大佬思维', '案例拆解', '运营笔记', '时事观点']
</script>

<style scoped>
.content-filters {
  margin-top: 48px;
}

.main-tabs {
  display: flex;
  gap: 0;
  border-bottom: 1px solid #e0e0e0;
  margin-bottom: 32px;
}

.main-tab {
  padding: 12px 24px;
  background: none;
  border: none;
  font-size: 16px;
  color: #666666;
  cursor: pointer;
  position: relative;
  transition: color 0.2s;
  border-bottom: 2px solid transparent;
}

.main-tab:hover {
  color: #000000;
}

.main-tab.active {
  color: #000000;
  border-bottom-color: #000000;
}

.filter-section {
  margin-bottom: 24px;
}

.filter-label {
  font-size: 14px;
  color: #666666;
  margin-bottom: 12px;
}

.filter-buttons {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}

.filter-btn {
  padding: 8px 16px;
  background-color: #f5f5f5;
  border: 1px solid #e0e0e0;
  border-radius: 6px;
  font-size: 14px;
  color: #000000;
  cursor: pointer;
  transition: all 0.2s;
}

.filter-btn:hover {
  background-color: #eeeeee;
}

.filter-btn.active {
  background-color: #333333;
  color: #ffffff;
  border-color: #333333;
}

.search-section {
  margin-top: 32px;
}

.search-box {
  position: relative;
  max-width: 400px;
}

.search-icon {
  position: absolute;
  left: 12px;
  top: 50%;
  transform: translateY(-50%);
  width: 18px;
  height: 18px;
  color: #999999;
}

.search-input {
  width: 100%;
  padding: 12px 12px 12px 40px;
  border: 1px solid #e0e0e0;
  border-radius: 6px;
  font-size: 14px;
  background-color: #ffffff;
  transition: border-color 0.2s;
}

.search-input:focus {
  outline: none;
  border-color: #333333;
}
</style>

```

```vue
<template>
  <div class="article-list">
    <ArticleItem
      v-for="article in articles"
      :key="article.id"
      :article="article"
    />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import ArticleItem from './ArticleItem.vue'

const articles = ref([
  {
    id: 1,
    department: '人力部',
    title: '《别让猴子跳回背上》如何做一个合理的管理者(下)',
    description: '作为管理者,你的贡献来自于你的判断力与影响力,你的职责不是亲力亲为地背负所有猴子,而是要提供动力让其他人发挥所长。',
    image: 'https://images.unsplash.com/photo-1497366216548-37526070297c?w=200&h=150&fit=crop'
  },
  {
    id: 2,
    department: '人力部',
    title: '《别让猴子跳回背上》为什么领导没时间,下属没事做?(上)',
    description: '一旦你接受了这些本不属于你的猴子,一个更严重的问题便随之而来:你为什么越努力,反而越忙乱?',
    image: 'https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=200&h=150&fit=crop'
  },
  {
    id: 3,
    department: '品牌部',
    title: '《上瘾》如何培养用户的使用习惯?(下)',
    description: '成功的习惯养成类产品,本质上是将用户面临的问题与产品提供的解决方案,通过一次又一次的循环,紧密地联系在一起,直至这种联系变成一种近乎本能的反应。',
    image: 'https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=200&h=150&fit=crop'
  },
  {
    id: 4,
    department: '品牌部',
    title: '《上瘾》让产品成为用户生活中不可或缺的一部分(上)',
    description: '在这个注意上你的产品惯"用你的产品生死和',
    image: 'https://images.unsplash.com/photo-1542744173-8e7e53415bb0?w=200&h=150&fit=crop'
  }
])
</script>

<style scoped>
.article-list {
  margin-top: 32px;
  display: flex;
  flex-direction: column;
  gap: 24px;
}
</style>

```

```vue
<template>
  <div class="article-item">
    <div class="article-image">
      <img :src="article.image" :alt="article.title" />
    </div>
    <div class="article-content">
      <div class="article-meta">
        <span class="department-tag">{{ article.department }}</span>
      </div>
      <h3 class="article-title">{{ article.title }}</h3>
      <p class="article-description">{{ article.description }}</p>
    </div>
  </div>
</template>

<script setup>
defineProps({
  article: {
    type: Object,
    required: true
  }
})
</script>

<style scoped>
.article-item {
  display: flex;
  gap: 20px;
  padding: 20px;
  background-color: #ffffff;
  border-radius: 8px;
  border: 1px solid #f0f0f0;
  transition: box-shadow 0.2s;
}

.article-item:hover {
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

.article-image {
  width: 160px;
  height: 120px;
  flex-shrink: 0;
  border-radius: 6px;
  overflow: hidden;
  background-color: #f0f0f0;
}

.article-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.article-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.article-meta {
  margin-bottom: 4px;
}

.department-tag {
  display: inline-block;
  padding: 4px 10px;
  background-color: #f5f5f5;
  color: #666666;
  border-radius: 4px;
  font-size: 12px;
}

.article-title {
  font-size: 18px;
  font-weight: 600;
  color: #000000;
  margin: 0;
  line-height: 1.4;
}

.article-description {
  font-size: 14px;
  color: #666666;
  line-height: 1.6;
  margin: 0;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>

```


检查 lint 错误，并更新侧边栏顶部文字：



更新侧边栏顶部，添加广告文字：


```vue
<template>
  <aside class="sidebar">
    <div class="logo-section">
      <div class="logo-ad">找工作上BOSS直聘直接谈</div>
      <div class="logo">Pitch.</div>
    </div>
    
    <nav class="nav-menu">
      <a href="#" class="nav-item active">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path>
          <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path>
        </svg>
        <span>学习</span>
      </a>
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
          <circle cx="12" cy="7" r="4"></circle>
        </svg>
        <span>牛人</span>
      </a>
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path>
          <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path>
        </svg>
        <span>链接</span>
      </a>
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <circle cx="12" cy="12" r="10"></circle>
          <path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path>
          <path d="M12 17h.01"></path>
        </svg>
        <span>项目</span>
      </a>
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
          <circle cx="12" cy="10" r="3"></circle>
        </svg>
        <span>活动</span>
      </a>
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
          <circle cx="12" cy="7" r="4"></circle>
        </svg>
        <span>我的</span>
      </a>
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
</template>

<script setup>
</script>

<style scoped>
.sidebar {
  width: 240px;
  background-color: #f5f5f5;
  display: flex;
  flex-direction: column;
  padding: 24px 16px;
  min-height: 100vh;
  flex-shrink: 0;
}

.logo {
  background-color: #000000;
  color: #ffffff;
  padding: 12px 16px;
  border-radius: 8px;
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 32px;
  text-align: center;
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
</style>


```

```vue
<template>
  <aside class="sidebar">
    <div class="logo-section">
      <div class="logo-ad">找工作上BOSS直聘直接谈</div>
      <div class="logo">Pitch.</div>
    </div>
    
    <nav class="nav-menu">
      <a href="#" class="nav-item active">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path>
          <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path>
        </svg>
        <span>学习</span>
      </a>
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
          <circle cx="12" cy="7" r="4"></circle>
        </svg>
        <span>牛人</span>
      </a>
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path>
          <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path>
        </svg>
        <span>链接</span>
      </a>
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <circle cx="12" cy="12" r="10"></circle>
          <path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path>
          <path d="M12 17h.01"></path>
        </svg>
        <span>项目</span>
      </a>
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
          <circle cx="12" cy="10" r="3"></circle>
        </svg>
        <span>活动</span>
      </a>
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
          <circle cx="12" cy="7" r="4"></circle>
        </svg>
        <span>我的</span>
      </a>
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
</template>

<script setup>
</script>

<style scoped>
.sidebar {
  width: 240px;
  background-color: #f5f5f5;
  display: flex;
  flex-direction: column;
  padding: 24px 16px;
  min-height: 100vh;
  flex-shrink: 0;
}

.logo-section {
  background-color: #000000;
  color: #ffffff;
  padding: 16px;
  border-radius: 8px;
  margin-bottom: 32px;
}

.logo-ad {
  font-size: 12px;
  color: #ffffff;
  margin-bottom: 8px;
  text-align: center;
}

.logo {
  font-size: 24px;
  font-weight: 700;
  text-align: center;
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
</style>


```


检查并优化样式细节，确保与设计一致：


```vue
<template>
  <div class="feature-grid">
    <div class="feature-item">
      <svg class="feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path>
        <polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline>
        <line x1="12" y1="22.08" x2="12" y2="12"></line>
      </svg>
      <span class="feature-text">战略部</span>
    </div>
    <div class="feature-item">
      <svg class="feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
      </svg>
      <span class="feature-text">品牌部</span>
    </div>
    <div class="feature-item">
      <svg class="feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6"></path>
        <path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18"></path>
        <path d="M4 22h16"></path>
        <path d="M10 14.66V17c0 .55-.47.98-.97 1.21C7.85 18.75 7 20.24 7 22"></path>
        <path d="M14 14.66V17c0 .55.47.98.97 1.21C16.15 18.75 17 20.24 17 22"></path>
        <path d="M18 2H6v7a6 6 0 0 0 12 0V2Z"></path>
      </svg>
      <span class="feature-text">销售部</span>
    </div>
    <div class="feature-item">
      <svg class="feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <circle cx="12" cy="12" r="10"></circle>
        <circle cx="12" cy="12" r="3"></circle>
        <line x1="12" y1="1" x2="12" y2="3"></line>
        <line x1="12" y1="21" x2="12" y2="23"></line>
        <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
        <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
        <line x1="1" y1="12" x2="3" y2="12"></line>
        <line x1="21" y1="12" x2="23" y2="12"></line>
        <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
        <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
      </svg>
      <span class="feature-text">人力部</span>
    </div>
    <div class="feature-item">
      <svg class="feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
        <polyline points="14 2 14 8 20 8"></polyline>
        <line x1="16" y1="13" x2="8" y2="13"></line>
        <line x1="16" y1="17" x2="8" y2="17"></line>
        <polyline points="10 9 9 9 8 9"></polyline>
      </svg>
      <span class="feature-text">财法部</span>
    </div>
    <div class="feature-item">
      <svg class="feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect>
        <line x1="8" y1="21" x2="16" y2="21"></line>
        <line x1="12" y1="17" x2="12" y2="21"></line>
      </svg>
      <span class="feature-text">技术部</span>
    </div>
  </div>
</template>

<script setup>
</script>

<style scoped>
.feature-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  margin-top: 0;
  margin-bottom: 48px;
}

.feature-item {
  aspect-ratio: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 12px;
  background-color: #f8f8f8;
  border-radius: 8px;
  transition: background-color 0.2s, transform 0.2s;
  cursor: pointer;
  padding: 20px;
}

.feature-item:hover {
  background-color: #f0f0f0;
  transform: translateY(-2px);
}

.feature-icon {
  width: 40px;
  height: 40px;
  color: #000000;
  stroke: currentColor;
  stroke-width: 1.5;
  fill: none;
}

.feature-text {
  font-size: 15px;
  font-weight: 500;
  color: #000000;
}
</style>


```

```vue
<template>
  <main class="main-content">
    <div class="content-header">
      <h1 class="main-title">Starter Studies</h1>
      <p class="subtitle">把自己当公司来经营</p>
      
      <div class="header-tabs">
        <button class="header-tab active">CEO图书馆</button>
        <button class="header-tab">最近更新</button>
      </div>
    </div>

    <div class="content-cards-section">
      <div class="cards-container">
        <ContentCard
          v-for="card in cards"
          :key="card.id"
          :title="card.title"
          :description="card.description"
          :image="card.image"
        />
      </div>
    </div>

    <div class="content-bottom">
      <FeatureGrid />
      
      <ContentFilters />
      
      <ArticleList />
    </div>
  </main>
</template>

<script setup>
import { ref } from 'vue'
import ContentCard from './ContentCard.vue'
import FeatureGrid from './FeatureGrid.vue'
import ContentFilters from './ContentFilters.vue'
import ArticleList from './ArticleList.vue'

const cards = ref([
  {
    id: 1,
    title: '《别让猴子跳回背上》如何做一个合理的管理者(下)',
    description: '作为管理者,你的贡献来自于你的判断力与影响力,你的职责不是亲力亲为地背负所有猴子,而是要提供动力让其他人发挥所长。',
    image: 'https://images.unsplash.com/photo-1497366216548-37526070297c?w=400&h=250&fit=crop'
  },
  {
    id: 2,
    title: '《别让猴子跳回背上》为什么领导没时间,下属没事做?(上)',
    description: '一旦你接受了这些本不属于你的猴子,一个更严重的问题便随之而来:你为什么越努力,反而越忙乱?',
    image: 'https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=400&h=250&fit=crop'
  },
  {
    id: 3,
    title: '《上瘾》如何培养用户的使用习惯?(下)',
    description: '成功的习惯养成类产品,本质上是将用户面临的问题与产品提供的解决方案,通过一次又一次的循环,紧密地联系在一起,直至这种联系变成一种近乎本能的反应。',
    image: 'https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=400&h=250&fit=crop'
  },
  {
    id: 4,
    title: '《上瘾》可或缺的-',
    description: '在这个注意上你的产品惯"用你的产品生死和',
    image: 'https://images.unsplash.com/photo-1542744173-8e7e53415bb0?w=400&h=250&fit=crop'
  }
])
</script>

<style scoped>
.main-content {
  flex: 1;
  padding: 40px 48px;
  background-color: #ffffff;
  overflow-y: auto;
  min-width: 0;
}

.content-header {
  margin-bottom: 40px;
}

.main-title {
  font-size: 42px;
  font-weight: 700;
  color: #000000;
  margin-bottom: 8px;
  letter-spacing: -0.5px;
}

.subtitle {
  font-size: 18px;
  color: #666666;
  margin-bottom: 32px;
}

.header-tabs {
  display: flex;
  gap: 12px;
}

.header-tab {
  padding: 10px 20px;
  border: none;
  border-radius: 6px;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.2s;
  background-color: #ffffff;
  color: #000000;
  border: 1px solid #e0e0e0;
}

.header-tab:hover {
  background-color: #f5f5f5;
}

.header-tab.active {
  background-color: #333333;
  color: #ffffff;
  border-color: #333333;
}

.content-cards-section {
  margin-bottom: 60px;
}

.cards-container {
  display: flex;
  gap: 20px;
  overflow-x: auto;
  padding-bottom: 16px;
  scrollbar-width: thin;
  scrollbar-color: #c0c0c0 #f0f0f0;
}

.cards-container::-webkit-scrollbar {
  height: 8px;
}

.cards-container::-webkit-scrollbar-track {
  background: #f0f0f0;
  border-radius: 4px;
}

.cards-container::-webkit-scrollbar-thumb {
  background: #c0c0c0;
  border-radius: 4px;
}

.cards-container::-webkit-scrollbar-thumb:hover {
  background: #a0a0a0;
}

.content-bottom {
  margin-top: 60px;
  padding-bottom: 40px;
}
</style>


```


已完成以下更新：

## 主要修改：

1. **顶部标签改为按钮样式**：将"CEO图书馆"和"最近更新"从下划线标签改为圆角按钮，激活状态为深色背景、白色文字。

2. **部门功能网格更新为3x2布局**：包含6个部门：
   - 战略部、品牌部、销售部
   - 人力部、财法部、技术部

3. **新增内容过滤和搜索区域**（`ContentFilters.vue`）：
   - 主标签：全部文章、资料分享、行业数据库
   - 部门筛选按钮行
   - 内容类型筛选按钮行
   - 搜索框（带搜索图标）

4. **新增文章列表**（`ArticleList.vue` 和 `ArticleItem.vue`）：
   - 垂直列表布局
   - 每篇文章包含：缩略图、部门标签、标题、描述

5. **侧边栏更新**：顶部添加"找工作上BOSS直聘直接谈"广告文字

页面现在支持向下滚动查看完整内容，包括部门网格、过滤器和文章列表。所有组件已创建并集成到主内容区域。

---

**User**

去掉所有广告 目前的页面在向下滚动的时候 页面会一起向下划 我提供原来的网页滚动前后的图片 左边栏的位置不会随着页面滚动

---

**Cursor**

```vue
<template>
  <aside class="sidebar">
    <div class="logo">Pitch.</div>
    
    <nav class="nav-menu">
      <a href="#" class="nav-item active">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path>
          <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path>
        </svg>
        <span>学习</span>
      </a>
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
          <circle cx="12" cy="7" r="4"></circle>
        </svg>
        <span>牛人</span>
      </a>
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path>
          <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path>
        </svg>
        <span>链接</span>
      </a>
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <circle cx="12" cy="12" r="10"></circle>
          <path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path>
          <path d="M12 17h.01"></path>
        </svg>
        <span>项目</span>
      </a>
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
          <circle cx="12" cy="10" r="3"></circle>
        </svg>
        <span>活动</span>
      </a>
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
          <circle cx="12" cy="7" r="4"></circle>
        </svg>
        <span>我的</span>
      </a>
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
</template>

<script setup>
</script>

<style scoped>
.sidebar {
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
</style>


```

```vue
<template>
  <div class="app-container">
    <Sidebar />
    <MainContent />
  </div>
</template>

<script setup>
import Sidebar from './components/Sidebar.vue'
import MainContent from './components/MainContent.vue'
</script>

<style scoped>
.app-container {
  display: flex;
  height: 100vh;
  overflow: hidden;
  background-color: #ffffff;
}
</style>

```

```vue
<template>
  <main class="main-content">
    <div class="content-header">
      <h1 class="main-title">Starter Studies</h1>
      <p class="subtitle">把自己当公司来经营</p>
      
      <div class="header-tabs">
        <button class="header-tab active">CEO图书馆</button>
        <button class="header-tab">最近更新</button>
      </div>
    </div>

    <div class="content-cards-section">
      <div class="cards-container">
        <ContentCard
          v-for="card in cards"
          :key="card.id"
          :title="card.title"
          :description="card.description"
          :image="card.image"
        />
      </div>
    </div>

    <div class="content-bottom">
      <FeatureGrid />
      
      <ContentFilters />
      
      <ArticleList />
    </div>
  </main>
</template>

<script setup>
import { ref } from 'vue'
import ContentCard from './ContentCard.vue'
import FeatureGrid from './FeatureGrid.vue'
import ContentFilters from './ContentFilters.vue'
import ArticleList from './ArticleList.vue'

const cards = ref([
  {
    id: 1,
    title: '《别让猴子跳回背上》如何做一个合理的管理者(下)',
    description: '作为管理者,你的贡献来自于你的判断力与影响力,你的职责不是亲力亲为地背负所有猴子,而是要提供动力让其他人发挥所长。',
    image: 'https://images.unsplash.com/photo-1497366216548-37526070297c?w=400&h=250&fit=crop'
  },
  {
    id: 2,
    title: '《别让猴子跳回背上》为什么领导没时间,下属没事做?(上)',
    description: '一旦你接受了这些本不属于你的猴子,一个更严重的问题便随之而来:你为什么越努力,反而越忙乱?',
    image: 'https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=400&h=250&fit=crop'
  },
  {
    id: 3,
    title: '《上瘾》如何培养用户的使用习惯?(下)',
    description: '成功的习惯养成类产品,本质上是将用户面临的问题与产品提供的解决方案,通过一次又一次的循环,紧密地联系在一起,直至这种联系变成一种近乎本能的反应。',
    image: 'https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=400&h=250&fit=crop'
  },
  {
    id: 4,
    title: '《上瘾》可或缺的-',
    description: '在这个注意上你的产品惯"用你的产品生死和',
    image: 'https://images.unsplash.com/photo-1542744173-8e7e53415bb0?w=400&h=250&fit=crop'
  }
])
</script>

<style scoped>
.main-content {
  flex: 1;
  padding: 40px 48px;
  background-color: #ffffff;
  overflow-y: auto;
  height: 100vh;
  min-width: 0;
}

.content-header {
  margin-bottom: 40px;
}

.main-title {
  font-size: 42px;
  font-weight: 700;
  color: #000000;
  margin-bottom: 8px;
  letter-spacing: -0.5px;
}

.subtitle {
  font-size: 18px;
  color: #666666;
  margin-bottom: 32px;
}

.header-tabs {
  display: flex;
  gap: 12px;
}

.header-tab {
  padding: 10px 20px;
  border: none;
  border-radius: 6px;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.2s;
  background-color: #ffffff;
  color: #000000;
  border: 1px solid #e0e0e0;
}

.header-tab:hover {
  background-color: #f5f5f5;
}

.header-tab.active {
  background-color: #333333;
  color: #ffffff;
  border-color: #333333;
}

.content-cards-section {
  margin-bottom: 60px;
}

.cards-container {
  display: flex;
  gap: 20px;
  overflow-x: auto;
  padding-bottom: 16px;
  scrollbar-width: thin;
  scrollbar-color: #c0c0c0 #f0f0f0;
}

.cards-container::-webkit-scrollbar {
  height: 8px;
}

.cards-container::-webkit-scrollbar-track {
  background: #f0f0f0;
  border-radius: 4px;
}

.cards-container::-webkit-scrollbar-thumb {
  background: #c0c0c0;
  border-radius: 4px;
}

.cards-container::-webkit-scrollbar-thumb:hover {
  background: #a0a0a0;
}

.content-bottom {
  margin-top: 60px;
  padding-bottom: 40px;
}
</style>


```

```css
@import './base.css';

#app {
  width: 100%;
  margin: 0;
  padding: 0;
  font-weight: normal;
  height: 100vh;
}

* {
  box-sizing: border-box;
}

body {
  margin: 0;
  padding: 0;
}

```

```vue
<template>
  <div class="app-container">
    <Sidebar />
    <MainContent />
  </div>
</template>

<script setup>
import Sidebar from './components/Sidebar.vue'
import MainContent from './components/MainContent.vue'
</script>

<style scoped>
.app-container {
  display: flex;
  height: 100vh;
  background-color: #ffffff;
}
</style>

```

```css
@import './base.css';

#app {
  width: 100%;
  margin: 0;
  padding: 0;
  font-weight: normal;
  height: 100vh;
}

* {
  box-sizing: border-box;
}

body {
  margin: 0;
  padding: 0;
  height: 100vh;
  overflow: hidden;
}

```

## 更新概览
- 去除所有广告位，还原左侧 Logo 区仅显示 `Pitch.`，并保持黑底白字样式。  
```2:20:src/components/Sidebar.vue
  <div class="logo">Pitch.</div>
  ...
.sidebar {
  width: 240px;
  ...
  position: sticky;
  top: 0;
}
```
- 为侧边栏启用 `position: sticky` 与 `height: 100vh`，并将主体容器限定为 `100vh`，将页面滚动限制在主内容区域。  
```13:20:src/App.vue
.app-container {
  display: flex;
  height: 100vh;
  background-color: #ffffff;
}
```
- 让主内容区域独立滚动，并全局限制 `body/#app` 高度，防止整体页面跟随滚动。  
```3:12:src/assets/main.css
#app { ... height: 100vh; }
body {
  margin: 0;
  padding: 0;
  height: 100vh;
  overflow: hidden;
}
```
```69:80:src/components/MainContent.vue
.main-content {
  flex: 1;
  ...
  overflow-y: auto;
  height: 100vh;
}
```

## 下一步建议
- 运行 `npm run dev` 后在浏览器中验证：向下滚动时左侧栏应保持固定，只让右侧内容滚动。  
- 若需移动端适配，可额外针对窄屏调整侧边栏展示（折叠或置顶）。

```vue
  <div class="logo">Pitch.</div>
  ...
.sidebar {
  width: 240px;
  ...
  position: sticky;
  top: 0;
}
```

```vue
.app-container {
  display: flex;
  height: 100vh;
  background-color: #ffffff;
}
```

```css
#app { ... height: 100vh; }
body {
  margin: 0;
  padding: 0;
  height: 100vh;
  overflow: hidden;
}
```

```vue
.main-content {
  flex: 1;
  ...
  overflow-y: auto;
  height: 100vh;
}
```

---

**User**

按照这个风格生成一个牛人页面点击牛人可以跳转过去 我提供参考的网页

---

**Cursor**

```json
{
  "name": "vue",
  "version": "0.0.0",
  "private": true,
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "vue": "^3.4.29",
    "vue-router": "^4.3.0"
  },
  "devDependencies": {
    "@vitejs/plugin-vue": "^5.0.5",
    "vite": "^5.3.1"
  }
}

```

```javascript
import { createRouter, createWebHistory } from 'vue-router'

import HomePage from '../components/MainContent.vue'
import TalentPage from '../pages/TalentPage.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomePage
  },
  {
    path: '/talents',
    name: 'talents',
    component: TalentPage
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router

```

```vue
<template>
  <main class="talent-page">
    <section class="page-header">
      <h1 class="page-title">超级牛人库</h1>
      <p class="page-subtitle">发现各行各业的顶尖操盘手，快速建立你的专家顾问团。</p>

      <div class="header-actions">
        <div class="stats">
          <div class="stat-item">
            <span class="stat-value">368</span>
            <span class="stat-label">精选牛人</span>
          </div>
          <div class="stat-divider" />
          <div class="stat-item">
            <span class="stat-value">29</span>
            <span class="stat-label">热门赛道</span>
          </div>
          <div class="stat-divider" />
          <div class="stat-item">
            <span class="stat-value">142</span>
            <span class="stat-label">实时邀约</span>
          </div>
        </div>
        <div class="cta-buttons">
          <button class="btn primary">发布合作需求</button>
          <button class="btn secondary">推荐牛人</button>
        </div>
      </div>

      <div class="topic-tabs">
        <button
          v-for="tab in topicTabs"
          :key="tab"
          :class="['topic-tab', { active: activeTopic === tab }]"
          @click="activeTopic = tab"
        >
          {{ tab }}
        </button>
      </div>
    </section>

    <section class="talent-spotlight">
      <div class="section-header">
        <h2>本周焦点</h2>
        <button class="link-button">全部牛人</button>
      </div>

      <div class="talent-grid">
        <article v-for="talent in featuredTalents" :key="talent.id" class="talent-card">
          <div class="talent-card-header">
            <div class="avatar">
              <img :src="talent.avatar" :alt="talent.name" />
            </div>
            <div class="identity">
              <div class="name">{{ talent.name }}</div>
              <div class="role">{{ talent.role }}</div>
              <div class="meta">{{ talent.company }} · {{ talent.location }}</div>
            </div>
            <button class="connect-btn">邀约</button>
          </div>

          <p class="talent-description">{{ talent.description }}</p>

          <div class="talent-tags">
            <span v-for="tag in talent.tags" :key="tag" class="tag">
              {{ tag }}
            </span>
          </div>

          <div class="talent-stats">
            <div class="stat">
              <span class="stat-number">{{ talent.projects }}</span>
              <span class="stat-text">操盘项目</span>
            </div>
            <div class="stat">
              <span class="stat-number">{{ talent.experience }}</span>
              <span class="stat-text">行业经验</span>
            </div>
            <div class="stat">
              <span class="stat-number">{{ talent.followers }}</span>
              <span class="stat-text">关注</span>
            </div>
          </div>
        </article>
      </div>
    </section>

    <section class="talent-filters">
      <div class="filter-group">
        <span class="filter-label">擅长领域</span>
        <div class="filter-buttons">
          <button
            v-for="field in fields"
            :key="field"
            :class="['filter-btn', { active: activeField === field }]"
            @click="activeField = field"
          >
            {{ field }}
          </button>
        </div>
      </div>
      <div class="filter-group">
        <span class="filter-label">城市</span>
        <div class="filter-buttons">
          <button
            v-for="city in cities"
            :key="city"
            :class="['filter-btn', { active: activeCity === city }]"
            @click="activeCity = city"
          >
            {{ city }}
          </button>
        </div>
      </div>
      <div class="search-box">
        <svg class="search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="11" cy="11" r="8" />
          <path d="m21 21-4.35-4.35" />
        </svg>
        <input class="search-input" type="text" placeholder="输入牛人姓名或关键词搜索" />
      </div>
    </section>

    <section class="talent-list-section">
      <div class="section-header">
        <h2>最新上架</h2>
        <button class="link-button">查看更多</button>
      </div>

      <div class="talent-list">
        <div v-for="talent in recentTalents" :key="talent.id" class="talent-list-item">
          <div class="list-avatar">
            <img :src="talent.avatar" :alt="talent.name" />
          </div>
          <div class="list-body">
            <div class="list-header">
              <div>
                <div class="list-name">{{ talent.name }}</div>
                <div class="list-meta">{{ talent.role }} · {{ talent.company }} · {{ talent.location }}</div>
              </div>
              <button class="connect-outline">查看档案</button>
            </div>
            <p class="list-description">{{ talent.description }}</p>
            <div class="list-tags">
              <span v-for="tag in talent.tags" :key="tag" class="tag">
                {{ tag }}
              </span>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>
</template>

<script setup>
import { ref } from 'vue'

const topicTabs = ['全部领域', '运营增长', '品牌营销', '产品战略', '组织管理', '融资并购']
const activeTopic = ref(topicTabs[0])

const fields = ['不限', '增长', '品牌', '组织', '产品', '商业化', '供应链']
const activeField = ref(fields[0])

const cities = ['不限', '北京', '上海', '深圳', '杭州']
const activeCity = ref(cities[0])

const featuredTalents = ref([
  {
    id: 1,
    name: '李若彤',
    role: '增长产品负责人',
    company: '酷玩科技',
    location: '上海',
    avatar: 'https://images.unsplash.com/photo-1544723795-3fb6469f5b39?w=200&h=200&fit=crop',
    description: '连续操盘 3 款出海工具产品，从 0 到 1 完成冷启动，擅长构建增长闭环与漏斗体系。',
    tags: ['冷启动', '出海', '数据驱动'],
    projects: '12',
    experience: '8年',
    followers: '3.4k'
  },
  {
    id: 2,
    name: '周乙',
    role: '品牌总监',
    company: '夜航文化',
    location: '北京',
    avatar: 'https://images.unsplash.com/photo-1504595403659-9088ce801e29?w=200&h=200&fit=crop',
    description: '帮助消费品牌完成从定位、视觉到内容矩阵的系统打造，擅长新品上市与营销节奏设计。',
    tags: ['品牌战略', '视觉体系', '上市策划'],
    projects: '27',
    experience: '10年',
    followers: '5.1k'
  },
  {
    id: 3,
    name: '陈音',
    role: '组织发展顾问',
    company: '镜像咨询',
    location: '深圳',
    avatar: 'https://images.unsplash.com/photo-1524504388940-b1c1722653e1?w=200&h=200&fit=crop',
    description: '为 30+ 科技公司搭建组织能力模型与绩效体系，擅长高速增长阶段的组织升级。',
    tags: ['OD', '绩效管理', '组织升级'],
    projects: '19',
    experience: '12年',
    followers: '2.7k'
  }
])

const recentTalents = ref([
  {
    id: 10,
    name: '王晨',
    role: '社区运营负责人',
    company: '语雀',
    location: '杭州',
    avatar: 'https://images.unsplash.com/photo-1524504388940-b1c1722653e1?w=120&h=120&fit=crop',
    description: '负责构建百万用户社区体系，搭建内容与激励模型，推动 NPS 提升 30%。',
    tags: ['社区运营', '用户增长', '内容体系']
  },
  {
    id: 11,
    name: '赵芷柔',
    role: 'SaaS 商业化顾问',
    company: '独立顾问',
    location: '北京',
    avatar: 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=120&h=120&fit=crop',
    description: '深度服务 6 家 B 端公司，帮助构建售前演示、销售手册及续费体系，年度 ARR 提升 45%。',
    tags: ['商业化', '销售体系', 'B2B']
  },
  {
    id: 12,
    name: 'Alex Chen',
    role: '出海品牌顾问',
    company: 'Sparrow Lab',
    location: '上海',
    avatar: 'https://images.unsplash.com/photo-1544723795-3fb6469f5b39?w=120&h=120&fit=crop',
    description: '擅长欧美市场 DTC 品牌运营，搭建全链路营销体系，单月广告 ROI 提升 2.3 倍。',
    tags: ['出海', 'DTC', '广告投放']
  },
  {
    id: 13,
    name: '刘白',
    role: '产品战略负责人',
    company: '北极光智造',
    location: '深圳',
    avatar: 'https://images.unsplash.com/photo-1487412720507-e7ab37603c6f?w=120&h=120&fit=crop',
    description: '主导智能硬件产品线规划，从 0 到 1 构建模块化体系，实现 3 年内 4 款新品上市。',
    tags: ['产品战略', '硬件', '模块化']
  }
])
</script>

<style scoped>
.talent-page {
  flex: 1;
  padding: 40px 48px;
  background-color: #ffffff;
  overflow-y: auto;
  height: 100vh;
}

.page-header {
  margin-bottom: 40px;
}

.page-title {
  font-size: 42px;
  font-weight: 700;
  color: #000000;
  margin-bottom: 8px;
  letter-spacing: -0.5px;
}

.page-subtitle {
  font-size: 18px;
  color: #666666;
  margin-bottom: 24px;
}

.header-actions {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
  margin-bottom: 32px;
}

.stats {
  display: flex;
  align-items: center;
  gap: 24px;
  padding: 16px 24px;
  background-color: #f8f8f8;
  border-radius: 12px;
}

.stat-item {
  display: flex;
  flex-direction: column;
  gap: 4px;
  min-width: 80px;
}

.stat-value {
  font-size: 24px;
  font-weight: 600;
  color: #000000;
}

.stat-label {
  font-size: 12px;
  color: #666666;
  letter-spacing: 1px;
  text-transform: uppercase;
}

.stat-divider {
  width: 1px;
  height: 36px;
  background-color: #e0e0e0;
}

.cta-buttons {
  display: flex;
  gap: 12px;
}

.btn {
  padding: 12px 20px;
  border-radius: 8px;
  border: 1px solid transparent;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.2s;
}

.btn.primary {
  background-color: #000000;
  color: #ffffff;
}

.btn.primary:hover {
  background-color: #222222;
}

.btn.secondary {
  background-color: #ffffff;
  color: #000000;
  border-color: #d9d9d9;
}

.btn.secondary:hover {
  background-color: #f5f5f5;
}

.topic-tabs {
  display: flex;
  gap: 12px;
}

.topic-tab {
  padding: 8px 18px;
  border-radius: 999px;
  border: 1px solid #e0e0e0;
  background-color: #ffffff;
  font-size: 14px;
  color: #666666;
  cursor: pointer;
  transition: all 0.2s;
}

.topic-tab:hover {
  color: #000000;
  border-color: #cccccc;
}

.topic-tab.active {
  background-color: #000000;
  color: #ffffff;
  border-color: #000000;
}

.section-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 24px;
}

.section-header h2 {
  font-size: 22px;
  font-weight: 600;
  color: #000000;
}

.link-button {
  background: none;
  border: none;
  font-size: 14px;
  color: #333333;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 4px;
  transition: color 0.2s;
}

.link-button:hover {
  color: #000000;
}

.talent-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
  margin-bottom: 48px;
}

.talent-card {
  background-color: #ffffff;
  border-radius: 16px;
  border: 1px solid #eeeeee;
  padding: 24px;
  display: flex;
  flex-direction: column;
  gap: 16px;
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.04);
}

.talent-card-header {
  display: flex;
  align-items: center;
  gap: 16px;
}

.avatar {
  width: 62px;
  height: 62px;
  border-radius: 16px;
  overflow: hidden;
  background-color: #f0f0f0;
  flex-shrink: 0;
}

.avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.identity {
  flex: 1;
}

.name {
  font-size: 18px;
  font-weight: 600;
  color: #000000;
}

.role {
  font-size: 14px;
  color: #333333;
  margin: 2px 0;
}

.meta {
  font-size: 12px;
  color: #999999;
}

.connect-btn {
  background-color: #000000;
  color: #ffffff;
  border: none;
  border-radius: 6px;
  padding: 10px 16px;
  font-size: 14px;
  cursor: pointer;
  transition: background-color 0.2s;
}

.connect-btn:hover {
  background-color: #222222;
}

.talent-description {
  font-size: 14px;
  color: #444444;
  line-height: 1.7;
}

.talent-tags,
.list-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.tag {
  display: inline-flex;
  align-items: center;
  padding: 6px 12px;
  background-color: #f5f5f5;
  color: #666666;
  border-radius: 999px;
  font-size: 12px;
}

.talent-stats {
  display: flex;
  justify-content: space-between;
  padding-top: 12px;
  border-top: 1px solid #f0f0f0;
}

.stat {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.stat-number {
  font-size: 16px;
  font-weight: 600;
  color: #000000;
}

.stat-text {
  font-size: 12px;
  color: #888888;
}

.talent-filters {
  background-color: #f9f9f9;
  border-radius: 16px;
  padding: 24px;
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin-bottom: 36px;
  border: 1px solid #f0f0f0;
}

.filter-group {
  display: flex;
  align-items: center;
  gap: 16px;
  flex-wrap: wrap;
}

.filter-label {
  font-size: 14px;
  color: #666666;
  min-width: 64px;
}

.filter-buttons {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}

.filter-btn {
  padding: 8px 16px;
  border-radius: 999px;
  border: 1px solid #e0e0e0;
  background-color: #ffffff;
  font-size: 13px;
  color: #666666;
  cursor: pointer;
  transition: all 0.2s;
}

.filter-btn:hover {
  border-color: #cccccc;
  color: #000000;
}

.filter-btn.active {
  background-color: #000000;
  color: #ffffff;
  border-color: #000000;
}

.search-box {
  position: relative;
  max-width: 420px;
}

.search-icon {
  position: absolute;
  left: 16px;
  top: 50%;
  transform: translateY(-50%);
  width: 18px;
  height: 18px;
  color: #999999;
}

.search-input {
  width: 100%;
  padding: 12px 16px 12px 44px;
  border-radius: 999px;
  border: 1px solid #e0e0e0;
  background-color: #ffffff;
  font-size: 14px;
  transition: border-color 0.2s;
}

.search-input:focus {
  outline: none;
  border-color: #333333;
}

.talent-list {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.talent-list-item {
  display: flex;
  gap: 20px;
  padding: 20px;
  border-radius: 12px;
  border: 1px solid #f0f0f0;
  background-color: #ffffff;
  transition: box-shadow 0.2s;
}

.talent-list-item:hover {
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.05);
}

.list-avatar {
  width: 68px;
  height: 68px;
  border-radius: 16px;
  overflow: hidden;
  background-color: #f0f0f0;
  flex-shrink: 0;
}

.list-avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.list-body {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.list-header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 16px;
}

.list-name {
  font-size: 18px;
  font-weight: 600;
  color: #000000;
}

.list-meta {
  font-size: 13px;
  color: #888888;
  margin-top: 4px;
}

.list-description {
  font-size: 14px;
  color: #555555;
  line-height: 1.6;
  margin: 0;
}

.connect-outline {
  background-color: #ffffff;
  color: #000000;
  border: 1px solid #d9d9d9;
  border-radius: 6px;
  padding: 8px 14px;
  font-size: 13px;
  cursor: pointer;
  transition: all 0.2s;
}

.connect-outline:hover {
  border-color: #000000;
  color: #000000;
}

@media (max-width: 1280px) {
  .talent-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 1024px) {
  .header-actions {
    flex-direction: column;
    align-items: flex-start;
  }

  .stats {
    width: 100%;
  }

  .talent-grid {
    grid-template-columns: 1fr;
  }
}
</style>

```

```javascript
import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

createApp(App).use(router).mount('#app')

```

```vue
<template>
  <div class="app-container">
    <Sidebar />
    <RouterView />
  </div>
</template>

<script setup>
import Sidebar from './components/Sidebar.vue'
import { RouterView } from 'vue-router'
</script>

<style scoped>
.app-container {
  display: flex;
  height: 100vh;
  background-color: #ffffff;
}
</style>

```

```vue
<template>
  <aside class="sidebar">
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
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path>
          <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path>
        </svg>
        <span>链接</span>
      </a>
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <circle cx="12" cy="12" r="10"></circle>
          <path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path>
          <path d="M12 17h.01"></path>
        </svg>
        <span>项目</span>
      </a>
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
          <circle cx="12" cy="10" r="3"></circle>
        </svg>
        <span>活动</span>
      </a>
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
          <circle cx="12" cy="7" r="4"></circle>
        </svg>
        <span>我的</span>
      </a>
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
</template>

<script setup>
import { useRoute, RouterLink } from 'vue-router'

const route = useRoute()
</script>

<style scoped>
.sidebar {
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
</style>


```

```vue
<template>
  <aside class="sidebar">
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
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path>
          <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path>
        </svg>
        <span>链接</span>
      </a>
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <circle cx="12" cy="12" r="10"></circle>
          <path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path>
          <path d="M12 17h.01"></path>
        </svg>
        <span>项目</span>
      </a>
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
          <circle cx="12" cy="10" r="3"></circle>
        </svg>
        <span>活动</span>
      </a>
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
          <circle cx="12" cy="7" r="4"></circle>
        </svg>
        <span>我的</span>
      </a>
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
</template>

<script setup>
import { useRoute } from 'vue-router'

const route = useRoute()
</script>

<style scoped>
.sidebar {
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
</style>


```

```vue
<template>
  <aside class="sidebar">
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
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path>
          <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path>
        </svg>
        <span>链接</span>
      </a>
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <circle cx="12" cy="12" r="10"></circle>
          <path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path>
          <path d="M12 17h.01"></path>
        </svg>
        <span>项目</span>
      </a>
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
          <circle cx="12" cy="10" r="3"></circle>
        </svg>
        <span>活动</span>
      </a>
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
          <circle cx="12" cy="7" r="4"></circle>
        </svg>
        <span>我的</span>
      </a>
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
</template>

<script setup>
import { useRoute } from 'vue-router'

const route = useRoute()
</script>

<style scoped>
.sidebar {
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
</style>


```

## 结果概览
- 接入 `vue-router`，将 `Sidebar` 常驻在左侧，右侧内容由路由切换呈现，滚动只作用在内容区域。  
```1:20:src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
...
```
- 首页内容作为 `/` 路由保留，新增 `TalentPage` 作为 `/talents`。页面包含焦点牛人卡片、筛选、最新上架列表等版块，风格与原站保持统一。  
```1:200:src/pages/TalentPage.vue
<template>
  <main class="talent-page">
    <section class="page-header">
...
```
- `Sidebar` 切换为 `RouterLink`，点击“学习”、“牛人”即可在不刷新情况下跳转并高亮当前菜单。  
```1:120:src/components/Sidebar.vue
<RouterLink to="/" class="logo">Pitch.</RouterLink>
...
```
- `App.vue` 使用 `<RouterView />` 渲染路由内容；`main.js` 注册路由。  
```1:40:src/App.vue
  <div class="app-container">
    <Sidebar />
    <RouterView />
  </div>
```

## 后续建议
- 新增了 `vue-router` 依赖，请执行 `npm install` 同步本地依赖。
- 运行 `npm run dev`，验证 `/` 与 `/talents` 的导航是否符合预期，尤其是左侧栏固定、右侧内容滚动的体验。

```javascript
import { createRouter, createWebHistory } from 'vue-router'
...
```

```vue
<template>
  <main class="talent-page">
    <section class="page-header">
...
```

```vue
<RouterLink to="/" class="logo">Pitch.</RouterLink>
...
```

```vue
  <div class="app-container">
    <Sidebar />
    <RouterView />
  </div>
```

---

**User**

打开网页报错了 [plugin:vite:import-analysis] Failed to resolve import "vue-router" from "src/router/index.js". Does the file exist?

/home/devbox/project/src/router/index.js:1:49

1  |  import { createRouter, createWebHistory } from 'vue-router'

   |                                                  ^

2  |  

3  |  import HomePage from '../components/MainContent.vue'

    at TransformPluginContext._formatError (file:///home/devbox/project/node_modules/vite/dist/node/chunks/dep-C6uTJdX2.js:49258:41)

    at TransformPluginContext.error (file:///home/devbox/project/node_modules/vite/dist/node/chunks/dep-C6uTJdX2.js:49253:16)

    at normalizeUrl (file:///home/devbox/project/node_modules/vite/dist/node/chunks/dep-C6uTJdX2.js:64291:23)

    at async file:///home/devbox/project/node_modules/vite/dist/node/chunks/dep-C6uTJdX2.js:64423:39

    at async Promise.all (index 0)

    at async TransformPluginContext.transform (file:///home/devbox/project/node_modules/vite/dist/node/chunks/dep-C6uTJdX2.js:64350:7)

    at async PluginContainer.transform (file:///home/devbox/project/node_modules/vite/dist/node/chunks/dep-C6uTJdX2.js:49099:18)

    at async loadAndTransform (file:///home/devbox/project/node_modules/vite/dist/node/chunks/dep-C6uTJdX2.js:51977:27)

    at async viteTransformMiddleware (file:///home/devbox/project/node_modules/vite/dist/node/chunks/dep-C6uTJdX2.js:62105:24

Click outside, press Esc key, or fix the code to dismiss.

You can also disable this overlay by setting server.hmr.overlay to false in vite.config.js.

---

**Cursor**

已通过 `npm install vue-router@^4.3.0` 安装缺失依赖，重新运行 `npm run dev` 即可解决导入报错。若命令后仍有问题，请告知细节。

---

**User**

按照这个风格生成一个链接页面 点击链接可以跳转过去 注意这个链接是牛人这一栏的  我提供参考的网页 注意到咖啡广场下的图片是会自动切换的

---

**Cursor**

```javascript
import { createRouter, createWebHistory } from 'vue-router'

import HomePage from '../components/MainContent.vue'
import TalentPage from '../pages/TalentPage.vue'
import LinkPage from '../pages/LinkPage.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomePage
  },
  {
    path: '/talents',
    name: 'talents',
    component: TalentPage
  },
  {
    path: '/links',
    name: 'links',
    component: LinkPage
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router


```

```vue
<template>
  <main class="link-page">
    <section class="page-header">
      <h1 class="page-title">Starter Network</h1>
      <p class="page-subtitle">认识100位社区CEO</p>

      <div class="tab-row">
        <button
          v-for="tab in tabs"
          :key="tab"
          :class="['tab-btn', { active: activeTab === tab }]"
          @click="activeTab = tab"
        >
          {{ tab }}
        </button>
      </div>
    </section>

    <section class="hero-section">
      <div class="hero-slider">
        <transition-group name="fade" tag="div">
          <div
            v-for="(slide, index) in slides"
            :key="slide.id"
            v-show="currentSlide === index"
            class="hero-slide"
          >
            <img :src="slide.image" :alt="slide.title" />
            <div class="hero-caption">
              <h2>{{ slide.title }}</h2>
              <p>{{ slide.description }}</p>
            </div>
          </div>
        </transition-group>

        <div class="slider-controls">
          <button
            v-for="(slide, index) in slides"
            :key="slide.id"
            :class="['dot', { active: currentSlide === index }]"
            @click="setSlide(index)"
          />
        </div>
      </div>
      <div class="hero-actions">
        <button class="hero-btn">投案例</button>
        <button class="hero-btn outline">约牛人</button>
      </div>
    </section>

    <section class="filter-section">
      <div class="filter-tags">
        <button
          v-for="tag in tags"
          :key="tag"
          :class="['tag-btn', { active: activeTag === tag }]"
          @click="activeTag = tag"
        >
          {{ tag }}
        </button>
      </div>
      <div class="search-box">
        <svg class="search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="11" cy="11" r="8" />
          <path d="m21 21-4.35-4.35" />
        </svg>
        <input class="search-input" type="text" placeholder="搜索社区、话题或人脉" />
      </div>
    </section>

    <section class="link-cards">
      <article v-for="item in linkItems" :key="item.id" class="link-card">
        <header class="card-header">
          <div class="card-title">{{ item.title }}</div>
          <button class="view-btn">查看名片</button>
        </header>
        <div class="card-meta">
          <span>{{ item.host }}</span>
          <span>{{ item.location }}</span>
        </div>
        <p class="card-desc">{{ item.description }}</p>
        <div class="card-tags">
          <span v-for="tag in item.tags" :key="tag" class="card-tag">{{ tag }}</span>
        </div>
        <footer class="card-footer">
          <div class="avatars">
            <img
              v-for="(avatar, index) in item.members"
              :key="index"
              :src="avatar"
              alt="member"
            />
          </div>
          <div class="member-count">{{ item.memberCount }} 位成员正在活跃</div>
        </footer>
      </article>
    </section>
  </main>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'

const tabs = ['咖啡广场', '聊天群', '1v1咨询']
const tags = ['不限', '消费', '制造', '文娱', '教育', '互联网', 'SaaS', '金融', 'AI', '泛科技', '企服', '新媒体', '大健康', '出海']

const activeTab = ref(tabs[0])
const activeTag = ref(tags[0])

const slides = [
  {
    id: 1,
    title: '这是一个共创社区',
    description: '解锁新灵感，认识新朋友，找到值得信赖的合作伙伴。',
    image: 'https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=1400&h=600&fit=crop'
  },
  {
    id: 2,
    title: '每周线下沙龙',
    description: '不同赛道的 CEO 分享真实操盘经验，开放问答与深度交流。',
    image: 'https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=1400&h=600&fit=crop'
  },
  {
    id: 3,
    title: '跨行业协作社区',
    description: '帮你快速对接项目资源，构建从创意到落地的一站式网络。',
    image: 'https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=1400&h=600&fit=crop'
  }
]

const currentSlide = ref(0)
let timer = null

const startTimer = () => {
  stopTimer()
  timer = setInterval(() => {
    currentSlide.value = (currentSlide.value + 1) % slides.length
  }, 5000)
}

const stopTimer = () => {
  if (timer) {
    clearInterval(timer)
    timer = null
  }
}

const setSlide = (index) => {
  currentSlide.value = index
  startTimer()
}

onMounted(() => {
  startTimer()
})

onBeforeUnmount(() => {
  stopTimer()
})

const linkItems = [
  {
    id: 1,
    title: '一水',
    host: '@个人创业',
    location: '南京 · 啡咖咖啡',
    description: '集合空间插画设计，针对传统线下消费的见解，欢迎交流合作。',
    tags: ['品牌升级', '消费体验', '空间设计'],
    members: [
      'https://images.unsplash.com/photo-1521572267360-ee0c2909d518?w=100&h=100&fit=crop',
      'https://images.unsplash.com/photo-1544723795-3fb6469f5b39?w=100&h=100&fit=crop',
      'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=100&h=100&fit=crop'
    ],
    memberCount: 46
  },
  {
    id: 2,
    title: '李天遥',
    host: '@某公司大客户销售经理',
    location: '深圳南山 · 喝杯咖啡',
    description: '互联网行业经验丰富，擅长针对中大型客户的解决方案打造与项目推进。',
    tags: ['B2B销售', '行业洞察', '客户经营'],
    members: [
      'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100&h=100&fit=crop',
      'https://images.unsplash.com/photo-1487412720507-e7ab37603c6f?w=100&h=100&fit=crop',
      'https://images.unsplash.com/photo-1524504388940-b1c1722653e1?w=100&h=100&fit=crop'
    ],
    memberCount: 58
  },
  {
    id: 3,
    title: '黄泽江',
    host: '@可想能源技术发展(深圳)有限公司投资经理',
    location: '上海 · 优质投资机构',
    description: '新能源与智能硬件投资经验，擅长发现潜力项目并提供投后赋能。',
    tags: ['新能源', '投融资', '业务拓展'],
    members: [
      'https://images.unsplash.com/photo-1524504388940-b1c1722653e1?w=100&h=100&fit=crop',
      'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=100&h=100&fit=crop',
      'https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=100&h=100&fit=crop'
    ],
    memberCount: 39
  },
  {
    id: 4,
    title: '刘捷',
    host: '@上海合提信息科技有限公司创始人',
    location: '上海 · 创业者社群',
    description: '具备 0-1 产品战略经验，帮助创业团队建立从产品到商业化的全链路能力。',
    tags: ['产品战略', '商业化', '创业方法'],
    members: [
      'https://images.unsplash.com/photo-1544723795-3fb6469f5b39?w=100&h=100&fit=crop',
      'https://images.unsplash.com/photo-1487412720507-e7ab37603c6f?w=100&h=100&fit=crop',
      'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100&h=100&fit=crop'
    ],
    memberCount: 64
  }
]
</script>

<style scoped>
.link-page {
  flex: 1;
  padding: 40px 48px;
  background-color: #ffffff;
  overflow-y: auto;
  height: 100vh;
}

.page-header {
  margin-bottom: 32px;
}

.page-title {
  font-size: 42px;
  font-weight: 700;
  color: #162231;
  margin-bottom: 8px;
  letter-spacing: -0.5px;
}

.page-subtitle {
  font-size: 20px;
  font-weight: 600;
  color: #1c2940;
}

.tab-row {
  display: flex;
  gap: 32px;
  margin-top: 32px;
  border-bottom: 1px solid #e7e7e7;
}

.tab-btn {
  padding: 12px 0;
  font-size: 16px;
  color: #7d8591;
  background: none;
  border: none;
  position: relative;
  cursor: pointer;
  transition: color 0.2s;
}

.tab-btn::after {
  content: '';
  position: absolute;
  left: 0;
  bottom: -1px;
  width: 100%;
  height: 2px;
  background-color: transparent;
  transition: background-color 0.2s;
}

.tab-btn:hover {
  color: #111827;
}

.tab-btn.active {
  color: #111827;
  font-weight: 600;
}

.tab-btn.active::after {
  background-color: #111827;
}

.hero-section {
  background-color: #f7f7f7;
  border-radius: 24px;
  padding: 24px;
  display: grid;
  grid-template-columns: 1fr max-content;
  gap: 24px;
  margin-bottom: 32px;
  border: 1px solid #f0f0f0;
}

.hero-slider {
  position: relative;
  overflow: hidden;
  border-radius: 20px;
  height: 340px;
}

.hero-slide {
  position: absolute;
  inset: 0;
}

.hero-slide img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.hero-caption {
  position: absolute;
  left: 24px;
  bottom: 24px;
  background: rgba(0, 0, 0, 0.55);
  backdrop-filter: blur(4px);
  color: #ffffff;
  padding: 16px 20px;
  border-radius: 12px;
  max-width: 420px;
}

.hero-caption h2 {
  margin: 0 0 8px;
  font-size: 18px;
  font-weight: 600;
}

.hero-caption p {
  margin: 0;
  font-size: 14px;
  line-height: 1.6;
}

.slider-controls {
  position: absolute;
  bottom: 16px;
  right: 16px;
  display: flex;
  gap: 8px;
}

.dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  border: none;
  background-color: rgba(255, 255, 255, 0.4);
  cursor: pointer;
  transition: background-color 0.2s;
}

.dot.active {
  background-color: #ffffff;
}

.hero-actions {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.hero-btn {
  padding: 12px 24px;
  border-radius: 12px;
  font-size: 16px;
  border: none;
  cursor: pointer;
  background-color: #111827;
  color: #ffffff;
  transition: transform 0.2s, box-shadow 0.2s;
  min-width: 140px;
}

.hero-btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 12px 24px rgba(17, 24, 39, 0.12);
}

.hero-btn.outline {
  background-color: #ffffff;
  color: #111827;
  border: 1px solid #d1d5db;
  box-shadow: none;
}

.hero-btn.outline:hover {
  box-shadow: 0 12px 24px rgba(17, 24, 39, 0.08);
}

.filter-section {
  display: flex;
  flex-direction: column;
  gap: 16px;
  margin-bottom: 32px;
}

.filter-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}

.tag-btn {
  padding: 8px 16px;
  border-radius: 999px;
  border: 1px solid #e0e0e0;
  background-color: #ffffff;
  font-size: 13px;
  color: #7d8591;
  cursor: pointer;
  transition: all 0.2s;
}

.tag-btn:hover {
  border-color: #cbd5e0;
  color: #111827;
}

.tag-btn.active {
  background-color: #111827;
  color: #ffffff;
  border-color: #111827;
}

.search-box {
  position: relative;
  max-width: 420px;
}

.search-icon {
  position: absolute;
  left: 16px;
  top: 50%;
  transform: translateY(-50%);
  width: 18px;
  height: 18px;
  color: #9ca3af;
}

.search-input {
  width: 100%;
  padding: 12px 16px 12px 44px;
  border-radius: 999px;
  border: 1px solid #e0e0e0;
  background-color: #ffffff;
  font-size: 14px;
  transition: border-color 0.2s;
}

.search-input:focus {
  outline: none;
  border-color: #111827;
}

.link-cards {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 24px;
  padding-bottom: 48px;
}

.link-card {
  border-radius: 20px;
  border: 1px solid #e5e7eb;
  padding: 24px;
  background-color: #ffffff;
  display: flex;
  flex-direction: column;
  gap: 16px;
  box-shadow: 0 16px 32px rgba(17, 24, 39, 0.04);
  transition: transform 0.2s, box-shadow 0.2s;
}

.link-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 24px 40px rgba(17, 24, 39, 0.08);
}

.card-header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
}

.card-title {
  font-size: 18px;
  font-weight: 600;
  color: #111827;
}

.view-btn {
  background-color: #000000;
  color: #ffffff;
  border: none;
  border-radius: 999px;
  padding: 6px 16px;
  font-size: 13px;
  cursor: pointer;
}

.card-meta {
  display: flex;
  gap: 12px;
  font-size: 13px;
  color: #6b7280;
}

.card-desc {
  font-size: 14px;
  color: #374151;
  line-height: 1.6;
  margin: 0;
}

.card-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.card-tag {
  padding: 6px 12px;
  border-radius: 999px;
  background-color: #f3f4f6;
  color: #4b5563;
  font-size: 12px;
}

.card-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
}

.avatars {
  display: flex;
  align-items: center;
}

.avatars img {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  border: 2px solid #ffffff;
  margin-left: -8px;
  background-color: #f3f4f6;
}

.avatars img:first-child {
  margin-left: 0;
}

.member-count {
  font-size: 12px;
  color: #6b7280;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.6s;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

@media (max-width: 1280px) {
  .link-cards {
    grid-template-columns: 1fr;
  }

  .hero-section {
    grid-template-columns: 1fr;
  }

  .hero-actions {
    flex-direction: row;
    justify-content: flex-end;
  }
}

@media (max-width: 900px) {
  .link-page {
    padding: 32px 24px;
  }

  .page-title {
    font-size: 32px;
  }
}
</style>

```

```vue
<template>
  <aside class="sidebar">
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
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <circle cx="12" cy="12" r="10"></circle>
          <path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path>
          <path d="M12 17h.01"></path>
        </svg>
        <span>项目</span>
      </a>
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
          <circle cx="12" cy="10" r="3"></circle>
        </svg>
        <span>活动</span>
      </a>
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
          <circle cx="12" cy="7" r="4"></circle>
        </svg>
        <span>我的</span>
      </a>
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
</template>

<script setup>
import { useRoute } from 'vue-router'

const route = useRoute()
</script>

<style scoped>
.sidebar {
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
</style>


```

## 更新内容
- 新增 `LinkPage` 路由页，复刻参考样式：包括“咖啡广场/聊天群/1v1咨询”页签、自动轮播图、筛选标签、搜索框以及社区卡片列表。
- 轮播图使用 `setInterval` 自动切换，点击小圆点可手动跳转。
- `Sidebar` 中“链接”菜单改为 `RouterLink`，与“学习”“牛人”同样支持路由跳转并高亮。
- 路由表新增 `/links`，可通过左侧菜单或直接访问跳转。

## 使用方式
- 运行 `npm run dev` 后，通过左侧菜单点击“链接”即可进入新页面，轮播将自动播放。

---

**User**

这个链接页面和参考页面有些不同 投案例和约牛人的位置不合适

---

**Cursor**

```vue
<template>
  <main class="link-page">
    <section class="page-header">
      <h1 class="page-title">Starter Network</h1>
      <p class="page-subtitle">认识100位社区CEO</p>

      <div class="tab-row">
        <button
          v-for="tab in tabs"
          :key="tab"
          :class="['tab-btn', { active: activeTab === tab }]"
          @click="activeTab = tab"
        >
          {{ tab }}
        </button>
      </div>
    </section>

    <section class="hero-section">
      <div class="hero-slider">
        <transition-group name="fade" tag="div">
          <div
            v-for="(slide, index) in slides"
            :key="slide.id"
            v-show="currentSlide === index"
            class="hero-slide"
          >
            <img :src="slide.image" :alt="slide.title" />
            <div class="hero-caption">
              <h2>{{ slide.title }}</h2>
              <p>{{ slide.description }}</p>
            </div>
          </div>
        </transition-group>

        <div class="slider-controls">
          <button
            v-for="(slide, index) in slides"
            :key="slide.id"
            :class="['dot', { active: currentSlide === index }]"
            @click="setSlide(index)"
          />
        </div>
      </div>
      <div class="hero-actions">
        <button class="hero-btn">投案例</button>
        <button class="hero-btn outline">约牛人</button>
      </div>
    </section>

    <section class="filter-section">
      <div class="filter-tags">
        <button
          v-for="tag in tags"
          :key="tag"
          :class="['tag-btn', { active: activeTag === tag }]"
          @click="activeTag = tag"
        >
          {{ tag }}
        </button>
      </div>
      <div class="search-box">
        <svg class="search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="11" cy="11" r="8" />
          <path d="m21 21-4.35-4.35" />
        </svg>
        <input class="search-input" type="text" placeholder="搜索社区、话题或人脉" />
      </div>
    </section>

    <section class="link-cards">
      <article v-for="item in linkItems" :key="item.id" class="link-card">
        <header class="card-header">
          <div class="card-title">{{ item.title }}</div>
          <button class="view-btn">查看名片</button>
        </header>
        <div class="card-meta">
          <span>{{ item.host }}</span>
          <span>{{ item.location }}</span>
        </div>
        <p class="card-desc">{{ item.description }}</p>
        <div class="card-tags">
          <span v-for="tag in item.tags" :key="tag" class="card-tag">{{ tag }}</span>
        </div>
        <footer class="card-footer">
          <div class="avatars">
            <img
              v-for="(avatar, index) in item.members"
              :key="index"
              :src="avatar"
              alt="member"
            />
          </div>
          <div class="member-count">{{ item.memberCount }} 位成员正在活跃</div>
        </footer>
      </article>
    </section>
  </main>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'

const tabs = ['咖啡广场', '聊天群', '1v1咨询']
const tags = ['不限', '消费', '制造', '文娱', '教育', '互联网', 'SaaS', '金融', 'AI', '泛科技', '企服', '新媒体', '大健康', '出海']

const activeTab = ref(tabs[0])
const activeTag = ref(tags[0])

const slides = [
  {
    id: 1,
    title: '这是一个共创社区',
    description: '解锁新灵感，认识新朋友，找到值得信赖的合作伙伴。',
    image: 'https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=1400&h=600&fit=crop'
  },
  {
    id: 2,
    title: '每周线下沙龙',
    description: '不同赛道的 CEO 分享真实操盘经验，开放问答与深度交流。',
    image: 'https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=1400&h=600&fit=crop'
  },
  {
    id: 3,
    title: '跨行业协作社区',
    description: '帮你快速对接项目资源，构建从创意到落地的一站式网络。',
    image: 'https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=1400&h=600&fit=crop'
  }
]

const currentSlide = ref(0)
let timer = null

const startTimer = () => {
  stopTimer()
  timer = setInterval(() => {
    currentSlide.value = (currentSlide.value + 1) % slides.length
  }, 5000)
}

const stopTimer = () => {
  if (timer) {
    clearInterval(timer)
    timer = null
  }
}

const setSlide = (index) => {
  currentSlide.value = index
  startTimer()
}

onMounted(() => {
  startTimer()
})

onBeforeUnmount(() => {
  stopTimer()
})

const linkItems = [
  {
    id: 1,
    title: '一水',
    host: '@个人创业',
    location: '南京 · 啡咖咖啡',
    description: '集合空间插画设计，针对传统线下消费的见解，欢迎交流合作。',
    tags: ['品牌升级', '消费体验', '空间设计'],
    members: [
      'https://images.unsplash.com/photo-1521572267360-ee0c2909d518?w=100&h=100&fit=crop',
      'https://images.unsplash.com/photo-1544723795-3fb6469f5b39?w=100&h=100&fit=crop',
      'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=100&h=100&fit=crop'
    ],
    memberCount: 46
  },
  {
    id: 2,
    title: '李天遥',
    host: '@某公司大客户销售经理',
    location: '深圳南山 · 喝杯咖啡',
    description: '互联网行业经验丰富，擅长针对中大型客户的解决方案打造与项目推进。',
    tags: ['B2B销售', '行业洞察', '客户经营'],
    members: [
      'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100&h=100&fit=crop',
      'https://images.unsplash.com/photo-1487412720507-e7ab37603c6f?w=100&h=100&fit=crop',
      'https://images.unsplash.com/photo-1524504388940-b1c1722653e1?w=100&h=100&fit=crop'
    ],
    memberCount: 58
  },
  {
    id: 3,
    title: '黄泽江',
    host: '@可想能源技术发展(深圳)有限公司投资经理',
    location: '上海 · 优质投资机构',
    description: '新能源与智能硬件投资经验，擅长发现潜力项目并提供投后赋能。',
    tags: ['新能源', '投融资', '业务拓展'],
    members: [
      'https://images.unsplash.com/photo-1524504388940-b1c1722653e1?w=100&h=100&fit=crop',
      'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=100&h=100&fit=crop',
      'https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=100&h=100&fit=crop'
    ],
    memberCount: 39
  },
  {
    id: 4,
    title: '刘捷',
    host: '@上海合提信息科技有限公司创始人',
    location: '上海 · 创业者社群',
    description: '具备 0-1 产品战略经验，帮助创业团队建立从产品到商业化的全链路能力。',
    tags: ['产品战略', '商业化', '创业方法'],
    members: [
      'https://images.unsplash.com/photo-1544723795-3fb6469f5b39?w=100&h=100&fit=crop',
      'https://images.unsplash.com/photo-1487412720507-e7ab37603c6f?w=100&h=100&fit=crop',
      'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100&h=100&fit=crop'
    ],
    memberCount: 64
  }
]
</script>

<style scoped>
.link-page {
  flex: 1;
  padding: 40px 48px;
  background-color: #ffffff;
  overflow-y: auto;
  height: 100vh;
}

.page-header {
  margin-bottom: 32px;
}

.page-title {
  font-size: 42px;
  font-weight: 700;
  color: #162231;
  margin-bottom: 8px;
  letter-spacing: -0.5px;
}

.page-subtitle {
  font-size: 20px;
  font-weight: 600;
  color: #1c2940;
}

.tab-row {
  display: flex;
  gap: 32px;
  margin-top: 32px;
  border-bottom: 1px solid #e7e7e7;
}

.tab-btn {
  padding: 12px 0;
  font-size: 16px;
  color: #7d8591;
  background: none;
  border: none;
  position: relative;
  cursor: pointer;
  transition: color 0.2s;
}

.tab-btn::after {
  content: '';
  position: absolute;
  left: 0;
  bottom: -1px;
  width: 100%;
  height: 2px;
  background-color: transparent;
  transition: background-color 0.2s;
}

.tab-btn:hover {
  color: #111827;
}

.tab-btn.active {
  color: #111827;
  font-weight: 600;
}

.tab-btn.active::after {
  background-color: #111827;
}

.hero-section {
  background-color: #f7f7f7;
  border-radius: 24px;
  padding: 24px;
  display: grid;
  grid-template-columns: 1fr max-content;
  gap: 24px;
  margin-bottom: 32px;
  border: 1px solid #f0f0f0;
}

.hero-slider {
  position: relative;
  overflow: hidden;
  border-radius: 20px;
  height: 340px;
}

.hero-slide {
  position: absolute;
  inset: 0;
}

.hero-slide img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.hero-caption {
  position: absolute;
  left: 24px;
  bottom: 24px;
  background: rgba(0, 0, 0, 0.55);
  backdrop-filter: blur(4px);
  color: #ffffff;
  padding: 16px 20px;
  border-radius: 12px;
  max-width: 420px;
}

.hero-caption h2 {
  margin: 0 0 8px;
  font-size: 18px;
  font-weight: 600;
}

.hero-caption p {
  margin: 0;
  font-size: 14px;
  line-height: 1.6;
}

.slider-controls {
  position: absolute;
  bottom: 16px;
  right: 16px;
  display: flex;
  gap: 8px;
}

.dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  border: none;
  background-color: rgba(255, 255, 255, 0.4);
  cursor: pointer;
  transition: background-color 0.2s;
}

.dot.active {
  background-color: #ffffff;
}

.hero-actions {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.hero-btn {
  padding: 12px 24px;
  border-radius: 12px;
  font-size: 16px;
  border: none;
  cursor: pointer;
  background-color: #111827;
  color: #ffffff;
  transition: transform 0.2s, box-shadow 0.2s;
  min-width: 140px;
}

.hero-btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 12px 24px rgba(17, 24, 39, 0.12);
}

.hero-btn.outline {
  background-color: #ffffff;
  color: #111827;
  border: 1px solid #d1d5db;
  box-shadow: none;
}

.hero-btn.outline:hover {
  box-shadow: 0 12px 24px rgba(17, 24, 39, 0.08);
}

.filter-section {
  display: flex;
  flex-direction: column;
  gap: 16px;
  margin-bottom: 32px;
}

.filter-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}

.tag-btn {
  padding: 8px 16px;
  border-radius: 999px;
  border: 1px solid #e0e0e0;
  background-color: #ffffff;
  font-size: 13px;
  color: #7d8591;
  cursor: pointer;
  transition: all 0.2s;
}

.tag-btn:hover {
  border-color: #cbd5e0;
  color: #111827;
}

.tag-btn.active {
  background-color: #111827;
  color: #ffffff;
  border-color: #111827;
}

.search-box {
  position: relative;
  max-width: 420px;
}

.search-icon {
  position: absolute;
  left: 16px;
  top: 50%;
  transform: translateY(-50%);
  width: 18px;
  height: 18px;
  color: #9ca3af;
}

.search-input {
  width: 100%;
  padding: 12px 16px 12px 44px;
  border-radius: 999px;
  border: 1px solid #e0e0e0;
  background-color: #ffffff;
  font-size: 14px;
  transition: border-color 0.2s;
}

.search-input:focus {
  outline: none;
  border-color: #111827;
}

.link-cards {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 24px;
  padding-bottom: 48px;
}

.link-card {
  border-radius: 20px;
  border: 1px solid #e5e7eb;
  padding: 24px;
  background-color: #ffffff;
  display: flex;
  flex-direction: column;
  gap: 16px;
  box-shadow: 0 16px 32px rgba(17, 24, 39, 0.04);
  transition: transform 0.2s, box-shadow 0.2s;
}

.link-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 24px 40px rgba(17, 24, 39, 0.08);
}

.card-header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
}

.card-title {
  font-size: 18px;
  font-weight: 600;
  color: #111827;
}

.view-btn {
  background-color: #000000;
  color: #ffffff;
  border: none;
  border-radius: 999px;
  padding: 6px 16px;
  font-size: 13px;
  cursor: pointer;
}

.card-meta {
  display: flex;
  gap: 12px;
  font-size: 13px;
  color: #6b7280;
}

.card-desc {
  font-size: 14px;
  color: #374151;
  line-height: 1.6;
  margin: 0;
}

.card-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.card-tag {
  padding: 6px 12px;
  border-radius: 999px;
  background-color: #f3f4f6;
  color: #4b5563;
  font-size: 12px;
}

.card-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
}

.avatars {
  display: flex;
  align-items: center;
}

.avatars img {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  border: 2px solid #ffffff;
  margin-left: -8px;
  background-color: #f3f4f6;
}

.avatars img:first-child {
  margin-left: 0;
}

.member-count {
  font-size: 12px;
  color: #6b7280;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.6s;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

@media (max-width: 1280px) {
  .link-cards {
    grid-template-columns: 1fr;
  }

  .hero-section {
    grid-template-columns: 1fr;
  }

  .hero-actions {
    flex-direction: row;
    justify-content: flex-end;
  }
}

@media (max-width: 900px) {
  .link-page {
    padding: 32px 24px;
  }

  .page-title {
    font-size: 32px;
  }
}
</style>


```

```vue
<template>
  <main class="link-page">
    <section class="page-header">
      <h1 class="page-title">Starter Network</h1>
      <p class="page-subtitle">认识100位社区CEO</p>

      <div class="tab-row">
        <button
          v-for="tab in tabs"
          :key="tab"
          :class="['tab-btn', { active: activeTab === tab }]"
          @click="activeTab = tab"
        >
          {{ tab }}
        </button>
      </div>
    </section>

    <section class="hero-section">
      <div class="hero-slider">
        <transition-group name="fade" tag="div">
          <div
            v-for="(slide, index) in slides"
            :key="slide.id"
            v-show="currentSlide === index"
            class="hero-slide"
          >
            <img :src="slide.image" :alt="slide.title" />
            <div class="hero-caption">
              <h2>{{ slide.title }}</h2>
              <p>{{ slide.description }}</p>
            </div>
          </div>
        </transition-group>

        <div class="slider-controls">
          <button
            v-for="(slide, index) in slides"
            :key="slide.id"
            :class="['dot', { active: currentSlide === index }]"
            @click="setSlide(index)"
          />
        </div>
      </div>
      <div class="hero-actions">
        <button class="hero-btn">投案例</button>
        <button class="hero-btn outline">约牛人</button>
      </div>
    </section>

    <section class="filter-section">
      <div class="filter-tags">
        <button
          v-for="tag in tags"
          :key="tag"
          :class="['tag-btn', { active: activeTag === tag }]"
          @click="activeTag = tag"
        >
          {{ tag }}
        </button>
      </div>
      <div class="search-box">
        <svg class="search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="11" cy="11" r="8" />
          <path d="m21 21-4.35-4.35" />
        </svg>
        <input class="search-input" type="text" placeholder="搜索社区、话题或人脉" />
      </div>
    </section>

    <section class="link-cards">
      <article v-for="item in linkItems" :key="item.id" class="link-card">
        <header class="card-header">
          <div class="card-title">{{ item.title }}</div>
          <button class="view-btn">查看名片</button>
        </header>
        <div class="card-meta">
          <span>{{ item.host }}</span>
          <span>{{ item.location }}</span>
        </div>
        <p class="card-desc">{{ item.description }}</p>
        <div class="card-tags">
          <span v-for="tag in item.tags" :key="tag" class="card-tag">{{ tag }}</span>
        </div>
        <footer class="card-footer">
          <div class="avatars">
            <img
              v-for="(avatar, index) in item.members"
              :key="index"
              :src="avatar"
              alt="member"
            />
          </div>
          <div class="member-count">{{ item.memberCount }} 位成员正在活跃</div>
        </footer>
      </article>
    </section>
  </main>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'

const tabs = ['咖啡广场', '聊天群', '1v1咨询']
const tags = ['不限', '消费', '制造', '文娱', '教育', '互联网', 'SaaS', '金融', 'AI', '泛科技', '企服', '新媒体', '大健康', '出海']

const activeTab = ref(tabs[0])
const activeTag = ref(tags[0])

const slides = [
  {
    id: 1,
    title: '这是一个共创社区',
    description: '解锁新灵感，认识新朋友，找到值得信赖的合作伙伴。',
    image: 'https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=1400&h=600&fit=crop'
  },
  {
    id: 2,
    title: '每周线下沙龙',
    description: '不同赛道的 CEO 分享真实操盘经验，开放问答与深度交流。',
    image: 'https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=1400&h=600&fit=crop'
  },
  {
    id: 3,
    title: '跨行业协作社区',
    description: '帮你快速对接项目资源，构建从创意到落地的一站式网络。',
    image: 'https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=1400&h=600&fit=crop'
  }
]

const currentSlide = ref(0)
let timer = null

const startTimer = () => {
  stopTimer()
  timer = setInterval(() => {
    currentSlide.value = (currentSlide.value + 1) % slides.length
  }, 5000)
}

const stopTimer = () => {
  if (timer) {
    clearInterval(timer)
    timer = null
  }
}

const setSlide = (index) => {
  currentSlide.value = index
  startTimer()
}

onMounted(() => {
  startTimer()
})

onBeforeUnmount(() => {
  stopTimer()
})

const linkItems = [
  {
    id: 1,
    title: '一水',
    host: '@个人创业',
    location: '南京 · 啡咖咖啡',
    description: '集合空间插画设计，针对传统线下消费的见解，欢迎交流合作。',
    tags: ['品牌升级', '消费体验', '空间设计'],
    members: [
      'https://images.unsplash.com/photo-1521572267360-ee0c2909d518?w=100&h=100&fit=crop',
      'https://images.unsplash.com/photo-1544723795-3fb6469f5b39?w=100&h=100&fit=crop',
      'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=100&h=100&fit=crop'
    ],
    memberCount: 46
  },
  {
    id: 2,
    title: '李天遥',
    host: '@某公司大客户销售经理',
    location: '深圳南山 · 喝杯咖啡',
    description: '互联网行业经验丰富，擅长针对中大型客户的解决方案打造与项目推进。',
    tags: ['B2B销售', '行业洞察', '客户经营'],
    members: [
      'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100&h=100&fit=crop',
      'https://images.unsplash.com/photo-1487412720507-e7ab37603c6f?w=100&h=100&fit=crop',
      'https://images.unsplash.com/photo-1524504388940-b1c1722653e1?w=100&h=100&fit=crop'
    ],
    memberCount: 58
  },
  {
    id: 3,
    title: '黄泽江',
    host: '@可想能源技术发展(深圳)有限公司投资经理',
    location: '上海 · 优质投资机构',
    description: '新能源与智能硬件投资经验，擅长发现潜力项目并提供投后赋能。',
    tags: ['新能源', '投融资', '业务拓展'],
    members: [
      'https://images.unsplash.com/photo-1524504388940-b1c1722653e1?w=100&h=100&fit=crop',
      'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=100&h=100&fit=crop',
      'https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=100&h=100&fit=crop'
    ],
    memberCount: 39
  },
  {
    id: 4,
    title: '刘捷',
    host: '@上海合提信息科技有限公司创始人',
    location: '上海 · 创业者社群',
    description: '具备 0-1 产品战略经验，帮助创业团队建立从产品到商业化的全链路能力。',
    tags: ['产品战略', '商业化', '创业方法'],
    members: [
      'https://images.unsplash.com/photo-1544723795-3fb6469f5b39?w=100&h=100&fit=crop',
      'https://images.unsplash.com/photo-1487412720507-e7ab37603c6f?w=100&h=100&fit=crop',
      'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100&h=100&fit=crop'
    ],
    memberCount: 64
  }
]
</script>

<style scoped>
.link-page {
  flex: 1;
  padding: 40px 48px;
  background-color: #ffffff;
  overflow-y: auto;
  height: 100vh;
}

.page-header {
  margin-bottom: 32px;
}

.page-title {
  font-size: 42px;
  font-weight: 700;
  color: #162231;
  margin-bottom: 8px;
  letter-spacing: -0.5px;
}

.page-subtitle {
  font-size: 20px;
  font-weight: 600;
  color: #1c2940;
}

.tab-row {
  display: flex;
  gap: 32px;
  margin-top: 32px;
  border-bottom: 1px solid #e7e7e7;
}

.tab-btn {
  padding: 12px 0;
  font-size: 16px;
  color: #7d8591;
  background: none;
  border: none;
  position: relative;
  cursor: pointer;
  transition: color 0.2s;
}

.tab-btn::after {
  content: '';
  position: absolute;
  left: 0;
  bottom: -1px;
  width: 100%;
  height: 2px;
  background-color: transparent;
  transition: background-color 0.2s;
}

.tab-btn:hover {
  color: #111827;
}

.tab-btn.active {
  color: #111827;
  font-weight: 600;
}

.tab-btn.active::after {
  background-color: #111827;
}

.hero-section {
  position: relative;
  background-color: #f7f8fa;
  border-radius: 24px;
  padding: 24px;
  margin-bottom: 32px;
  border: 1px solid #f0f0f0;
}

.hero-slider {
  position: relative;
  overflow: hidden;
  border-radius: 20px;
  height: 360px;
}

.hero-slide {
  position: absolute;
  inset: 0;
}

.hero-slide img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.hero-caption {
  position: absolute;
  left: 24px;
  bottom: 24px;
  background: rgba(0, 0, 0, 0.55);
  backdrop-filter: blur(4px);
  color: #ffffff;
  padding: 18px 24px;
  border-radius: 14px;
  max-width: 440px;
}

.hero-caption h2 {
  margin: 0 0 8px;
  font-size: 20px;
  font-weight: 600;
}

.hero-caption p {
  margin: 0;
  font-size: 14px;
  line-height: 1.6;
}

.slider-controls {
  position: absolute;
  bottom: 16px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 8px;
}

.dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  border: none;
  background-color: rgba(255, 255, 255, 0.4);
  cursor: pointer;
  transition: background-color 0.2s;
}

.dot.active {
  background-color: #ffffff;
}

.hero-actions {
  position: absolute;
  right: 36px;
  bottom: 36px;
  display: flex;
  gap: 12px;
}

.hero-btn {
  padding: 12px 24px;
  border-radius: 999px;
  font-size: 14px;
  border: none;
  cursor: pointer;
  background-color: #111827;
  color: #ffffff;
  transition: transform 0.2s, box-shadow 0.2s;
  min-width: 120px;
}

.hero-btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 12px 24px rgba(17, 24, 39, 0.12);
}

.hero-btn.outline {
  background-color: #ffffff;
  color: #111827;
  border: 1px solid #d1d5db;
  box-shadow: none;
}

.hero-btn.outline:hover {
  box-shadow: 0 12px 24px rgba(17, 24, 39, 0.08);
}

.filter-section {
  display: flex;
  flex-direction: column;
  gap: 16px;
  margin-bottom: 32px;
}

.filter-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}

.tag-btn {
  padding: 8px 16px;
  border-radius: 999px;
  border: 1px solid #e0e0e0;
  background-color: #ffffff;
  font-size: 13px;
  color: #7d8591;
  cursor: pointer;
  transition: all 0.2s;
}

.tag-btn:hover {
  border-color: #cbd5e0;
  color: #111827;
}

.tag-btn.active {
  background-color: #111827;
  color: #ffffff;
  border-color: #111827;
}

.search-box {
  position: relative;
  max-width: 420px;
}

.search-icon {
  position: absolute;
  left: 16px;
  top: 50%;
  transform: translateY(-50%);
  width: 18px;
  height: 18px;
  color: #9ca3af;
}

.search-input {
  width: 100%;
  padding: 12px 16px 12px 44px;
  border-radius: 999px;
  border: 1px solid #e0e0e0;
  background-color: #ffffff;
  font-size: 14px;
  transition: border-color 0.2s;
}

.search-input:focus {
  outline: none;
  border-color: #111827;
}

.link-cards {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 24px;
  padding-bottom: 48px;
}

.link-card {
  border-radius: 20px;
  border: 1px solid #e5e7eb;
  padding: 24px;
  background-color: #ffffff;
  display: flex;
  flex-direction: column;
  gap: 16px;
  box-shadow: 0 16px 32px rgba(17, 24, 39, 0.04);
  transition: transform 0.2s, box-shadow 0.2s;
}

.link-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 24px 40px rgba(17, 24, 39, 0.08);
}

.card-header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
}

.card-title {
  font-size: 18px;
  font-weight: 600;
  color: #111827;
}

.view-btn {
  background-color: #000000;
  color: #ffffff;
  border: none;
  border-radius: 999px;
  padding: 6px 16px;
  font-size: 13px;
  cursor: pointer;
}

.card-meta {
  display: flex;
  gap: 12px;
  font-size: 13px;
  color: #6b7280;
}

.card-desc {
  font-size: 14px;
  color: #374151;
  line-height: 1.6;
  margin: 0;
}

.card-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.card-tag {
  padding: 6px 12px;
  border-radius: 999px;
  background-color: #f3f4f6;
  color: #4b5563;
  font-size: 12px;
}

.card-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
}

.avatars {
  display: flex;
  align-items: center;
}

.avatars img {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  border: 2px solid #ffffff;
  margin-left: -8px;
  background-color: #f3f4f6;
}

.avatars img:first-child {
  margin-left: 0;
}

.member-count {
  font-size: 12px;
  color: #6b7280;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.6s;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

@media (max-width: 1280px) {
  .link-cards {
    grid-template-columns: 1fr;
  }

  .hero-section {
    grid-template-columns: 1fr;
  }

  .hero-actions {
    flex-direction: row;
    justify-content: flex-end;
  }
}

@media (max-width: 900px) {
  .link-page {
    padding: 32px 24px;
  }

  .page-title {
    font-size: 32px;
  }
}
</style>


```

- 调整了链接页顶部 Hero 模块布局：改为单列全宽轮播，按钮 `投案例` 与 `约牛人` 绝对定位在右下角，更贴近参考页面。
- 轮播图底部指示点移至居中位置，按钮使用圆角 Pill 风格，与参考风格一致。
- 轮播标题卡片与高度、留白一并优化，更符合视觉比例。

---

**User**

按照这个风格生成一个项目界面 点击链接可以跳转过去 我提供参考页面

---

**Cursor**

```javascript
import { createRouter, createWebHistory } from 'vue-router'

import HomePage from '../components/MainContent.vue'
import TalentPage from '../pages/TalentPage.vue'
import LinkPage from '../pages/LinkPage.vue'
import ProjectPage from '../pages/ProjectPage.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomePage
  },
  {
    path: '/talents',
    name: 'talents',
    component: TalentPage
  },
  {
    path: '/links',
    name: 'links',
    component: LinkPage
  },
  {
    path: '/projects',
    name: 'projects',
    component: ProjectPage
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router


```

```vue
<template>
  <aside class="sidebar">
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
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
          <circle cx="12" cy="10" r="3"></circle>
        </svg>
        <span>活动</span>
      </a>
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
          <circle cx="12" cy="7" r="4"></circle>
        </svg>
        <span>我的</span>
      </a>
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
</template>

<script setup>
import { useRoute } from 'vue-router'

const route = useRoute()
</script>

<style scoped>
.sidebar {
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
</style>


```

```vue
<template>
  <main class="project-page">
    <section class="page-header">
      <h1 class="page-title">Starter Solutions</h1>
      <p class="page-subtitle">资源库 · 需求发布广场</p>
      <p class="page-desc">也许这里的一个项目，就是你事业的新起点</p>

      <div class="header-actions">
        <button class="primary-btn">发布我的项目</button>
      </div>
    </section>

    <section class="filters">
      <div class="category-tabs">
        <button
          v-for="category in categories"
          :key="category"
          :class="['category-tab', { active: activeCategory === category }]"
          @click="activeCategory = category"
        >
          {{ category }}
        </button>
      </div>

      <div class="sub-filters">
        <div class="filter-group">
          <span class="filter-label">需求分类</span>
          <div class="filter-buttons">
            <button
              v-for="tag in demandTags"
              :key="tag"
              :class="['filter-btn', { active: activeDemand === tag }]"
              @click="activeDemand = tag"
            >
              {{ tag }}
            </button>
          </div>
        </div>
        <div class="search-box">
          <svg class="search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="11" cy="11" r="8" />
            <path d="m21 21-4.35-4.35" />
          </svg>
          <input type="text" class="search-input" placeholder="搜索合作方向、关键词或企业名称" />
        </div>
      </div>
    </section>

    <section class="project-list">
      <article v-for="project in projects" :key="project.id" class="project-card">
        <div class="card-logo">
          <img :src="project.logo" :alt="project.name" />
        </div>
        <div class="card-body">
          <header class="card-header">
            <h2 class="project-name">{{ project.name }}</h2>
            <span class="project-type">{{ project.type }}</span>
          </header>
          <p class="project-desc">{{ project.description }}</p>
          <div class="project-tags">
            <span v-for="tag in project.tags" :key="tag" class="tag">
              {{ tag }}
            </span>
          </div>
        </div>
        <div class="card-actions">
          <button class="outline-btn">查看详情</button>
        </div>
      </article>
    </section>
  </main>
</template>

<script setup>
import { ref } from 'vue'

const categories = [
  '品牌加盟',
  '产品找代理',
  '寻找合伙人',
  '数字化服务',
  '流量合作',
  '资源链接',
  '寻找好产品',
  '品牌赞助',
  '融资',
  '其他'
]

const demandTags = ['不限', '消费', '企业服务', '文娱', '教育', 'AI', '品牌', '渠道', '资本', '产业链']

const activeCategory = ref(categories[0])
const activeDemand = ref(demandTags[0])

const projects = [
  {
    id: 1,
    name: 'Mindee',
    type: 'SaaS · 客户运营',
    description: '首创“24小时贴身情绪AI伙伴”，陪伴一监测一干预一成长全流程守护。需要算力、服务商、线下运营咨询、医院、资质等方向的合作。',
    logo: 'https://images.unsplash.com/photo-1633332755192-727a05c4013d?w=120&h=120&fit=crop',
    tags: ['情绪AI陪护', '智能硬件', '服务商合作']
  },
  {
    id: 2,
    name: '掌乐',
    type: '新媒体 · AI营销',
    description: '掌乐是一个AI驱动的短视频创作分发平台，通过“AI沉淀”模式解决市场痛点，实现从“人找货”到“货找人”的智能匹配。',
    logo: 'https://images.unsplash.com/photo-1545239351-1141bd82e8a6?w=120&h=120&fit=crop',
    tags: ['品牌增长', 'AI营销', '内容合作']
  },
  {
    id: 3,
    name: '球秀',
    type: '社区 · 运动科技',
    description: 'AI驱动的运动社区视频平台，连接教练、运动达人与品牌，为运动生态提供内容解决方案。',
    logo: 'https://images.unsplash.com/photo-1545239351-1141bd82e8a6?w=120&h=120&fit=crop',
    tags: ['体育品牌', '赛事合作', '内容共创']
  },
  {
    id: 4,
    name: 'Koogle',
    type: '应用 · 工具',
    description: '像使用 Google 一样快速准确地检索海外头条，帮助跨境营销团队提升海外研究效率。',
    logo: 'https://images.unsplash.com/photo-1580894732444-8ecded7900cd?w=120&h=120&fit=crop',
    tags: ['跨境营销', '数据服务', '工具分发']
  }
]
</script>

<style scoped>
.project-page {
  flex: 1;
  padding: 40px 48px;
  background-color: #ffffff;
  overflow-y: auto;
  height: 100vh;
}

.page-header {
  margin-bottom: 32px;
}

.page-title {
  font-size: 42px;
  font-weight: 700;
  color: #1f2937;
  margin-bottom: 8px;
}

.page-subtitle {
  font-size: 28px;
  font-weight: 600;
  color: #111827;
  margin-bottom: 8px;
}

.page-desc {
  font-size: 16px;
  color: #6b7280;
  margin-bottom: 24px;
}

.header-actions {
  display: flex;
  gap: 12px;
}

.primary-btn {
  padding: 12px 28px;
  border-radius: 999px;
  background-color: #111827;
  color: #ffffff;
  border: none;
  font-size: 16px;
  cursor: pointer;
  transition: transform 0.2s, box-shadow 0.2s;
}

.primary-btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 12px 24px rgba(17, 24, 39, 0.12);
}

.filters {
  margin-bottom: 32px;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.category-tabs {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}

.category-tab {
  padding: 10px 16px;
  border-radius: 999px;
  border: 1px solid #e0e0e0;
  background-color: #ffffff;
  font-size: 14px;
  color: #6b7280;
  cursor: pointer;
  transition: all 0.2s;
}

.category-tab:hover {
  color: #111827;
  border-color: #cbd5e0;
}

.category-tab.active {
  background-color: #111827;
  color: #ffffff;
  border-color: #111827;
}

.sub-filters {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 16px;
}

.filter-group {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.filter-label {
  font-size: 13px;
  color: #6b7280;
}

.filter-buttons {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.filter-btn {
  padding: 8px 14px;
  border-radius: 999px;
  border: 1px solid #e5e7eb;
  background-color: #ffffff;
  font-size: 13px;
  color: #6b7280;
  cursor: pointer;
  transition: all 0.2s;
}

.filter-btn:hover {
  border-color: #cbd5e0;
  color: #111827;
}

.filter-btn.active {
  background-color: #111827;
  color: #ffffff;
  border-color: #111827;
}

.search-box {
  position: relative;
  width: 320px;
}

.search-icon {
  position: absolute;
  left: 14px;
  top: 50%;
  transform: translateY(-50%);
  width: 18px;
  height: 18px;
  color: #9ca3af;
}

.search-input {
  width: 100%;
  padding: 10px 14px 10px 42px;
  border: 1px solid #e5e7eb;
  border-radius: 999px;
  background-color: #ffffff;
  font-size: 14px;
  transition: border-color 0.2s;
}

.search-input:focus {
  outline: none;
  border-color: #111827;
}

.project-list {
  display: flex;
  flex-direction: column;
  gap: 24px;
  padding-bottom: 48px;
}

.project-card {
  display: grid;
  grid-template-columns: 120px 1fr auto;
  gap: 24px;
  padding: 24px;
  border-radius: 24px;
  border: 1px solid #e5e7eb;
  background-color: #ffffff;
  box-shadow: 0 18px 32px rgba(15, 23, 42, 0.05);
  align-items: center;
  transition: transform 0.2s, box-shadow 0.2s;
}

.project-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 24px 40px rgba(15, 23, 42, 0.08);
}

.card-logo {
  width: 120px;
  height: 120px;
  border-radius: 24px;
  background-color: #f9fafb;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.card-logo img {
  width: 80%;
  height: 80%;
  object-fit: contain;
}

.card-body {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.card-header {
  display: flex;
  align-items: center;
  gap: 12px;
}

.project-name {
  font-size: 20px;
  font-weight: 600;
  color: #111827;
}

.project-type {
  padding: 4px 10px;
  border-radius: 999px;
  background-color: #eef2ff;
  color: #4338ca;
  font-size: 12px;
  font-weight: 500;
}

.project-desc {
  font-size: 14px;
  color: #4b5563;
  line-height: 1.7;
  margin: 0;
}

.project-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.tag {
  padding: 6px 12px;
  border-radius: 999px;
  background-color: #f3f4f6;
  color: #4b5563;
  font-size: 12px;
}

.card-actions {
  display: flex;
  align-items: center;
}

.outline-btn {
  padding: 10px 18px;
  border-radius: 999px;
  border: 1px solid #d1d5db;
  background-color: #ffffff;
  color: #111827;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.2s;
}

.outline-btn:hover {
  border-color: #111827;
}

@media (max-width: 1280px) {
  .project-card {
    grid-template-columns: 90px 1fr;
    grid-template-areas:
      'logo header'
      'logo body'
      'logo actions';
  }

  .card-logo {
    grid-area: logo;
    width: 90px;
    height: 90px;
  }

  .card-body {
    grid-area: body;
  }

  .card-actions {
    grid-area: actions;
    justify-content: flex-start;
  }
}

@media (max-width: 900px) {
  .project-page {
    padding: 32px 24px;
  }

  .sub-filters {
    flex-direction: column;
    align-items: stretch;
  }

  .search-box {
    width: 100%;
  }
}
</style>

```

- 新增 `ProjectPage` 路由页（`/projects`），复制参考页面的结构：顶部标题与介绍、发布按钮、需求分类与搜索、项目列表卡片等。
- 项目卡片包含 logo、类型、描述和标签，样式采用大字号、圆角卡片、柔和阴影，匹配参考视觉。
- 在 `Sidebar` 中增加“项目”菜单为 `RouterLink`，与其他菜单保持激活态同步。
- 路由表加入 `/projects`，现可通过左侧栏进入项目页面。

---

**User**

这是目前的项目页面 相比较于参考页面 需求分类的字体样式不对 应该是淡色小字号 搜索栏在独立一行 多了一行

---

**Cursor**

```vue
<template>
  <main class="project-page">
    <section class="page-header">
      <h1 class="page-title">Starter Solutions</h1>
      <p class="page-subtitle">资源库 · 需求发布广场</p>
      <p class="page-desc">也许这里的一个项目，就是你事业的新起点</p>

      <div class="header-actions">
        <button class="primary-btn">发布我的项目</button>
      </div>
    </section>

    <section class="filters">
      <div class="category-tabs">
        <button
          v-for="category in categories"
          :key="category"
          :class="['category-tab', { active: activeCategory === category }]"
          @click="activeCategory = category"
        >
          {{ category }}
        </button>
      </div>

      <div class="sub-filters">
        <span class="filter-label">需求分类</span>
        <div class="filter-buttons">
          <button
            v-for="tag in demandTags"
            :key="tag"
            :class="['filter-btn', { active: activeDemand === tag }]"
            @click="activeDemand = tag"
          >
            {{ tag }}
          </button>
        </div>
      </div>

      <div class="search-row">
        <div class="search-box">
          <svg class="search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="11" cy="11" r="8" />
            <path d="m21 21-4.35-4.35" />
          </svg>
          <input type="text" class="search-input" placeholder="搜索合作方向、关键词或企业名称" />
        </div>
      </div>
    </section>

    <section class="project-list">
      <article v-for="project in projects" :key="project.id" class="project-card">
        <div class="card-logo">
          <img :src="project.logo" :alt="project.name" />
        </div>
        <div class="card-body">
          <header class="card-header">
            <h2 class="project-name">{{ project.name }}</h2>
            <span class="project-type">{{ project.type }}</span>
          </header>
          <p class="project-desc">{{ project.description }}</p>
          <div class="project-tags">
            <span v-for="tag in project.tags" :key="tag" class="tag">
              {{ tag }}
            </span>
          </div>
        </div>
        <div class="card-actions">
          <button class="outline-btn">查看详情</button>
        </div>
      </article>
    </section>
  </main>
</template>

<script setup>
import { ref } from 'vue'

const categories = [
  '品牌加盟',
  '产品找代理',
  '寻找合伙人',
  '数字化服务',
  '流量合作',
  '资源链接',
  '寻找好产品',
  '品牌赞助',
  '融资',
  '其他'
]

const demandTags = ['不限', '消费', '企业服务', '文娱', '教育', 'AI', '品牌', '渠道', '资本', '产业链']

const activeCategory = ref(categories[0])
const activeDemand = ref(demandTags[0])

const projects = [
  {
    id: 1,
    name: 'Mindee',
    type: 'SaaS · 客户运营',
    description: '首创“24小时贴身情绪AI伙伴”，陪伴一监测一干预一成长全流程守护。需要算力、服务商、线下运营咨询、医院、资质等方向的合作。',
    logo: 'https://images.unsplash.com/photo-1633332755192-727a05c4013d?w=120&h=120&fit=crop',
    tags: ['情绪AI陪护', '智能硬件', '服务商合作']
  },
  {
    id: 2,
    name: '掌乐',
    type: '新媒体 · AI营销',
    description: '掌乐是一个AI驱动的短视频创作分发平台，通过“AI沉淀”模式解决市场痛点，实现从“人找货”到“货找人”的智能匹配。',
    logo: 'https://images.unsplash.com/photo-1545239351-1141bd82e8a6?w=120&h=120&fit=crop',
    tags: ['品牌增长', 'AI营销', '内容合作']
  },
  {
    id: 3,
    name: '球秀',
    type: '社区 · 运动科技',
    description: 'AI驱动的运动社区视频平台，连接教练、运动达人与品牌，为运动生态提供内容解决方案。',
    logo: 'https://images.unsplash.com/photo-1545239351-1141bd82e8a6?w=120&h=120&fit=crop',
    tags: ['体育品牌', '赛事合作', '内容共创']
  },
  {
    id: 4,
    name: 'Koogle',
    type: '应用 · 工具',
    description: '像使用 Google 一样快速准确地检索海外头条，帮助跨境营销团队提升海外研究效率。',
    logo: 'https://images.unsplash.com/photo-1580894732444-8ecded7900cd?w=120&h=120&fit=crop',
    tags: ['跨境营销', '数据服务', '工具分发']
  }
]
</script>

<style scoped>
.project-page {
  flex: 1;
  padding: 40px 48px;
  background-color: #ffffff;
  overflow-y: auto;
  height: 100vh;
}

.page-header {
  margin-bottom: 32px;
}

.page-title {
  font-size: 42px;
  font-weight: 700;
  color: #1f2937;
  margin-bottom: 8px;
}

.page-subtitle {
  font-size: 28px;
  font-weight: 600;
  color: #111827;
  margin-bottom: 8px;
}

.page-desc {
  font-size: 16px;
  color: #6b7280;
  margin-bottom: 24px;
}

.header-actions {
  display: flex;
  gap: 12px;
}

.primary-btn {
  padding: 12px 28px;
  border-radius: 999px;
  background-color: #111827;
  color: #ffffff;
  border: none;
  font-size: 16px;
  cursor: pointer;
  transition: transform 0.2s, box-shadow 0.2s;
}

.primary-btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 12px 24px rgba(17, 24, 39, 0.12);
}

.filters {
  margin-bottom: 32px;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.category-tabs {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}

.category-tab {
  padding: 10px 16px;
  border-radius: 999px;
  border: 1px solid #e0e0e0;
  background-color: #ffffff;
  font-size: 14px;
  color: #6b7280;
  cursor: pointer;
  transition: all 0.2s;
}

.category-tab:hover {
  color: #111827;
  border-color: #cbd5e0;
}

.category-tab.active {
  background-color: #111827;
  color: #ffffff;
  border-color: #111827;
}

.sub-filters {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 16px;
}

.filter-group {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.filter-label {
  font-size: 13px;
  color: #6b7280;
}

.filter-buttons {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.filter-btn {
  padding: 8px 14px;
  border-radius: 999px;
  border: 1px solid #e5e7eb;
  background-color: #ffffff;
  font-size: 13px;
  color: #6b7280;
  cursor: pointer;
  transition: all 0.2s;
}

.filter-btn:hover {
  border-color: #cbd5e0;
  color: #111827;
}

.filter-btn.active {
  background-color: #111827;
  color: #ffffff;
  border-color: #111827;
}

.search-box {
  position: relative;
  width: 320px;
}

.search-icon {
  position: absolute;
  left: 14px;
  top: 50%;
  transform: translateY(-50%);
  width: 18px;
  height: 18px;
  color: #9ca3af;
}

.search-input {
  width: 100%;
  padding: 10px 14px 10px 42px;
  border: 1px solid #e5e7eb;
  border-radius: 999px;
  background-color: #ffffff;
  font-size: 14px;
  transition: border-color 0.2s;
}

.search-input:focus {
  outline: none;
  border-color: #111827;
}

.project-list {
  display: flex;
  flex-direction: column;
  gap: 24px;
  padding-bottom: 48px;
}

.project-card {
  display: grid;
  grid-template-columns: 120px 1fr auto;
  gap: 24px;
  padding: 24px;
  border-radius: 24px;
  border: 1px solid #e5e7eb;
  background-color: #ffffff;
  box-shadow: 0 18px 32px rgba(15, 23, 42, 0.05);
  align-items: center;
  transition: transform 0.2s, box-shadow 0.2s;
}

.project-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 24px 40px rgba(15, 23, 42, 0.08);
}

.card-logo {
  width: 120px;
  height: 120px;
  border-radius: 24px;
  background-color: #f9fafb;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.card-logo img {
  width: 80%;
  height: 80%;
  object-fit: contain;
}

.card-body {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.card-header {
  display: flex;
  align-items: center;
  gap: 12px;
}

.project-name {
  font-size: 20px;
  font-weight: 600;
  color: #111827;
}

.project-type {
  padding: 4px 10px;
  border-radius: 999px;
  background-color: #eef2ff;
  color: #4338ca;
  font-size: 12px;
  font-weight: 500;
}

.project-desc {
  font-size: 14px;
  color: #4b5563;
  line-height: 1.7;
  margin: 0;
}

.project-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.tag {
  padding: 6px 12px;
  border-radius: 999px;
  background-color: #f3f4f6;
  color: #4b5563;
  font-size: 12px;
}

.card-actions {
  display: flex;
  align-items: center;
}

.outline-btn {
  padding: 10px 18px;
  border-radius: 999px;
  border: 1px solid #d1d5db;
  background-color: #ffffff;
  color: #111827;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.2s;
}

.outline-btn:hover {
  border-color: #111827;
}

@media (max-width: 1280px) {
  .project-card {
    grid-template-columns: 90px 1fr;
    grid-template-areas:
      'logo header'
      'logo body'
      'logo actions';
  }

  .card-logo {
    grid-area: logo;
    width: 90px;
    height: 90px;
  }

  .card-body {
    grid-area: body;
  }

  .card-actions {
    grid-area: actions;
    justify-content: flex-start;
  }
}

@media (max-width: 900px) {
  .project-page {
    padding: 32px 24px;
  }

  .sub-filters {
    flex-direction: column;
    align-items: stretch;
  }

  .search-box {
    width: 100%;
  }
}
</style>


```

```vue
<template>
  <main class="project-page">
    <section class="page-header">
      <h1 class="page-title">Starter Solutions</h1>
      <p class="page-subtitle">资源库 · 需求发布广场</p>
      <p class="page-desc">也许这里的一个项目，就是你事业的新起点</p>

      <div class="header-actions">
        <button class="primary-btn">发布我的项目</button>
      </div>
    </section>

    <section class="filters">
      <div class="category-tabs">
        <button
          v-for="category in categories"
          :key="category"
          :class="['category-tab', { active: activeCategory === category }]"
          @click="activeCategory = category"
        >
          {{ category }}
        </button>
      </div>

      <div class="sub-filters">
        <span class="filter-label">需求分类</span>
        <div class="filter-buttons">
          <button
            v-for="tag in demandTags"
            :key="tag"
            :class="['filter-btn', { active: activeDemand === tag }]"
            @click="activeDemand = tag"
          >
            {{ tag }}
          </button>
        </div>
      </div>

      <div class="search-row">
        <div class="search-box">
          <svg class="search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="11" cy="11" r="8" />
            <path d="m21 21-4.35-4.35" />
          </svg>
          <input type="text" class="search-input" placeholder="搜索合作方向、关键词或企业名称" />
        </div>
      </div>
    </section>

    <section class="project-list">
      <article v-for="project in projects" :key="project.id" class="project-card">
        <div class="card-logo">
          <img :src="project.logo" :alt="project.name" />
        </div>
        <div class="card-body">
          <header class="card-header">
            <h2 class="project-name">{{ project.name }}</h2>
            <span class="project-type">{{ project.type }}</span>
          </header>
          <p class="project-desc">{{ project.description }}</p>
          <div class="project-tags">
            <span v-for="tag in project.tags" :key="tag" class="tag">
              {{ tag }}
            </span>
          </div>
        </div>
        <div class="card-actions">
          <button class="outline-btn">查看详情</button>
        </div>
      </article>
    </section>
  </main>
</template>

<script setup>
import { ref } from 'vue'

const categories = [
  '品牌加盟',
  '产品找代理',
  '寻找合伙人',
  '数字化服务',
  '流量合作',
  '资源链接',
  '寻找好产品',
  '品牌赞助',
  '融资',
  '其他'
]

const demandTags = ['不限', '消费', '企业服务', '文娱', '教育', 'AI', '品牌', '渠道', '资本', '产业链']

const activeCategory = ref(categories[0])
const activeDemand = ref(demandTags[0])

const projects = [
  {
    id: 1,
    name: 'Mindee',
    type: 'SaaS · 客户运营',
    description: '首创“24小时贴身情绪AI伙伴”，陪伴一监测一干预一成长全流程守护。需要算力、服务商、线下运营咨询、医院、资质等方向的合作。',
    logo: 'https://images.unsplash.com/photo-1633332755192-727a05c4013d?w=120&h=120&fit=crop',
    tags: ['情绪AI陪护', '智能硬件', '服务商合作']
  },
  {
    id: 2,
    name: '掌乐',
    type: '新媒体 · AI营销',
    description: '掌乐是一个AI驱动的短视频创作分发平台，通过“AI沉淀”模式解决市场痛点，实现从“人找货”到“货找人”的智能匹配。',
    logo: 'https://images.unsplash.com/photo-1545239351-1141bd82e8a6?w=120&h=120&fit=crop',
    tags: ['品牌增长', 'AI营销', '内容合作']
  },
  {
    id: 3,
    name: '球秀',
    type: '社区 · 运动科技',
    description: 'AI驱动的运动社区视频平台，连接教练、运动达人与品牌，为运动生态提供内容解决方案。',
    logo: 'https://images.unsplash.com/photo-1545239351-1141bd82e8a6?w=120&h=120&fit=crop',
    tags: ['体育品牌', '赛事合作', '内容共创']
  },
  {
    id: 4,
    name: 'Koogle',
    type: '应用 · 工具',
    description: '像使用 Google 一样快速准确地检索海外头条，帮助跨境营销团队提升海外研究效率。',
    logo: 'https://images.unsplash.com/photo-1580894732444-8ecded7900cd?w=120&h=120&fit=crop',
    tags: ['跨境营销', '数据服务', '工具分发']
  }
]
</script>

<style scoped>
.project-page {
  flex: 1;
  padding: 40px 48px;
  background-color: #ffffff;
  overflow-y: auto;
  height: 100vh;
}

.page-header {
  margin-bottom: 32px;
}

.page-title {
  font-size: 42px;
  font-weight: 700;
  color: #1f2937;
  margin-bottom: 8px;
}

.page-subtitle {
  font-size: 28px;
  font-weight: 600;
  color: #111827;
  margin-bottom: 8px;
}

.page-desc {
  font-size: 16px;
  color: #6b7280;
  margin-bottom: 24px;
}

.header-actions {
  display: flex;
  gap: 12px;
}

.primary-btn {
  padding: 12px 28px;
  border-radius: 999px;
  background-color: #111827;
  color: #ffffff;
  border: none;
  font-size: 16px;
  cursor: pointer;
  transition: transform 0.2s, box-shadow 0.2s;
}

.primary-btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 12px 24px rgba(17, 24, 39, 0.12);
}

.filters {
  margin-bottom: 32px;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.category-tabs {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}

.category-tab {
  padding: 10px 18px;
  border-radius: 999px;
  border: 1px solid #e7eaf1;
  background-color: #ffffff;
  font-size: 14px;
  color: #515a6b;
  cursor: pointer;
  transition: all 0.2s;
}

.category-tab:hover {
  color: #111827;
  border-color: #cbd5e0;
}

.category-tab.active {
  background-color: #111827;
  color: #ffffff;
  border-color: #111827;
}

.sub-filters {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 12px;
}

.filter-label {
  font-size: 12px;
  letter-spacing: 0.4px;
  color: #a0a7b4;
  text-transform: uppercase;
}

.filter-buttons {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.filter-btn {
  padding: 6px 14px;
  border-radius: 999px;
  border: 1px solid #edf0f5;
  background-color: #f8f9fb;
  font-size: 13px;
  color: #5b6170;
  cursor: pointer;
  transition: all 0.2s;
}

.filter-btn:hover {
  border-color: #d7dce6;
  color: #111827;
}

.filter-btn.active {
  background-color: #111827;
  color: #ffffff;
  border-color: #111827;
}

.search-row {
  display: flex;
  justify-content: flex-start;
}

.search-box {
  position: relative;
  width: 100%;
  max-width: 420px;
}

.search-icon {
  position: absolute;
  left: 14px;
  top: 50%;
  transform: translateY(-50%);
  width: 18px;
  height: 18px;
  color: #9ca3af;
}

.search-input {
  width: 100%;
  padding: 10px 14px 10px 42px;
  border: 1px solid #e5e7eb;
  border-radius: 999px;
  background-color: #ffffff;
  font-size: 14px;
  transition: border-color 0.2s;
}

.search-input:focus {
  outline: none;
  border-color: #111827;
}

.project-list {
  display: flex;
  flex-direction: column;
  gap: 24px;
  padding-bottom: 48px;
}

.project-card {
  display: grid;
  grid-template-columns: 120px 1fr auto;
  gap: 24px;
  padding: 24px;
  border-radius: 24px;
  border: 1px solid #e5e7eb;
  background-color: #ffffff;
  box-shadow: 0 18px 32px rgba(15, 23, 42, 0.05);
  align-items: center;
  transition: transform 0.2s, box-shadow 0.2s;
}

.project-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 24px 40px rgba(15, 23, 42, 0.08);
}

.card-logo {
  width: 120px;
  height: 120px;
  border-radius: 24px;
  background-color: #f9fafb;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.card-logo img {
  width: 80%;
  height: 80%;
  object-fit: contain;
}

.card-body {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.card-header {
  display: flex;
  align-items: center;
  gap: 12px;
}

.project-name {
  font-size: 20px;
  font-weight: 600;
  color: #111827;
}

.project-type {
  padding: 4px 10px;
  border-radius: 999px;
  background-color: #eef2ff;
  color: #4338ca;
  font-size: 12px;
  font-weight: 500;
}

.project-desc {
  font-size: 14px;
  color: #4b5563;
  line-height: 1.7;
  margin: 0;
}

.project-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.tag {
  padding: 6px 12px;
  border-radius: 999px;
  background-color: #f3f4f6;
  color: #4b5563;
  font-size: 12px;
}

.card-actions {
  display: flex;
  align-items: center;
}

.outline-btn {
  padding: 10px 18px;
  border-radius: 999px;
  border: 1px solid #d1d5db;
  background-color: #ffffff;
  color: #111827;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.2s;
}

.outline-btn:hover {
  border-color: #111827;
}

@media (max-width: 1280px) {
  .project-card {
    grid-template-columns: 90px 1fr;
    grid-template-areas:
      'logo header'
      'logo body'
      'logo actions';
  }

  .card-logo {
    grid-area: logo;
    width: 90px;
    height: 90px;
  }

  .card-body {
    grid-area: body;
  }

  .card-actions {
    grid-area: actions;
    justify-content: flex-start;
  }
}

@media (max-width: 900px) {
  .project-page {
    padding: 32px 24px;
  }

  .sub-filters {
    flex-direction: column;
    align-items: stretch;
  }

  .search-box {
    width: 100%;
  }
}
</style>


```

- 调整“需求分类”部分的结构：标签行保持一行展示，字体改为淡灰小字号（12px，全部大写），标签 pill 采用浅灰背景与细边框，更贴近参考图。
- 搜索框单独占据下一行，宽度自适应（最大 420px），避免与标签同行导致额外行。
- 分类标签及筛选按钮的边框、背景和字号同步优化，整体对齐参考页面的轻量灰度风格。

---

**User**

将我用红色框圈起来的地方删除

---

**Cursor**

```vue
<template>
  <main class="project-page">
    <section class="page-header">
      <h1 class="page-title">Starter Solutions</h1>
      <p class="page-subtitle">资源库 · 需求发布广场</p>
      <p class="page-desc">也许这里的一个项目，就是你事业的新起点</p>

      <div class="header-actions">
        <button class="primary-btn">发布我的项目</button>
      </div>
    </section>

    <section class="filters">
      <div class="sub-filters">
        <span class="filter-label">需求分类</span>
        <div class="filter-buttons">
          <button
            v-for="tag in demandTags"
            :key="tag"
            :class="['filter-btn', { active: activeDemand === tag }]"
            @click="activeDemand = tag"
          >
            {{ tag }}
          </button>
        </div>
      </div>

      <div class="search-row">
        <div class="search-box">
          <svg class="search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="11" cy="11" r="8" />
            <path d="m21 21-4.35-4.35" />
          </svg>
          <input type="text" class="search-input" placeholder="搜索合作方向、关键词或企业名称" />
        </div>
      </div>
    </section>

    <section class="project-list">
      <article v-for="project in projects" :key="project.id" class="project-card">
        <div class="card-logo">
          <img :src="project.logo" :alt="project.name" />
        </div>
        <div class="card-body">
          <header class="card-header">
            <h2 class="project-name">{{ project.name }}</h2>
            <span class="project-type">{{ project.type }}</span>
          </header>
          <p class="project-desc">{{ project.description }}</p>
          <div class="project-tags">
            <span v-for="tag in project.tags" :key="tag" class="tag">
              {{ tag }}
            </span>
          </div>
        </div>
        <div class="card-actions">
          <button class="outline-btn">查看详情</button>
        </div>
      </article>
    </section>
  </main>
</template>

<script setup>
import { ref } from 'vue'

const demandTags = ['不限', '消费', '企业服务', '文娱', '教育', 'AI', '品牌', '渠道', '资本', '产业链']

const activeDemand = ref(demandTags[0])

const projects = [
  {
    id: 1,
    name: 'Mindee',
    type: 'SaaS · 客户运营',
    description: '首创“24小时贴身情绪AI伙伴”，陪伴一监测一干预一成长全流程守护。需要算力、服务商、线下运营咨询、医院、资质等方向的合作。',
    logo: 'https://images.unsplash.com/photo-1633332755192-727a05c4013d?w=120&h=120&fit=crop',
    tags: ['情绪AI陪护', '智能硬件', '服务商合作']
  },
  {
    id: 2,
    name: '掌乐',
    type: '新媒体 · AI营销',
    description: '掌乐是一个AI驱动的短视频创作分发平台，通过“AI沉淀”模式解决市场痛点，实现从“人找货”到“货找人”的智能匹配。',
    logo: 'https://images.unsplash.com/photo-1545239351-1141bd82e8a6?w=120&h=120&fit=crop',
    tags: ['品牌增长', 'AI营销', '内容合作']
  },
  {
    id: 3,
    name: '球秀',
    type: '社区 · 运动科技',
    description: 'AI驱动的运动社区视频平台，连接教练、运动达人与品牌，为运动生态提供内容解决方案。',
    logo: 'https://images.unsplash.com/photo-1545239351-1141bd82e8a6?w=120&h=120&fit=crop',
    tags: ['体育品牌', '赛事合作', '内容共创']
  },
  {
    id: 4,
    name: 'Koogle',
    type: '应用 · 工具',
    description: '像使用 Google 一样快速准确地检索海外头条，帮助跨境营销团队提升海外研究效率。',
    logo: 'https://images.unsplash.com/photo-1580894732444-8ecded7900cd?w=120&h=120&fit=crop',
    tags: ['跨境营销', '数据服务', '工具分发']
  }
]
</script>

<style scoped>
.project-page {
  flex: 1;
  padding: 40px 48px;
  background-color: #ffffff;
  overflow-y: auto;
  height: 100vh;
}

.page-header {
  margin-bottom: 32px;
}

.page-title {
  font-size: 42px;
  font-weight: 700;
  color: #1f2937;
  margin-bottom: 8px;
}

.page-subtitle {
  font-size: 28px;
  font-weight: 600;
  color: #111827;
  margin-bottom: 8px;
}

.page-desc {
  font-size: 16px;
  color: #6b7280;
  margin-bottom: 24px;
}

.header-actions {
  display: flex;
  gap: 12px;
}

.primary-btn {
  padding: 12px 28px;
  border-radius: 999px;
  background-color: #111827;
  color: #ffffff;
  border: none;
  font-size: 16px;
  cursor: pointer;
  transition: transform 0.2s, box-shadow 0.2s;
}

.primary-btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 12px 24px rgba(17, 24, 39, 0.12);
}

.filters {
  margin-bottom: 32px;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.category-tabs {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}

.category-tab {
  padding: 10px 18px;
  border-radius: 999px;
  border: 1px solid #e7eaf1;
  background-color: #ffffff;
  font-size: 14px;
  color: #515a6b;
  cursor: pointer;
  transition: all 0.2s;
}

.category-tab:hover {
  color: #111827;
  border-color: #cbd5e0;
}

.category-tab.active {
  background-color: #111827;
  color: #ffffff;
  border-color: #111827;
}

.sub-filters {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 12px;
}

.filter-label {
  font-size: 12px;
  letter-spacing: 0.4px;
  color: #a0a7b4;
  text-transform: uppercase;
}

.filter-buttons {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.filter-btn {
  padding: 6px 14px;
  border-radius: 999px;
  border: 1px solid #edf0f5;
  background-color: #f8f9fb;
  font-size: 13px;
  color: #5b6170;
  cursor: pointer;
  transition: all 0.2s;
}

.filter-btn:hover {
  border-color: #d7dce6;
  color: #111827;
}

.filter-btn.active {
  background-color: #111827;
  color: #ffffff;
  border-color: #111827;
}

.search-row {
  display: flex;
  justify-content: flex-start;
}

.search-box {
  position: relative;
  width: 100%;
  max-width: 420px;
}

.search-icon {
  position: absolute;
  left: 14px;
  top: 50%;
  transform: translateY(-50%);
  width: 18px;
  height: 18px;
  color: #9ca3af;
}

.search-input {
  width: 100%;
  padding: 10px 14px 10px 42px;
  border: 1px solid #e5e7eb;
  border-radius: 999px;
  background-color: #ffffff;
  font-size: 14px;
  transition: border-color 0.2s;
}

.search-input:focus {
  outline: none;
  border-color: #111827;
}

.project-list {
  display: flex;
  flex-direction: column;
  gap: 24px;
  padding-bottom: 48px;
}

.project-card {
  display: grid;
  grid-template-columns: 120px 1fr auto;
  gap: 24px;
  padding: 24px;
  border-radius: 24px;
  border: 1px solid #e5e7eb;
  background-color: #ffffff;
  box-shadow: 0 18px 32px rgba(15, 23, 42, 0.05);
  align-items: center;
  transition: transform 0.2s, box-shadow 0.2s;
}

.project-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 24px 40px rgba(15, 23, 42, 0.08);
}

.card-logo {
  width: 120px;
  height: 120px;
  border-radius: 24px;
  background-color: #f9fafb;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.card-logo img {
  width: 80%;
  height: 80%;
  object-fit: contain;
}

.card-body {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.card-header {
  display: flex;
  align-items: center;
  gap: 12px;
}

.project-name {
  font-size: 20px;
  font-weight: 600;
  color: #111827;
}

.project-type {
  padding: 4px 10px;
  border-radius: 999px;
  background-color: #eef2ff;
  color: #4338ca;
  font-size: 12px;
  font-weight: 500;
}

.project-desc {
  font-size: 14px;
  color: #4b5563;
  line-height: 1.7;
  margin: 0;
}

.project-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.tag {
  padding: 6px 12px;
  border-radius: 999px;
  background-color: #f3f4f6;
  color: #4b5563;
  font-size: 12px;
}

.card-actions {
  display: flex;
  align-items: center;
}

.outline-btn {
  padding: 10px 18px;
  border-radius: 999px;
  border: 1px solid #d1d5db;
  background-color: #ffffff;
  color: #111827;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.2s;
}

.outline-btn:hover {
  border-color: #111827;
}

@media (max-width: 1280px) {
  .project-card {
    grid-template-columns: 90px 1fr;
    grid-template-areas:
      'logo header'
      'logo body'
      'logo actions';
  }

  .card-logo {
    grid-area: logo;
    width: 90px;
    height: 90px;
  }

  .card-body {
    grid-area: body;
  }

  .card-actions {
    grid-area: actions;
    justify-content: flex-start;
  }
}

@media (max-width: 900px) {
  .project-page {
    padding: 32px 24px;
  }

  .sub-filters {
    flex-direction: column;
    align-items: stretch;
  }

  .search-box {
    width: 100%;
  }
}
</style>


```

```vue
<template>
  <main class="project-page">
    <section class="page-header">
      <h1 class="page-title">Starter Solutions</h1>
      <p class="page-subtitle">资源库 · 需求发布广场</p>
      <p class="page-desc">也许这里的一个项目，就是你事业的新起点</p>

      <div class="header-actions">
        <button class="primary-btn">发布我的项目</button>
      </div>
    </section>

    <section class="filters">
      <div class="sub-filters">
        <span class="filter-label">需求分类</span>
        <div class="filter-buttons">
          <button
            v-for="tag in demandTags"
            :key="tag"
            :class="['filter-btn', { active: activeDemand === tag }]"
            @click="activeDemand = tag"
          >
            {{ tag }}
          </button>
        </div>
      </div>

      <div class="search-row">
        <div class="search-box">
          <svg class="search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="11" cy="11" r="8" />
            <path d="m21 21-4.35-4.35" />
          </svg>
          <input type="text" class="search-input" placeholder="搜索合作方向、关键词或企业名称" />
        </div>
      </div>
    </section>

    <section class="project-list">
      <article v-for="project in projects" :key="project.id" class="project-card">
        <div class="card-logo">
          <img :src="project.logo" :alt="project.name" />
        </div>
        <div class="card-body">
          <header class="card-header">
            <h2 class="project-name">{{ project.name }}</h2>
            <span class="project-type">{{ project.type }}</span>
          </header>
          <p class="project-desc">{{ project.description }}</p>
          <div class="project-tags">
            <span v-for="tag in project.tags" :key="tag" class="tag">
              {{ tag }}
            </span>
          </div>
        </div>
        <div class="card-actions">
          <button class="outline-btn">查看详情</button>
        </div>
      </article>
    </section>
  </main>
</template>

<script setup>
import { ref } from 'vue'

const demandTags = ['不限', '消费', '企业服务', '文娱', '教育', 'AI', '品牌', '渠道', '资本', '产业链']

const activeDemand = ref(demandTags[0])

const projects = [
  {
    id: 1,
    name: 'Mindee',
    type: 'SaaS · 客户运营',
    description: '首创“24小时贴身情绪AI伙伴”，陪伴一监测一干预一成长全流程守护。需要算力、服务商、线下运营咨询、医院、资质等方向的合作。',
    logo: 'https://images.unsplash.com/photo-1633332755192-727a05c4013d?w=120&h=120&fit=crop',
    tags: ['情绪AI陪护', '智能硬件', '服务商合作']
  },
  {
    id: 2,
    name: '掌乐',
    type: '新媒体 · AI营销',
    description: '掌乐是一个AI驱动的短视频创作分发平台，通过“AI沉淀”模式解决市场痛点，实现从“人找货”到“货找人”的智能匹配。',
    logo: 'https://images.unsplash.com/photo-1545239351-1141bd82e8a6?w=120&h=120&fit=crop',
    tags: ['品牌增长', 'AI营销', '内容合作']
  },
  {
    id: 3,
    name: '球秀',
    type: '社区 · 运动科技',
    description: 'AI驱动的运动社区视频平台，连接教练、运动达人与品牌，为运动生态提供内容解决方案。',
    logo: 'https://images.unsplash.com/photo-1545239351-1141bd82e8a6?w=120&h=120&fit=crop',
    tags: ['体育品牌', '赛事合作', '内容共创']
  },
  {
    id: 4,
    name: 'Koogle',
    type: '应用 · 工具',
    description: '像使用 Google 一样快速准确地检索海外头条，帮助跨境营销团队提升海外研究效率。',
    logo: 'https://images.unsplash.com/photo-1580894732444-8ecded7900cd?w=120&h=120&fit=crop',
    tags: ['跨境营销', '数据服务', '工具分发']
  }
]
</script>

<style scoped>
.project-page {
  flex: 1;
  padding: 40px 48px;
  background-color: #ffffff;
  overflow-y: auto;
  height: 100vh;
}

.page-header {
  margin-bottom: 32px;
}

.page-title {
  font-size: 42px;
  font-weight: 700;
  color: #1f2937;
  margin-bottom: 8px;
}

.page-subtitle {
  font-size: 28px;
  font-weight: 600;
  color: #111827;
  margin-bottom: 8px;
}

.page-desc {
  font-size: 16px;
  color: #6b7280;
  margin-bottom: 24px;
}

.header-actions {
  display: flex;
  gap: 12px;
}

.primary-btn {
  padding: 12px 28px;
  border-radius: 999px;
  background-color: #111827;
  color: #ffffff;
  border: none;
  font-size: 16px;
  cursor: pointer;
  transition: transform 0.2s, box-shadow 0.2s;
}

.primary-btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 12px 24px rgba(17, 24, 39, 0.12);
}

.filters {
  margin-bottom: 32px;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.category-tabs {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}

.category-tab {
  padding: 10px 18px;
  border-radius: 999px;
  border: 1px solid #e7eaf1;
  background-color: #ffffff;
  font-size: 14px;
  color: #515a6b;
  cursor: pointer;
  transition: all 0.2s;
}

.category-tab:hover {
  color: #111827;
  border-color: #cbd5e0;
}

.category-tab.active {
  background-color: #111827;
  color: #ffffff;
  border-color: #111827;
}

.sub-filters {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 12px;
}

.filter-label {
  font-size: 12px;
  letter-spacing: 0.4px;
  color: #a0a7b4;
  text-transform: uppercase;
}

.filter-buttons {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.filter-btn {
  padding: 6px 14px;
  border-radius: 999px;
  border: 1px solid #edf0f5;
  background-color: #f8f9fb;
  font-size: 13px;
  color: #5b6170;
  cursor: pointer;
  transition: all 0.2s;
}

.filter-btn:hover {
  border-color: #d7dce6;
  color: #111827;
}

.filter-btn.active {
  background-color: #111827;
  color: #ffffff;
  border-color: #111827;
}

.search-row {
  display: flex;
  justify-content: flex-start;
}

.search-box {
  position: relative;
  width: 100%;
  max-width: 420px;
}

.search-icon {
  position: absolute;
  left: 14px;
  top: 50%;
  transform: translateY(-50%);
  width: 18px;
  height: 18px;
  color: #9ca3af;
}

.search-input {
  width: 100%;
  padding: 10px 14px 10px 42px;
  border: 1px solid #e5e7eb;
  border-radius: 999px;
  background-color: #ffffff;
  font-size: 14px;
  transition: border-color 0.2s;
}

.search-input:focus {
  outline: none;
  border-color: #111827;
}

.project-list {
  display: flex;
  flex-direction: column;
  gap: 24px;
  padding-bottom: 48px;
}

.project-card {
  display: grid;
  grid-template-columns: 120px 1fr auto;
  gap: 24px;
  padding: 24px;
  border-radius: 24px;
  border: 1px solid #e5e7eb;
  background-color: #ffffff;
  box-shadow: 0 18px 32px rgba(15, 23, 42, 0.05);
  align-items: center;
  transition: transform 0.2s, box-shadow 0.2s;
}

.project-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 24px 40px rgba(15, 23, 42, 0.08);
}

.card-logo {
  width: 120px;
  height: 120px;
  border-radius: 24px;
  background-color: #f9fafb;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.card-logo img {
  width: 80%;
  height: 80%;
  object-fit: contain;
}

.card-body {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.card-header {
  display: flex;
  align-items: center;
  gap: 12px;
}

.project-name {
  font-size: 20px;
  font-weight: 600;
  color: #111827;
}

.project-type {
  padding: 4px 10px;
  border-radius: 999px;
  background-color: #eef2ff;
  color: #4338ca;
  font-size: 12px;
  font-weight: 500;
}

.project-desc {
  font-size: 14px;
  color: #4b5563;
  line-height: 1.7;
  margin: 0;
}

.project-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.tag {
  padding: 6px 12px;
  border-radius: 999px;
  background-color: #f3f4f6;
  color: #4b5563;
  font-size: 12px;
}

.card-actions {
  display: flex;
  align-items: center;
}

.outline-btn {
  padding: 10px 18px;
  border-radius: 999px;
  border: 1px solid #d1d5db;
  background-color: #ffffff;
  color: #111827;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.2s;
}

.outline-btn:hover {
  border-color: #111827;
}

@media (max-width: 1280px) {
  .project-card {
    grid-template-columns: 90px 1fr;
    grid-template-areas:
      'logo header'
      'logo body'
      'logo actions';
  }

  .card-logo {
    grid-area: logo;
    width: 90px;
    height: 90px;
  }

  .card-body {
    grid-area: body;
  }

  .card-actions {
    grid-area: actions;
    justify-content: flex-start;
  }
}

@media (max-width: 900px) {
  .project-page {
    padding: 32px 24px;
  }

  .sub-filters {
    flex-direction: column;
    align-items: stretch;
  }

  .search-box {
    width: 100%;
  }
}
</style>


```

```vue
<template>
  <main class="project-page">
    <section class="page-header">
      <h1 class="page-title">Starter Solutions</h1>
      <p class="page-subtitle">资源库 · 需求发布广场</p>
      <p class="page-desc">也许这里的一个项目，就是你事业的新起点</p>

      <div class="header-actions">
        <button class="primary-btn">发布我的项目</button>
      </div>
    </section>

    <section class="filters">
      <div class="sub-filters">
        <span class="filter-label">需求分类</span>
        <div class="filter-buttons">
          <button
            v-for="tag in demandTags"
            :key="tag"
            :class="['filter-btn', { active: activeDemand === tag }]"
            @click="activeDemand = tag"
          >
            {{ tag }}
          </button>
        </div>
      </div>

      <div class="search-row">
        <div class="search-box">
          <svg class="search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="11" cy="11" r="8" />
            <path d="m21 21-4.35-4.35" />
          </svg>
          <input type="text" class="search-input" placeholder="搜索合作方向、关键词或企业名称" />
        </div>
      </div>
    </section>

    <section class="project-list">
      <article v-for="project in projects" :key="project.id" class="project-card">
        <div class="card-logo">
          <img :src="project.logo" :alt="project.name" />
        </div>
        <div class="card-body">
          <header class="card-header">
            <h2 class="project-name">{{ project.name }}</h2>
            <span class="project-type">{{ project.type }}</span>
          </header>
          <p class="project-desc">{{ project.description }}</p>
          <div class="project-tags">
            <span v-for="tag in project.tags" :key="tag" class="tag">
              {{ tag }}
            </span>
          </div>
        </div>
        <div class="card-actions">
          <button class="outline-btn">查看详情</button>
        </div>
      </article>
    </section>
  </main>
</template>

<script setup>
import { ref } from 'vue'

const demandTags = ['不限', '消费', '企业服务', '文娱', '教育', 'AI', '品牌', '渠道', '资本', '产业链']

const activeDemand = ref(demandTags[0])

const projects = [
  {
    id: 1,
    name: 'Mindee',
    type: 'SaaS · 客户运营',
    description: '首创“24小时贴身情绪AI伙伴”，陪伴一监测一干预一成长全流程守护。需要算力、服务商、线下运营咨询、医院、资质等方向的合作。',
    logo: 'https://images.unsplash.com/photo-1633332755192-727a05c4013d?w=120&h=120&fit=crop',
    tags: ['情绪AI陪护', '智能硬件', '服务商合作']
  },
  {
    id: 2,
    name: '掌乐',
    type: '新媒体 · AI营销',
    description: '掌乐是一个AI驱动的短视频创作分发平台，通过“AI沉淀”模式解决市场痛点，实现从“人找货”到“货找人”的智能匹配。',
    logo: 'https://images.unsplash.com/photo-1545239351-1141bd82e8a6?w=120&h=120&fit=crop',
    tags: ['品牌增长', 'AI营销', '内容合作']
  },
  {
    id: 3,
    name: '球秀',
    type: '社区 · 运动科技',
    description: 'AI驱动的运动社区视频平台，连接教练、运动达人与品牌，为运动生态提供内容解决方案。',
    logo: 'https://images.unsplash.com/photo-1545239351-1141bd82e8a6?w=120&h=120&fit=crop',
    tags: ['体育品牌', '赛事合作', '内容共创']
  },
  {
    id: 4,
    name: 'Koogle',
    type: '应用 · 工具',
    description: '像使用 Google 一样快速准确地检索海外头条，帮助跨境营销团队提升海外研究效率。',
    logo: 'https://images.unsplash.com/photo-1580894732444-8ecded7900cd?w=120&h=120&fit=crop',
    tags: ['跨境营销', '数据服务', '工具分发']
  }
]
</script>

<style scoped>
.project-page {
  flex: 1;
  padding: 40px 48px;
  background-color: #ffffff;
  overflow-y: auto;
  height: 100vh;
}

.page-header {
  margin-bottom: 32px;
}

.page-title {
  font-size: 42px;
  font-weight: 700;
  color: #1f2937;
  margin-bottom: 8px;
}

.page-subtitle {
  font-size: 28px;
  font-weight: 600;
  color: #111827;
  margin-bottom: 8px;
}

.page-desc {
  font-size: 16px;
  color: #6b7280;
  margin-bottom: 24px;
}

.header-actions {
  display: flex;
  gap: 12px;
}

.primary-btn {
  padding: 12px 28px;
  border-radius: 999px;
  background-color: #111827;
  color: #ffffff;
  border: none;
  font-size: 16px;
  cursor: pointer;
  transition: transform 0.2s, box-shadow 0.2s;
}

.primary-btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 12px 24px rgba(17, 24, 39, 0.12);
}

.filters {
  margin-bottom: 32px;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.sub-filters {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 12px;
}

.filter-label {
  font-size: 12px;
  letter-spacing: 0.4px;
  color: #a0a7b4;
  text-transform: uppercase;
}

.filter-buttons {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.filter-btn {
  padding: 6px 14px;
  border-radius: 999px;
  border: 1px solid #edf0f5;
  background-color: #f8f9fb;
  font-size: 13px;
  color: #5b6170;
  cursor: pointer;
  transition: all 0.2s;
}

.filter-btn:hover {
  border-color: #d7dce6;
  color: #111827;
}

.filter-btn.active {
  background-color: #111827;
  color: #ffffff;
  border-color: #111827;
}

.search-row {
  display: flex;
  justify-content: flex-start;
}

.search-box {
  position: relative;
  width: 100%;
  max-width: 420px;
}

.search-icon {
  position: absolute;
  left: 14px;
  top: 50%;
  transform: translateY(-50%);
  width: 18px;
  height: 18px;
  color: #9ca3af;
}

.search-input {
  width: 100%;
  padding: 10px 14px 10px 42px;
  border: 1px solid #e5e7eb;
  border-radius: 999px;
  background-color: #ffffff;
  font-size: 14px;
  transition: border-color 0.2s;
}

.search-input:focus {
  outline: none;
  border-color: #111827;
}

.project-list {
  display: flex;
  flex-direction: column;
  gap: 24px;
  padding-bottom: 48px;
}

.project-card {
  display: grid;
  grid-template-columns: 120px 1fr auto;
  gap: 24px;
  padding: 24px;
  border-radius: 24px;
  border: 1px solid #e5e7eb;
  background-color: #ffffff;
  box-shadow: 0 18px 32px rgba(15, 23, 42, 0.05);
  align-items: center;
  transition: transform 0.2s, box-shadow 0.2s;
}

.project-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 24px 40px rgba(15, 23, 42, 0.08);
}

.card-logo {
  width: 120px;
  height: 120px;
  border-radius: 24px;
  background-color: #f9fafb;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.card-logo img {
  width: 80%;
  height: 80%;
  object-fit: contain;
}

.card-body {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.card-header {
  display: flex;
  align-items: center;
  gap: 12px;
}

.project-name {
  font-size: 20px;
  font-weight: 600;
  color: #111827;
}

.project-type {
  padding: 4px 10px;
  border-radius: 999px;
  background-color: #eef2ff;
  color: #4338ca;
  font-size: 12px;
  font-weight: 500;
}

.project-desc {
  font-size: 14px;
  color: #4b5563;
  line-height: 1.7;
  margin: 0;
}

.project-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.tag {
  padding: 6px 12px;
  border-radius: 999px;
  background-color: #f3f4f6;
  color: #4b5563;
  font-size: 12px;
}

.card-actions {
  display: flex;
  align-items: center;
}

.outline-btn {
  padding: 10px 18px;
  border-radius: 999px;
  border: 1px solid #d1d5db;
  background-color: #ffffff;
  color: #111827;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.2s;
}

.outline-btn:hover {
  border-color: #111827;
}

@media (max-width: 1280px) {
  .project-card {
    grid-template-columns: 90px 1fr;
    grid-template-areas:
      'logo header'
      'logo body'
      'logo actions';
  }

  .card-logo {
    grid-area: logo;
    width: 90px;
    height: 90px;
  }

  .card-body {
    grid-area: body;
  }

  .card-actions {
    grid-area: actions;
    justify-content: flex-start;
  }
}

@media (max-width: 900px) {
  .project-page {
    padding: 32px 24px;
  }

  .sub-filters {
    flex-direction: column;
    align-items: stretch;
  }

  .search-box {
    width: 100%;
  }
}
</style>


```

已移除参考截图中标出的顶部分类标签区域，仅保留“需求分类”标签和搜索框两行，样式保持其余部分不变。

---

**User**

按照这个风格生成一个活动界面 点击链接可以跳转过去 我提供参考界面 同样的探索前沿，碰撞机会下方的图片是可以自动切换的

---

**Cursor**

```javascript
import { createRouter, createWebHistory } from 'vue-router'

import HomePage from '../components/MainContent.vue'
import TalentPage from '../pages/TalentPage.vue'
import LinkPage from '../pages/LinkPage.vue'
import ProjectPage from '../pages/ProjectPage.vue'
import EventsPage from '../pages/EventsPage.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomePage
  },
  {
    path: '/talents',
    name: 'talents',
    component: TalentPage
  },
  {
    path: '/links',
    name: 'links',
    component: LinkPage
  },
  {
    path: '/projects',
    name: 'projects',
    component: ProjectPage
  },
  {
    path: '/events',
    name: 'events',
    component: EventsPage
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router


```

```vue
<template>
  <aside class="sidebar">
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
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
          <circle cx="12" cy="7" r="4"></circle>
        </svg>
        <span>我的</span>
      </a>
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
</template>

<script setup>
import { useRoute } from 'vue-router'

const route = useRoute()
</script>

<style scoped>
.sidebar {
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
</style>


```

```vue
<template>
  <main class="events-page">
    <section class="hero">
      <h1 class="title">Starter Community</h1>
      <p class="subtitle">探索前沿，碰撞机会</p>

      <div class="hero-slider">
        <transition-group name="fade" tag="div">
          <div
            v-for="(slide, index) in slides"
            :key="slide.id"
            v-show="currentSlide === index"
            class="hero-slide"
          >
            <img :src="slide.image" :alt="'slide-' + slide.id" />
          </div>
        </transition-group>

        <div class="slider-dots">
          <button
            v-for="(slide, index) in slides"
            :key="slide.id"
            :class="['dot', { active: currentSlide === index }]"
            @click="setSlide(index)"
          />
        </div>

        <div class="hero-actions">
          <button class="pill-btn">往期主题</button>
          <button class="pill-btn outline">往期嘉宾</button>
        </div>
      </div>
    </section>

    <section class="upcoming">
      <div class="section-header">
        <h2>查看近期活动</h2>
        <div class="filters">
          <button v-for="tab in tabs" :key="tab" :class="['tab', { active: activeTab === tab }]" @click="activeTab = tab">
            {{ tab }}
          </button>
        </div>
      </div>

      <div class="card-grid">
        <article v-for="event in events" :key="event.id" class="event-card">
          <div class="cover">
            <img :src="event.cover" :alt="event.title" />
          </div>
          <div class="card-content">
            <h3 class="event-title">{{ event.title }}</h3>
            <p class="event-desc">{{ event.description }}</p>
            <div class="meta">
              <span class="meta-text">开放报名</span>
              <span class="meta-text">{{ event.date }}</span>
              <span class="meta-text">{{ event.location }}</span>
            </div>
            <div class="tags">
              <span class="tag">会员活动</span>
              <span class="tag primary">火热报名中</span>
            </div>
          </div>
        </article>
      </div>
    </section>
  </main>
  </template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'

const tabs = ['不限', '即将开始', '往期活动']
const activeTab = ref(tabs[0])

const slides = [
  { id: 1, image: 'https://images.unsplash.com/photo-1492684223066-81342ee5ff30?w=1600&h=900&fit=crop' },
  { id: 2, image: 'https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=1600&h=900&fit=crop' },
  { id: 3, image: 'https://images.unsplash.com/photo-1551836022-d5d88e9218df?w=1600&h=900&fit=crop' }
]

const currentSlide = ref(0)
let timer = null

const start = () => {
  stop()
  timer = setInterval(() => {
    currentSlide.value = (currentSlide.value + 1) % slides.length
  }, 5000)
}

const stop = () => {
  if (timer) {
    clearInterval(timer)
    timer = null
  }
}

const setSlide = (i) => {
  currentSlide.value = i
  start()
}

onMounted(() => start())
onBeforeUnmount(() => stop())

const events = ref([
  {
    id: 1,
    title: '消费品牌出海空中路演 Demo Day | 线上开放麦',
    description: '亮相你的出海消费品牌，找用户、找合作、找投资。',
    date: '2025/11/28 · 19:30',
    location: '线上',
    cover: 'https://images.unsplash.com/photo-1540575467063-178a50c2df87?w=900&h=600&fit=crop'
  },
  {
    id: 2,
    title: '创始人 IP，能变现的短视频 | 空中茶话会',
    description: '系统拆解从人设打造到短视频变现流程 SOP。',
    date: '2025/11/27 · 20:00',
    location: '线上',
    cover: 'https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?w=900&h=600&fit=crop'
  },
  {
    id: 3,
    title: '一人公司 CEO 聚会（长沙版）',
    description: '你的“一人公司”怎么样了？',
    date: '2025/11/22 · 14:00',
    location: '长沙',
    cover: 'https://images.unsplash.com/photo-1503428593586-e225b39bddfe?w=900&h=600&fit=crop'
  },
  {
    id: 4,
    title: 'AI 产品冷启动：找到你的第一个真爱用户',
    description: '北上创业研讨会 · 深入交流产品冷启动方法。',
    date: '2025/11/18 · 19:00',
    location: '北京',
    cover: 'https://images.unsplash.com/photo-1542744173-8e7e53415bb0?w=900&h=600&fit=crop'
  }
])
</script>

<style scoped>
.events-page {
  flex: 1;
  padding: 32px 40px;
  background-color: #ffffff;
  overflow-y: auto;
  height: 100vh;
}

.hero {
  margin-bottom: 28px;
}

.title {
  font-size: 40px;
  font-weight: 800;
  color: #111827;
  margin: 0 0 6px;
}

.subtitle {
  font-size: 22px;
  color: #1f2937;
  font-weight: 700;
  margin: 0 0 16px;
}

.hero-slider {
  position: relative;
  border-radius: 16px;
  overflow: hidden;
  border: 1px solid #e5e7eb;
}

.hero-slide {
  position: absolute;
  inset: 0;
}

.hero-slide img {
  width: 100%;
  height: 520px;
  object-fit: cover;
  display: block;
}

.slider-dots {
  position: absolute;
  left: 50%;
  bottom: 14px;
  transform: translateX(-50%);
  display: flex;
  gap: 8px;
}

.dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  border: none;
  background-color: rgba(255, 255, 255, 0.4);
  cursor: pointer;
}

.dot.active {
  background-color: #ffffff;
}

.hero-actions {
  position: absolute;
  right: 16px;
  bottom: 16px;
  display: flex;
  gap: 10px;
}

.pill-btn {
  padding: 10px 16px;
  border-radius: 999px;
  background-color: #111827;
  color: #ffffff;
  border: 1px solid #111827;
  font-size: 14px;
  cursor: pointer;
}

.pill-btn.outline {
  background-color: #ffffff;
  color: #111827;
  border-color: #d1d5db;
}

.upcoming .section-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin: 18px 0;
}

.upcoming h2 {
  font-size: 20px;
  color: #111827;
  font-weight: 700;
  margin: 0;
}

.filters {
  display: flex;
  gap: 8px;
}

.tab {
  padding: 8px 14px;
  background-color: #f4f6f8;
  border: 1px solid #e5e7eb;
  color: #4b5563;
  font-size: 13px;
  border-radius: 999px;
  cursor: pointer;
}

.tab.active {
  background-color: #111827;
  color: #ffffff;
  border-color: #111827;
}

.card-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  padding-bottom: 36px;
}

.event-card {
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  overflow: hidden;
  background-color: #ffffff;
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.04);
  display: flex;
  flex-direction: column;
}

.cover {
  width: 100%;
  height: 170px;
  background-color: #f3f4f6;
}

.cover img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.card-content {
  padding: 14px 16px 16px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.event-title {
  font-size: 16px;
  color: #111827;
  font-weight: 600;
  margin: 0;
}

.event-desc {
  font-size: 13px;
  color: #4b5563;
  line-height: 1.6;
  margin: 0;
}

.meta {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}

.meta-text {
  font-size: 12px;
  color: #6b7280;
}

.tags {
  display: flex;
  gap: 8px;
}

.tag {
  padding: 4px 10px;
  border-radius: 999px;
  background-color: #f3f4f6;
  color: #6b7280;
  font-size: 12px;
}

.tag.primary {
  background-color: #111827;
  color: #ffffff;
}

@media (max-width: 1280px) {
  .card-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 900px) {
  .events-page {
    padding: 24px;
  }

  .card-grid {
    grid-template-columns: 1fr;
  }
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.6s;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>

```

- 已新增活动页 `EventsPage`（/events）：包含“Starter Community · 探索前沿，碰撞机会”大图轮播，自动切换并支持指示点点击切换；右下角提供“往期主题/往期嘉宾”按钮。
- “查看近期活动”模块：提供筛选标签（不限/即将开始/往期活动）与三列卡片网格，卡片含封面、标题、简介、时间地点与状态标签。
- 侧边栏“活动”入口已改为可点击路由，支持激活态高亮。
- 已在路由中注册 `/events`。运行后点击左侧“活动”即可进入，轮播会自动播放。

---

**User**

这是目前的前端页面 相比较于参考页面缺少一个大图片显示滚动

---

**Cursor**

```vue
<template>
  <main class="events-page">
    <section class="hero">
      <h1 class="title">Starter Community</h1>
      <p class="subtitle">探索前沿，碰撞机会</p>

      <div class="hero-slider">
        <transition-group name="fade" tag="div">
          <div
            v-for="(slide, index) in slides"
            :key="slide.id"
            v-show="currentSlide === index"
            class="hero-slide"
          >
            <img :src="slide.image" :alt="'slide-' + slide.id" />
          </div>
        </transition-group>

        <div class="slider-dots">
          <button
            v-for="(slide, index) in slides"
            :key="slide.id"
            :class="['dot', { active: currentSlide === index }]"
            @click="setSlide(index)"
          />
        </div>

        <div class="hero-actions">
          <button class="pill-btn">往期主题</button>
          <button class="pill-btn outline">往期嘉宾</button>
        </div>
      </div>

      <div class="hero-below">
        <div class="hero-stats">
          <div class="stat-line">累计邀请200+分享嘉宾</div>
          <div class="stat-line sub">汇聚6000+创始人</div>
        </div>
      </div>
    </section>

    <section class="upcoming">
      <div class="section-header">
        <h2>查看近期活动</h2>
        <div class="filters">
          <button v-for="tab in tabs" :key="tab" :class="['tab', { active: activeTab === tab }]" @click="activeTab = tab">
            {{ tab }}
          </button>
        </div>
      </div>

      <div class="card-grid">
        <article v-for="event in events" :key="event.id" class="event-card">
          <div class="cover">
            <img :src="event.cover" :alt="event.title" />
          </div>
          <div class="card-content">
            <h3 class="event-title">{{ event.title }}</h3>
            <p class="event-desc">{{ event.description }}</p>
            <div class="meta">
              <span class="meta-text">开放报名</span>
              <span class="meta-text">{{ event.date }}</span>
              <span class="meta-text">{{ event.location }}</span>
            </div>
            <div class="tags">
              <span class="tag">会员活动</span>
              <span class="tag primary">火热报名中</span>
            </div>
          </div>
        </article>
      </div>
    </section>
  </main>
  </template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'

const tabs = ['不限', '即将开始', '往期活动']
const activeTab = ref(tabs[0])

const slides = [
  { id: 1, image: 'https://images.unsplash.com/photo-1492684223066-81342ee5ff30?w=1600&h=900&fit=crop' },
  { id: 2, image: 'https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=1600&h=900&fit=crop' },
  { id: 3, image: 'https://images.unsplash.com/photo-1551836022-d5d88e9218df?w=1600&h=900&fit=crop' }
]

const currentSlide = ref(0)
let timer = null

const start = () => {
  stop()
  timer = setInterval(() => {
    currentSlide.value = (currentSlide.value + 1) % slides.length
  }, 5000)
}

const stop = () => {
  if (timer) {
    clearInterval(timer)
    timer = null
  }
}

const setSlide = (i) => {
  currentSlide.value = i
  start()
}

onMounted(() => start())
onBeforeUnmount(() => stop())

const events = ref([
  {
    id: 1,
    title: '消费品牌出海空中路演 Demo Day | 线上开放麦',
    description: '亮相你的出海消费品牌，找用户、找合作、找投资。',
    date: '2025/11/28 · 19:30',
    location: '线上',
    cover: 'https://images.unsplash.com/photo-1540575467063-178a50c2df87?w=900&h=600&fit=crop'
  },
  {
    id: 2,
    title: '创始人 IP，能变现的短视频 | 空中茶话会',
    description: '系统拆解从人设打造到短视频变现流程 SOP。',
    date: '2025/11/27 · 20:00',
    location: '线上',
    cover: 'https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?w=900&h=600&fit=crop'
  },
  {
    id: 3,
    title: '一人公司 CEO 聚会（长沙版）',
    description: '你的“一人公司”怎么样了？',
    date: '2025/11/22 · 14:00',
    location: '长沙',
    cover: 'https://images.unsplash.com/photo-1503428593586-e225b39bddfe?w=900&h=600&fit=crop'
  },
  {
    id: 4,
    title: 'AI 产品冷启动：找到你的第一个真爱用户',
    description: '北上创业研讨会 · 深入交流产品冷启动方法。',
    date: '2025/11/18 · 19:00',
    location: '北京',
    cover: 'https://images.unsplash.com/photo-1542744173-8e7e53415bb0?w=900&h=600&fit=crop'
  }
])
</script>

<style scoped>
.events-page {
  flex: 1;
  padding: 32px 40px;
  background-color: #ffffff;
  overflow-y: auto;
  height: 100vh;
}

.hero {
  margin-bottom: 28px;
}

.title {
  font-size: 40px;
  font-weight: 800;
  color: #111827;
  margin: 0 0 6px;
}

.subtitle {
  font-size: 22px;
  color: #1f2937;
  font-weight: 700;
  margin: 0 0 16px;
}

.hero-slider {
  position: relative;
  border-radius: 16px;
  overflow: hidden;
  border: 1px solid #e5e7eb;
}

.hero-slide {
  position: absolute;
  inset: 0;
}

.hero-slide img {
  width: 100%;
  height: 520px;
  object-fit: cover;
  display: block;
}

.slider-dots {
  position: absolute;
  left: 50%;
  bottom: 14px;
  transform: translateX(-50%);
  display: flex;
  gap: 8px;
}

.dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  border: none;
  background-color: rgba(255, 255, 255, 0.4);
  cursor: pointer;
}

.dot.active {
  background-color: #ffffff;
}

.hero-actions {
  position: absolute;
  right: 16px;
  bottom: 16px;
  display: flex;
  gap: 10px;
}

.pill-btn {
  padding: 10px 16px;
  border-radius: 999px;
  background-color: #111827;
  color: #ffffff;
  border: 1px solid #111827;
  font-size: 14px;
  cursor: pointer;
}

.pill-btn.outline {
  background-color: #ffffff;
  color: #111827;
  border-color: #d1d5db;
}

.upcoming .section-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin: 18px 0;
}

.upcoming h2 {
  font-size: 20px;
  color: #111827;
  font-weight: 700;
  margin: 0;
}

.filters {
  display: flex;
  gap: 8px;
}

.tab {
  padding: 8px 14px;
  background-color: #f4f6f8;
  border: 1px solid #e5e7eb;
  color: #4b5563;
  font-size: 13px;
  border-radius: 999px;
  cursor: pointer;
}

.tab.active {
  background-color: #111827;
  color: #ffffff;
  border-color: #111827;
}

.card-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  padding-bottom: 36px;
}

.event-card {
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  overflow: hidden;
  background-color: #ffffff;
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.04);
  display: flex;
  flex-direction: column;
}

.cover {
  width: 100%;
  height: 170px;
  background-color: #f3f4f6;
}

.cover img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.card-content {
  padding: 14px 16px 16px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.event-title {
  font-size: 16px;
  color: #111827;
  font-weight: 600;
  margin: 0;
}

.event-desc {
  font-size: 13px;
  color: #4b5563;
  line-height: 1.6;
  margin: 0;
}

.meta {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}

.meta-text {
  font-size: 12px;
  color: #6b7280;
}

.tags {
  display: flex;
  gap: 8px;
}

.tag {
  padding: 4px 10px;
  border-radius: 999px;
  background-color: #f3f4f6;
  color: #6b7280;
  font-size: 12px;
}

.tag.primary {
  background-color: #111827;
  color: #ffffff;
}

@media (max-width: 1280px) {
  .card-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 900px) {
  .events-page {
    padding: 24px;
  }

  .card-grid {
    grid-template-columns: 1fr;
  }
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.6s;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>


```

```vue
<template>
  <main class="events-page">
    <section class="hero">
      <h1 class="title">Starter Community</h1>
      <p class="subtitle">探索前沿，碰撞机会</p>

      <div class="hero-slider">
        <transition-group name="fade" tag="div">
          <div
            v-for="(slide, index) in slides"
            :key="slide.id"
            v-show="currentSlide === index"
            class="hero-slide"
          >
            <img :src="slide.image" :alt="'slide-' + slide.id" />
          </div>
        </transition-group>

        <div class="slider-dots">
          <button
            v-for="(slide, index) in slides"
            :key="slide.id"
            :class="['dot', { active: currentSlide === index }]"
            @click="setSlide(index)"
          />
        </div>

        <div class="hero-actions">
          <button class="pill-btn">往期主题</button>
          <button class="pill-btn outline">往期嘉宾</button>
        </div>
      </div>

      <div class="hero-below">
        <div class="hero-stats">
          <div class="stat-line">累计邀请200+分享嘉宾</div>
          <div class="stat-line sub">汇聚6000+创始人</div>
        </div>
      </div>
    </section>

    <section class="upcoming">
      <div class="section-header">
        <h2>查看近期活动</h2>
        <div class="filters">
          <button v-for="tab in tabs" :key="tab" :class="['tab', { active: activeTab === tab }]" @click="activeTab = tab">
            {{ tab }}
          </button>
        </div>
      </div>

      <div class="card-grid">
        <article v-for="event in events" :key="event.id" class="event-card">
          <div class="cover">
            <img :src="event.cover" :alt="event.title" />
          </div>
          <div class="card-content">
            <h3 class="event-title">{{ event.title }}</h3>
            <p class="event-desc">{{ event.description }}</p>
            <div class="meta">
              <span class="meta-text">开放报名</span>
              <span class="meta-text">{{ event.date }}</span>
              <span class="meta-text">{{ event.location }}</span>
            </div>
            <div class="tags">
              <span class="tag">会员活动</span>
              <span class="tag primary">火热报名中</span>
            </div>
          </div>
        </article>
      </div>
    </section>
  </main>
  </template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'

const tabs = ['不限', '即将开始', '往期活动']
const activeTab = ref(tabs[0])

const slides = [
  { id: 1, image: 'https://images.unsplash.com/photo-1492684223066-81342ee5ff30?w=1600&h=900&fit=crop' },
  { id: 2, image: 'https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=1600&h=900&fit=crop' },
  { id: 3, image: 'https://images.unsplash.com/photo-1551836022-d5d88e9218df?w=1600&h=900&fit=crop' }
]

const currentSlide = ref(0)
let timer = null

const start = () => {
  stop()
  timer = setInterval(() => {
    currentSlide.value = (currentSlide.value + 1) % slides.length
  }, 5000)
}

const stop = () => {
  if (timer) {
    clearInterval(timer)
    timer = null
  }
}

const setSlide = (i) => {
  currentSlide.value = i
  start()
}

onMounted(() => start())
onBeforeUnmount(() => stop())

const events = ref([
  {
    id: 1,
    title: '消费品牌出海空中路演 Demo Day | 线上开放麦',
    description: '亮相你的出海消费品牌，找用户、找合作、找投资。',
    date: '2025/11/28 · 19:30',
    location: '线上',
    cover: 'https://images.unsplash.com/photo-1540575467063-178a50c2df87?w=900&h=600&fit=crop'
  },
  {
    id: 2,
    title: '创始人 IP，能变现的短视频 | 空中茶话会',
    description: '系统拆解从人设打造到短视频变现流程 SOP。',
    date: '2025/11/27 · 20:00',
    location: '线上',
    cover: 'https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?w=900&h=600&fit=crop'
  },
  {
    id: 3,
    title: '一人公司 CEO 聚会（长沙版）',
    description: '你的“一人公司”怎么样了？',
    date: '2025/11/22 · 14:00',
    location: '长沙',
    cover: 'https://images.unsplash.com/photo-1503428593586-e225b39bddfe?w=900&h=600&fit=crop'
  },
  {
    id: 4,
    title: 'AI 产品冷启动：找到你的第一个真爱用户',
    description: '北上创业研讨会 · 深入交流产品冷启动方法。',
    date: '2025/11/18 · 19:00',
    location: '北京',
    cover: 'https://images.unsplash.com/photo-1542744173-8e7e53415bb0?w=900&h=600&fit=crop'
  }
])
</script>

<style scoped>
.events-page {
  flex: 1;
  padding: 32px 40px;
  background-color: #ffffff;
  overflow-y: auto;
  height: 100vh;
}

.hero {
  margin-bottom: 28px;
}

.title {
  font-size: 40px;
  font-weight: 800;
  color: #111827;
  margin: 0 0 6px;
}

.subtitle {
  font-size: 22px;
  color: #1f2937;
  font-weight: 700;
  margin: 0 0 16px;
}

.hero-slider {
  position: relative;
  border-radius: 16px;
  overflow: hidden;
  border: 1px solid #e5e7eb;
}

.hero-slide {
  position: absolute;
  inset: 0;
}

.hero-slide img {
  width: 100%;
  height: 560px;
  object-fit: cover;
  display: block;
}

.slider-dots {
  position: absolute;
  left: 50%;
  bottom: 14px;
  transform: translateX(-50%);
  display: flex;
  gap: 8px;
}

.dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  border: none;
  background-color: rgba(255, 255, 255, 0.4);
  cursor: pointer;
}

.dot.active {
  background-color: #ffffff;
}

.hero-actions {
  position: absolute;
  right: 16px;
  bottom: 16px;
  display: flex;
  gap: 10px;
}

.pill-btn {
  padding: 10px 16px;
  border-radius: 999px;
  background-color: #111827;
  color: #ffffff;
  border: 1px solid #111827;
  font-size: 14px;
  cursor: pointer;
}

.pill-btn.outline {
  background-color: #ffffff;
  color: #111827;
  border-color: #d1d5db;
}

.hero-below {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 6px 0;
}

.hero-stats .stat-line {
  font-size: 14px;
  color: #111827;
}

.hero-stats .stat-line.sub {
  color: #6b7280;
  margin-top: 2px;
}

.upcoming .section-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin: 18px 0;
}

.upcoming h2 {
  font-size: 20px;
  color: #111827;
  font-weight: 700;
  margin: 0;
}

.filters {
  display: flex;
  gap: 8px;
}

.tab {
  padding: 8px 14px;
  background-color: #f4f6f8;
  border: 1px solid #e5e7eb;
  color: #4b5563;
  font-size: 13px;
  border-radius: 999px;
  cursor: pointer;
}

.tab.active {
  background-color: #111827;
  color: #ffffff;
  border-color: #111827;
}

.card-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  padding-bottom: 36px;
}

.event-card {
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  overflow: hidden;
  background-color: #ffffff;
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.04);
  display: flex;
  flex-direction: column;
}

.cover {
  width: 100%;
  height: 170px;
  background-color: #f3f4f6;
}

.cover img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.card-content {
  padding: 14px 16px 16px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.event-title {
  font-size: 16px;
  color: #111827;
  font-weight: 600;
  margin: 0;
}

.event-desc {
  font-size: 13px;
  color: #4b5563;
  line-height: 1.6;
  margin: 0;
}

.meta {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}

.meta-text {
  font-size: 12px;
  color: #6b7280;
}

.tags {
  display: flex;
  gap: 8px;
}

.tag {
  padding: 4px 10px;
  border-radius: 999px;
  background-color: #f3f4f6;
  color: #6b7280;
  font-size: 12px;
}

.tag.primary {
  background-color: #111827;
  color: #ffffff;
}

@media (max-width: 1280px) {
  .card-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 900px) {
  .events-page {
    padding: 24px;
  }

  .card-grid {
    grid-template-columns: 1fr;
  }
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.6s;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>


```

我已补上首页大图轮播区，并贴近参考样式：

- 在活动页顶部增加“英雄区”全宽大图轮播（自动切换、指示点可点击），右下角保留“往期主题 / 往期嘉宾”按钮。
- 轮播下方新增两行说明文字：“累计邀请200+分享嘉宾 / 汇聚6000+创始人”。
- 调整大图高度为 560px，使视觉更接近参考页面。

现在进入“活动”路由应首先看到大图轮播，且能自动轮播与手动切换。

---

**User**

还是没有图片 这是目前的页面

---

**Cursor**

```vue
<template>
  <main class="events-page">
    <section class="hero">
      <h1 class="title">Starter Community</h1>
      <p class="subtitle">探索前沿，碰撞机会</p>

      <div class="hero-slider">
        <transition-group name="fade" tag="div">
          <div
            v-for="(slide, index) in slides"
            :key="slide.id"
            v-show="currentSlide === index"
            class="hero-slide"
          >
            <img :src="slide.image" :alt="'slide-' + slide.id" />
          </div>
        </transition-group>

        <div class="slider-dots">
          <button
            v-for="(slide, index) in slides"
            :key="slide.id"
            :class="['dot', { active: currentSlide === index }]"
            @click="setSlide(index)"
          />
        </div>

        <div class="hero-actions">
          <button class="pill-btn">往期主题</button>
          <button class="pill-btn outline">往期嘉宾</button>
        </div>
      </div>

      <div class="hero-below">
        <div class="hero-stats">
          <div class="stat-line">累计邀请200+分享嘉宾</div>
          <div class="stat-line sub">汇聚6000+创始人</div>
        </div>
      </div>
    </section>

    <section class="upcoming">
      <div class="section-header">
        <h2>查看近期活动</h2>
        <div class="filters">
          <button v-for="tab in tabs" :key="tab" :class="['tab', { active: activeTab === tab }]" @click="activeTab = tab">
            {{ tab }}
          </button>
        </div>
      </div>

      <div class="card-grid">
        <article v-for="event in events" :key="event.id" class="event-card">
          <div class="cover">
            <img :src="event.cover" :alt="event.title" />
          </div>
          <div class="card-content">
            <h3 class="event-title">{{ event.title }}</h3>
            <p class="event-desc">{{ event.description }}</p>
            <div class="meta">
              <span class="meta-text">开放报名</span>
              <span class="meta-text">{{ event.date }}</span>
              <span class="meta-text">{{ event.location }}</span>
            </div>
            <div class="tags">
              <span class="tag">会员活动</span>
              <span class="tag primary">火热报名中</span>
            </div>
          </div>
        </article>
      </div>
    </section>
  </main>
  </template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'

const tabs = ['不限', '即将开始', '往期活动']
const activeTab = ref(tabs[0])

const slides = [
  { id: 1, image: 'https://images.unsplash.com/photo-1492684223066-81342ee5ff30?w=1600&h=900&fit=crop' },
  { id: 2, image: 'https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=1600&h=900&fit=crop' },
  { id: 3, image: 'https://images.unsplash.com/photo-1551836022-d5d88e9218df?w=1600&h=900&fit=crop' }
]

const currentSlide = ref(0)
let timer = null

const start = () => {
  stop()
  timer = setInterval(() => {
    currentSlide.value = (currentSlide.value + 1) % slides.length
  }, 5000)
}

const stop = () => {
  if (timer) {
    clearInterval(timer)
    timer = null
  }
}

const setSlide = (i) => {
  currentSlide.value = i
  start()
}

onMounted(() => start())
onBeforeUnmount(() => stop())

const events = ref([
  {
    id: 1,
    title: '消费品牌出海空中路演 Demo Day | 线上开放麦',
    description: '亮相你的出海消费品牌，找用户、找合作、找投资。',
    date: '2025/11/28 · 19:30',
    location: '线上',
    cover: 'https://images.unsplash.com/photo-1540575467063-178a50c2df87?w=900&h=600&fit=crop'
  },
  {
    id: 2,
    title: '创始人 IP，能变现的短视频 | 空中茶话会',
    description: '系统拆解从人设打造到短视频变现流程 SOP。',
    date: '2025/11/27 · 20:00',
    location: '线上',
    cover: 'https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?w=900&h=600&fit=crop'
  },
  {
    id: 3,
    title: '一人公司 CEO 聚会（长沙版）',
    description: '你的“一人公司”怎么样了？',
    date: '2025/11/22 · 14:00',
    location: '长沙',
    cover: 'https://images.unsplash.com/photo-1503428593586-e225b39bddfe?w=900&h=600&fit=crop'
  },
  {
    id: 4,
    title: 'AI 产品冷启动：找到你的第一个真爱用户',
    description: '北上创业研讨会 · 深入交流产品冷启动方法。',
    date: '2025/11/18 · 19:00',
    location: '北京',
    cover: 'https://images.unsplash.com/photo-1542744173-8e7e53415bb0?w=900&h=600&fit=crop'
  }
])
</script>

<style scoped>
.events-page {
  flex: 1;
  padding: 32px 40px;
  background-color: #ffffff;
  overflow-y: auto;
  height: 100vh;
}

.hero {
  margin-bottom: 28px;
}

.title {
  font-size: 40px;
  font-weight: 800;
  color: #111827;
  margin: 0 0 6px;
}

.subtitle {
  font-size: 22px;
  color: #1f2937;
  font-weight: 700;
  margin: 0 0 16px;
}

.hero-slider {
  position: relative;
  border-radius: 16px;
  overflow: hidden;
  border: 1px solid #e5e7eb;
  height: 560px;
  margin-bottom: 6px;
}

.hero-slide {
  position: absolute;
  inset: 0;
}

.hero-slide img {
  width: 100%;
  height: 560px;
  object-fit: cover;
  display: block;
}

.slider-dots {
  position: absolute;
  left: 50%;
  bottom: 14px;
  transform: translateX(-50%);
  display: flex;
  gap: 8px;
}

.dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  border: none;
  background-color: rgba(255, 255, 255, 0.4);
  cursor: pointer;
}

.dot.active {
  background-color: #ffffff;
}

.hero-actions {
  position: absolute;
  right: 16px;
  bottom: 16px;
  display: flex;
  gap: 10px;
}

.pill-btn {
  padding: 10px 16px;
  border-radius: 999px;
  background-color: #111827;
  color: #ffffff;
  border: 1px solid #111827;
  font-size: 14px;
  cursor: pointer;
}

.pill-btn.outline {
  background-color: #ffffff;
  color: #111827;
  border-color: #d1d5db;
}

.hero-below {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 6px 0;
}

.hero-stats .stat-line {
  font-size: 14px;
  color: #111827;
}

.hero-stats .stat-line.sub {
  color: #6b7280;
  margin-top: 2px;
}

.upcoming .section-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin: 18px 0;
}

.upcoming h2 {
  font-size: 20px;
  color: #111827;
  font-weight: 700;
  margin: 0;
}

.filters {
  display: flex;
  gap: 8px;
}

.tab {
  padding: 8px 14px;
  background-color: #f4f6f8;
  border: 1px solid #e5e7eb;
  color: #4b5563;
  font-size: 13px;
  border-radius: 999px;
  cursor: pointer;
}

.tab.active {
  background-color: #111827;
  color: #ffffff;
  border-color: #111827;
}

.card-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  padding-bottom: 36px;
}

.event-card {
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  overflow: hidden;
  background-color: #ffffff;
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.04);
  display: flex;
  flex-direction: column;
}

.cover {
  width: 100%;
  height: 170px;
  background-color: #f3f4f6;
}

.cover img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.card-content {
  padding: 14px 16px 16px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.event-title {
  font-size: 16px;
  color: #111827;
  font-weight: 600;
  margin: 0;
}

.event-desc {
  font-size: 13px;
  color: #4b5563;
  line-height: 1.6;
  margin: 0;
}

.meta {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}

.meta-text {
  font-size: 12px;
  color: #6b7280;
}

.tags {
  display: flex;
  gap: 8px;
}

.tag {
  padding: 4px 10px;
  border-radius: 999px;
  background-color: #f3f4f6;
  color: #6b7280;
  font-size: 12px;
}

.tag.primary {
  background-color: #111827;
  color: #ffffff;
}

@media (max-width: 1280px) {
  .card-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 900px) {
  .events-page {
    padding: 24px;
  }

  .card-grid {
    grid-template-columns: 1fr;
  }
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.6s;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>


```

已修复。原因是轮播容器没有高度（子元素是 absolute），导致整块被折叠不可见。我给 `.hero-slider` 增加了固定高度并留出下边距，现在大图会正常显示并自动轮播。请刷新活动页再看一眼。

---

**User**

按照这个风格生成一个我的页面 点击链接可以跳转过去 我提供参考图片

hello

