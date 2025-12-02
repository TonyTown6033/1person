# Super Club API 后端服务

基于 FastAPI + PostgreSQL 实现的后端 API 服务，提供 Super Club 平台的所有接口功能。

## 技术栈

- **FastAPI**: 现代、快速的 Web 框架
- **PostgreSQL**: 关系型数据库
- **SQLAlchemy**: ORM 框架
- **JWT**: 用户认证
- **Pydantic**: 数据验证

## 项目结构

```
project/
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── auth.py          # 认证接口
│   │       ├── users.py          # 用户管理
│   │       ├── talents.py        # 人才库
│   │       ├── projects.py       # 项目资源库
│   │       ├── events.py         # 活动管理
│   │       ├── links.py          # 社区网络
│   │       └── content.py        # 内容库
│   ├── core/
│   │   ├── config.py             # 配置管理
│   │   ├── database.py           # 数据库连接
│   │   ├── security.py           # 安全相关（JWT、密码）
│   │   └── dependencies.py       # 依赖注入
│   ├── models/                   # 数据库模型
│   ├── schemas/                  # Pydantic 模型
│   └── main.py                   # 应用入口
├── docs/                         # API 文档
├── requirements.txt              # Python 依赖
├── .env                          # 环境变量
├── run.py                        # 开发启动脚本
├── init_db.py                    # 数据库初始化脚本
└── entrypoint.sh                 # 生产启动脚本
```

## 安装和运行

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置环境变量

编辑 `.env` 文件，设置数据库连接信息：

```env
DATABASE_URL=postgresql://postgres:tbrn2kq9@test-db-postgresql.ns-tmbwyn2v.svc:5432/postgres
SECRET_KEY=your-secret-key-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
REFRESH_TOKEN_EXPIRE_DAYS=7
```

### 3. 初始化数据库

```bash
python3 init_db.py
```

这将创建所有必要的数据库表。

### 4. 启动服务

**开发模式：**
```bash
python3 run.py
# 或
bash entrypoint.sh
```

**生产模式：**
```bash
bash entrypoint.sh production
```

服务将在 `http://localhost:8000` 启动。

### 5. 访问 API 文档

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API 接口

所有接口都遵循文档 `docs/API_DOCUMENTATION.md` 中定义的规范。

### 主要接口模块

1. **认证模块** (`/api/auth`)
   - POST `/api/auth/register` - 用户注册
   - POST `/api/auth/login` - 用户登录
   - POST `/api/auth/refresh` - 刷新令牌
   - POST `/api/auth/logout` - 退出登录

2. **用户管理** (`/api/user`)
   - GET `/api/user/profile` - 获取用户信息
   - PUT `/api/user/profile` - 更新用户信息
   - POST `/api/user/avatar` - 上传头像
   - GET `/api/user/favorites` - 获取收藏列表
   - POST `/api/user/favorites` - 添加收藏
   - DELETE `/api/user/favorites/{id}` - 取消收藏

3. **人才库** (`/api/talents`)
   - GET `/api/talents` - 获取人才列表
   - GET `/api/talents/{id}` - 获取人才详情
   - GET `/api/talents/featured` - 获取精选人才
   - POST `/api/talents/{id}/invite` - 邀约人才
   - GET `/api/talents/stats` - 获取人才统计

4. **项目资源库** (`/api/projects`)
   - GET `/api/projects` - 获取项目列表
   - GET `/api/projects/{id}` - 获取项目详情
   - POST `/api/projects` - 发布项目
   - PUT `/api/projects/{id}` - 更新项目
   - DELETE `/api/projects/{id}` - 删除项目
   - POST `/api/projects/{id}/interest` - 表达合作意向

5. **活动管理** (`/api/events`)
   - GET `/api/events` - 获取活动列表
   - GET `/api/events/{id}` - 获取活动详情
   - POST `/api/events/{id}/register` - 报名活动
   - DELETE `/api/events/{id}/register` - 取消报名
   - GET `/api/events/my-events` - 获取我的活动
   - GET `/api/events/carousel` - 获取轮播图

6. **社区网络** (`/api/links`)
   - GET `/api/links` - 获取社区成员列表
   - POST `/api/links/connect` - 建立连接
   - GET `/api/links/my-connections` - 获取我的连接
   - PUT `/api/links/connections/{id}` - 接受/拒绝连接
   - GET `/api/links/carousel` - 获取轮播图

7. **内容库** (`/api/content`)
   - GET `/api/content/cards` - 获取内容卡片
   - GET `/api/content/articles` - 获取文章列表
   - GET `/api/content/articles/{id}` - 获取文章详情
   - POST `/api/content/articles/{id}/like` - 点赞文章
   - DELETE `/api/content/articles/{id}/like` - 取消点赞
   - POST `/api/content/articles/{id}/comments` - 评论文章
   - GET `/api/content/articles/{id}/comments` - 获取评论列表

## 认证方式

大部分接口需要 JWT 认证。在请求头中添加：

```
Authorization: Bearer <your_access_token>
```

通过登录接口获取 `accessToken` 和 `refreshToken`。

## 响应格式

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
    "code": "ERROR_CODE",
    "message": "错误信息",
    "details": {}
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

## 数据库

数据库使用 PostgreSQL，所有表结构定义在 `app/models/` 目录下。

主要数据表：
- `users` - 用户表
- `talents` - 人才表
- `projects` - 项目表
- `events` - 活动表
- `contents` - 内容表
- `connections` - 连接表
- `favorites` - 收藏表
- `likes` - 点赞表
- `comments` - 评论表
- 等等...

## 开发说明

1. 所有接口都遵循 RESTful 规范
2. 使用 Pydantic 进行数据验证
3. 使用 SQLAlchemy ORM 进行数据库操作
4. JWT 用于用户认证
5. 支持分页、筛选、排序等功能

## 注意事项

1. 生产环境请修改 `.env` 中的 `SECRET_KEY`
2. 数据库连接信息请根据实际情况配置
3. 文件上传功能（如头像）需要配置存储服务
4. 部分统计功能使用了简化实现，可根据需求优化

## 测试

可以使用 FastAPI 自动生成的 Swagger UI 进行接口测试：
http://localhost:8000/docs

## 许可证

MIT License

