<template>
  <main class="talent-page">
    <section class="page-header">
      <h1 class="page-title">Super Elite Card</h1>
      <p class="page-subtitle">发现各行各业的顶尖操盘手，快速建立你的专家顾问团。</p>

      <div class="header-actions">
        <div class="stats">
          <div class="stat-item">
            <span class="stat-value">{{ stats.totalTalents }}</span>
            <span class="stat-label">精选牛人</span>
          </div>
          <div class="stat-divider" />
          <div class="stat-item">
            <span class="stat-value">{{ stats.totalTracks }}</span>
            <span class="stat-label">热门赛道</span>
          </div>
          <div class="stat-divider" />
          <div class="stat-item">
            <span class="stat-value">{{ stats.activeInvitations }}</span>
            <span class="stat-label">实时邀约</span>
          </div>
        </div>
        <div class="cta-buttons">
          <button class="btn primary">发布合作需求</button>
          <button class="btn secondary">推荐牛人</button>
        </div>
      </div>

      <div class="topic-tabs">
        <button
          v-for="tab in topicTabs"
          :key="tab"
          :class="['topic-tab', { active: activeTopic === tab }]"
          @click="activeTopic = tab"
        >
          {{ tab }}
        </button>
      </div>
    </section>

    <section class="talent-spotlight">
      <div class="section-header">
        <h2>本周焦点</h2>
        <button class="link-button">全部牛人</button>
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
            <button class="connect-btn">邀约</button>
          </div>

          <p class="talent-description">{{ talent.description }}</p>

          <div class="talent-tags">
            <span v-for="tag in talent.tags" :key="tag" class="tag">
              {{ tag }}
            </span>
          </div>

          <div class="talent-stats">
            <div class="stat">
              <span class="stat-number">{{ talent.projects }}</span>
              <span class="stat-text">操盘项目</span>
            </div>
            <div class="stat">
              <span class="stat-number">{{ talent.experience }}</span>
              <span class="stat-text">行业经验</span>
            </div>
            <div class="stat">
              <span class="stat-number">{{ talent.followers }}</span>
              <span class="stat-text">关注</span>
            </div>
          </div>
        </article>
      </div>
    </section>

    <section class="talent-filters">
      <div class="filter-group">
        <span class="filter-label">擅长领域</span>
        <div class="filter-buttons">
          <button
            v-for="field in fields"
            :key="field"
            :class="['filter-btn', { active: activeField === field }]"
            @click="activeField = field"
          >
            {{ field }}
          </button>
        </div>
      </div>
      <div class="filter-group">
        <span class="filter-label">城市</span>
        <div class="filter-buttons">
          <button
            v-for="city in cities"
            :key="city"
            :class="['filter-btn', { active: activeCity === city }]"
            @click="activeCity = city"
          >
            {{ city }}
          </button>
        </div>
      </div>
      <div class="search-box">
        <svg class="search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="11" cy="11" r="8" />
          <path d="m21 21-4.35-4.35" />
        </svg>
        <input class="search-input" type="text" placeholder="输入牛人姓名或关键词搜索" />
      </div>
    </section>

    <section class="talent-list-section">
      <div class="section-header">
        <h2>最新上架</h2>
        <button class="link-button">查看更多</button>
      </div>

      <div class="talent-list">
        <div v-for="talent in recentTalents" :key="talent.id" class="talent-list-item">
          <div class="list-avatar">
            <img :src="talent.avatar" :alt="talent.name" />
          </div>
          <div class="list-body">
            <div class="list-header">
              <div>
                <div class="list-name">{{ talent.name }}</div>
                <div class="list-meta">{{ talent.role }} · {{ talent.company }} · {{ talent.location }}</div>
              </div>
              <button class="connect-outline">查看档案</button>
            </div>
            <p class="list-description">{{ talent.description }}</p>
            <div class="list-tags">
              <span v-for="tag in talent.tags" :key="tag" class="tag">
                {{ tag }}
              </span>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import { talentsAPI } from '@/api'

const topicTabs = ['全部领域', '运营增长', '品牌营销', '产品战略', '组织管理', '融资并购']
const activeTopic = ref(topicTabs[0])

const fields = ['不限', '增长', '品牌', '组织', '产品', '商业化', '供应链']
const activeField = ref(fields[0])

const cities = ['不限', '北京', '上海', '深圳', '杭州']
const activeCity = ref(cities[0])

// 数据状态
const featuredTalents = ref([])
const recentTalents = ref([])
const stats = ref({
  totalTalents: 0,
  totalTracks: 0,
  activeInvitations: 0
})
const loading = ref(false)
const error = ref(null)

// 获取精选人才
const fetchFeaturedTalents = async () => {
  try {
    loading.value = true
    error.value = null
    const data = await talentsAPI.getFeatured(3)
    featuredTalents.value = data.items || []
  } catch (err) {
    console.error('获取精选人才失败:', err)
    error.value = err.message
  } finally {
    loading.value = false
  }
}

// 获取人才列表
const fetchTalents = async () => {
  try {
    loading.value = true
    error.value = null

    const params = {
      page: 1,
      limit: 20,
      sort: 'latest'
    }

    // 添加筛选条件
    if (activeField.value && activeField.value !== '不限') {
      params.field = activeField.value
    }

    if (activeCity.value && activeCity.value !== '不限') {
      params.city = activeCity.value
    }

    const data = await talentsAPI.getList(params)
    recentTalents.value = data.items || []
  } catch (err) {
    console.error('获取人才列表失败:', err)
    error.value = err.message
  } finally {
    loading.value = false
  }
}

// 获取统计数据
const fetchStats = async () => {
  try {
    const data = await talentsAPI.getStats()
    stats.value = {
      totalTalents: data.totalTalents || 0,
      totalTracks: data.totalTracks || 0,
      activeInvitations: data.activeInvitations || 0
    }
  } catch (err) {
    console.error('获取统计数据失败:', err)
  }
}

// 初始化加载数据
onMounted(async () => {
  await Promise.all([
    fetchFeaturedTalents(),
    fetchTalents(),
    fetchStats()
  ])
})

// 监听筛选条件变化
watch([activeField, activeCity], () => {
  fetchTalents()
})
</script>

<style scoped>
.talent-page {
  flex: 1;
  padding: 40px 48px;
  background-color: #ffffff;
  overflow-y: auto;
  height: 100vh;
}

.page-header {
  margin-bottom: 40px;
}

.page-title {
  font-size: 42px;
  font-weight: 700;
  color: #000000;
  margin-bottom: 8px;
  letter-spacing: -0.5px;
}

.page-subtitle {
  font-size: 18px;
  color: #666666;
  margin-bottom: 24px;
}

.header-actions {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
  margin-bottom: 32px;
}

.stats {
  display: flex;
  align-items: center;
  gap: 24px;
  padding: 16px 24px;
  background-color: #f8f8f8;
  border-radius: 12px;
}

.stat-item {
  display: flex;
  flex-direction: column;
  gap: 4px;
  min-width: 80px;
}

.stat-value {
  font-size: 24px;
  font-weight: 600;
  color: #000000;
}

.stat-label {
  font-size: 12px;
  color: #666666;
  letter-spacing: 1px;
  text-transform: uppercase;
}

.stat-divider {
  width: 1px;
  height: 36px;
  background-color: #e0e0e0;
}

.cta-buttons {
  display: flex;
  gap: 12px;
}

.btn {
  padding: 12px 20px;
  border-radius: 8px;
  border: 1px solid transparent;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.2s;
}

.btn.primary {
  background-color: #000000;
  color: #ffffff;
}

.btn.primary:hover {
  background-color: #222222;
}

.btn.secondary {
  background-color: #ffffff;
  color: #000000;
  border-color: #d9d9d9;
}

.btn.secondary:hover {
  background-color: #f5f5f5;
}

.topic-tabs {
  display: flex;
  gap: 12px;
}

.topic-tab {
  padding: 8px 18px;
  border-radius: 999px;
  border: 1px solid #e0e0e0;
  background-color: #ffffff;
  font-size: 14px;
  color: #666666;
  cursor: pointer;
  transition: all 0.2s;
}

.topic-tab:hover {
  color: #000000;
  border-color: #cccccc;
}

.topic-tab.active {
  background-color: #000000;
  color: #ffffff;
  border-color: #000000;
}

.section-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 24px;
}

.section-header h2 {
  font-size: 22px;
  font-weight: 600;
  color: #000000;
}

.link-button {
  background: none;
  border: none;
  font-size: 14px;
  color: #333333;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 4px;
  transition: color 0.2s;
}

.link-button:hover {
  color: #000000;
}

.talent-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
  margin-bottom: 48px;
}

.talent-card {
  background-color: #ffffff;
  border-radius: 16px;
  border: 1px solid #eeeeee;
  padding: 24px;
  display: flex;
  flex-direction: column;
  gap: 16px;
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.04);
}

.talent-card-header {
  display: flex;
  align-items: center;
  gap: 16px;
}

.avatar {
  width: 62px;
  height: 62px;
  border-radius: 16px;
  overflow: hidden;
  background-color: #f0f0f0;
  flex-shrink: 0;
}

.avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.identity {
  flex: 1;
}

.name {
  font-size: 18px;
  font-weight: 600;
  color: #000000;
}

.role {
  font-size: 14px;
  color: #333333;
  margin: 2px 0;
}

.meta {
  font-size: 12px;
  color: #999999;
}

.connect-btn {
  background-color: #000000;
  color: #ffffff;
  border: none;
  border-radius: 6px;
  padding: 10px 16px;
  font-size: 14px;
  cursor: pointer;
  transition: background-color 0.2s;
}

.connect-btn:hover {
  background-color: #222222;
}

.talent-description {
  font-size: 14px;
  color: #444444;
  line-height: 1.7;
}

.talent-tags,
.list-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.tag {
  display: inline-flex;
  align-items: center;
  padding: 6px 12px;
  background-color: #f5f5f5;
  color: #666666;
  border-radius: 999px;
  font-size: 12px;
}

.talent-stats {
  display: flex;
  justify-content: space-between;
  padding-top: 12px;
  border-top: 1px solid #f0f0f0;
}

.stat {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.stat-number {
  font-size: 16px;
  font-weight: 600;
  color: #000000;
}

.stat-text {
  font-size: 12px;
  color: #888888;
}

.talent-filters {
  background-color: #f9f9f9;
  border-radius: 16px;
  padding: 24px;
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin-bottom: 36px;
  border: 1px solid #f0f0f0;
}

.filter-group {
  display: flex;
  align-items: center;
  gap: 16px;
  flex-wrap: wrap;
}

.filter-label {
  font-size: 14px;
  color: #666666;
  min-width: 64px;
}

.filter-buttons {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}

.filter-btn {
  padding: 8px 16px;
  border-radius: 999px;
  border: 1px solid #e0e0e0;
  background-color: #ffffff;
  font-size: 13px;
  color: #666666;
  cursor: pointer;
  transition: all 0.2s;
}

.filter-btn:hover {
  border-color: #cccccc;
  color: #000000;
}

.filter-btn.active {
  background-color: #000000;
  color: #ffffff;
  border-color: #000000;
}

.search-box {
  position: relative;
  max-width: 420px;
}

.search-icon {
  position: absolute;
  left: 16px;
  top: 50%;
  transform: translateY(-50%);
  width: 18px;
  height: 18px;
  color: #999999;
}

.search-input {
  width: 100%;
  padding: 12px 16px 12px 44px;
  border-radius: 999px;
  border: 1px solid #e0e0e0;
  background-color: #ffffff;
  font-size: 14px;
  transition: border-color 0.2s;
}

.search-input:focus {
  outline: none;
  border-color: #333333;
}

.talent-list {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.talent-list-item {
  display: flex;
  gap: 20px;
  padding: 20px;
  border-radius: 12px;
  border: 1px solid #f0f0f0;
  background-color: #ffffff;
  transition: box-shadow 0.2s;
}

.talent-list-item:hover {
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.05);
}

.list-avatar {
  width: 68px;
  height: 68px;
  border-radius: 16px;
  overflow: hidden;
  background-color: #f0f0f0;
  flex-shrink: 0;
}

.list-avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.list-body {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.list-header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 16px;
}

.list-name {
  font-size: 18px;
  font-weight: 600;
  color: #000000;
}

.list-meta {
  font-size: 13px;
  color: #888888;
  margin-top: 4px;
}

.list-description {
  font-size: 14px;
  color: #555555;
  line-height: 1.6;
  margin: 0;
}

.connect-outline {
  background-color: #ffffff;
  color: #000000;
  border: 1px solid #d9d9d9;
  border-radius: 6px;
  padding: 8px 14px;
  font-size: 13px;
  cursor: pointer;
  transition: all 0.2s;
}

.connect-outline:hover {
  border-color: #000000;
  color: #000000;
}

@media (max-width: 1280px) {
  .talent-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 1024px) {
  .header-actions {
    flex-direction: column;
    align-items: flex-start;
  }

  .stats {
    width: 100%;
  }

  .talent-grid {
    grid-template-columns: 1fr;
  }
}
</style>

