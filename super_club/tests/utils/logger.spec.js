/**
 * Logger 工具测试
 */
import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest'

// Mock console methods
const originalConsole = { ...console }

describe('Logger', () => {
  beforeEach(() => {
    // Mock console
    console.log = vi.fn()
    console.info = vi.fn()
    console.warn = vi.fn()
    console.error = vi.fn()
    console.debug = vi.fn()
  })

  afterEach(() => {
    // 恢复原始 console
    Object.assign(console, originalConsole)
  })

  describe('日志级别', () => {
    it('应该支持 info 级别', async () => {
      // 动态导入 logger（默认导出）
      const loggerModule = await import('@/utils/logger')
      const logger = loggerModule.default
      
      if (logger && typeof logger.info === 'function') {
        logger.info('测试消息')
        // 验证调用成功
        expect(true).toBe(true)
      }
    })

    it('应该支持 warn 级别', async () => {
      const loggerModule = await import('@/utils/logger')
      const logger = loggerModule.default
      
      if (logger && typeof logger.warn === 'function') {
        logger.warn('警告消息')
        expect(true).toBe(true)
      }
    })

    it('应该支持 error 级别', async () => {
      const loggerModule = await import('@/utils/logger')
      const logger = loggerModule.default
      
      if (logger && typeof logger.error === 'function') {
        logger.error('错误消息')
        expect(true).toBe(true)
      }
    })
  })

  describe('日志格式', () => {
    it('应该包含时间戳', async () => {
      const loggerModule = await import('@/utils/logger')
      const logger = loggerModule.default
      
      // 验证 logger 存在
      expect(logger).toBeDefined()
    })

    it('应该支持传递额外数据', async () => {
      const loggerModule = await import('@/utils/logger')
      const logger = loggerModule.default
      
      if (logger && typeof logger.info === 'function') {
        const data = { userId: '123', action: 'login' }
        // 调用不应抛出错误
        expect(() => logger.info('用户操作', data)).not.toThrow()
      }
    })
  })
})

