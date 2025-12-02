import request from './request'
import { API_ENDPOINTS } from '@/config/api'

/**
 * 项目资源库相关API
 */
export const projectsAPI = {
  /**
   * 获取项目列表
   * @param {Object} params - 查询参数
   * @param {string} params.category - 需求分类
   * @param {string} params.search - 搜索关键词
   * @param {number} params.page - 页码
   * @param {number} params.limit - 每页数量
   * @param {string} params.sort - 排序方式
   */
  getList(params = {}) {
    return request.get(API_ENDPOINTS.PROJECTS.LIST, params)
  },

  /**
   * 获取项目详情
   * @param {string} id - 项目ID
   */
  getDetail(id) {
    return request.get(API_ENDPOINTS.PROJECTS.DETAIL(id))
  },

  /**
   * 发布项目
   * @param {Object} data - 项目数据
   */
  create(data) {
    return request.post(API_ENDPOINTS.PROJECTS.CREATE, data)
  },

  /**
   * 更新项目
   * @param {string} id - 项目ID
   * @param {Object} data - 项目数据
   */
  update(id, data) {
    return request.put(API_ENDPOINTS.PROJECTS.UPDATE(id), data)
  },

  /**
   * 删除项目
   * @param {string} id - 项目ID
   */
  delete(id) {
    return request.delete(API_ENDPOINTS.PROJECTS.DELETE(id))
  },

  /**
   * 表达合作意向
   * @param {string} id - 项目ID
   * @param {Object} data - 意向数据
   * @param {string} data.message - 留言
   * @param {string} data.capability - 能力描述
   * @param {Object} data.contact - 联系方式
   */
  expressInterest(id, data) {
    return request.post(API_ENDPOINTS.PROJECTS.INTEREST(id), data)
  }
}
