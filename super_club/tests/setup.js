/**
 * 测试设置文件
 */

// Mock localStorage
const localStorageMock = {
  getItem: vi.fn(),
  setItem: vi.fn(),
  removeItem: vi.fn(),
  clear: vi.fn()
}
global.localStorage = localStorageMock

// Mock fetch
global.fetch = vi.fn()

// 重置 mocks
beforeEach(() => {
  vi.clearAllMocks()
  localStorage.getItem.mockClear()
  localStorage.setItem.mockClear()
  localStorage.removeItem.mockClear()
})

