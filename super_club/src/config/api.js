// API 配置文件
export const API_CONFIG = {
  // 后端API基础URL（优先使用环境变量，否则使用默认值）
  baseURL: import.meta.env.VITE_API_BASE_URL || 'http://127.0.0.1:8001/api',

  // 请求超时时间（毫秒）
  timeout: 10000,

  // 是否携带认证信息
  withCredentials: false
}

// API端点
export const API_ENDPOINTS = {
  // 用户管理
  AUTH: {
    REGISTER: '/auth/register',
    LOGIN: '/auth/login',
    LOGOUT: '/auth/logout',
    REFRESH: '/auth/refresh'
  },

  USER: {
    PROFILE: '/user/profile',
    AVATAR: '/user/avatar',
    FAVORITES: '/user/favorites'
  },

  // 人才库
  TALENTS: {
    LIST: '/talents',
    DETAIL: (id) => `/talents/${id}`,
    FEATURED: '/talents/featured',
    STATS: '/talents/stats',
    INVITE: (id) => `/talents/${id}/invite`
  },

  // 项目资源库
  PROJECTS: {
    LIST: '/projects',
    DETAIL: (id) => `/projects/${id}`,
    CREATE: '/projects',
    UPDATE: (id) => `/projects/${id}`,
    DELETE: (id) => `/projects/${id}`,
    INTEREST: (id) => `/projects/${id}/interest`
  },

  // 活动管理
  EVENTS: {
    LIST: '/events',
    DETAIL: (id) => `/events/${id}`,
    REGISTER: (id) => `/events/${id}/register`,
    MY_EVENTS: '/events/my-events',
    CAROUSEL: '/events/carousel'
  },

  // 社区网络
  LINKS: {
    LIST: '/links',
    CONNECT: '/links/connect',
    MY_CONNECTIONS: '/links/my-connections',
    UPDATE_CONNECTION: (id) => `/links/connections/${id}`,
    CAROUSEL: '/links/carousel'
  },

  // 内容库
  CONTENT: {
    CARDS: '/content/cards',
    ARTICLES: '/content/articles',
    ARTICLE_DETAIL: (id) => `/content/articles/${id}`,
    LIKE_ARTICLE: (id) => `/content/articles/${id}/like`,
    COMMENTS: (id) => `/content/articles/${id}/comments`
  }
}
