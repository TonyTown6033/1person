<template>
  <div class="app-container" :class="{ 'admin-layout': isAdminRoute }">
    <Sidebar v-if="!isAdminRoute" />
    <RouterView />
  </div>
</template>

<script setup>
import { RouterView, useRoute } from 'vue-router'
import { computed } from 'vue'
import Sidebar from './components/Sidebar.vue'

const route = useRoute()

// 检查是否是管理后台路由
const isAdminRoute = computed(() => {
  return route.path.startsWith('/admin')
})
</script>

<style scoped>
.app-container {
  display: flex;
  height: 100vh;
  background-color: #ffffff;
}

/* 管理后台布局 - 不使用flex，让AdminLayout组件完全控制布局 */
.app-container.admin-layout {
  display: block;
  height: 100vh;
  background-color: #f5f6fa;
}

/* 移动端为底部导航栏留出空间 */
@media (max-width: 768px) {
  .app-container:not(.admin-layout) {
    flex-direction: column;
    height: auto;
    min-height: 100vh;
    padding-bottom: 60px;
  }
}
</style>
