<template>
  <main class="link-page">
    <section class="page-header">
      <h1 class="page-title">Starter Network</h1>
      <p class="page-subtitle">认识100位社区CEO</p>

      <div class="tab-row">
        <button
          v-for="tab in tabs"
          :key="tab"
          :class="['tab-btn', { active: activeTab === tab }]"
          @click="activeTab = tab"
        >
          {{ tab }}
        </button>
      </div>
    </section>

    <section class="hero-section">
      <div class="hero-slider">
        <transition-group name="fade" tag="div">
          <div
            v-for="(slide, index) in slides"
            :key="slide.id"
            v-show="currentSlide === index"
            class="hero-slide"
          >
            <img :src="slide.image" :alt="slide.title" />
            <div class="hero-caption">
              <h2>{{ slide.title }}</h2>
              <p>{{ slide.description }}</p>
            </div>
          </div>
        </transition-group>

        <div class="slider-controls">
          <button
            v-for="(slide, index) in slides"
            :key="slide.id"
            :class="['dot', { active: currentSlide === index }]"
            @click="setSlide(index)"
          />
        </div>
      </div>
      <div class="hero-actions">
        <button class="hero-btn">投案例</button>
        <button class="hero-btn outline">约牛人</button>
      </div>
    </section>

    <section class="filter-section">
      <div class="filter-tags">
        <button
          v-for="tag in tags"
          :key="tag"
          :class="['tag-btn', { active: activeTag === tag }]"
          @click="activeTag = tag"
        >
          {{ tag }}
        </button>
      </div>
      <div class="search-box">
        <svg class="search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="11" cy="11" r="8" />
          <path d="m21 21-4.35-4.35" />
        </svg>
        <input class="search-input" type="text" placeholder="搜索社区、话题或人脉" />
      </div>
    </section>

    <section class="link-cards">
      <article v-for="item in linkItems" :key="item.id" class="link-card">
        <header class="card-header">
          <div class="card-title">{{ item.title }}</div>
          <button class="view-btn">查看名片</button>
        </header>
        <div class="card-meta">
          <span>{{ item.host }}</span>
          <span>{{ item.location }}</span>
        </div>
        <p class="card-desc">{{ item.description }}</p>
        <div class="card-tags">
          <span v-for="tag in item.tags" :key="tag" class="card-tag">{{ tag }}</span>
        </div>
        <footer class="card-footer">
          <div class="avatars">
            <img
              v-for="(avatar, index) in item.members"
              :key="index"
              :src="avatar"
              alt="member"
            />
          </div>
          <div class="member-count">{{ item.memberCount }} 位成员正在活跃</div>
        </footer>
      </article>
    </section>
  </main>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount, watch } from 'vue'
import { linksAPI } from '@/api'

const tabs = ['咖啡广场', '聊天群', '1v1咨询']
const tags = ['不限', '消费', '制造', '文娱', '教育', '互联网', 'SaaS', '金融', 'AI', '泛科技', '企服', '新媒体', '大健康', '出海']

const activeTab = ref(tabs[0])
const activeTag = ref(tags[0])

// 轮播图数据
const slides = ref([])

const currentSlide = ref(0)
let timer = null

const startTimer = () => {
  stopTimer()
  if (slides.value.length > 0) {
    timer = setInterval(() => {
      currentSlide.value = (currentSlide.value + 1) % slides.value.length
    }, 5000)
  }
}

const stopTimer = () => {
  if (timer) {
    clearInterval(timer)
    timer = null
  }
}

const setSlide = (index) => {
  currentSlide.value = index
  startTimer()
}

// 数据状态
const linkItems = ref([])
const loading = ref(false)
const error = ref(null)

// 获取轮播图
const fetchCarousel = async () => {
  try {
    const data = await linksAPI.getCarousel()
    slides.value = data.slides || []
  } catch (err) {
    console.error('获取轮播图失败:', err)
  }
}

// 获取社区成员列表
const fetchLinks = async () => {
  try {
    loading.value = true
    error.value = null

    const params = {
      page: 1,
      limit: 20
    }

    // 添加分类筛选
    if (activeTag.value && activeTag.value !== '不限') {
      params.category = activeTag.value
    }

    const data = await linksAPI.getList(params)
    linkItems.value = data.items || []
  } catch (err) {
    console.error('获取社区成员失败:', err)
    error.value = err.message
  } finally {
    loading.value = false
  }
}

// 初始化
onMounted(async () => {
  await Promise.all([
    fetchCarousel(),
    fetchLinks()
  ])
  if (slides.value.length > 0) {
    startTimer()
  }
})

onBeforeUnmount(() => {
  stopTimer()
})

// 监听筛选条件变化
watch(activeTag, () => {
  fetchLinks()
})

// 保留原mock数据作为fallback
const mockLinkItems = [
  {
    id: 1,
    title: '一水',
    host: '@个人创业',
    location: '南京 · 啡咖咖啡',
    description: '集合空间插画设计，针对传统线下消费的见解，欢迎交流合作。',
    tags: ['品牌升级', '消费体验', '空间设计'],
    members: [
      'https://images.unsplash.com/photo-1521572267360-ee0c2909d518?w=100&h=100&fit=crop',
      'https://images.unsplash.com/photo-1544723795-3fb6469f5b39?w=100&h=100&fit=crop',
      'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=100&h=100&fit=crop'
    ],
    memberCount: 46
  },
  {
    id: 2,
    title: '李天遥',
    host: '@某公司大客户销售经理',
    location: '深圳南山 · 喝杯咖啡',
    description: '互联网行业经验丰富，擅长针对中大型客户的解决方案打造与项目推进。',
    tags: ['B2B销售', '行业洞察', '客户经营'],
    members: [
      'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100&h=100&fit=crop',
      'https://images.unsplash.com/photo-1487412720507-e7ab37603c6f?w=100&h=100&fit=crop',
      'https://images.unsplash.com/photo-1524504388940-b1c1722653e1?w=100&h=100&fit=crop'
    ],
    memberCount: 58
  },
  {
    id: 3,
    title: '黄泽江',
    host: '@可想能源技术发展(深圳)有限公司投资经理',
    location: '上海 · 优质投资机构',
    description: '新能源与智能硬件投资经验，擅长发现潜力项目并提供投后赋能。',
    tags: ['新能源', '投融资', '业务拓展'],
    members: [
      'https://images.unsplash.com/photo-1524504388940-b1c1722653e1?w=100&h=100&fit=crop',
      'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=100&h=100&fit=crop',
      'https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=100&h=100&fit=crop'
    ],
    memberCount: 39
  },
  {
    id: 4,
    title: '刘捷',
    host: '@上海合提信息科技有限公司创始人',
    location: '上海 · 创业者社群',
    description: '具备 0-1 产品战略经验，帮助创业团队建立从产品到商业化的全链路能力。',
    tags: ['产品战略', '商业化', '创业方法'],
    members: [
      'https://images.unsplash.com/photo-1544723795-3fb6469f5b39?w=100&h=100&fit=crop',
      'https://images.unsplash.com/photo-1487412720507-e7ab37603c6f?w=100&h=100&fit=crop',
      'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100&h=100&fit=crop'
    ],
    memberCount: 64
  }
]
</script>

<style scoped>
.link-page {
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
  color: #162231;
  margin-bottom: 8px;
  letter-spacing: -0.5px;
}

.page-subtitle {
  font-size: 20px;
  font-weight: 600;
  color: #1c2940;
}

.tab-row {
  display: flex;
  gap: 32px;
  margin-top: 32px;
  border-bottom: 1px solid #e7e7e7;
}

.tab-btn {
  padding: 12px 0;
  font-size: 16px;
  color: #7d8591;
  background: none;
  border: none;
  position: relative;
  cursor: pointer;
  transition: color 0.2s;
}

.tab-btn::after {
  content: '';
  position: absolute;
  left: 0;
  bottom: -1px;
  width: 100%;
  height: 2px;
  background-color: transparent;
  transition: background-color 0.2s;
}

.tab-btn:hover {
  color: #111827;
}

.tab-btn.active {
  color: #111827;
  font-weight: 600;
}

.tab-btn.active::after {
  background-color: #111827;
}

.hero-section {
  position: relative;
  background-color: #f7f8fa;
  border-radius: 24px;
  padding: 24px;
  margin-bottom: 32px;
  border: 1px solid #f0f0f0;
}

.hero-slider {
  position: relative;
  overflow: hidden;
  border-radius: 20px;
  height: 360px;
}

.hero-slide {
  position: absolute;
  inset: 0;
}

.hero-slide img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.hero-caption {
  position: absolute;
  left: 24px;
  bottom: 24px;
  background: rgba(0, 0, 0, 0.55);
  backdrop-filter: blur(4px);
  color: #ffffff;
  padding: 18px 24px;
  border-radius: 14px;
  max-width: 440px;
}

.hero-caption h2 {
  margin: 0 0 8px;
  font-size: 20px;
  font-weight: 600;
}

.hero-caption p {
  margin: 0;
  font-size: 14px;
  line-height: 1.6;
}

.slider-controls {
  position: absolute;
  bottom: 16px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 8px;
}

.dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  border: none;
  background-color: rgba(255, 255, 255, 0.4);
  cursor: pointer;
  transition: background-color 0.2s;
}

.dot.active {
  background-color: #ffffff;
}

.hero-actions {
  position: absolute;
  right: 36px;
  bottom: 36px;
  display: flex;
  gap: 12px;
}

.hero-btn {
  padding: 12px 24px;
  border-radius: 999px;
  font-size: 14px;
  border: none;
  cursor: pointer;
  background-color: #111827;
  color: #ffffff;
  transition: transform 0.2s, box-shadow 0.2s;
  min-width: 120px;
}

.hero-btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 12px 24px rgba(17, 24, 39, 0.12);
}

.hero-btn.outline {
  background-color: #ffffff;
  color: #111827;
  border: 1px solid #d1d5db;
  box-shadow: none;
}

.hero-btn.outline:hover {
  box-shadow: 0 12px 24px rgba(17, 24, 39, 0.08);
}

.filter-section {
  display: flex;
  flex-direction: column;
  gap: 16px;
  margin-bottom: 32px;
}

.filter-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}

.tag-btn {
  padding: 8px 16px;
  border-radius: 999px;
  border: 1px solid #e0e0e0;
  background-color: #ffffff;
  font-size: 13px;
  color: #7d8591;
  cursor: pointer;
  transition: all 0.2s;
}

.tag-btn:hover {
  border-color: #cbd5e0;
  color: #111827;
}

.tag-btn.active {
  background-color: #111827;
  color: #ffffff;
  border-color: #111827;
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
  color: #9ca3af;
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
  border-color: #111827;
}

.link-cards {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 24px;
  padding-bottom: 48px;
}

.link-card {
  border-radius: 20px;
  border: 1px solid #e5e7eb;
  padding: 24px;
  background-color: #ffffff;
  display: flex;
  flex-direction: column;
  gap: 16px;
  box-shadow: 0 16px 32px rgba(17, 24, 39, 0.04);
  transition: transform 0.2s, box-shadow 0.2s;
}

.link-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 24px 40px rgba(17, 24, 39, 0.08);
}

.card-header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
}

.card-title {
  font-size: 18px;
  font-weight: 600;
  color: #111827;
}

.view-btn {
  background-color: #000000;
  color: #ffffff;
  border: none;
  border-radius: 999px;
  padding: 6px 16px;
  font-size: 13px;
  cursor: pointer;
}

.card-meta {
  display: flex;
  gap: 12px;
  font-size: 13px;
  color: #6b7280;
}

.card-desc {
  font-size: 14px;
  color: #374151;
  line-height: 1.6;
  margin: 0;
}

.card-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.card-tag {
  padding: 6px 12px;
  border-radius: 999px;
  background-color: #f3f4f6;
  color: #4b5563;
  font-size: 12px;
}

.card-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
}

.avatars {
  display: flex;
  align-items: center;
}

.avatars img {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  border: 2px solid #ffffff;
  margin-left: -8px;
  background-color: #f3f4f6;
}

.avatars img:first-child {
  margin-left: 0;
}

.member-count {
  font-size: 12px;
  color: #6b7280;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.6s;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

@media (max-width: 1280px) {
  .link-cards {
    grid-template-columns: 1fr;
  }

  .hero-section {
    grid-template-columns: 1fr;
  }

  .hero-actions {
    flex-direction: row;
    justify-content: flex-end;
  }
}

@media (max-width: 900px) {
  .link-page {
    padding: 32px 24px;
  }

  .page-title {
    font-size: 32px;
  }
}
</style>

