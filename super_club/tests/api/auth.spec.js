/**
 * 认证 API 测试
 */
import { describe, it, expect, vi, beforeEach } from 'vitest'

// Mock request module
vi.mock('@/api/request', () => ({
  default: {
    post: vi.fn(),
    get: vi.fn()
  }
}))

// Mock API endpoints
vi.mock('@/config/api', () => ({
  API_ENDPOINTS: {
    AUTH: {
      REGISTER: '/api/auth/register',
      LOGIN: '/api/auth/login',
      LOGOUT: '/api/auth/logout',
      REFRESH: '/api/auth/refresh'
    }
  }
}))

import { authAPI } from '@/api/auth'
import request from '@/api/request'

describe('authAPI', () => {
  beforeEach(() => {
    vi.clearAllMocks()
    localStorage.getItem.mockClear()
    localStorage.setItem.mockClear()
    localStorage.removeItem.mockClear()
  })

  describe('register', () => {
    it('应该调用正确的注册端点', async () => {
      const userData = {
        email: 'test@example.com',
        password: 'Password123',
        name: '测试用户'
      }
      
      request.post.mockResolvedValue({ user: {}, tokens: {} })
      
      await authAPI.register(userData)
      
      expect(request.post).toHaveBeenCalledWith(
        '/api/auth/register',
        userData
      )
    })
  })

  describe('login', () => {
    it('应该调用正确的登录端点', async () => {
      const credentials = {
        email: 'test@example.com',
        password: 'Password123'
      }
      
      const mockResponse = {
        user: { id: '1', name: '测试用户' },
        tokens: {
          accessToken: 'access_token',
          refreshToken: 'refresh_token'
        }
      }
      
      request.post.mockResolvedValue(mockResponse)
      
      await authAPI.login(credentials)
      
      expect(request.post).toHaveBeenCalledWith(
        '/api/auth/login',
        credentials
      )
    })

    it('登录成功后应该保存 token 到 localStorage', async () => {
      const credentials = {
        email: 'test@example.com',
        password: 'Password123'
      }
      
      const mockResponse = {
        user: { id: '1', name: '测试用户' },
        tokens: {
          accessToken: 'access_token',
          refreshToken: 'refresh_token'
        }
      }
      
      request.post.mockResolvedValue(mockResponse)
      
      await authAPI.login(credentials)
      
      expect(localStorage.setItem).toHaveBeenCalledWith('access_token', 'access_token')
      expect(localStorage.setItem).toHaveBeenCalledWith('refresh_token', 'refresh_token')
    })
  })

  describe('logout', () => {
    it('应该调用登出端点并清除 localStorage', async () => {
      request.post.mockResolvedValue({})
      
      await authAPI.logout()
      
      expect(request.post).toHaveBeenCalledWith('/api/auth/logout')
      expect(localStorage.removeItem).toHaveBeenCalledWith('access_token')
      expect(localStorage.removeItem).toHaveBeenCalledWith('refresh_token')
      expect(localStorage.removeItem).toHaveBeenCalledWith('user')
    })

    it('即使请求失败也应该清除 localStorage', async () => {
      request.post.mockRejectedValue(new Error('Network error'))
      
      try {
        await authAPI.logout()
      } catch (e) {
        // 忽略错误
      }
      
      expect(localStorage.removeItem).toHaveBeenCalledWith('access_token')
    })
  })

  describe('refresh', () => {
    it('应该使用刷新令牌更新访问令牌', async () => {
      const mockResponse = {
        accessToken: 'new_access_token'
      }
      
      request.post.mockResolvedValue(mockResponse)
      
      await authAPI.refresh('old_refresh_token')
      
      expect(request.post).toHaveBeenCalledWith(
        '/api/auth/refresh',
        { refreshToken: 'old_refresh_token' }
      )
      expect(localStorage.setItem).toHaveBeenCalledWith('access_token', 'new_access_token')
    })
  })
})

