# 组件文档

本文档详细说明项目中所有组件的使用方法、Props、Events 和样式。

## 目录

- [布局组件](#布局组件)
  - [App.vue](#appvue)
  - [Sidebar.vue](#sidebarvue)
- [页面组件](#页面组件)
  - [MainContent.vue](#maincontentvue)
  - [TalentPage.vue](#talentpagevue)
  - [LinkPage.vue](#linkpagevue)
  - [ProjectPage.vue](#projectpagevue)
  - [EventsPage.vue](#eventspagevue)
- [内容组件](#内容组件)
  - [ContentCard.vue](#contentcardvue)
  - [ArticleItem.vue](#articleitemvue)
  - [ArticleList.vue](#articlelistvue)
  - [FeatureGrid.vue](#featuregridvue)
  - [ContentFilters.vue](#contentfiltersvue)

---

## 布局组件

### App.vue

**描述**：应用的根组件，负责整体布局结构。

**结构**：
```vue
<Sidebar /> + <RouterView />
```

**布局特点**：
- 使用 Flexbox 横向布局
- 侧边栏固定宽度，内容区域自适应
- 高度占满整个视口（100vh）

**样式要点**：
```css
.app-container {
  display: flex;
  height: 100vh;
  background-color: #ffffff;
}
```

---

### Sidebar.vue

**描述**：左侧固定导航栏，包含品牌 Logo、导航菜单和用户信息。

**位置**：`src/components/Sidebar.vue`

**功能模块**：

1. **品牌 Logo**
   - 显示 "Pitch." 品牌名
   - 可点击返回首页
   - 黑色背景，白色文字

2. **导航菜单**
   - 学习（首页）
   - 牛人
   - 链接
   - 项目
   - 活动
   - 我的（静态链接）

3. **底部区域**
   - 首页/名片切换按钮
   - 用户头像和用户名
   - 通知铃铛图标

**依赖**：
```javascript
import { useRoute } from 'vue-router'
```

**路由交互**：
- 使用 `RouterLink` 进行页面导航
- 通过 `route.name` 判断当前激活路由
- 激活状态自动高亮显示

**样式特点**：
- 宽度：240px
- 背景色：#f5f5f5
- 固定定位，粘性布局
- SVG 图标统一样式（20x20px，1.5px stroke）

**图标列表**：
- 学习：书本图标
- 牛人：用户图标
- 链接：链接图标
- 项目：问号/帮助图标
- 活动：地图标记图标
- 我的：用户图标

---

## 页面组件

### MainContent.vue

**描述**：首页主内容区域，展示学习内容和推荐课程。

**位置**：`src/components/MainContent.vue`

**区域划分**：

1. **页面头部**（content-header）
   - 主标题："Starter Studies"
   - 副标题："把自己当公司来经营"
   - 标签页：CEO图书馆、最近更新

2. **卡片展示区**（content-cards-section）
   - 横向滚动卡片容器
   - 展示 4 张推荐课程卡片
   - 支持鼠标滚轮和拖拽滚动

3. **功能网格**（content-bottom）
   - FeatureGrid 组件（战略部、品牌部等）
   - ContentFilters 筛选器
   - ArticleList 文章列表

**数据结构**：
```javascript
const cards = ref([
  {
    id: 1,
    title: '课程标题',
    description: '课程描述',
    image: '图片URL'
  }
])
```

**子组件**：
- ContentCard（内容卡片）
- FeatureGrid（功能网格）
- ContentFilters（内容筛选）
- ArticleList（文章列表）

**样式特点**：
- 主内容区域自适应宽度（flex: 1）
- 内边距：40px 48px
- 垂直滚动
- 标题字号：42px

---

### TalentPage.vue

**描述**：牛人页面，展示行业专家和意见领袖。

**位置**：`src/pages/TalentPage.vue`

**功能**：
- 展示牛人列表
- 牛人简介和成就
- 关注功能（待实现）

**布局**：待扩展

---

### LinkPage.vue

**描述**：链接管理页面，收藏和管理有用的资源链接。

**位置**：`src/pages/LinkPage.vue`

**功能**：
- 链接分类
- 链接收藏
- 链接搜索

**布局**：待扩展

---

### ProjectPage.vue

**描述**：项目展示页面，展示个人或团队项目。

**位置**：`src/pages/ProjectPage.vue`

**功能**：
- 项目列表展示
- 项目详情查看
- 项目状态跟踪

**布局**：待扩展

---

### EventsPage.vue

**描述**：活动页面，展示即将举行的活动和报名信息。

**位置**：`src/pages/EventsPage.vue`

**功能**：
- 活动日历
- 活动详情
- 报名功能

**布局**：待扩展

---

## 内容组件

### ContentCard.vue

**描述**：内容卡片组件，用于展示课程、文章等内容。

**位置**：`src/components/ContentCard.vue`

**Props**：

| 属性 | 类型 | 必需 | 默认值 | 描述 |
|-----|------|------|--------|------|
| title | String | 是 | - | 卡片标题 |
| description | String | 是 | - | 卡片描述 |
| image | String | 是 | - | 卡片图片 URL |

**使用示例**：
```vue
<ContentCard
  title="《别让猴子跳回背上》如何做一个合理的管理者(下)"
  description="作为管理者,你的贡献来自于你的判断力与影响力..."
  image="https://images.unsplash.com/photo-1497366216548-37526070297c"
/>
```

**结构**：
```vue
<div class="content-card">
  <div class="card-image-wrapper">
    <img />
    <span class="ai-tag">AI生成</span>
  </div>
  <div class="card-content">
    <h3 class="card-title">{{ title }}</h3>
    <p class="card-description">{{ description }}</p>
  </div>
</div>
```

**样式特点**：
- 固定宽度：320px
- 圆角：12px
- 图片高度：200px
- 悬停效果：向上平移 4px + 阴影加深
- 标题截断：最多显示 2 行
- 描述截断：最多显示 3 行

**交互效果**：
- 悬停时卡片上浮
- 悬停时阴影从 0 2px 8px 变为 0 4px 16px
- 过渡时间：0.2s

---

### ArticleItem.vue

**描述**：文章列表项组件。

**位置**：`src/components/ArticleItem.vue`

**Props**：

| 属性 | 类型 | 必需 | 默认值 | 描述 |
|-----|------|------|--------|------|
| title | String | 是 | - | 文章标题 |
| author | String | 否 | - | 作者名称 |
| date | String | 否 | - | 发布日期 |
| views | Number | 否 | 0 | 阅读量 |
| comments | Number | 否 | 0 | 评论数 |
| tags | Array | 否 | [] | 标签列表 |

**使用示例**：
```vue
<ArticleItem
  title="如何成为一名优秀的管理者"
  author="张三"
  date="2024-01-15"
  :views="1234"
  :comments="56"
  :tags="['管理', '领导力']"
/>
```

---

### ArticleList.vue

**描述**：文章列表容器组件。

**位置**：`src/components/ArticleList.vue`

**功能**：
- 展示多篇文章
- 支持分页或无限滚动
- 响应式布局

**使用示例**：
```vue
<ArticleList />
```

---

### FeatureGrid.vue

**描述**：功能网格组件，展示四个核心部门。

**位置**：`src/components/FeatureGrid.vue`

**功能模块**：
- 战略部（Strategy）
- 品牌部（Brand）
- 运营部（Operations）
- 销售部（Sales）

**布局**：
- 2x2 网格布局（grid-template-columns: repeat(2, 1fr)）
- 每个格子 1:1 宽高比（aspect-ratio: 1）
- 间距：24px

**样式特点**：
- 背景色：#f8f8f8
- 圆角：12px
- 图标大小：48x48px
- 悬停效果：背景变深 + 向上平移

**图标说明**：
- 战略部：立方体/包裹图标
- 品牌部：心形图标
- 运营部：目标/瞄准图标
- 销售部：奖杯图标

---

### ContentFilters.vue

**描述**：内容筛选组件，提供标签筛选功能。

**位置**：`src/components/ContentFilters.vue`

**功能**：
- 标签页切换（系统阅读、专题策展）
- 内容分类筛选
- 排序功能

**使用示例**：
```vue
<ContentFilters />
```

---

## 样式规范

### 颜色系统

```css
/* 主色 */
--color-primary: #000000;
--color-background: #ffffff;

/* 灰度 */
--color-gray-100: #f8f8f8;
--color-gray-200: #f5f5f5;
--color-gray-300: #e8e8e8;
--color-gray-400: #e0e0e0;
--color-gray-500: #c0c0c0;
--color-gray-600: #666666;

/* 文字 */
--text-primary: #000000;
--text-secondary: #666666;
```

### 间距系统

```css
/* 间距单位 */
--spacing-xs: 4px;
--spacing-sm: 8px;
--spacing-md: 12px;
--spacing-lg: 16px;
--spacing-xl: 24px;
--spacing-2xl: 32px;
--spacing-3xl: 40px;
--spacing-4xl: 48px;
```

### 圆角规范

```css
--radius-sm: 4px;
--radius-md: 8px;
--radius-lg: 12px;
```

### 字体大小

```css
--text-xs: 12px;
--text-sm: 14px;
--text-base: 16px;
--text-lg: 18px;
--text-xl: 24px;
--text-2xl: 42px;
--text-3xl: 48px;
```

---

## 组件开发指南

### 1. 创建新组件

```vue
<template>
  <div class="component-name">
    <!-- 组件内容 -->
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'

// Props 定义
const props = defineProps({
  propName: {
    type: String,
    required: true,
    default: ''
  }
})

// Events 定义
const emit = defineEmits(['eventName'])

// 组件逻辑
const state = ref('')

const handleClick = () => {
  emit('eventName', state.value)
}
</script>

<style scoped>
.component-name {
  /* 组件样式 */
}
</style>
```

### 2. Props 命名规范

- 使用 camelCase 命名
- 始终定义 type
- 对于必需的 props，设置 required: true
- 为可选 props 提供默认值

### 3. 事件命名规范

- 使用 kebab-case 命名
- 使用动词描述事件（如：update:modelValue、click、change）

### 4. 样式编写规范

- 使用 `scoped` 避免样式污染
- 遵循 BEM 命名规范
- 使用语义化的类名
- 避免深层嵌套（最多 3 层）

---

## 常见问题

### Q: 如何修改侧边栏颜色？

A: 在 `Sidebar.vue` 中修改：
```css
.sidebar {
  background-color: #你的颜色;
}
```

### Q: 如何添加新的导航菜单项？

A: 在 `Sidebar.vue` 的 `<nav class="nav-menu">` 中添加：
```vue
<RouterLink to="/your-path" class="nav-item">
  <svg class="nav-icon">...</svg>
  <span>菜单名称</span>
</RouterLink>
```

### Q: 如何自定义卡片样式？

A: ContentCard 组件使用 scoped 样式，可以通过以下方式覆盖：
1. 修改组件内部样式
2. 使用 `:deep()` 伪类
3. 创建新的卡片组件

---

## 更新日志

- 2024-11-10: 初始版本，完成所有核心组件文档
