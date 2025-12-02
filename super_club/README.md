# Super Club - Starter Studies 学习平台

> 把自己当公司来经营 - 一个基于 Vue 3 的现代化学习管理平台

## 项目简介

Super Club 是一个使用 Vue 3 + Vite 构建的单页面应用（SPA），旨在为用户提供一个完整的学习管理平台。该项目展示了如何使用 Vue 3 的最新特性（Composition API、响应式系统等）构建一个功能完整、界面美观的 Web 应用。

项目的核心理念是"把自己当公司来经营"，通过系统化的学习内容管理，帮助用户更好地规划和组织自己的学习路径。

## 功能特点

- **多页面导航系统**：包含学习、牛人、链接、项目、活动等多个功能模块
- **响应式设计**：适配不同屏幕尺寸，提供良好的用户体验
- **组件化架构**：高度模块化的组件设计，易于维护和扩展
- **路由管理**：使用 Vue Router 实现页面导航和状态管理
- **内容卡片展示**：支持图文并茂的内容展示，包含 AI 生成标签
- **文章列表系统**：支持多标签分类和筛选功能
- **现代化 UI**：简洁美观的界面设计，流畅的交互动画

## 技术栈

- **框架**：Vue 3.4.29（使用 Composition API 和 script setup 语法）
- **构建工具**：Vite 5.3.1（提供快速的开发体验和优化的构建）
- **路由管理**：Vue Router 4.6.3
- **样式方案**：Scoped CSS（组件级样式隔离）
- **开发语言**：JavaScript (ES6+)
- **图标方案**：SVG 内联图标（自定义 stroke-based 图标）

## 项目结构

```
super_club/
├── src/
│   ├── assets/              # 静态资源
│   │   ├── base.css        # 基础样式
│   │   └── main.css        # 主样式文件
│   ├── components/          # 公共组件
│   │   ├── Sidebar.vue     # 侧边栏导航组件
│   │   ├── MainContent.vue # 主内容区域（首页）
│   │   ├── ContentCard.vue # 内容卡片组件
│   │   ├── ContentFilters.vue  # 内容筛选组件
│   │   ├── FeatureGrid.vue     # 功能网格组件
│   │   ├── ArticleItem.vue     # 文章项组件
│   │   └── ArticleList.vue     # 文章列表组件
│   ├── pages/              # 页面组件
│   │   ├── TalentPage.vue  # 牛人页面
│   │   ├── LinkPage.vue    # 链接页面
│   │   ├── ProjectPage.vue # 项目页面
│   │   └── EventsPage.vue  # 活动页面
│   ├── router/             # 路由配置
│   │   └── index.js        # 路由定义
│   ├── App.vue             # 根组件
│   └── main.js             # 应用入口
├── public/                 # 公共静态资源
├── package.json            # 项目依赖配置
├── vite.config.js          # Vite 配置文件
└── README.md              # 项目文档
```

## 快速开始

### 环境要求

- Node.js >= 16.0.0
- npm >= 8.0.0 或 yarn >= 1.22.0

### 安装依赖

```bash
npm install
```

或使用 yarn：

```bash
yarn install
```

### 开发模式

启动开发服务器，支持热模块替换（HMR）：

```bash
npm run dev
```

应用将在 `http://localhost:5173` 启动（Vite 默认端口）

### 生产构建

```bash
npm run build
```

构建产物将输出到 `dist/` 目录

### 预览生产构建

```bash
npm run preview
```

## 页面路由

| 路径 | 页面名称 | 组件 | 说明 |
|------|---------|------|------|
| `/` | 学习 | MainContent.vue | 首页，展示学习内容和课程 |
| `/talents` | 牛人 | TalentPage.vue | 展示行业专家和牛人 |
| `/links` | 链接 | LinkPage.vue | 资源链接管理 |
| `/projects` | 项目 | ProjectPage.vue | 项目展示和管理 |
| `/events` | 活动 | EventsPage.vue | 活动信息和报名 |

## 核心组件说明

### Sidebar.vue - 侧边栏导航

功能：
- 品牌 Logo 展示
- 多级导航菜单
- 路由激活状态高亮
- 用户信息展示
- 通知铃铛图标

特点：
- 固定定位，始终可见
- SVG 图标自定义
- 支持 RouterLink 导航

### MainContent.vue - 主内容区域

功能：
- 页面标题和副标题
- 标签页切换（CEO图书馆、最近更新）
- 内容卡片横向滚动展示
- 功能分区网格
- 文章列表展示

### ContentCard.vue - 内容卡片

功能：
- 图片展示（支持外部图片源）
- AI 生成标签显示
- 标题和描述文本
- 悬停动画效果

Props：
- `title`: 卡片标题
- `description`: 卡片描述
- `image`: 卡片图片 URL

### FeatureGrid.vue - 功能网格

功能：
- 2x2 网格布局
- 展示四个核心部门：战略部、品牌部、运营部、销售部
- SVG 图标 + 文字说明
- 悬停交互效果

### ArticleList.vue - 文章列表

功能：
- 文章条目展示
- 支持阅读量、评论数等信息
- 响应式布局

## 开发指南

### 添加新页面

1. 在 `src/pages/` 目录下创建新的 Vue 组件
2. 在 `src/router/index.js` 中添加路由配置
3. 在 `Sidebar.vue` 中添加对应的导航链接

示例：

```javascript
// router/index.js
import NewPage from '../pages/NewPage.vue'

const routes = [
  // ... 其他路由
  {
    path: '/new-page',
    name: 'newPage',
    component: NewPage
  }
]
```

### 创建新组件

1. 在 `src/components/` 目录下创建 `.vue` 文件
2. 使用 `<script setup>` 语法编写组件逻辑
3. 使用 `scoped` 样式确保样式隔离

组件模板：

```vue
<template>
  <div class="component-name">
    <!-- 组件内容 -->
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

// 组件逻辑
</script>

<style scoped>
.component-name {
  /* 组件样式 */
}
</style>
```

### 样式规范

- 使用 `scoped` 样式避免全局污染
- 颜色规范：
  - 主色：`#000000` (黑色)
  - 背景色：`#ffffff` (白色)
  - 辅助背景：`#f5f5f5`, `#f8f8f8`
  - 边框色：`#e0e0e0`
  - 文字灰色：`#666666`
- 圆角规范：`8px`, `12px`
- 间距规范：`8px`, `12px`, `16px`, `24px`, `32px`

### SVG 图标使用

项目使用内联 SVG 图标，参考 Feather Icons 风格：

```vue
<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
  <path d="..."></path>
</svg>
```

## 部署

### 使用 Vite 构建

```bash
npm run build
```

### Docker 部署

项目包含 `entrypoint.sh` 脚本，支持 Docker 容器化部署：

```bash
# 开发模式
bash entrypoint.sh

# 生产模式
bash entrypoint.sh production
```

### 静态托管

构建完成后，将 `dist/` 目录部署到任何静态文件托管服务：
- Vercel
- Netlify
- GitHub Pages
- 云服务器（Nginx/Apache）

## 浏览器支持

- Chrome >= 87
- Firefox >= 78
- Safari >= 14
- Edge >= 88

## 开发历史

本项目基于交互式开发过程构建，完整的开发记录保存在 `cursor_vue.md` 文件中，包含：
- 初始项目搭建
- 组件开发过程
- 样式调整和优化
- 路由配置
- 功能迭代

## 性能优化

- 使用 Vite 的快速冷启动和热模块替换
- 组件懒加载（路由级别）
- 图片使用外部 CDN（Unsplash）
- CSS 作用域隔离减少全局样式计算
- 生产构建自动进行代码分割和压缩

## 许可证

MIT License

## 维护者

本项目由 Claude Code 辅助开发，详细的开发过程记录在 `cursor_vue.md` 文件中。

## 更新日志

### Version 1.0.0 (初始版本)
- ✅ 完成基础项目架构搭建
- ✅ 实现侧边栏导航组件
- ✅ 实现主内容区域和卡片展示
- ✅ 实现路由系统和多页面导航
- ✅ 实现文章列表和筛选功能
- ✅ 完成响应式布局适配

## 相关资源

- [Vue 3 官方文档](https://vuejs.org/)
- [Vite 官方文档](https://vitejs.dev/)
- [Vue Router 文档](https://router.vuejs.org/)

---

如有问题或建议，欢迎提交 Issue 或 Pull Request。
