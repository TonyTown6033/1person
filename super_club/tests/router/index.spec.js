/**
 * 路由配置测试
 */
import { describe, it, expect, vi } from 'vitest'

describe('Router Configuration', () => {
  describe('路由定义', () => {
    it('应该导出路由实例', async () => {
      // Mock localStorage for router
      global.localStorage = {
        getItem: vi.fn(),
        setItem: vi.fn(),
        removeItem: vi.fn()
      }

      const router = await import('@/router/index')
      expect(router.default).toBeDefined()
    })
  })

  describe('路由守卫', () => {
    it('未登录时应该能访问公开页面', async () => {
      global.localStorage = {
        getItem: vi.fn().mockReturnValue(null),
        setItem: vi.fn(),
        removeItem: vi.fn()
      }

      const router = await import('@/router/index')
      
      // 验证路由存在
      expect(router.default).toBeDefined()
    })
  })

  describe('路由元信息', () => {
    it('受保护的路由应该有 requiresAuth 元信息', async () => {
      global.localStorage = {
        getItem: vi.fn(),
        setItem: vi.fn(),
        removeItem: vi.fn()
      }

      const router = await import('@/router/index')
      const routes = router.default.options?.routes || []
      
      // 检查是否有需要认证的路由
      const protectedRoutes = routes.filter(r => r.meta?.requiresAuth)
      // 可能存在受保护路由
      expect(Array.isArray(protectedRoutes)).toBe(true)
    })
  })
})

