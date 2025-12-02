# 开发指南

本指南提供项目开发的详细说明，包括环境搭建、开发流程、代码规范等。

## 目录

- [环境搭建](#环境搭建)
- [项目架构](#项目架构)
- [开发流程](#开发流程)
- [代码规范](#代码规范)
- [调试技巧](#调试技巧)
- [性能优化](#性能优化)
- [常见问题](#常见问题)

---

## 环境搭建

### 系统要求

- **操作系统**：Windows 10+, macOS 10.15+, Linux (Ubuntu 20.04+)
- **Node.js**：>= 16.0.0（推荐使用 LTS 版本）
- **包管理器**：npm >= 8.0.0 或 yarn >= 1.22.0
- **编辑器**：VS Code（推荐）或其他现代代码编辑器

### 安装 Node.js

#### macOS（使用 Homebrew）
```bash
brew install node
```

#### Ubuntu/Debian
```bash
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs
```

#### Windows
从 [Node.js 官网](https://nodejs.org/) 下载安装包。

### 克隆项目

```bash
git clone <repository-url>
cd super_club
```

### 安装依赖

```bash
npm install
```

或使用 yarn：

```bash
yarn install
```

### VS Code 推荐扩展

在 VS Code 中安装以下扩展以获得最佳开发体验：

1. **Volar** - Vue 3 官方语言支持
2. **ESLint** - 代码质量检查
3. **Prettier** - 代码格式化
4. **Vue VSCode Snippets** - Vue 代码片段
5. **Auto Rename Tag** - 自动重命名配对标签
6. **Path Intellisense** - 路径自动补全

### 配置 VS Code

创建 `.vscode/settings.json`：

```json
{
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "[vue]": {
    "editor.defaultFormatter": "Vue.volar"
  },
  "volar.completion.preferredTagNameCase": "pascal",
  "volar.autoCompleteRefs": true
}
```

---

## 项目架构

### 目录结构详解

```
super_club/
├── docs/                    # 项目文档
│   ├── COMPONENTS.md       # 组件文档
│   ├── DEVELOPMENT_GUIDE.md # 开发指南
│   └── API.md              # API 文档
├── public/                  # 静态资源（不会被 Vite 处理）
│   └── favicon.ico
├── src/
│   ├── assets/             # 静态资源（会被 Vite 处理）
│   │   ├── base.css       # 基础样式
│   │   └── main.css       # 主样式文件
│   ├── components/         # 可复用组件
│   │   ├── Sidebar.vue
│   │   ├── MainContent.vue
│   │   ├── ContentCard.vue
│   │   ├── ContentFilters.vue
│   │   ├── FeatureGrid.vue
│   │   ├── ArticleItem.vue
│   │   └── ArticleList.vue
│   ├── pages/              # 页面组件
│   │   ├── TalentPage.vue
│   │   ├── LinkPage.vue
│   │   ├── ProjectPage.vue
│   │   └── EventsPage.vue
│   ├── router/             # 路由配置
│   │   └── index.js
│   ├── composables/        # 组合式函数（未来扩展）
│   ├── utils/              # 工具函数（未来扩展）
│   ├── App.vue             # 根组件
│   └── main.js             # 应用入口
├── .gitignore              # Git 忽略文件
├── index.html              # HTML 模板
├── package.json            # 项目配置
├── vite.config.js          # Vite 配置
└── README.md               # 项目说明
```

### 架构设计原则

1. **组件化**：将 UI 拆分为独立、可复用的组件
2. **单一职责**：每个组件只负责一个功能
3. **数据驱动**：使用响应式数据驱动 UI 更新
4. **props down, events up**：父组件通过 props 传递数据，子组件通过 events 通知父组件

### 数据流

```
App.vue (根组件)
  ├── Sidebar (固定导航)
  └── RouterView (路由视图)
        ├── MainContent (首页)
        │     ├── ContentCard (内容卡片)
        │     ├── FeatureGrid (功能网格)
        │     ├── ContentFilters (筛选器)
        │     └── ArticleList (文章列表)
        │           └── ArticleItem (文章项)
        ├── TalentPage (牛人页面)
        ├── LinkPage (链接页面)
        ├── ProjectPage (项目页面)
        └── EventsPage (活动页面)
```

---

## 开发流程

### 1. 启动开发服务器

```bash
npm run dev
```

访问 `http://localhost:5173`

### 2. 创建新功能的步骤

#### 步骤 1：创建组件

在 `src/components/` 或 `src/pages/` 创建新组件：

```vue
<!-- src/components/NewComponent.vue -->
<template>
  <div class="new-component">
    <h2>{{ title }}</h2>
    <p>{{ content }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({
  title: String,
  content: String
})
</script>

<style scoped>
.new-component {
  padding: 20px;
  background: #f5f5f5;
  border-radius: 8px;
}
</style>
```

#### 步骤 2：添加路由（如果是页面组件）

在 `src/router/index.js` 添加路由：

```javascript
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

#### 步骤 3：添加导航链接

在 `Sidebar.vue` 添加导航项：

```vue
<RouterLink to="/new-page" class="nav-item">
  <svg class="nav-icon"><!-- SVG 图标 --></svg>
  <span>新页面</span>
</RouterLink>
```

#### 步骤 4：测试功能

1. 检查页面渲染
2. 测试路由跳转
3. 验证响应式行为
4. 测试浏览器兼容性

### 3. Git 工作流

#### 提交规范

使用语义化提交信息：

```bash
# 功能开发
git commit -m "feat: 添加用户资料页面"

# Bug 修复
git commit -m "fix: 修复侧边栏导航高亮问题"

# 样式调整
git commit -m "style: 优化卡片组件间距"

# 文档更新
git commit -m "docs: 更新组件使用说明"

# 代码重构
git commit -m "refactor: 重构文章列表组件"

# 性能优化
git commit -m "perf: 优化图片加载性能"
```

#### 分支策略

```bash
# 主分支
main/master - 生产环境代码

# 开发分支
develop - 开发环境代码

# 功能分支
feature/feature-name - 新功能开发

# 修复分支
fix/bug-name - Bug 修复
```

---

## 代码规范

### Vue 组件规范

#### 1. 组件命名

- **文件名**：使用 PascalCase（如：`ContentCard.vue`）
- **组件名**：与文件名保持一致
- **多单词**：组件名应该总是多个单词（除了 App.vue）

#### 2. Props 定义

```vue
<script setup>
// ✅ 推荐：详细的 Props 定义
const props = defineProps({
  title: {
    type: String,
    required: true
  },
  count: {
    type: Number,
    default: 0
  },
  tags: {
    type: Array,
    default: () => []
  }
})

// ❌ 不推荐：简化的 Props 定义
const props = defineProps(['title', 'count', 'tags'])
</script>
```

#### 3. 组件选项顺序

```vue
<script setup>
// 1. 导入依赖
import { ref, computed, onMounted } from 'vue'
import ChildComponent from './ChildComponent.vue'

// 2. Props 定义
const props = defineProps({...})

// 3. Emits 定义
const emit = defineEmits(['update', 'delete'])

// 4. 响应式状态
const count = ref(0)
const list = ref([])

// 5. 计算属性
const doubleCount = computed(() => count.value * 2)

// 6. 方法
const handleClick = () => {
  count.value++
}

// 7. 生命周期钩子
onMounted(() => {
  console.log('Component mounted')
})
</script>
```

#### 4. 模板规范

```vue
<template>
  <!-- ✅ 推荐：使用短横线命名属性 -->
  <ContentCard
    :article-title="title"
    :article-count="count"
    @update-content="handleUpdate"
  />

  <!-- ❌ 不推荐：使用驼峰命名属性 -->
  <ContentCard
    :articleTitle="title"
    :articleCount="count"
    @updateContent="handleUpdate"
  />

  <!-- ✅ 推荐：v-for 使用 key -->
  <div v-for="item in items" :key="item.id">
    {{ item.name }}
  </div>

  <!-- ✅ 推荐：条件渲染使用 v-show 或 v-if -->
  <div v-if="isVisible">显示内容</div>
  <div v-show="isActive">切换显示</div>
</template>
```

### JavaScript 规范

#### 1. 变量命名

```javascript
// ✅ 推荐：使用有意义的变量名
const userList = ref([])
const isLoading = ref(false)
const fetchUserData = async () => {}

// ❌ 不推荐：使用无意义的变量名
const data = ref([])
const flag = ref(false)
const fn = async () => {}
```

#### 2. 函数编写

```javascript
// ✅ 推荐：单一职责函数
const calculateTotal = (items) => {
  return items.reduce((sum, item) => sum + item.price, 0)
}

const formatCurrency = (amount) => {
  return `¥${amount.toFixed(2)}`
}

// ✅ 推荐：使用箭头函数
const handleClick = () => {
  console.log('Clicked')
}

// ✅ 推荐：异步函数使用 async/await
const fetchData = async () => {
  try {
    const response = await fetch('/api/data')
    const data = await response.json()
    return data
  } catch (error) {
    console.error('Fetch error:', error)
  }
}
```

### CSS 规范

#### 1. 类名命名

使用 BEM 命名规范：

```css
/* Block（块） */
.card {}

/* Element（元素） */
.card__title {}
.card__content {}

/* Modifier（修饰符） */
.card--featured {}
.card__title--large {}
```

#### 2. 样式组织

```css
.component {
  /* 1. 定位属性 */
  position: relative;
  top: 0;
  left: 0;

  /* 2. 盒模型 */
  display: flex;
  width: 100%;
  height: auto;
  padding: 16px;
  margin: 0;

  /* 3. 排版 */
  font-size: 16px;
  line-height: 1.5;
  text-align: center;

  /* 4. 视觉 */
  background-color: #fff;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  color: #000;

  /* 5. 其他 */
  cursor: pointer;
  transition: all 0.2s;
}
```

#### 3. 响应式设计

```css
/* Mobile First 策略 */
.container {
  padding: 16px;
}

/* 平板 */
@media (min-width: 768px) {
  .container {
    padding: 24px;
  }
}

/* 桌面 */
@media (min-width: 1024px) {
  .container {
    padding: 32px;
  }
}
```

---

## 调试技巧

### 1. Vue DevTools

安装 Vue DevTools 浏览器扩展：
- [Chrome](https://chrome.google.com/webstore/detail/vuejs-devtools/nhdogjmejiglipccpnnnanhbledajbpd)
- [Firefox](https://addons.mozilla.org/en-US/firefox/addon/vue-js-devtools/)

功能：
- 检查组件树
- 查看组件状态
- 追踪事件
- 性能分析

### 2. 控制台调试

```javascript
// 在组件中使用 console
const handleClick = () => {
  console.log('Current state:', state.value)
  console.table(items.value)
  console.group('Debug Info')
  console.log('User:', user.value)
  console.log('Settings:', settings.value)
  console.groupEnd()
}
```

### 3. Vite 调试

在 `vite.config.js` 中启用 source map：

```javascript
export default {
  build: {
    sourcemap: true
  }
}
```

### 4. 网络请求调试

使用浏览器开发者工具的 Network 面板：
1. 查看请求/响应数据
2. 检查请求状态码
3. 分析请求时间
4. 查看请求头和响应头

---

## 性能优化

### 1. 组件懒加载

```javascript
// 路由懒加载
const routes = [
  {
    path: '/talents',
    name: 'talents',
    component: () => import('../pages/TalentPage.vue')
  }
]
```

### 2. 图片优化

```vue
<template>
  <!-- 使用适当的图片格式 -->
  <img
    src="image.webp"
    alt="描述"
    loading="lazy"
    width="400"
    height="300"
  />
</template>
```

### 3. 列表渲染优化

```vue
<template>
  <!-- 使用 key 优化列表渲染 -->
  <div v-for="item in items" :key="item.id">
    {{ item.name }}
  </div>

  <!-- 使用 v-show 代替频繁切换的 v-if -->
  <div v-show="isVisible">内容</div>
</template>
```

### 4. 计算属性缓存

```javascript
// ✅ 使用计算属性（有缓存）
const filteredList = computed(() => {
  return list.value.filter(item => item.active)
})

// ❌ 使用方法（无缓存）
const filteredList = () => {
  return list.value.filter(item => item.active)
}
```

---

## 常见问题

### Q1: 为什么修改数据后页面没有更新？

A: 确保使用响应式数据：
```javascript
// ✅ 正确
const count = ref(0)
count.value++

// ❌ 错误
let count = 0
count++
```

### Q2: 如何在组件间通信？

A:
- 父→子：使用 Props
- 子→父：使用 Events (emit)
- 跨组件：使用 provide/inject 或状态管理

### Q3: 样式不生效怎么办？

A: 检查：
1. 是否使用了 `scoped` 属性
2. CSS 选择器优先级
3. 是否被其他样式覆盖
4. 浏览器缓存

### Q4: 路由跳转后组件没有重新渲染？

A: 使用 `:key` 强制重新渲染：
```vue
<RouterView :key="$route.fullPath" />
```

---

## 推荐资源

- [Vue 3 官方文档](https://vuejs.org/)
- [Vue Router 文档](https://router.vuejs.org/)
- [Vite 文档](https://vitejs.dev/)
- [Vue 3 Composition API 指南](https://vuejs.org/guide/extras/composition-api-faq.html)
- [Vue 样式指南](https://vuejs.org/style-guide/)

---

## 更新日志

- 2024-11-10: 初始版本，包含完整开发指南
