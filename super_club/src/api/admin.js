import request from './request.js'

export const adminAPI = {
  // 仪表板统计
  getDashboardStats() {
    return request.get('/admin/dashboard/stats')
  },

  // 用户管理
  getUsers(params = {}) {
    return request.get('/admin/users', { params })
  },

  updateUserStatus(userId, isActive) {
    return request.put(`/admin/users/${userId}/status`, null, {
      params: { is_active: isActive }
    })
  },

  updateUserRole(userId, role) {
    return request.put(`/admin/users/${userId}/role`, null, {
      params: { role }
    })
  },

  // 项目管理
  getProjects(params = {}) {
    return request.get('/admin/projects', { params })
  },

  toggleProjectFeatured(projectId, isFeatured) {
    return request.put(`/admin/projects/${projectId}/featured`, null, {
      params: { is_featured: isFeatured }
    })
  },

  deleteProject(projectId) {
    return request.delete(`/admin/projects/${projectId}`)
  },

  // 最近活动
  getRecentActivities(limit = 10) {
    return request.get('/admin/recent-activities', {
      params: { limit }
    })
  },

  // ==================== 内容管理 ====================
  
  // 获取内容列表
  getContent(params = {}) {
    return request.get('/admin/content', params)
  },

  // 获取内容详情
  getContentDetail(contentId) {
    return request.get(`/admin/content/${contentId}`)
  },

  // 创建内容
  createContent(data) {
    return request.post('/admin/content', data)
  },

  // 更新内容
  updateContent(contentId, data) {
    return request.put(`/admin/content/${contentId}`, data)
  },

  // 切换发布状态
  toggleContentPublish(contentId, isPublished) {
    return request.put(`/admin/content/${contentId}/publish?is_published=${isPublished}`)
  },

  // 切换精选状态
  toggleContentFeatured(contentId, isFeatured) {
    return request.put(`/admin/content/${contentId}/featured?is_featured=${isFeatured}`)
  },

  // 删除内容
  deleteContent(contentId) {
    return request.delete(`/admin/content/${contentId}`)
  },

  // 获取内容统计
  getContentStats() {
    return request.get('/admin/content/stats/overview')
  }
}
