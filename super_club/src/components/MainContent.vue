<template>
  <main class="main-content">
    <div class="content-header">
      <h1 class="main-title">Starter Studies</h1>
      <p class="subtitle">把自己当公司来经营</p>
      
      <div class="header-tabs">
        <button class="header-tab active">CEO图书馆</button>
        <button class="header-tab">最近更新</button>
      </div>
    </div>

    <div class="content-cards-section">
      <div class="cards-container">
        <ContentCard
          v-for="card in cards"
          :key="card.id"
          :title="card.title"
          :description="card.description"
          :image="card.image"
        />
      </div>
    </div>

    <div class="content-bottom">
      <FeatureGrid />
      
      <ContentFilters />
      
      <ArticleList />
    </div>
  </main>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { contentAPI } from '@/api'
import ContentCard from './ContentCard.vue'
import FeatureGrid from './FeatureGrid.vue'
import ContentFilters from './ContentFilters.vue'
import ArticleList from './ArticleList.vue'

// 数据状态
const cards = ref([])
const loading = ref(false)
const error = ref(null)

// 获取内容卡片
const fetchCards = async () => {
  try {
    loading.value = true
    error.value = null

    const params = {
      page: 1,
      limit: 4
    }

    const data = await contentAPI.getCards(params)
    cards.value = data.items || []
  } catch (err) {
    console.error('获取内容卡片失败:', err)
    error.value = err.message
  } finally {
    loading.value = false
  }
}

// 初始化加载数据
onMounted(() => {
  fetchCards()
})
</script>

<style scoped>
.main-content {
  flex: 1;
  padding: 40px 48px;
  background-color: #ffffff;
  overflow-y: auto;
  height: 100vh;
  min-width: 0;
}

/* 移动端样式调整 */
@media (max-width: 768px) {
  .main-content {
    padding: 16px;
    padding-top: 80px;
    padding-bottom: 80px;
    height: auto;
    min-height: calc(100vh - 60px);
  }

  .content-header {
    margin-bottom: 24px;
  }

  .main-title {
    font-size: 28px;
    margin-bottom: 8px;
  }

  .subtitle {
    font-size: 16px;
    margin-bottom: 24px;
  }

  .header-tabs {
    gap: 8px;
  }

  .header-tab {
    padding: 8px 16px;
    font-size: 13px;
  }

  .content-cards-section {
    margin-bottom: 40px;
  }

  .content-bottom {
    margin-top: 40px;
    padding-bottom: 20px;
  }
}

.content-header {
  margin-bottom: 40px;
}

.main-title {
  font-size: 42px;
  font-weight: 700;
  color: #000000;
  margin-bottom: 8px;
  letter-spacing: -0.5px;
}

.subtitle {
  font-size: 18px;
  color: #666666;
  margin-bottom: 32px;
}

.header-tabs {
  display: flex;
  gap: 12px;
}

.header-tab {
  padding: 10px 20px;
  border: none;
  border-radius: 6px;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.2s;
  background-color: #ffffff;
  color: #000000;
  border: 1px solid #e0e0e0;
}

.header-tab:hover {
  background-color: #f5f5f5;
}

.header-tab.active {
  background-color: #333333;
  color: #ffffff;
  border-color: #333333;
}

.content-cards-section {
  margin-bottom: 60px;
}

.cards-container {
  display: flex;
  gap: 20px;
  overflow-x: auto;
  padding-bottom: 16px;
  scrollbar-width: thin;
  scrollbar-color: #c0c0c0 #f0f0f0;
}

.cards-container::-webkit-scrollbar {
  height: 8px;
}

.cards-container::-webkit-scrollbar-track {
  background: #f0f0f0;
  border-radius: 4px;
}

.cards-container::-webkit-scrollbar-thumb {
  background: #c0c0c0;
  border-radius: 4px;
}

.cards-container::-webkit-scrollbar-thumb:hover {
  background: #a0a0a0;
}

.content-bottom {
  margin-top: 60px;
  padding-bottom: 40px;
}
</style>

