<template>
  <main class="events-page">
    <section class="hero">
      <h1 class="title">Starter Community</h1>
      <p class="subtitle">探索前沿，碰撞机会</p>

      <div class="hero-slider">
        <transition-group name="fade" tag="div">
          <div
            v-for="(slide, index) in slides"
            :key="slide.id"
            v-show="currentSlide === index"
            class="hero-slide"
          >
            <img :src="slide.image" :alt="'slide-' + slide.id" />
          </div>
        </transition-group>

        <div class="slider-dots">
          <button
            v-for="(slide, index) in slides"
            :key="slide.id"
            :class="['dot', { active: currentSlide === index }]"
            @click="setSlide(index)"
          />
        </div>

        <div class="hero-actions">
          <button class="pill-btn">往期主题</button>
          <button class="pill-btn outline">往期嘉宾</button>
        </div>
      </div>

      <div class="hero-below">
        <div class="hero-stats">
          <div class="stat-line">累计邀请200+分享嘉宾</div>
          <div class="stat-line sub">汇聚6000+创始人</div>
        </div>
      </div>
    </section>

    <section class="upcoming">
      <div class="section-header">
        <h2>查看近期活动</h2>
        <div class="filters">
          <button v-for="tab in tabs" :key="tab" :class="['tab', { active: activeTab === tab }]" @click="activeTab = tab">
            {{ tab }}
          </button>
        </div>
      </div>

      <div class="card-grid">
        <article v-for="event in events" :key="event.id" class="event-card">
          <div class="cover">
            <img :src="event.cover" :alt="event.title" />
          </div>
          <div class="card-content">
            <h3 class="event-title">{{ event.title }}</h3>
            <p class="event-desc">{{ event.description }}</p>
            <div class="meta">
              <span class="meta-text">开放报名</span>
              <span class="meta-text">{{ event.date }}</span>
              <span class="meta-text">{{ event.location }}</span>
            </div>
            <div class="tags">
              <span class="tag">会员活动</span>
              <span class="tag primary">火热报名中</span>
            </div>
          </div>
        </article>
      </div>
    </section>
  </main>
  </template>

<script setup>
import { ref, onMounted, onBeforeUnmount, watch } from 'vue'
import { eventsAPI } from '@/api'

const tabs = ['不限', '即将开始', '往期活动']
const activeTab = ref(tabs[0])

// 轮播图数据
const slides = ref([])
const currentSlide = ref(0)
let timer = null

const start = () => {
  stop()
  timer = setInterval(() => {
    currentSlide.value = (currentSlide.value + 1) % slides.value.length
  }, 5000)
}

const stop = () => {
  if (timer) {
    clearInterval(timer)
    timer = null
  }
}

const setSlide = (i) => {
  currentSlide.value = i
  start()
}

// 活动数据
const events = ref([])
const loading = ref(false)
const error = ref(null)

// 获取轮播图数据
const fetchCarousel = async () => {
  try {
    const data = await eventsAPI.getCarousel()
    slides.value = data.slides || []
  } catch (err) {
    console.error('获取轮播图失败:', err)
  }
}

// 获取活动列表
const fetchEvents = async () => {
  try {
    loading.value = true
    error.value = null

    const params = {
      page: 1,
      limit: 12
    }

    // 根据tab设置status参数
    if (activeTab.value === '即将开始') {
      params.status = 'upcoming'
    } else if (activeTab.value === '往期活动') {
      params.status = 'past'
    } else {
      params.status = 'all'
    }

    const data = await eventsAPI.getList(params)
    events.value = data.items || []
  } catch (err) {
    console.error('获取活动列表失败:', err)
    error.value = err.message
  } finally {
    loading.value = false
  }
}

// 初始化
onMounted(async () => {
  await Promise.all([
    fetchCarousel(),
    fetchEvents()
  ])
  if (slides.value.length > 0) {
    start()
  }
})

onBeforeUnmount(() => stop())

// 监听tab变化
watch(activeTab, () => {
  fetchEvents()
})
</script>

<style scoped>
.events-page {
  flex: 1;
  padding: 32px 40px;
  background-color: #ffffff;
  overflow-y: auto;
  height: 100vh;
}

.hero {
  margin-bottom: 28px;
}

.title {
  font-size: 40px;
  font-weight: 800;
  color: #111827;
  margin: 0 0 6px;
}

.subtitle {
  font-size: 22px;
  color: #1f2937;
  font-weight: 700;
  margin: 0 0 16px;
}

.hero-slider {
  position: relative;
  border-radius: 16px;
  overflow: hidden;
  border: 1px solid #e5e7eb;
  height: 560px;
  margin-bottom: 6px;
}

.hero-slide {
  position: absolute;
  inset: 0;
}

.hero-slide img {
  width: 100%;
  height: 560px;
  object-fit: cover;
  display: block;
}

.slider-dots {
  position: absolute;
  left: 50%;
  bottom: 14px;
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
}

.dot.active {
  background-color: #ffffff;
}

.hero-actions {
  position: absolute;
  right: 16px;
  bottom: 16px;
  display: flex;
  gap: 10px;
}

.pill-btn {
  padding: 10px 16px;
  border-radius: 999px;
  background-color: #111827;
  color: #ffffff;
  border: 1px solid #111827;
  font-size: 14px;
  cursor: pointer;
}

.pill-btn.outline {
  background-color: #ffffff;
  color: #111827;
  border-color: #d1d5db;
}

.hero-below {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 6px 0;
}

.hero-stats .stat-line {
  font-size: 14px;
  color: #111827;
}

.hero-stats .stat-line.sub {
  color: #6b7280;
  margin-top: 2px;
}

.upcoming .section-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin: 18px 0;
}

.upcoming h2 {
  font-size: 20px;
  color: #111827;
  font-weight: 700;
  margin: 0;
}

.filters {
  display: flex;
  gap: 8px;
}

.tab {
  padding: 8px 14px;
  background-color: #f4f6f8;
  border: 1px solid #e5e7eb;
  color: #4b5563;
  font-size: 13px;
  border-radius: 999px;
  cursor: pointer;
}

.tab.active {
  background-color: #111827;
  color: #ffffff;
  border-color: #111827;
}

.card-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  padding-bottom: 36px;
}

.event-card {
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  overflow: hidden;
  background-color: #ffffff;
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.04);
  display: flex;
  flex-direction: column;
}

.cover {
  width: 100%;
  height: 170px;
  background-color: #f3f4f6;
}

.cover img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.card-content {
  padding: 14px 16px 16px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.event-title {
  font-size: 16px;
  color: #111827;
  font-weight: 600;
  margin: 0;
}

.event-desc {
  font-size: 13px;
  color: #4b5563;
  line-height: 1.6;
  margin: 0;
}

.meta {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}

.meta-text {
  font-size: 12px;
  color: #6b7280;
}

.tags {
  display: flex;
  gap: 8px;
}

.tag {
  padding: 4px 10px;
  border-radius: 999px;
  background-color: #f3f4f6;
  color: #6b7280;
  font-size: 12px;
}

.tag.primary {
  background-color: #111827;
  color: #ffffff;
}

@media (max-width: 1280px) {
  .card-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 900px) {
  .events-page {
    padding: 24px;
  }

  .card-grid {
    grid-template-columns: 1fr;
  }
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.6s;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>

