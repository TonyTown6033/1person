import request from './request'
import { API_ENDPOINTS } from '@/config/api'

/**
 * 用户相关API
 */
export const userAPI = {
  /**
   * 获取用户信息
   */
  getProfile() {
    return request.get(API_ENDPOINTS.USER.PROFILE)
  },

  /**
   * 更新用户信息
   * @param {Object} data - 用户数据
   * @param {string} data.name - 姓名
   * @param {string} data.bio - 个人简介
   * @param {string} data.company - 公司
   * @param {string} data.position - 职位
   * @param {string} data.phone - 手机号
   */
  updateProfile(data) {
    return request.put(API_ENDPOINTS.USER.PROFILE, data)
  },

  /**
   * 上传头像
   * @param {File} file - 图片文件
   */
  uploadAvatar(file) {
    const formData = new FormData()
    formData.append('avatar', file)
    return request.upload(API_ENDPOINTS.USER.AVATAR, formData)
  },

  /**
   * 获取收藏列表
   * @param {Object} params - 查询参数
   * @param {string} params.type - 收藏类型: talent/project/event/content
   * @param {number} params.page - 页码
   * @param {number} params.limit - 每页数量
   */
  getFavorites(params = {}) {
    return request.get(API_ENDPOINTS.USER.FAVORITES, params)
  },

  /**
   * 添加收藏
   * @param {Object} data - 收藏数据
   * @param {string} data.type - 资源类型
   * @param {string} data.resourceId - 资源ID
   */
  addFavorite(data) {
    return request.post(API_ENDPOINTS.USER.FAVORITES, data)
  },

  /**
   * 取消收藏
   * @param {string} favoriteId - 收藏ID
   */
  removeFavorite(favoriteId) {
    return request.delete(`${API_ENDPOINTS.USER.FAVORITES}/${favoriteId}`)
  }
}
