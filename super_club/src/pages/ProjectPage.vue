<template>
  <main class="project-page">
    <section class="page-header">
      <h1 class="page-title">Starter Solutions</h1>
      <p class="page-subtitle">资源库 · 需求发布广场</p>
      <p class="page-desc">也许这里的一个项目，就是你事业的新起点</p>

      <div class="header-actions">
        <button class="primary-btn">发布我的项目</button>
      </div>
    </section>

    <section class="filters">
      <div class="sub-filters">
        <span class="filter-label">需求分类</span>
        <div class="filter-buttons">
          <button
            v-for="tag in demandTags"
            :key="tag"
            :class="['filter-btn', { active: activeDemand === tag }]"
            @click="activeDemand = tag"
          >
            {{ tag }}
          </button>
        </div>
      </div>

      <div class="search-row">
        <div class="search-box">
          <svg class="search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="11" cy="11" r="8" />
            <path d="m21 21-4.35-4.35" />
          </svg>
          <input type="text" class="search-input" placeholder="搜索合作方向、关键词或企业名称" />
        </div>
      </div>
    </section>

    <section class="project-list">
      <article v-for="project in projects" :key="project.id" class="project-card">
        <div class="card-logo">
          <img :src="project.logo" :alt="project.name" />
        </div>
        <div class="card-body">
          <header class="card-header">
            <h2 class="project-name">{{ project.name }}</h2>
            <span class="project-type">{{ project.type }}</span>
          </header>
          <p class="project-desc">{{ project.description }}</p>
          <div class="project-tags">
            <span v-for="tag in project.tags" :key="tag" class="tag">
              {{ tag }}
            </span>
          </div>
        </div>
        <div class="card-actions">
          <button class="outline-btn">查看详情</button>
        </div>
      </article>
    </section>
  </main>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import { projectsAPI } from '@/api'

const demandTags = ['不限', '消费', '企业服务', '文娱', '教育', 'AI', '品牌', '渠道', '资本', '产业链']

const activeDemand = ref(demandTags[0])
const searchKeyword = ref('')

// 数据状态
const projects = ref([])
const loading = ref(false)
const error = ref(null)

// 获取项目列表
const fetchProjects = async () => {
  try {
    loading.value = true
    error.value = null

    const params = {
      page: 1,
      limit: 20,
      sort: 'latest'
    }

    // 添加分类筛选
    if (activeDemand.value && activeDemand.value !== '不限') {
      params.category = activeDemand.value
    }

    // 添加搜索关键词
    if (searchKeyword.value) {
      params.search = searchKeyword.value
    }

    const data = await projectsAPI.getList(params)
    projects.value = data.items || []
  } catch (err) {
    console.error('获取项目列表失败:', err)
    error.value = err.message
  } finally {
    loading.value = false
  }
}

// 初始化加载数据
onMounted(() => {
  fetchProjects()
})

// 监听筛选条件变化
watch(activeDemand, () => {
  fetchProjects()
})
</script>

<style scoped>
.project-page {
  flex: 1;
  padding: 40px 48px;
  background-color: #ffffff;
  overflow-y: auto;
  height: 100vh;
}

.page-header {
  margin-bottom: 32px;
}

.page-title {
  font-size: 42px;
  font-weight: 700;
  color: #1f2937;
  margin-bottom: 8px;
}

.page-subtitle {
  font-size: 28px;
  font-weight: 600;
  color: #111827;
  margin-bottom: 8px;
}

.page-desc {
  font-size: 16px;
  color: #6b7280;
  margin-bottom: 24px;
}

.header-actions {
  display: flex;
  gap: 12px;
}

.primary-btn {
  padding: 12px 28px;
  border-radius: 999px;
  background-color: #111827;
  color: #ffffff;
  border: none;
  font-size: 16px;
  cursor: pointer;
  transition: transform 0.2s, box-shadow 0.2s;
}

.primary-btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 12px 24px rgba(17, 24, 39, 0.12);
}

.filters {
  margin-bottom: 32px;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.sub-filters {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 12px;
}

.filter-label {
  font-size: 12px;
  letter-spacing: 0.4px;
  color: #a0a7b4;
  text-transform: uppercase;
}

.filter-buttons {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.filter-btn {
  padding: 6px 14px;
  border-radius: 999px;
  border: 1px solid #edf0f5;
  background-color: #f8f9fb;
  font-size: 13px;
  color: #5b6170;
  cursor: pointer;
  transition: all 0.2s;
}

.filter-btn:hover {
  border-color: #d7dce6;
  color: #111827;
}

.filter-btn.active {
  background-color: #111827;
  color: #ffffff;
  border-color: #111827;
}

.search-row {
  display: flex;
  justify-content: flex-start;
}

.search-box {
  position: relative;
  width: 100%;
  max-width: 420px;
}

.search-icon {
  position: absolute;
  left: 14px;
  top: 50%;
  transform: translateY(-50%);
  width: 18px;
  height: 18px;
  color: #9ca3af;
}

.search-input {
  width: 100%;
  padding: 10px 14px 10px 42px;
  border: 1px solid #e5e7eb;
  border-radius: 999px;
  background-color: #ffffff;
  font-size: 14px;
  transition: border-color 0.2s;
}

.search-input:focus {
  outline: none;
  border-color: #111827;
}

.project-list {
  display: flex;
  flex-direction: column;
  gap: 24px;
  padding-bottom: 48px;
}

.project-card {
  display: grid;
  grid-template-columns: 120px 1fr auto;
  gap: 24px;
  padding: 24px;
  border-radius: 24px;
  border: 1px solid #e5e7eb;
  background-color: #ffffff;
  box-shadow: 0 18px 32px rgba(15, 23, 42, 0.05);
  align-items: center;
  transition: transform 0.2s, box-shadow 0.2s;
}

.project-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 24px 40px rgba(15, 23, 42, 0.08);
}

.card-logo {
  width: 120px;
  height: 120px;
  border-radius: 24px;
  background-color: #f9fafb;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.card-logo img {
  width: 80%;
  height: 80%;
  object-fit: contain;
}

.card-body {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.card-header {
  display: flex;
  align-items: center;
  gap: 12px;
}

.project-name {
  font-size: 20px;
  font-weight: 600;
  color: #111827;
}

.project-type {
  padding: 4px 10px;
  border-radius: 999px;
  background-color: #eef2ff;
  color: #4338ca;
  font-size: 12px;
  font-weight: 500;
}

.project-desc {
  font-size: 14px;
  color: #4b5563;
  line-height: 1.7;
  margin: 0;
}

.project-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.tag {
  padding: 6px 12px;
  border-radius: 999px;
  background-color: #f3f4f6;
  color: #4b5563;
  font-size: 12px;
}

.card-actions {
  display: flex;
  align-items: center;
}

.outline-btn {
  padding: 10px 18px;
  border-radius: 999px;
  border: 1px solid #d1d5db;
  background-color: #ffffff;
  color: #111827;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.2s;
}

.outline-btn:hover {
  border-color: #111827;
}

@media (max-width: 1280px) {
  .project-card {
    grid-template-columns: 90px 1fr;
    grid-template-areas:
      'logo header'
      'logo body'
      'logo actions';
  }

  .card-logo {
    grid-area: logo;
    width: 90px;
    height: 90px;
  }

  .card-body {
    grid-area: body;
  }

  .card-actions {
    grid-area: actions;
    justify-content: flex-start;
  }
}

@media (max-width: 900px) {
  .project-page {
    padding: 32px 24px;
  }

  .sub-filters {
    flex-direction: column;
    align-items: stretch;
  }

  .search-box {
    width: 100%;
  }
}
</style>

