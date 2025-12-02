import request from './request'
import { API_ENDPOINTS } from '@/config/api'

/**
 * 内容库相关API
 */
export const contentAPI = {
  /**
   * 获取内容卡片
   * @param {Object} params - 查询参数
   * @param {string} params.department - 部门筛选
   * @param {string} params.type - 内容类型
   * @param {string} params.search - 搜索关键词
   * @param {number} params.page - 页码
   * @param {number} params.limit - 每页数量
   */
  getCards(params = {}) {
    return request.get(API_ENDPOINTS.CONTENT.CARDS, params)
  },

  /**
   * 获取文章列表
   * @param {Object} params - 查询参数
   * @param {string} params.category - 分类
   * @param {string} params.tag - 标签
   * @param {number} params.page - 页码
   * @param {number} params.limit - 每页数量
   */
  getArticles(params = {}) {
    return request.get(API_ENDPOINTS.CONTENT.ARTICLES, params)
  },

  /**
   * 获取文章详情
   * @param {string} id - 文章ID
   */
  getArticleDetail(id) {
    return request.get(API_ENDPOINTS.CONTENT.ARTICLE_DETAIL(id))
  },

  /**
   * 点赞文章
   * @param {string} id - 文章ID
   */
  likeArticle(id) {
    return request.post(API_ENDPOINTS.CONTENT.LIKE_ARTICLE(id))
  },

  /**
   * 取消点赞
   * @param {string} id - 文章ID
   */
  unlikeArticle(id) {
    return request.delete(API_ENDPOINTS.CONTENT.LIKE_ARTICLE(id))
  },

  /**
   * 评论文章
   * @param {string} id - 文章ID
   * @param {Object} data - 评论数据
   * @param {string} data.content - 评论内容
   * @param {string} data.parentId - 父评论ID（回复时）
   */
  commentArticle(id, data) {
    return request.post(API_ENDPOINTS.CONTENT.COMMENTS(id), data)
  },

  /**
   * 获取评论列表
   * @param {string} id - 文章ID
   * @param {Object} params - 查询参数
   * @param {number} params.page - 页码
   * @param {number} params.limit - 每页数量
   * @param {string} params.sort - 排序: latest/hot
   */
  getComments(id, params = {}) {
    return request.get(API_ENDPOINTS.CONTENT.COMMENTS(id), params)
  }
}
