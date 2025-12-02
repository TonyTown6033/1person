/**
 * 前端日志工具
 */

const LOG_LEVELS = {
  DEBUG: 0,
  INFO: 1,
  WARN: 2,
  ERROR: 3,
  NONE: 4
}

class Logger {
  constructor(name = 'App', level = 'INFO') {
    this.name = name
    this.level = LOG_LEVELS[level.toUpperCase()] || LOG_LEVELS.INFO
    this.logs = [] // 存储日志（用于调试）
    this.maxLogs = 100 // 最多存储100条日志
  }

  /**
   * 格式化日志消息
   */
  formatMessage(level, message, data = null) {
    const timestamp = new Date().toISOString()
    const logEntry = {
      timestamp,
      level,
      name: this.name,
      message,
      data
    }
    
    // 存储日志
    this.logs.push(logEntry)
    if (this.logs.length > this.maxLogs) {
      this.logs.shift()
    }
    
    return logEntry
  }

  /**
   * 输出日志
   */
  output(level, message, data = null) {
    if (LOG_LEVELS[level] < this.level) {
      return
    }

    const logEntry = this.formatMessage(level, message, data)
    const prefix = `[${logEntry.timestamp}] [${level}] [${this.name}]`

    switch (level) {
      case 'DEBUG':
        console.debug(prefix, message, data || '')
        break
      case 'INFO':
        console.info(prefix, message, data || '')
        break
      case 'WARN':
        console.warn(prefix, message, data || '')
        break
      case 'ERROR':
        console.error(prefix, message, data || '')
        // 错误日志可以发送到服务器
        this.sendErrorToServer(logEntry)
        break
      default:
        console.log(prefix, message, data || '')
    }
  }

  /**
   * 发送错误日志到服务器
   */
  async sendErrorToServer(logEntry) {
    try {
      // 只在生产环境发送错误日志
      if (import.meta.env.PROD) {
        // 可以发送到错误收集服务
        // await fetch('/api/logs/error', {
        //   method: 'POST',
        //   headers: { 'Content-Type': 'application/json' },
        //   body: JSON.stringify(logEntry)
        // })
      }
    } catch (e) {
      // 静默失败，避免日志收集本身导致错误
    }
  }

  debug(message, data = null) {
    this.output('DEBUG', message, data)
  }

  info(message, data = null) {
    this.output('INFO', message, data)
  }

  warn(message, data = null) {
    this.output('WARN', message, data)
  }

  error(message, error = null) {
    const errorData = error ? {
      message: error.message,
      stack: error.stack,
      name: error.name
    } : null
    this.output('ERROR', message, errorData)
  }

  /**
   * 记录 API 请求
   */
  logApiRequest(method, url, params = null) {
    this.debug(`API Request: ${method} ${url}`, params)
  }

  /**
   * 记录 API 响应
   */
  logApiResponse(method, url, status, duration, data = null) {
    const level = status >= 400 ? 'ERROR' : status >= 300 ? 'WARN' : 'INFO'
    this.output(level, `API Response: ${method} ${url} - ${status} (${duration}ms)`, data)
  }

  /**
   * 记录 API 错误
   */
  logApiError(method, url, error) {
    this.error(`API Error: ${method} ${url}`, error)
  }

  /**
   * 获取所有日志
   */
  getLogs() {
    return this.logs
  }

  /**
   * 清空日志
   */
  clearLogs() {
    this.logs = []
  }

  /**
   * 导出日志
   */
  exportLogs() {
    return JSON.stringify(this.logs, null, 2)
  }
}

// 创建默认日志实例
const defaultLogger = new Logger('App', import.meta.env.DEV ? 'DEBUG' : 'INFO')

// 创建各个模块的日志实例
export const apiLogger = new Logger('API', import.meta.env.DEV ? 'DEBUG' : 'INFO')
export const componentLogger = new Logger('Component', import.meta.env.DEV ? 'DEBUG' : 'WARN')
export const errorLogger = new Logger('Error', 'ERROR')

export default defaultLogger







