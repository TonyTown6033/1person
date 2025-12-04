/**
 * Sidebar 组件测试
 */
import { describe, it, expect, vi } from 'vitest'
import { mount } from '@vue/test-utils'
import { createRouter, createWebHistory } from 'vue-router'
import Sidebar from '@/components/Sidebar.vue'

// 创建测试路由
const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'home' },
    { path: '/talents', name: 'talents' },
    { path: '/projects', name: 'projects' },
    { path: '/events', name: 'events' },
    { path: '/links', name: 'links' },
    { path: '/login', name: 'login' },
    { path: '/profile', name: 'profile' }
  ]
})

describe('Sidebar', () => {
  const mountSidebar = async () => {
    const wrapper = mount(Sidebar, {
      global: {
        plugins: [router]
      }
    })
    await router.isReady()
    return wrapper
  }

  it('正确渲染侧边栏', async () => {
    const wrapper = await mountSidebar()
    
    expect(wrapper.find('.sidebar').exists()).toBe(true)
  })

  it('包含导航链接', async () => {
    const wrapper = await mountSidebar()
    
    const links = wrapper.findAll('a, .nav-item, router-link')
    expect(links.length).toBeGreaterThan(0)
  })

  it('显示 logo 或品牌', async () => {
    const wrapper = await mountSidebar()
    
    // 检查是否有 logo 相关元素
    const logoExists = wrapper.find('.logo').exists() || 
                       wrapper.find('.brand').exists() ||
                       wrapper.find('img').exists()
    expect(logoExists).toBe(true)
  })
})

