import request from './request'
import { API_ENDPOINTS } from '@/config/api'

/**
 * 活动管理相关API
 */
export const eventsAPI = {
  /**
   * 获取活动列表
   * @param {Object} params - 查询参数
   * @param {string} params.status - 活动状态: all/upcoming/past
   * @param {string} params.category - 活动分类
   * @param {number} params.page - 页码
   * @param {number} params.limit - 每页数量
   */
  getList(params = {}) {
    return request.get(API_ENDPOINTS.EVENTS.LIST, params)
  },

  /**
   * 获取活动详情
   * @param {string} id - 活动ID
   */
  getDetail(id) {
    return request.get(API_ENDPOINTS.EVENTS.DETAIL(id))
  },

  /**
   * 报名活动
   * @param {string} id - 活动ID
   * @param {Object} data - 报名信息
   * @param {Object} data.attendeeInfo - 参会者信息
   * @param {string} data.note - 备注
   * @param {Array} data.questions - 问卷回答
   */
  register(id, data) {
    return request.post(API_ENDPOINTS.EVENTS.REGISTER(id), data)
  },

  /**
   * 取消报名
   * @param {string} id - 活动ID
   */
  cancelRegister(id) {
    return request.delete(API_ENDPOINTS.EVENTS.REGISTER(id))
  },

  /**
   * 获取我的活动
   * @param {Object} params - 查询参数
   * @param {string} params.status - 状态: upcoming/past/all
   * @param {number} params.page - 页码
   * @param {number} params.limit - 每页数量
   */
  getMyEvents(params = {}) {
    return request.get(API_ENDPOINTS.EVENTS.MY_EVENTS, params)
  },

  /**
   * 获取轮播图
   */
  getCarousel() {
    return request.get(API_ENDPOINTS.EVENTS.CAROUSEL)
  }
}
