# Super Club 后端 API 快速开始指南

## 前端集成步骤

### 1. 安装依赖

```bash
npm install axios
```

### 2. 创建 API 配置文件

创建 `src/services/api.js`:

```javascript
import axios from 'axios'

// 创建 axios 实例
const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8000/api',
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json'
  }
})

// 请求拦截器 - 添加 Token
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('accessToken')
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

// 响应拦截器 - 处理错误
api.interceptors.response.use(
  (response) => {
    return response.data
  },
  async (error) => {
    const originalRequest = error.config

    // Token 过期，尝试刷新
    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true

      try {
        const refreshToken = localStorage.getItem('refreshToken')
        const { data } = await axios.post('/api/auth/refresh', { refreshToken })

        localStorage.setItem('accessToken', data.accessToken)
        originalRequest.headers.Authorization = `Bearer ${data.accessToken}`

        return api(originalRequest)
      } catch (refreshError) {
        // Refresh token 也过期，跳转登录页
        localStorage.removeItem('accessToken')
        localStorage.removeItem('refreshToken')
        window.location.href = '/login'
        return Promise.reject(refreshError)
      }
    }

    return Promise.reject(error)
  }
)

export default api
```

### 3. 创建各模块的 API 服务

创建 `src/services/talent.js`:

```javascript
import api from './api'

export const talentApi = {
  // 获取人才列表
  getList(params) {
    return api.get('/talents', { params })
  },

  // 获取人才详情
  getDetail(id) {
    return api.get(`/talents/${id}`)
  },

  // 获取精选人才
  getFeatured(limit = 3) {
    return api.get('/talents/featured', { params: { limit } })
  },

  // 邀约人才
  invite(id, data) {
    return api.post(`/talents/${id}/invite`, data)
  },

  // 获取统计数据
  getStats() {
    return api.get('/talents/stats')
  }
}
```

创建 `src/services/project.js`:

```javascript
import api from './api'

export const projectApi = {
  // 获取项目列表
  getList(params) {
    return api.get('/projects', { params })
  },

  // 获取项目详情
  getDetail(id) {
    return api.get(`/projects/${id}`)
  },

  // 发布项目
  create(data) {
    return api.post('/projects', data)
  },

  // 更新项目
  update(id, data) {
    return api.put(`/projects/${id}`, data)
  },

  // 删除项目
  delete(id) {
    return api.delete(`/projects/${id}`)
  },

  // 表达合作意向
  expressInterest(id, data) {
    return api.post(`/projects/${id}/interest`, data)
  }
}
```

创建 `src/services/event.js`:

```javascript
import api from './api'

export const eventApi = {
  // 获取活动列表
  getList(params) {
    return api.get('/events', { params })
  },

  // 获取活动详情
  getDetail(id) {
    return api.get(`/events/${id}`)
  },

  // 报名活动
  register(id, data) {
    return api.post(`/events/${id}/register`, data)
  },

  // 取消报名
  cancelRegistration(id) {
    return api.delete(`/events/${id}/register`)
  },

  // 获取我的活动
  getMyEvents(params) {
    return api.get('/events/my-events', { params })
  },

  // 获取轮播图
  getCarousel() {
    return api.get('/events/carousel')
  }
}
```

创建 `src/services/auth.js`:

```javascript
import api from './api'

export const authApi = {
  // 用户注册
  register(data) {
    return api.post('/auth/register', data)
  },

  // 用户登录
  async login(data) {
    const response = await api.post('/auth/login', data)
    if (response.success) {
      localStorage.setItem('accessToken', response.data.tokens.accessToken)
      localStorage.setItem('refreshToken', response.data.tokens.refreshToken)
      localStorage.setItem('user', JSON.stringify(response.data.user))
    }
    return response
  },

  // 退出登录
  async logout() {
    await api.post('/auth/logout')
    localStorage.removeItem('accessToken')
    localStorage.removeItem('refreshToken')
    localStorage.removeItem('user')
  },

  // 刷新 Token
  refresh(refreshToken) {
    return api.post('/auth/refresh', { refreshToken })
  }
}
```

创建 `src/services/user.js`:

```javascript
import api from './api'

export const userApi = {
  // 获取用户信息
  getProfile() {
    return api.get('/user/profile')
  },

  // 更新用户信息
  updateProfile(data) {
    return api.put('/user/profile', data)
  },

  // 上传头像
  uploadAvatar(file) {
    const formData = new FormData()
    formData.append('avatar', file)
    return api.post('/user/avatar', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    })
  },

  // 获取收藏列表
  getFavorites(params) {
    return api.get('/user/favorites', { params })
  },

  // 添加收藏
  addFavorite(data) {
    return api.post('/user/favorites', data)
  },

  // 取消收藏
  removeFavorite(id) {
    return api.delete(`/user/favorites/${id}`)
  }
}
```

### 4. 在组件中使用

更新 `src/pages/TalentPage.vue`:

```vue
<script setup>
import { ref, onMounted } from 'vue'
import { talentApi } from '@/services/talent'

// 数据状态
const featuredTalents = ref([])
const talents = ref([])
const stats = ref({})
const loading = ref(false)
const error = ref(null)

// 筛选条件
const selectedField = ref('不限')
const selectedCity = ref('不限')
const searchQuery = ref('')

// 分页
const currentPage = ref(1)
const totalPages = ref(1)

// 获取精选人才
const fetchFeaturedTalents = async () => {
  try {
    loading.value = true
    const response = await talentApi.getFeatured(3)
    if (response.success) {
      featuredTalents.value = response.data.items
    }
  } catch (err) {
    error.value = err.message
    console.error('获取精选人才失败:', err)
  } finally {
    loading.value = false
  }
}

// 获取人才列表
const fetchTalents = async () => {
  try {
    loading.value = true
    const params = {
      page: currentPage.value,
      limit: 20
    }

    if (selectedField.value !== '不限') {
      params.field = selectedField.value
    }
    if (selectedCity.value !== '不限') {
      params.city = selectedCity.value
    }
    if (searchQuery.value) {
      params.search = searchQuery.value
    }

    const response = await talentApi.getList(params)
    if (response.success) {
      talents.value = response.data.items
      totalPages.value = response.data.pagination.totalPages
    }
  } catch (err) {
    error.value = err.message
    console.error('获取人才列表失败:', err)
  } finally {
    loading.value = false
  }
}

// 获取统计数据
const fetchStats = async () => {
  try {
    const response = await talentApi.getStats()
    if (response.success) {
      stats.value = response.data
    }
  } catch (err) {
    console.error('获取统计数据失败:', err)
  }
}

// 邀约人才
const inviteTalent = async (talentId) => {
  try {
    const response = await talentApi.invite(talentId, {
      message: '您好，我对您的经验很感兴趣，希望能约个时间交流。',
      topic: '咨询交流'
    })

    if (response.success) {
      alert('邀约已发送！')
    }
  } catch (err) {
    alert('邀约失败: ' + err.message)
  }
}

// 筛选变化
const handleFilterChange = () => {
  currentPage.value = 1
  fetchTalents()
}

// 页面加载
onMounted(() => {
  fetchFeaturedTalents()
  fetchTalents()
  fetchStats()
})
</script>

<template>
  <main class="talent-page">
    <!-- 顶部统计 -->
    <section class="stats-hero">
      <div class="stat-item">
        <h2>{{ stats.totalTalents || 368 }}</h2>
        <p>精选牛人</p>
      </div>
      <div class="stat-item">
        <h2>{{ stats.totalTracks || 29 }}</h2>
        <p>覆盖赛道</p>
      </div>
      <div class="stat-item">
        <h2>{{ stats.activeInvitations || 142 }}</h2>
        <p>实时邀约</p>
      </div>
    </section>

    <!-- 加载状态 -->
    <div v-if="loading" class="loading">加载中...</div>

    <!-- 错误提示 -->
    <div v-if="error" class="error">{{ error }}</div>

    <!-- 本周焦点 -->
    <section v-if="!loading" class="talent-spotlight">
      <div class="section-header">
        <h2>本周焦点</h2>
      </div>

      <div class="talent-grid">
        <article v-for="talent in featuredTalents" :key="talent.id" class="talent-card">
          <div class="talent-card-header">
            <div class="avatar">
              <img :src="talent.avatar" :alt="talent.name" />
            </div>
            <div class="identity">
              <div class="name">{{ talent.name }}</div>
              <div class="role">{{ talent.role }}</div>
              <div class="meta">{{ talent.company }} · {{ talent.location }}</div>
            </div>
            <button class="connect-btn" @click="inviteTalent(talent.id)">
              邀约
            </button>
          </div>

          <p class="talent-description">{{ talent.description }}</p>

          <div class="talent-tags">
            <span v-for="tag in talent.tags" :key="tag" class="tag">
              {{ tag }}
            </span>
          </div>

          <div class="talent-stats">
            <div class="stat">
              <span class="stat-number">{{ talent.stats.projects }}</span>
              <span class="stat-text">操盘项目</span>
            </div>
            <div class="stat">
              <span class="stat-number">{{ talent.stats.experience }}</span>
              <span class="stat-text">行业经验</span>
            </div>
            <div class="stat">
              <span class="stat-number">{{ talent.stats.followers }}</span>
              <span class="stat-text">关注</span>
            </div>
          </div>
        </article>
      </div>
    </section>

    <!-- 筛选器 -->
    <section class="talent-filters">
      <div class="filter-group">
        <label>擅长领域</label>
        <select v-model="selectedField" @change="handleFilterChange">
          <option>不限</option>
          <option>增长</option>
          <option>品牌</option>
          <option>产品</option>
          <option>技术</option>
          <option>运营</option>
        </select>
      </div>

      <div class="filter-group">
        <label>所在城市</label>
        <select v-model="selectedCity" @change="handleFilterChange">
          <option>不限</option>
          <option>北京</option>
          <option>上海</option>
          <option>深圳</option>
          <option>杭州</option>
        </select>
      </div>

      <div class="search-box">
        <input
          v-model="searchQuery"
          type="text"
          placeholder="搜索姓名、公司或标签"
          @keyup.enter="handleFilterChange"
        />
        <button @click="handleFilterChange">搜索</button>
      </div>
    </section>

    <!-- 人才列表 -->
    <section class="talent-list">
      <article v-for="talent in talents" :key="talent.id" class="talent-item">
        <!-- 人才卡片内容 -->
      </article>
    </section>

    <!-- 分页 -->
    <div class="pagination">
      <button
        :disabled="currentPage === 1"
        @click="currentPage--; fetchTalents()"
      >
        上一页
      </button>
      <span>第 {{ currentPage }} / {{ totalPages }} 页</span>
      <button
        :disabled="currentPage === totalPages"
        @click="currentPage++; fetchTalents()"
      >
        下一页
      </button>
    </div>
  </main>
</template>
```

### 5. 环境变量配置

创建 `.env.development`:

```env
VITE_API_URL=http://localhost:8000/api
```

创建 `.env.production`:

```env
VITE_API_URL=https://api.superclub.com/api
```

### 6. 错误处理

创建 `src/utils/errorHandler.js`:

```javascript
export const handleApiError = (error) => {
  if (error.response) {
    // 服务器返回错误
    const { status, data } = error.response

    switch (status) {
      case 400:
        return '请求参数错误'
      case 401:
        return '请先登录'
      case 403:
        return '没有访问权限'
      case 404:
        return '资源不存在'
      case 422:
        return data.error?.message || '数据验证失败'
      case 429:
        return '请求过于频繁，请稍后再试'
      case 500:
        return '服务器错误，请稍后再试'
      default:
        return data.error?.message || '操作失败'
    }
  } else if (error.request) {
    // 请求发送但没有收到响应
    return '网络连接失败，请检查网络'
  } else {
    // 其他错误
    return error.message || '未知错误'
  }
}
```

在组件中使用:

```javascript
import { handleApiError } from '@/utils/errorHandler'

try {
  await talentApi.getList(params)
} catch (err) {
  const errorMessage = handleApiError(err)
  alert(errorMessage)
}
```

### 7. 加载状态管理

创建 `src/composables/useApi.js`:

```javascript
import { ref } from 'vue'
import { handleApiError } from '@/utils/errorHandler'

export const useApi = (apiFunction) => {
  const data = ref(null)
  const loading = ref(false)
  const error = ref(null)

  const execute = async (...args) => {
    try {
      loading.value = true
      error.value = null
      const response = await apiFunction(...args)
      data.value = response.data
      return response
    } catch (err) {
      error.value = handleApiError(err)
      throw err
    } finally {
      loading.value = false
    }
  }

  return {
    data,
    loading,
    error,
    execute
  }
}
```

在组件中使用:

```javascript
import { useApi } from '@/composables/useApi'
import { talentApi } from '@/services/talent'

const { data: talents, loading, error, execute: fetchTalents } = useApi(talentApi.getList)

onMounted(() => {
  fetchTalents({ page: 1, limit: 20 })
})
```

### 8. 认证路由守卫

在 `src/router/index.js` 中添加:

```javascript
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // ... 现有路由
  ]
})

// 需要认证的路由
const authRequiredRoutes = ['/profile', '/projects/create']

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('accessToken')
  const requiresAuth = authRequiredRoutes.some(route =>
    to.path.startsWith(route)
  )

  if (requiresAuth && !token) {
    // 重定向到登录页
    next('/login')
  } else {
    next()
  }
})

export default router
```

## 测试 API

### 使用 curl 测试

```bash
# 用户注册
curl -X POST http://localhost:8000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "Test123!",
    "name": "测试用户"
  }'

# 用户登录
curl -X POST http://localhost:8000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "Test123!"
  }'

# 获取人才列表（需要 token）
curl -X GET "http://localhost:8000/api/talents?page=1&limit=20" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### 使用 Postman

1. 导入 API 文档到 Postman
2. 设置环境变量 `base_url` = `http://localhost:8000/api`
3. 创建登录请求获取 token
4. 在 Collection 设置中添加 Authorization: Bearer {{token}}

## 常见问题

### Q: 如何处理 Token 过期？

A: 在 API 响应拦截器中已经处理，会自动使用 refresh token 刷新。

### Q: 如何上传文件？

A: 使用 FormData：

```javascript
const uploadAvatar = async (file) => {
  const formData = new FormData()
  formData.append('avatar', file)

  const response = await api.post('/user/avatar', formData, {
    headers: { 'Content-Type': 'multipart/form-data' }
  })

  return response
}
```

### Q: 如何实现分页加载？

A: 参考上面的 TalentPage.vue 示例，使用 page 和 limit 参数。

### Q: 如何取消正在进行的请求？

A: 使用 AbortController：

```javascript
const controller = new AbortController()

api.get('/talents', {
  signal: controller.signal
})

// 取消请求
controller.abort()
```

## 下一步

1. 阅读完整的 [API 文档](./API_DOCUMENTATION.md)
2. 查看 [数据库设计文档](./DATABASE_DESIGN.md)
3. 了解后端实现指南
