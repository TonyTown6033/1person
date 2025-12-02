import { API_CONFIG } from '../config/api'
import { apiLogger } from '../utils/logger'

/**
 * HTTP 请求封装
 * 使用原生 fetch API
 */
class Request {
  constructor(config) {
    this.baseURL = config.baseURL
    this.timeout = config.timeout
    this.withCredentials = config.withCredentials
  }

  /**
   * 请求拦截器 - 添加认证token等
   */
  beforeRequest(config, url) {
    // 判断是否是管理后台请求
    const isAdminRequest = url && url.includes('/admin')
    
    // 根据请求类型选择对应的token
    const token = isAdminRequest 
      ? localStorage.getItem('admin_token') 
      : localStorage.getItem('access_token')
    
    if (token) {
      config.headers = {
        ...config.headers,
        'Authorization': `Bearer ${token}`
      }
    }
    return config
  }

  /**
   * 响应拦截器 - 统一处理响应
   */
  async afterResponse(response) {
    const data = await response.json()

    // 根据API文档的响应格式处理
    if (!response.ok) {
      // HTTP错误
      const error = new Error(data.error?.message || '请求失败')
      error.code = data.error?.code
      error.details = data.error?.details
      error.status = response.status
      throw error
    }

    // 检查业务状态
    if (!data.success) {
      const error = new Error(data.error?.message || '操作失败')
      error.code = data.error?.code
      error.details = data.error?.details
      throw error
    }

    return data.data
  }

  /**
   * 通用请求方法
   */
  async request(url, options = {}) {
    const startTime = Date.now()
    const method = options.method || 'GET'
    
    // 构建完整URL
    const fullURL = url.startsWith('http') ? url : `${this.baseURL}${url}`

    // 记录请求
    apiLogger.logApiRequest(method, fullURL, options.body)

    // 默认配置
    let config = {
      method: method,
      headers: {
        'Content-Type': 'application/json',
        ...options.headers
      },
      credentials: this.withCredentials ? 'include' : 'same-origin'
    }

    // 添加请求体
    if (options.body) {
      if (options.body instanceof FormData) {
        // FormData类型（如文件上传），不设置Content-Type
        delete config.headers['Content-Type']
        config.body = options.body
      } else {
        // JSON数据
        config.body = JSON.stringify(options.body)
      }
    }

    // 请求拦截（传入url用于判断是否是管理后台请求）
    config = this.beforeRequest(config, url)

    try {
      // 添加超时控制
      const controller = new AbortController()
      const timeoutId = setTimeout(() => controller.abort(), this.timeout)

      config.signal = controller.signal

      const response = await fetch(fullURL, config)
      clearTimeout(timeoutId)

      const duration = Date.now() - startTime
      
      // 记录响应
      apiLogger.logApiResponse(method, fullURL, response.status, duration)

      // 响应拦截
      const result = await this.afterResponse(response)
      return result
    } catch (error) {
      const duration = Date.now() - startTime
      
      // 记录错误
      apiLogger.logApiError(method, fullURL, error)
      
      if (error.name === 'AbortError') {
        const timeoutError = new Error('请求超时')
        apiLogger.error('请求超时', timeoutError)
        throw timeoutError
      }
      throw error
    }
  }

  /**
   * GET 请求
   */
  get(url, params = {}) {
    // 构建查询字符串
    const queryString = Object.keys(params)
      .filter(key => params[key] !== undefined && params[key] !== null)
      .map(key => `${encodeURIComponent(key)}=${encodeURIComponent(params[key])}`)
      .join('&')

    const fullURL = queryString ? `${url}?${queryString}` : url

    return this.request(fullURL, { method: 'GET' })
  }

  /**
   * POST 请求
   */
  post(url, data = {}) {
    return this.request(url, {
      method: 'POST',
      body: data
    })
  }

  /**
   * PUT 请求
   */
  put(url, data = {}) {
    return this.request(url, {
      method: 'PUT',
      body: data
    })
  }

  /**
   * DELETE 请求
   */
  delete(url) {
    return this.request(url, { method: 'DELETE' })
  }

  /**
   * 文件上传
   */
  upload(url, formData) {
    return this.request(url, {
      method: 'POST',
      body: formData
    })
  }
}

// 创建请求实例
const request = new Request(API_CONFIG)

export default request
