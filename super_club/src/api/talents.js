import request from './request'
import { API_ENDPOINTS } from '@/config/api'

/**
 * 人才库相关API
 */
export const talentsAPI = {
  /**
   * 获取人才列表
   * @param {Object} params - 查询参数
   * @param {string} params.field - 擅长领域
   * @param {string} params.city - 所在城市
   * @param {string} params.search - 搜索关键词
   * @param {number} params.page - 页码
   * @param {number} params.limit - 每页数量
   * @param {string} params.sort - 排序方式
   */
  getList(params = {}) {
    return request.get(API_ENDPOINTS.TALENTS.LIST, params)
  },

  /**
   * 获取人才详情
   * @param {string} id - 人才ID
   */
  getDetail(id) {
    return request.get(API_ENDPOINTS.TALENTS.DETAIL(id))
  },

  /**
   * 获取精选人才（本周焦点）
   * @param {number} limit - 数量限制，默认3
   */
  getFeatured(limit = 3) {
    return request.get(API_ENDPOINTS.TALENTS.FEATURED, { limit })
  },

  /**
   * 获取人才统计数据
   */
  getStats() {
    return request.get(API_ENDPOINTS.TALENTS.STATS)
  },

  /**
   * 邀约人才
   * @param {string} id - 人才ID
   * @param {Object} data - 邀约信息
   * @param {string} data.message - 邀约留言
   * @param {string} data.preferredDate - 期望时间
   * @param {string} data.topic - 交流主题
   * @param {number} data.duration - 时长（分钟）
   */
  invite(id, data) {
    return request.post(API_ENDPOINTS.TALENTS.INVITE(id), data)
  }
}
