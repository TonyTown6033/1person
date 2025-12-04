# Super Club 测试指南

本文档介绍如何运行和编写项目的测试用例。

## 目录结构

```
1Person/
├── super_club/                 # 前端项目
│   ├── tests/
│   │   ├── setup.js           # 测试配置
│   │   ├── components/        # 组件测试
│   │   │   ├── ContentCard.spec.js
│   │   │   ├── ArticleItem.spec.js
│   │   │   └── Sidebar.spec.js
│   │   ├── api/               # API 测试
│   │   │   └── auth.spec.js
│   │   ├── utils/             # 工具函数测试
│   │   │   └── logger.spec.js
│   │   └── router/            # 路由测试
│   │       └── index.spec.js
│   └── vitest.config.js       # Vitest 配置
│
└── super_club_backend/         # 后端项目
    ├── tests/
    │   ├── conftest.py        # Pytest 配置
    │   ├── test_auth.py       # 认证测试
    │   ├── test_users.py      # 用户测试
    │   ├── test_content.py    # 内容测试
    │   ├── test_events.py     # 活动测试
    │   ├── test_health.py     # 健康检查测试
    │   ├── test_security.py   # 安全模块测试
    │   └── test_models.py     # 模型测试
    └── pytest.ini             # Pytest 配置
```

## 后端测试

### 环境准备

本项目使用 [uv](https://github.com/astral-sh/uv) 作为 Python 环境管理工具。

```bash
# 安装 uv（如果尚未安装）
curl -LsSf https://astral.sh/uv/install.sh | sh

# 或使用 Homebrew（macOS）
brew install uv
```

### 安装测试依赖

```bash
cd super_club_backend
uv sync
```

### 运行所有测试

```bash
cd super_club_backend
uv run pytest
```

### 运行特定测试文件

```bash
uv run pytest tests/test_auth.py
uv run pytest tests/test_users.py
uv run pytest tests/test_content.py
```

### 运行特定测试类或方法

```bash
# 运行测试类
uv run pytest tests/test_auth.py::TestLogin

# 运行单个测试
uv run pytest tests/test_auth.py::TestLogin::test_login_success
```

### 查看详细输出

```bash
uv run pytest -v
```

### 生成覆盖率报告

```bash
uv add pytest-cov --dev
uv run pytest --cov=app --cov-report=html
```

## 前端测试

### 安装测试依赖

```bash
cd super_club
npm install
```

### 运行所有测试

```bash
npm test
```

或运行一次性测试：

```bash
npm run test:run
```

### 运行特定测试文件

```bash
npx vitest tests/components/ContentCard.spec.js
```

### 监听模式

```bash
npm test
```

测试会在文件变更时自动重新运行。

### 生成覆盖率报告

```bash
npm run test:coverage
```

## 测试用例说明

### 后端测试

#### 认证测试 (test_auth.py)
- 用户注册（成功/重复邮箱/无效格式）
- 用户登录（成功/密码错误/用户不存在/账户禁用）
- 令牌刷新
- 用户登出

#### 用户测试 (test_users.py)
- 获取用户信息
- 更新用户资料
- 收藏功能（添加/删除/列表）

#### 内容测试 (test_content.py)
- 获取内容卡片（分页/筛选/搜索）
- 获取文章列表
- 获取文章详情
- 创建文章
- 点赞/取消点赞
- 评论功能

#### 安全测试 (test_security.py)
- 密码哈希和验证
- JWT 令牌创建和解码
- 边界情况处理

#### 模型测试 (test_models.py)
- 用户模型 CRUD
- 内容模型 CRUD
- 查询和过滤

### 前端测试

#### 组件测试
- ContentCard: 渲染、样式、属性绑定
- ArticleItem: 事件触发、数据展示
- Sidebar: 导航链接、路由集成

#### API 测试
- 认证 API: 登录/注册/登出/刷新令牌
- localStorage 操作

## 测试最佳实践

1. **隔离测试**: 每个测试应该独立运行，不依赖其他测试
2. **使用 fixtures**: 利用 pytest fixtures 和 Vue Test Utils 的 mount 选项
3. **Mock 外部依赖**: 使用 vi.mock() 模拟 API 调用和外部服务
4. **覆盖边界情况**: 测试正常流程和异常情况
5. **保持测试简洁**: 每个测试只验证一个行为

## 持续集成

建议在 CI/CD 流程中添加以下步骤：

```yaml
# 安装 uv
- name: Install uv
  uses: astral-sh/setup-uv@v4

# 后端测试
- name: Run Backend Tests
  run: |
    cd super_club_backend
    uv sync
    uv run pytest --cov=app

# 前端测试
- name: Run Frontend Tests
  run: |
    cd super_club
    npm install
    npm run test:run
```

