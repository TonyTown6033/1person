import request from './request'
import { API_ENDPOINTS } from '@/config/api'

/**
 * 社区网络相关API
 */
export const linksAPI = {
  /**
   * 获取社区成员列表
   * @param {Object} params - 查询参数
   * @param {string} params.category - 分类标签
   * @param {string} params.search - 搜索关键词
   * @param {number} params.page - 页码
   * @param {number} params.limit - 每页数量
   */
  getList(params = {}) {
    return request.get(API_ENDPOINTS.LINKS.LIST, params)
  },

  /**
   * 建立连接
   * @param {Object} data - 连接请求数据
   * @param {string} data.targetUserId - 目标用户ID
   * @param {string} data.message - 连接请求留言
   * @param {string} data.purpose - 连接目的
   */
  connect(data) {
    return request.post(API_ENDPOINTS.LINKS.CONNECT, data)
  },

  /**
   * 获取我的连接
   * @param {Object} params - 查询参数
   * @param {string} params.status - 状态: all/connected/pending
   * @param {number} params.page - 页码
   * @param {number} params.limit - 每页数量
   */
  getMyConnections(params = {}) {
    return request.get(API_ENDPOINTS.LINKS.MY_CONNECTIONS, params)
  },

  /**
   * 接受/拒绝连接请求
   * @param {string} id - 连接ID
   * @param {string} action - 操作: accept/reject
   */
  updateConnection(id, action) {
    return request.put(API_ENDPOINTS.LINKS.UPDATE_CONNECTION(id), { action })
  },

  /**
   * 获取轮播图
   */
  getCarousel() {
    return request.get(API_ENDPOINTS.LINKS.CAROUSEL)
  }
}
