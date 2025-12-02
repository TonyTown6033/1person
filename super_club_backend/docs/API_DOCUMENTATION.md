# Super Club 后端 API 文档

> 版本: v1.0.0
> 最后更新: 2025-11-11

## 目录

- [概述](#概述)
- [基础信息](#基础信息)
- [认证授权](#认证授权)
- [通用响应格式](#通用响应格式)
- [错误码](#错误码)
- [API 接口](#api-接口)
  - [1. 用户管理](#1-用户管理)
  - [2. 人才库](#2-人才库)
  - [3. 项目资源库](#3-项目资源库)
  - [4. 活动管理](#4-活动管理)
  - [5. 社区网络](#5-社区网络)
  - [6. 内容库](#6-内容库)
- [数据模型](#数据模型)
- [状态码说明](#状态码说明)

---

## 概述

Super Club 后端 API 为前端 Vue 应用提供数据服务，支持人才库、项目资源库、活动管理、社区网络等核心功能。

**核心功能模块:**
- 用户管理与认证
- 人才库管理
- 项目资源库
- 活动与事件管理
- 社区网络连接
- CEO 图书馆内容管理

---

## 基础信息

### Base URL

```
开发环境: http://localhost:8000/api
生产环境: https://api.superclub.com/api
```

### 请求格式

- Content-Type: `application/json`
- 字符编码: `UTF-8`

### 时间格式

- 所有时间使用 ISO 8601 格式: `2025-11-11T19:30:00Z`
- 时区: UTC

---

## 认证授权

### JWT Token 认证

所有需要认证的接口在 HTTP Header 中携带 JWT Token：

```http
Authorization: Bearer <your_access_token>
```

### Token 获取

通过登录接口获取 Access Token 和 Refresh Token：

```http
POST /api/auth/login
```

### Token 刷新

Access Token 过期时使用 Refresh Token 获取新的 Access Token：

```http
POST /api/auth/refresh
```

---

## 通用响应格式

### 成功响应

```json
{
  "success": true,
  "data": {},
  "message": "操作成功",
  "timestamp": "2025-11-11T12:00:00Z"
}
```

### 错误响应

```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "参数验证失败",
    "details": {
      "field": "email",
      "issue": "邮箱格式不正确"
    }
  },
  "timestamp": "2025-11-11T12:00:00Z"
}
```

### 分页响应

```json
{
  "success": true,
  "data": {
    "items": [],
    "pagination": {
      "page": 1,
      "limit": 20,
      "total": 100,
      "totalPages": 5
    }
  }
}
```

---

## 错误码

| 错误码 | 说明 | HTTP 状态码 |
|--------|------|-------------|
| `SUCCESS` | 成功 | 200 |
| `CREATED` | 资源创建成功 | 201 |
| `BAD_REQUEST` | 请求参数错误 | 400 |
| `UNAUTHORIZED` | 未授权 | 401 |
| `FORBIDDEN` | 禁止访问 | 403 |
| `NOT_FOUND` | 资源不存在 | 404 |
| `CONFLICT` | 资源冲突 | 409 |
| `VALIDATION_ERROR` | 数据验证失败 | 422 |
| `INTERNAL_ERROR` | 服务器内部错误 | 500 |
| `SERVICE_UNAVAILABLE` | 服务不可用 | 503 |

---

## API 接口

## 1. 用户管理

### 1.1 用户注册

创建新用户账号。

**接口地址:** `POST /api/auth/register`

**请求参数:**

```json
{
  "email": "user@example.com",
  "password": "SecurePass123!",
  "name": "张三",
  "phone": "13800138000"
}
```

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| email | string | 是 | 邮箱地址，唯一 |
| password | string | 是 | 密码，至少8位 |
| name | string | 是 | 用户姓名 |
| phone | string | 否 | 手机号码 |

**响应示例:**

```json
{
  "success": true,
  "data": {
    "user": {
      "id": "uuid-1234",
      "email": "user@example.com",
      "name": "张三",
      "avatar": "https://api.dicebear.com/7.x/avataaars/svg?seed=user",
      "createdAt": "2025-11-11T12:00:00Z"
    },
    "tokens": {
      "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
      "refreshToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
      "expiresIn": 3600
    }
  }
}
```

---

### 1.2 用户登录

用户登录获取访问令牌。

**接口地址:** `POST /api/auth/login`

**请求参数:**

```json
{
  "email": "user@example.com",
  "password": "SecurePass123!"
}
```

**响应示例:**

```json
{
  "success": true,
  "data": {
    "user": {
      "id": "uuid-1234",
      "email": "user@example.com",
      "name": "张三",
      "avatar": "https://...",
      "membershipLevel": "premium"
    },
    "tokens": {
      "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
      "refreshToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
      "expiresIn": 3600
    }
  }
}
```

---

### 1.3 刷新 Token

使用 Refresh Token 获取新的 Access Token。

**接口地址:** `POST /api/auth/refresh`

**请求参数:**

```json
{
  "refreshToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

**响应示例:**

```json
{
  "success": true,
  "data": {
    "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "expiresIn": 3600
  }
}
```

---

### 1.4 退出登录

**接口地址:** `POST /api/auth/logout`

**认证:** 需要

**响应示例:**

```json
{
  "success": true,
  "message": "退出成功"
}
```

---

### 1.5 获取用户信息

获取当前登录用户的详细信息。

**接口地址:** `GET /api/user/profile`

**认证:** 需要

**响应示例:**

```json
{
  "success": true,
  "data": {
    "id": "uuid-1234",
    "email": "user@example.com",
    "name": "张三",
    "avatar": "https://...",
    "phone": "13800138000",
    "bio": "连续创业者，关注 AI 和 SaaS 领域",
    "company": "创新科技有限公司",
    "position": "CEO",
    "membershipLevel": "premium",
    "membershipExpiry": "2026-12-31T23:59:59Z",
    "stats": {
      "projects": 3,
      "connections": 156,
      "events": 12,
      "favorites": 45
    },
    "createdAt": "2024-01-01T00:00:00Z",
    "updatedAt": "2025-11-11T12:00:00Z"
  }
}
```

---

### 1.6 更新用户信息

**接口地址:** `PUT /api/user/profile`

**认证:** 需要

**请求参数:**

```json
{
  "name": "张三丰",
  "bio": "更新后的个人简介",
  "company": "新公司名称",
  "position": "CTO",
  "phone": "13900139000"
}
```

**响应示例:**

```json
{
  "success": true,
  "data": {
    "id": "uuid-1234",
    "name": "张三丰",
    "bio": "更新后的个人简介",
    "updatedAt": "2025-11-11T12:30:00Z"
  },
  "message": "信息更新成功"
}
```

---

### 1.7 上传头像

**接口地址:** `POST /api/user/avatar`

**认证:** 需要

**Content-Type:** `multipart/form-data`

**请求参数:**

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| avatar | file | 是 | 图片文件（JPG/PNG，最大5MB） |

**响应示例:**

```json
{
  "success": true,
  "data": {
    "avatar": "https://cdn.superclub.com/avatars/uuid-1234.jpg",
    "updatedAt": "2025-11-11T12:00:00Z"
  }
}
```

---

### 1.8 获取收藏列表

**接口地址:** `GET /api/user/favorites`

**认证:** 需要

**查询参数:**

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| type | string | 否 | 收藏类型: talent/project/event/content |
| page | integer | 否 | 页码，默认1 |
| limit | integer | 否 | 每页数量，默认20 |

**响应示例:**

```json
{
  "success": true,
  "data": {
    "items": [
      {
        "id": "fav-1",
        "type": "talent",
        "resourceId": "talent-123",
        "resource": {
          "id": "talent-123",
          "name": "李若彤",
          "role": "增长产品负责人"
        },
        "createdAt": "2025-11-10T10:00:00Z"
      }
    ],
    "pagination": {
      "page": 1,
      "limit": 20,
      "total": 45,
      "totalPages": 3
    }
  }
}
```

---

### 1.9 添加收藏

**接口地址:** `POST /api/user/favorites`

**认证:** 需要

**请求参数:**

```json
{
  "type": "talent",
  "resourceId": "talent-123"
}
```

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| type | string | 是 | 资源类型: talent/project/event/content |
| resourceId | string | 是 | 资源ID |

**响应示例:**

```json
{
  "success": true,
  "data": {
    "id": "fav-1",
    "type": "talent",
    "resourceId": "talent-123",
    "createdAt": "2025-11-11T12:00:00Z"
  },
  "message": "收藏成功"
}
```

---

### 1.10 取消收藏

**接口地址:** `DELETE /api/user/favorites/{favoriteId}`

**认证:** 需要

**响应示例:**

```json
{
  "success": true,
  "message": "已取消收藏"
}
```

---

## 2. 人才库

### 2.1 获取人才列表

获取人才库列表，支持筛选和分页。

**接口地址:** `GET /api/talents`

**认证:** 需要

**查询参数:**

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| field | string | 否 | 擅长领域（增长/品牌/产品等） |
| city | string | 否 | 所在城市 |
| search | string | 否 | 搜索关键词（姓名/公司/标签） |
| page | integer | 否 | 页码，默认1 |
| limit | integer | 否 | 每页数量，默认20，最大100 |
| sort | string | 否 | 排序方式: latest/followers/experience |

**请求示例:**

```http
GET /api/talents?field=增长&city=上海&page=1&limit=20&sort=followers
```

**响应示例:**

```json
{
  "success": true,
  "data": {
    "items": [
      {
        "id": "talent-123",
        "name": "李若彤",
        "role": "增长产品负责人",
        "company": "酷玩科技",
        "location": "上海",
        "avatar": "https://images.unsplash.com/photo-1494790108377-be9c29b29330",
        "description": "连续操盘 3 款出海工具产品，成功将 DAU 从 0 提升至 50w+。擅长冷启动与数据驱动增长策略。",
        "tags": ["冷启动", "出海", "数据驱动"],
        "stats": {
          "projects": "12",
          "experience": "8年",
          "followers": "3.4k"
        },
        "verified": true,
        "available": true,
        "createdAt": "2025-01-15T10:00:00Z"
      },
      {
        "id": "talent-124",
        "name": "王建国",
        "role": "品牌营销专家",
        "company": "星辰传媒",
        "location": "北京",
        "avatar": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e",
        "description": "10年品牌营销经验，服务过50+知名品牌，擅长品牌定位与整合营销。",
        "tags": ["品牌定位", "整合营销", "创意策划"],
        "stats": {
          "projects": "50+",
          "experience": "10年",
          "followers": "5.2k"
        },
        "verified": true,
        "available": false,
        "createdAt": "2025-02-20T14:30:00Z"
      }
    ],
    "pagination": {
      "page": 1,
      "limit": 20,
      "total": 368,
      "totalPages": 19
    },
    "filters": {
      "availableFields": ["增长", "品牌", "产品", "销售", "技术", "运营", "财务", "人力"],
      "availableCities": ["北京", "上海", "深圳", "杭州", "广州", "成都"]
    }
  }
}
```

---

### 2.2 获取人才详情

**接口地址:** `GET /api/talents/{talentId}`

**认证:** 需要

**响应示例:**

```json
{
  "success": true,
  "data": {
    "id": "talent-123",
    "name": "李若彤",
    "role": "增长产品负责人",
    "company": "酷玩科技",
    "location": "上海",
    "avatar": "https://...",
    "bio": "连续操盘 3 款出海工具产品，成功将 DAU 从 0 提升至 50w+。擅长冷启动与数据驱动增长策略。",
    "tags": ["冷启动", "出海", "数据驱动"],
    "stats": {
      "projects": "12",
      "experience": "8年",
      "followers": "3.4k"
    },
    "verified": true,
    "available": true,
    "skills": [
      {
        "name": "增长黑客",
        "level": "expert"
      },
      {
        "name": "数据分析",
        "level": "advanced"
      }
    ],
    "projects": [
      {
        "id": "proj-1",
        "name": "酷玩社区",
        "role": "增长负责人",
        "period": "2023.01 - 2025.03",
        "achievement": "DAU 从 0 到 50w+，留存率提升 40%"
      }
    ],
    "education": [
      {
        "school": "清华大学",
        "degree": "硕士",
        "major": "计算机科学",
        "period": "2013 - 2015"
      }
    ],
    "contact": {
      "wechat": "lrt_growth",
      "email": "lrt@example.com",
      "linkedin": "https://linkedin.com/in/lrt"
    },
    "createdAt": "2025-01-15T10:00:00Z",
    "updatedAt": "2025-11-10T18:00:00Z"
  }
}
```

---

### 2.3 获取精选人才

获取本周焦点人才（首页展示）。

**接口地址:** `GET /api/talents/featured`

**认证:** 可选

**查询参数:**

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| limit | integer | 否 | 数量，默认3 |

**响应示例:**

```json
{
  "success": true,
  "data": {
    "items": [
      {
        "id": "talent-123",
        "name": "李若彤",
        "role": "增长产品负责人",
        "company": "酷玩科技",
        "location": "上海",
        "avatar": "https://...",
        "description": "连续操盘 3 款出海工具产品...",
        "tags": ["冷启动", "出海", "数据驱动"],
        "stats": {
          "projects": "12",
          "experience": "8年",
          "followers": "3.4k"
        }
      }
    ]
  }
}
```

---

### 2.4 邀约人才

向人才发送邀约请求。

**接口地址:** `POST /api/talents/{talentId}/invite`

**认证:** 需要

**请求参数:**

```json
{
  "message": "您好，我对您的增长经验很感兴趣，希望能约个时间交流一下。",
  "preferredDate": "2025-11-15T14:00:00Z",
  "topic": "增长策略咨询",
  "duration": 60
}
```

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| message | string | 是 | 邀约留言 |
| preferredDate | string | 否 | 期望时间（ISO 8601） |
| topic | string | 否 | 交流主题 |
| duration | integer | 否 | 时长（分钟），默认60 |

**响应示例:**

```json
{
  "success": true,
  "data": {
    "invitationId": "inv-456",
    "talentId": "talent-123",
    "status": "pending",
    "message": "您好，我对您的增长经验很感兴趣...",
    "createdAt": "2025-11-11T12:00:00Z"
  },
  "message": "邀约已发送，请等待对方回复"
}
```

---

### 2.5 获取人才统计

获取人才库总体统计数据。

**接口地址:** `GET /api/talents/stats`

**认证:** 可选

**响应示例:**

```json
{
  "success": true,
  "data": {
    "totalTalents": 368,
    "totalTracks": 29,
    "activeInvitations": 142,
    "fieldDistribution": {
      "增长": 68,
      "品牌": 52,
      "产品": 74,
      "技术": 89,
      "销售": 45,
      "其他": 40
    },
    "cityDistribution": {
      "北京": 120,
      "上海": 98,
      "深圳": 76,
      "杭州": 42,
      "其他": 32
    }
  }
}
```

---

## 3. 项目资源库

### 3.1 获取项目列表

**接口地址:** `GET /api/projects`

**认证:** 需要

**查询参数:**

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| category | string | 否 | 需求分类（消费/企业服务/文娱/教育/AI等） |
| search | string | 否 | 搜索关键词 |
| page | integer | 否 | 页码，默认1 |
| limit | integer | 否 | 每页数量，默认20 |
| sort | string | 否 | 排序: latest/popular |

**请求示例:**

```http
GET /api/projects?category=AI&search=情绪&page=1&limit=20
```

**响应示例:**

```json
{
  "success": true,
  "data": {
    "items": [
      {
        "id": "proj-1",
        "name": "Mindee",
        "type": "SaaS · 客户运营",
        "description": "首创"24小时贴身情绪AI伙伴"，陪伴一监测一干预一成长全流程守护。需要算力、服务商、线下运营咨询、医院、资质等方向的合作。",
        "logo": "https://images.unsplash.com/photo-1633332755192-727a05c4013d",
        "tags": ["情绪AI陪护", "智能硬件", "服务商合作"],
        "category": "AI",
        "status": "recruiting",
        "owner": {
          "id": "user-789",
          "name": "张创业",
          "company": "Mindee"
        },
        "stats": {
          "views": 1234,
          "interests": 56
        },
        "createdAt": "2025-10-15T10:00:00Z",
        "updatedAt": "2025-11-10T15:30:00Z"
      },
      {
        "id": "proj-2",
        "name": "掌乐",
        "type": "硬件 · 渠道拓展",
        "description": "智能钢琴陪练硬件，AI实时纠错+趣味化教学。寻求教育机构、乐器店等渠道合作伙伴。",
        "logo": "https://images.unsplash.com/photo-1558618666-fcd25c85cd64",
        "tags": ["音乐教育", "智能硬件", "渠道合作"],
        "category": "教育",
        "status": "active",
        "owner": {
          "id": "user-790",
          "name": "李音乐",
          "company": "掌乐科技"
        },
        "stats": {
          "views": 892,
          "interests": 34
        },
        "createdAt": "2025-09-20T14:00:00Z",
        "updatedAt": "2025-11-08T09:15:00Z"
      }
    ],
    "pagination": {
      "page": 1,
      "limit": 20,
      "total": 87,
      "totalPages": 5
    },
    "filters": {
      "categories": ["不限", "消费", "企业服务", "文娱", "教育", "AI", "品牌", "渠道", "资本", "产业链"]
    }
  }
}
```

---

### 3.2 获取项目详情

**接口地址:** `GET /api/projects/{projectId}`

**认证:** 需要

**响应示例:**

```json
{
  "success": true,
  "data": {
    "id": "proj-1",
    "name": "Mindee",
    "type": "SaaS · 客户运营",
    "description": "首创"24小时贴身情绪AI伙伴"，陪伴一监测一干预一成长全流程守护。",
    "fullDescription": "详细的项目介绍...",
    "logo": "https://...",
    "coverImage": "https://...",
    "tags": ["情绪AI陪护", "智能硬件", "服务商合作"],
    "category": "AI",
    "status": "recruiting",
    "owner": {
      "id": "user-789",
      "name": "张创业",
      "avatar": "https://...",
      "company": "Mindee",
      "position": "CEO"
    },
    "needs": [
      {
        "type": "算力",
        "description": "需要GPU算力支持"
      },
      {
        "type": "服务商",
        "description": "寻找情绪识别技术服务商"
      }
    ],
    "milestones": [
      {
        "date": "2024-01-01",
        "title": "产品上线",
        "description": "完成MVP版本开发并上线"
      }
    ],
    "team": [
      {
        "name": "张创业",
        "role": "CEO",
        "avatar": "https://..."
      }
    ],
    "stats": {
      "views": 1234,
      "interests": 56,
      "collaborations": 8
    },
    "contact": {
      "email": "contact@mindee.com",
      "wechat": "mindee_official"
    },
    "createdAt": "2025-10-15T10:00:00Z",
    "updatedAt": "2025-11-10T15:30:00Z"
  }
}
```

---

### 3.3 发布项目

发布新的项目需求。

**接口地址:** `POST /api/projects`

**认证:** 需要

**请求参数:**

```json
{
  "name": "项目名称",
  "type": "SaaS · 客户运营",
  "description": "项目简介，不超过200字",
  "fullDescription": "项目详细介绍",
  "category": "AI",
  "tags": ["标签1", "标签2", "标签3"],
  "needs": [
    {
      "type": "算力",
      "description": "需求详情"
    }
  ],
  "contact": {
    "email": "contact@example.com",
    "wechat": "wechat_id"
  }
}
```

**响应示例:**

```json
{
  "success": true,
  "data": {
    "id": "proj-123",
    "name": "项目名称",
    "status": "pending_review",
    "createdAt": "2025-11-11T12:00:00Z"
  },
  "message": "项目已提交，审核通过后将展示"
}
```

---

### 3.4 更新项目

**接口地址:** `PUT /api/projects/{projectId}`

**认证:** 需要（仅项目所有者）

**请求参数:** 同发布项目

**响应示例:**

```json
{
  "success": true,
  "data": {
    "id": "proj-123",
    "name": "更新后的项目名称",
    "updatedAt": "2025-11-11T12:30:00Z"
  },
  "message": "项目信息已更新"
}
```

---

### 3.5 删除项目

**接口地址:** `DELETE /api/projects/{projectId}`

**认证:** 需要（仅项目所有者）

**响应示例:**

```json
{
  "success": true,
  "message": "项目已删除"
}
```

---

### 3.6 表达合作意向

**接口地址:** `POST /api/projects/{projectId}/interest`

**认证:** 需要

**请求参数:**

```json
{
  "message": "我对贵项目的AI技术很感兴趣，希望能进一步了解合作机会。",
  "capability": "我们提供GPU算力服务，有丰富的AI项目合作经验。",
  "contact": {
    "name": "李合作",
    "phone": "13800138000",
    "email": "lihezuo@example.com"
  }
}
```

**响应示例:**

```json
{
  "success": true,
  "data": {
    "interestId": "int-456",
    "projectId": "proj-123",
    "status": "pending",
    "createdAt": "2025-11-11T12:00:00Z"
  },
  "message": "合作意向已提交"
}
```

---

## 4. 活动管理

### 4.1 获取活动列表

**接口地址:** `GET /api/events`

**认证:** 可选

**查询参数:**

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| status | string | 否 | 活动状态: all/upcoming/past |
| category | string | 否 | 活动分类 |
| page | integer | 否 | 页码 |
| limit | integer | 否 | 每页数量，默认12 |

**请求示例:**

```http
GET /api/events?status=upcoming&page=1&limit=12
```

**响应示例:**

```json
{
  "success": true,
  "data": {
    "items": [
      {
        "id": "event-1",
        "title": "消费品牌出海空中路演 Demo Day | 线上开放麦",
        "description": "亮相你的出海消费品牌，找用户、找合作、找投资。免费报名，创始人优先。",
        "cover": "https://images.unsplash.com/photo-1540575467063-178a50c2df87",
        "date": "2025-11-28T19:30:00Z",
        "endDate": "2025-11-28T21:30:00Z",
        "location": "线上",
        "locationType": "online",
        "category": "路演",
        "status": "upcoming",
        "capacity": 200,
        "registered": 87,
        "speakers": [
          {
            "id": "speaker-1",
            "name": "张导师",
            "title": "出海专家",
            "avatar": "https://..."
          }
        ],
        "tags": ["出海", "消费品牌", "Demo Day"],
        "organizer": {
          "name": "Super Club",
          "logo": "https://..."
        },
        "price": 0,
        "createdAt": "2025-10-20T10:00:00Z"
      },
      {
        "id": "event-2",
        "title": "AI 创业者闭门交流会 | 北京站",
        "description": "聚焦AI创业实战经验分享，限30人深度交流。",
        "cover": "https://images.unsplash.com/photo-1591115765373-5207764f72e7",
        "date": "2025-12-05T14:00:00Z",
        "endDate": "2025-12-05T18:00:00Z",
        "location": "北京·朝阳区",
        "locationType": "offline",
        "address": "北京市朝阳区建国路88号SOHO现代城",
        "category": "闭门会",
        "status": "upcoming",
        "capacity": 30,
        "registered": 28,
        "speakers": [
          {
            "id": "speaker-2",
            "name": "李AI",
            "title": "AI创业者",
            "avatar": "https://..."
          }
        ],
        "tags": ["AI", "创业", "闭门会"],
        "organizer": {
          "name": "Super Club",
          "logo": "https://..."
        },
        "price": 199,
        "createdAt": "2025-10-25T15:00:00Z"
      }
    ],
    "pagination": {
      "page": 1,
      "limit": 12,
      "total": 36,
      "totalPages": 3
    },
    "stats": {
      "totalSpeakers": "200+",
      "totalFounders": "6000+",
      "upcomingEvents": 8
    }
  }
}
```

---

### 4.2 获取活动详情

**接口地址:** `GET /api/events/{eventId}`

**认证:** 可选

**响应示例:**

```json
{
  "success": true,
  "data": {
    "id": "event-1",
    "title": "消费品牌出海空中路演 Demo Day | 线上开放麦",
    "description": "亮相你的出海消费品牌，找用户、找合作、找投资。",
    "fullDescription": "详细活动介绍...",
    "cover": "https://...",
    "date": "2025-11-28T19:30:00Z",
    "endDate": "2025-11-28T21:30:00Z",
    "location": "线上",
    "locationType": "online",
    "meetingLink": "https://zoom.us/j/123456789",
    "category": "路演",
    "status": "upcoming",
    "capacity": 200,
    "registered": 87,
    "agenda": [
      {
        "time": "19:30",
        "title": "开场致辞",
        "speaker": "主持人"
      },
      {
        "time": "19:45",
        "title": "项目路演（1）",
        "speaker": "创业者A"
      }
    ],
    "speakers": [
      {
        "id": "speaker-1",
        "name": "张导师",
        "title": "出海专家",
        "avatar": "https://...",
        "bio": "10年出海经验..."
      }
    ],
    "tags": ["出海", "消费品牌", "Demo Day"],
    "organizer": {
      "id": "org-1",
      "name": "Super Club",
      "logo": "https://...",
      "contact": "events@superclub.com"
    },
    "price": 0,
    "requirements": "创始人或联合创始人优先",
    "benefits": [
      "获得投资人反馈",
      "认识同行创业者",
      "免费曝光机会"
    ],
    "isRegistered": false,
    "createdAt": "2025-10-20T10:00:00Z",
    "updatedAt": "2025-11-10T16:00:00Z"
  }
}
```

---

### 4.3 报名活动

**接口地址:** `POST /api/events/{eventId}/register`

**认证:** 需要

**请求参数:**

```json
{
  "attendeeInfo": {
    "name": "张三",
    "phone": "13800138000",
    "email": "zhangsan@example.com",
    "company": "创新科技",
    "position": "CEO"
  },
  "note": "期待参加此次活动",
  "questions": [
    {
      "question": "您对哪个议题最感兴趣？",
      "answer": "AI创业实战经验"
    }
  ]
}
```

**响应示例:**

```json
{
  "success": true,
  "data": {
    "registrationId": "reg-789",
    "eventId": "event-1",
    "status": "confirmed",
    "qrCode": "https://cdn.superclub.com/qr/reg-789.png",
    "meetingLink": "https://zoom.us/j/123456789",
    "createdAt": "2025-11-11T12:00:00Z"
  },
  "message": "报名成功！活动前将发送提醒通知"
}
```

---

### 4.4 取消报名

**接口地址:** `DELETE /api/events/{eventId}/register`

**认证:** 需要

**响应示例:**

```json
{
  "success": true,
  "message": "已取消报名"
}
```

---

### 4.5 获取我的活动

获取当前用户报名的活动列表。

**接口地址:** `GET /api/events/my-events`

**认证:** 需要

**查询参数:**

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| status | string | 否 | upcoming/past/all |
| page | integer | 否 | 页码 |
| limit | integer | 否 | 每页数量 |

**响应示例:**

```json
{
  "success": true,
  "data": {
    "items": [
      {
        "registration": {
          "id": "reg-789",
          "status": "confirmed",
          "registeredAt": "2025-11-11T12:00:00Z"
        },
        "event": {
          "id": "event-1",
          "title": "消费品牌出海空中路演 Demo Day",
          "date": "2025-11-28T19:30:00Z",
          "location": "线上",
          "cover": "https://..."
        }
      }
    ],
    "pagination": {
      "page": 1,
      "limit": 20,
      "total": 12,
      "totalPages": 1
    }
  }
}
```

---

### 4.6 获取轮播图

获取活动页面的 Hero 轮播图数据。

**接口地址:** `GET /api/events/carousel`

**认证:** 可选

**响应示例:**

```json
{
  "success": true,
  "data": {
    "slides": [
      {
        "id": "slide-1",
        "image": "https://images.unsplash.com/photo-1540575467063-178a50c2df87",
        "title": "Super Club 创业者社区",
        "subtitle": "连接优秀创业者",
        "link": "/events/featured",
        "order": 1
      },
      {
        "id": "slide-2",
        "image": "https://images.unsplash.com/photo-1591115765373-5207764f72e7",
        "title": "每周精彩活动",
        "subtitle": "200+ 分享嘉宾，6000+ 创始人",
        "link": "/events",
        "order": 2
      },
      {
        "id": "slide-3",
        "image": "https://images.unsplash.com/photo-1505373877841-8d25f7d46678",
        "title": "免费参与路演",
        "subtitle": "找用户、找合作、找投资",
        "link": "/events/demo-day",
        "order": 3
      }
    ]
  }
}
```

---

## 5. 社区网络

### 5.1 获取社区成员列表

**接口地址:** `GET /api/links`

**认证:** 需要

**查询参数:**

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| category | string | 否 | 分类标签 |
| search | string | 否 | 搜索关键词 |
| page | integer | 否 | 页码 |
| limit | integer | 否 | 每页数量，默认20 |

**请求示例:**

```http
GET /api/links?category=消费&search=品牌&page=1&limit=20
```

**响应示例:**

```json
{
  "success": true,
  "data": {
    "items": [
      {
        "id": "link-1",
        "user": {
          "id": "user-123",
          "name": "张小美",
          "avatar": "https://images.unsplash.com/photo-1494790108377-be9c29b29330",
          "company": "美丽消费",
          "position": "创始人"
        },
        "bio": "专注美妆个护赛道，2年内打造3个爆款产品，总GMV突破5000万。",
        "tags": ["消费", "美妆", "品牌运营"],
        "stats": {
          "connections": 234,
          "posts": 45,
          "influence": "高"
        },
        "status": "online",
        "verified": true,
        "createdAt": "2025-06-15T10:00:00Z"
      },
      {
        "id": "link-2",
        "user": {
          "id": "user-124",
          "name": "李技术",
          "avatar": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e",
          "company": "云端科技",
          "position": "CTO"
        },
        "bio": "10年技术研发经验，擅长云计算和大数据架构。",
        "tags": ["技术", "云计算", "大数据"],
        "stats": {
          "connections": 567,
          "posts": 89,
          "influence": "高"
        },
        "status": "offline",
        "verified": true,
        "createdAt": "2025-05-20T14:00:00Z"
      }
    ],
    "pagination": {
      "page": 1,
      "limit": 20,
      "total": 156,
      "totalPages": 8
    },
    "filters": {
      "categories": ["不限", "消费", "文娱", "教育", "企服", "AI", "出海", "Web3", "硬件", "本地生活", "医疗健康", "社交", "金融科技", "新能源"]
    }
  }
}
```

---

### 5.2 建立连接

向其他用户发起连接请求。

**接口地址:** `POST /api/links/connect`

**认证:** 需要

**请求参数:**

```json
{
  "targetUserId": "user-123",
  "message": "您好，我对您的消费品牌经验很感兴趣，希望能建立连接。",
  "purpose": "business_cooperation"
}
```

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| targetUserId | string | 是 | 目标用户ID |
| message | string | 否 | 连接请求留言 |
| purpose | string | 否 | 连接目的: business_cooperation/learning/investment等 |

**响应示例:**

```json
{
  "success": true,
  "data": {
    "connectionId": "conn-456",
    "targetUserId": "user-123",
    "status": "pending",
    "createdAt": "2025-11-11T12:00:00Z"
  },
  "message": "连接请求已发送"
}
```

---

### 5.3 获取我的连接

**接口地址:** `GET /api/links/my-connections`

**认证:** 需要

**查询参数:**

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| status | string | 否 | 状态: all/connected/pending |
| page | integer | 否 | 页码 |
| limit | integer | 否 | 每页数量 |

**响应示例:**

```json
{
  "success": true,
  "data": {
    "items": [
      {
        "connectionId": "conn-456",
        "user": {
          "id": "user-123",
          "name": "张小美",
          "avatar": "https://...",
          "company": "美丽消费",
          "position": "创始人"
        },
        "status": "connected",
        "connectedAt": "2025-11-11T12:30:00Z",
        "mutualConnections": 12
      }
    ],
    "pagination": {
      "page": 1,
      "limit": 20,
      "total": 156,
      "totalPages": 8
    }
  }
}
```

---

### 5.4 接受/拒绝连接请求

**接口地址:** `PUT /api/links/connections/{connectionId}`

**认证:** 需要

**请求参数:**

```json
{
  "action": "accept"
}
```

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| action | string | 是 | accept/reject |

**响应示例:**

```json
{
  "success": true,
  "data": {
    "connectionId": "conn-456",
    "status": "connected",
    "updatedAt": "2025-11-11T12:00:00Z"
  },
  "message": "已接受连接请求"
}
```

---

### 5.5 获取轮播图

**接口地址:** `GET /api/links/carousel`

**认证:** 可选

**响应示例:**

```json
{
  "success": true,
  "data": {
    "slides": [
      {
        "id": "slide-1",
        "image": "https://images.unsplash.com/photo-1511632765486-a01980e01a18",
        "title": "Starter Network",
        "subtitle": "连接优秀创业者",
        "link": "/links",
        "order": 1
      }
    ]
  }
}
```

---

## 6. 内容库

### 6.1 获取内容卡片

获取 CEO 图书馆首页的内容卡片。

**接口地址:** `GET /api/content/cards`

**认证:** 可选

**查询参数:**

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| department | string | 否 | 部门筛选（战略部/品牌部等） |
| type | string | 否 | 内容类型（文章/视频/课程） |
| search | string | 否 | 搜索关键词 |
| page | integer | 否 | 页码 |
| limit | integer | 否 | 每页数量，默认4 |

**请求示例:**

```http
GET /api/content/cards?department=战略部&type=文章&page=1&limit=4
```

**响应示例:**

```json
{
  "success": true,
  "data": {
    "items": [
      {
        "id": "card-1",
        "title": "《别让猴子跳回背上》如何做一个合理的管理者(下)",
        "description": "作为管理者,你的贡献来自于你的判断力与影响力,而非你干了多少具体的活儿。本文通过"猴子"隐喻,教你如何避免成为下属问题的承担者...",
        "image": "https://images.unsplash.com/photo-1497366216548-37526070297c",
        "type": "article",
        "department": "战略部",
        "author": {
          "id": "author-1",
          "name": "管理大师",
          "avatar": "https://..."
        },
        "stats": {
          "views": 2345,
          "likes": 189,
          "comments": 23
        },
        "tags": ["管理", "领导力", "时间管理"],
        "publishedAt": "2025-11-05T10:00:00Z",
        "readingTime": 8
      },
      {
        "id": "card-2",
        "title": "品牌定位的底层逻辑",
        "description": "深入解析品牌定位的本质，从用户心智到市场竞争，构建清晰的品牌战略...",
        "image": "https://images.unsplash.com/photo-1552664730-d307ca884978",
        "type": "article",
        "department": "品牌部",
        "author": {
          "id": "author-2",
          "name": "品牌专家",
          "avatar": "https://..."
        },
        "stats": {
          "views": 1876,
          "likes": 145,
          "comments": 18
        },
        "tags": ["品牌", "定位", "营销"],
        "publishedAt": "2025-11-03T14:00:00Z",
        "readingTime": 12
      }
    ],
    "pagination": {
      "page": 1,
      "limit": 4,
      "total": 87,
      "totalPages": 22
    },
    "filters": {
      "departments": ["战略部", "品牌部", "销售部", "人力部", "财法部", "技术部"],
      "types": ["文章", "视频", "课程", "案例"]
    }
  }
}
```

---

### 6.2 获取文章列表

**接口地址:** `GET /api/content/articles`

**认证:** 可选

**查询参数:**

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| category | string | 否 | 分类 |
| tag | string | 否 | 标签 |
| page | integer | 否 | 页码 |
| limit | integer | 否 | 每页数量 |

**响应示例:**

```json
{
  "success": true,
  "data": {
    "items": [
      {
        "id": "article-1",
        "title": "《别让猴子跳回背上》如何做一个合理的管理者",
        "excerpt": "作为管理者,你的贡献来自于你的判断力与影响力...",
        "coverImage": "https://...",
        "author": {
          "id": "author-1",
          "name": "管理大师",
          "avatar": "https://..."
        },
        "department": "战略部",
        "tags": ["管理", "领导力"],
        "stats": {
          "views": 2345,
          "likes": 189,
          "comments": 23
        },
        "publishedAt": "2025-11-05T10:00:00Z",
        "readingTime": 8
      }
    ],
    "pagination": {
      "page": 1,
      "limit": 20,
      "total": 156,
      "totalPages": 8
    }
  }
}
```

---

### 6.3 获取文章详情

**接口地址:** `GET /api/content/articles/{articleId}`

**认证:** 可选

**响应示例:**

```json
{
  "success": true,
  "data": {
    "id": "article-1",
    "title": "《别让猴子跳回背上》如何做一个合理的管理者",
    "content": "文章完整内容，支持 Markdown 格式...",
    "coverImage": "https://...",
    "author": {
      "id": "author-1",
      "name": "管理大师",
      "avatar": "https://...",
      "bio": "资深管理顾问"
    },
    "department": "战略部",
    "tags": ["管理", "领导力", "时间管理"],
    "stats": {
      "views": 2345,
      "likes": 189,
      "comments": 23,
      "favorites": 67
    },
    "publishedAt": "2025-11-05T10:00:00Z",
    "updatedAt": "2025-11-05T10:00:00Z",
    "readingTime": 8,
    "relatedArticles": [
      {
        "id": "article-2",
        "title": "相关文章标题",
        "coverImage": "https://..."
      }
    ],
    "isFavorited": false,
    "isLiked": false
  }
}
```

---

### 6.4 点赞文章

**接口地址:** `POST /api/content/articles/{articleId}/like`

**认证:** 需要

**响应示例:**

```json
{
  "success": true,
  "data": {
    "articleId": "article-1",
    "isLiked": true,
    "totalLikes": 190
  },
  "message": "点赞成功"
}
```

---

### 6.5 取消点赞

**接口地址:** `DELETE /api/content/articles/{articleId}/like`

**认证:** 需要

**响应示例:**

```json
{
  "success": true,
  "data": {
    "articleId": "article-1",
    "isLiked": false,
    "totalLikes": 189
  },
  "message": "已取消点赞"
}
```

---

### 6.6 评论文章

**接口地址:** `POST /api/content/articles/{articleId}/comments`

**认证:** 需要

**请求参数:**

```json
{
  "content": "非常有启发的文章，感谢分享！",
  "parentId": null
}
```

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| content | string | 是 | 评论内容 |
| parentId | string | 否 | 父评论ID（回复评论时使用） |

**响应示例:**

```json
{
  "success": true,
  "data": {
    "id": "comment-1",
    "content": "非常有启发的文章，感谢分享！",
    "author": {
      "id": "user-123",
      "name": "张三",
      "avatar": "https://..."
    },
    "createdAt": "2025-11-11T12:00:00Z"
  },
  "message": "评论成功"
}
```

---

### 6.7 获取评论列表

**接口地址:** `GET /api/content/articles/{articleId}/comments`

**认证:** 可选

**查询参数:**

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| page | integer | 否 | 页码 |
| limit | integer | 否 | 每页数量 |
| sort | string | 否 | 排序: latest/hot |

**响应示例:**

```json
{
  "success": true,
  "data": {
    "items": [
      {
        "id": "comment-1",
        "content": "非常有启发的文章，感谢分享！",
        "author": {
          "id": "user-123",
          "name": "张三",
          "avatar": "https://..."
        },
        "likes": 12,
        "replies": [
          {
            "id": "comment-2",
            "content": "同感！",
            "author": {
              "id": "user-124",
              "name": "李四",
              "avatar": "https://..."
            },
            "createdAt": "2025-11-11T12:15:00Z"
          }
        ],
        "createdAt": "2025-11-11T12:00:00Z"
      }
    ],
    "pagination": {
      "page": 1,
      "limit": 20,
      "total": 23,
      "totalPages": 2
    }
  }
}
```

---

## 数据模型

### User (用户)

```typescript
interface User {
  id: string
  email: string
  name: string
  avatar: string
  phone?: string
  bio?: string
  company?: string
  position?: string
  membershipLevel: 'free' | 'premium' | 'vip'
  membershipExpiry?: string
  stats: {
    projects: number
    connections: number
    events: number
    favorites: number
  }
  verified: boolean
  createdAt: string
  updatedAt: string
}
```

### Talent (人才)

```typescript
interface Talent {
  id: string
  name: string
  role: string
  company: string
  location: string
  avatar: string
  description: string
  bio?: string
  tags: string[]
  stats: {
    projects: string
    experience: string
    followers: string
  }
  verified: boolean
  available: boolean
  skills?: Skill[]
  projects?: Project[]
  education?: Education[]
  contact?: Contact
  createdAt: string
  updatedAt: string
}
```

### Project (项目)

```typescript
interface Project {
  id: string
  name: string
  type: string
  description: string
  fullDescription?: string
  logo: string
  coverImage?: string
  tags: string[]
  category: string
  status: 'active' | 'recruiting' | 'paused' | 'completed'
  owner: {
    id: string
    name: string
    avatar?: string
    company: string
    position?: string
  }
  needs?: Need[]
  milestones?: Milestone[]
  team?: TeamMember[]
  stats: {
    views: number
    interests: number
    collaborations?: number
  }
  contact?: Contact
  createdAt: string
  updatedAt: string
}
```

### Event (活动)

```typescript
interface Event {
  id: string
  title: string
  description: string
  fullDescription?: string
  cover: string
  date: string
  endDate: string
  location: string
  locationType: 'online' | 'offline'
  address?: string
  meetingLink?: string
  category: string
  status: 'upcoming' | 'ongoing' | 'past' | 'cancelled'
  capacity: number
  registered: number
  agenda?: AgendaItem[]
  speakers: Speaker[]
  tags: string[]
  organizer: Organizer
  price: number
  requirements?: string
  benefits?: string[]
  isRegistered?: boolean
  createdAt: string
  updatedAt: string
}
```

### Content (内容)

```typescript
interface Content {
  id: string
  title: string
  description?: string
  excerpt?: string
  content?: string
  image?: string
  coverImage?: string
  type: 'article' | 'video' | 'course' | 'case'
  department: string
  author: {
    id: string
    name: string
    avatar?: string
    bio?: string
  }
  tags: string[]
  stats: {
    views: number
    likes: number
    comments: number
    favorites?: number
  }
  publishedAt: string
  updatedAt?: string
  readingTime?: number
  relatedArticles?: Content[]
  isFavorited?: boolean
  isLiked?: boolean
}
```

---

## 状态码说明

### HTTP 状态码

| 状态码 | 说明 |
|--------|------|
| 200 OK | 请求成功 |
| 201 Created | 资源创建成功 |
| 204 No Content | 请求成功，无返回内容 |
| 400 Bad Request | 请求参数错误 |
| 401 Unauthorized | 未授权，需要登录 |
| 403 Forbidden | 禁止访问，权限不足 |
| 404 Not Found | 资源不存在 |
| 409 Conflict | 资源冲突（如重复创建） |
| 422 Unprocessable Entity | 数据验证失败 |
| 429 Too Many Requests | 请求过于频繁 |
| 500 Internal Server Error | 服务器内部错误 |
| 503 Service Unavailable | 服务不可用 |

### 业务状态码

在响应的 `error.code` 字段中返回：

| 业务码 | 说明 |
|--------|------|
| `USER_NOT_FOUND` | 用户不存在 |
| `INVALID_CREDENTIALS` | 用户名或密码错误 |
| `EMAIL_ALREADY_EXISTS` | 邮箱已被注册 |
| `TOKEN_EXPIRED` | Token 已过期 |
| `TOKEN_INVALID` | Token 无效 |
| `INSUFFICIENT_PERMISSIONS` | 权限不足 |
| `RESOURCE_NOT_FOUND` | 资源不存在 |
| `DUPLICATE_RESOURCE` | 资源重复 |
| `VALIDATION_ERROR` | 数据验证失败 |
| `CAPACITY_FULL` | 活动人数已满 |
| `ALREADY_REGISTERED` | 已经报名过 |
| `ALREADY_CONNECTED` | 已经建立连接 |
| `RATE_LIMIT_EXCEEDED` | 超过请求频率限制 |

---

## 附录

### 分页参数说明

所有列表接口均支持分页参数：

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| page | integer | 1 | 当前页码，从1开始 |
| limit | integer | 20 | 每页数量，最大100 |

### 排序参数说明

部分接口支持排序参数：

| 值 | 说明 |
|----|------|
| latest | 最新优先 |
| popular | 热门优先 |
| followers | 关注数优先 |
| experience | 经验优先 |

### 时间格式

所有时间字段使用 ISO 8601 格式：

```
2025-11-11T19:30:00Z
```

### 文件上传限制

| 文件类型 | 最大大小 | 支持格式 |
|---------|---------|---------|
| 头像 | 5MB | JPG, PNG, GIF |
| 项目Logo | 2MB | JPG, PNG |
| 活动封面 | 5MB | JPG, PNG |

### 速率限制

| 用户等级 | 请求限制 |
|---------|---------|
| 免费用户 | 100次/小时 |
| Premium用户 | 500次/小时 |
| VIP用户 | 2000次/小时 |

超过限制后返回 `429 Too Many Requests` 状态码。

---

**文档版本:** v1.0.0
**更新日期:** 2025-11-11
**维护团队:** Super Club 后端开发团队
**联系邮箱:** dev@superclub.com
