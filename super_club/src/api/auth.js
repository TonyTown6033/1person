import request from './request'
import { API_ENDPOINTS } from '../config/api'

/**
 * 认证相关API
 */
export const authAPI = {
  /**
   * 用户注册
   * @param {Object} data - 注册数据
   * @param {string} data.email - 邮箱
   * @param {string} data.password - 密码
   * @param {string} data.name - 姓名
   * @param {string} data.phone - 手机号（可选）
   */
  register(data) {
    return request.post(API_ENDPOINTS.AUTH.REGISTER, data)
  },

  /**
   * 用户登录
   * @param {Object} data - 登录数据
   * @param {string} data.email - 邮箱
   * @param {string} data.password - 密码
   */
  login(data) {
    return request.post(API_ENDPOINTS.AUTH.LOGIN, data)
      .then(response => {
        // 保存token到localStorage
        if (response.tokens) {
          localStorage.setItem('access_token', response.tokens.accessToken)
          localStorage.setItem('refresh_token', response.tokens.refreshToken)
          localStorage.setItem('user', JSON.stringify(response.user))
        }
        return response
      })
  },

  /**
   * 退出登录
   */
  logout() {
    return request.post(API_ENDPOINTS.AUTH.LOGOUT)
      .finally(() => {
        // 清除本地存储
        localStorage.removeItem('access_token')
        localStorage.removeItem('refresh_token')
        localStorage.removeItem('user')
      })
  },

  /**
   * 刷新token
   * @param {string} refreshToken - Refresh Token
   */
  refresh(refreshToken) {
    return request.post(API_ENDPOINTS.AUTH.REFRESH, { refreshToken })
      .then(response => {
        // 更新token
        if (response.accessToken) {
          localStorage.setItem('access_token', response.accessToken)
        }
        return response
      })
  }
}
