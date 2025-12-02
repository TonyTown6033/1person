<template>
  <div class="article-list">
    <div v-if="loading" class="loading">加载中...</div>
    <div v-else-if="error" class="error">{{ error }}</div>
    <template v-else>
      <ArticleItem
        v-for="article in articles"
        :key="article.id"
        :article="article"
        @view-detail="handleViewDetail"
      />
      <div v-if="articles.length === 0" class="empty">
        暂无文章
      </div>
    </template>
    
    <!-- 内容详情弹窗 -->
    <ContentDetailModal
      :visible="showDetailModal"
      :content="detailContent"
      :loading="loadingDetail"
      :is-admin="false"
      @close="closeDetailModal"
      @like="handleLike"
      @share="handleShare"
    />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { contentAPI } from '@/api'
import { componentLogger } from '@/utils/logger'
import ArticleItem from './ArticleItem.vue'
import ContentDetailModal from './ContentDetailModal.vue'

const articles = ref([])
const loading = ref(false)
const error = ref(null)

// 详情弹窗状态
const showDetailModal = ref(false)
const detailContent = ref(null)
const loadingDetail = ref(false)

// 获取文章列表
const fetchArticles = async () => {
  try {
    loading.value = true
    error.value = null
    
    componentLogger.info('开始获取文章列表')
    
    const response = await contentAPI.getArticles({
      page: 1,
      limit: 20
    })
    
    componentLogger.debug('文章列表响应', response)
    
    // 处理文章数据，确保格式正确
    articles.value = (response.items || []).map(item => ({
      id: item.id,
      department: item.department || '未分类',
      title: item.title,
      description: item.excerpt || item.description || '',
      image: item.coverImage || item.image || 'https://images.unsplash.com/photo-1497366216548-37526070297c?w=200&h=150&fit=crop'
    }))
    
    componentLogger.info(`成功获取 ${articles.value.length} 篇文章`)
  } catch (err) {
    componentLogger.error('获取文章列表失败', err)
    error.value = err.message || '加载文章失败'
    // 如果 API 失败，使用默认数据作为后备
    articles.value = [
      {
        id: 1,
        department: '人力部',
        title: '《别让猴子跳回背上》如何做一个合理的管理者(下)',
        description: '作为管理者,你的贡献来自于你的判断力与影响力,你的职责不是亲力亲为地背负所有猴子,而是要提供动力让其他人发挥所长。',
        image: 'https://images.unsplash.com/photo-1497366216548-37526070297c?w=200&h=150&fit=crop'
      },
      {
        id: 2,
        department: '人力部',
        title: '《别让猴子跳回背上》为什么领导没时间,下属没事做?(上)',
        description: '一旦你接受了这些本不属于你的猴子,一个更严重的问题便随之而来:你为什么越努力,反而越忙乱?',
        image: 'https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=200&h=150&fit=crop'
      }
    ]
  } finally {
    loading.value = false
  }
}

// 查看文章详情
const handleViewDetail = async (article) => {
  showDetailModal.value = true
  loadingDetail.value = true
  detailContent.value = null
  
  try {
    // 调用API获取文章详情
    const response = await fetch(`http://127.0.0.1:8001/api/content/articles/${article.id}`)
    const data = await response.json()
    
    if (data.success && data.data) {
      // 转换API返回的数据格式，使其与ContentDetailModal组件兼容
      const apiData = data.data
      detailContent.value = {
        id: apiData.id,
        title: apiData.title,
        content: apiData.content,
        excerpt: apiData.excerpt,
        description: apiData.description,
        coverImage: apiData.coverImage,
        department: apiData.department,
        type: 'article',
        tags: apiData.tags || [],
        author: apiData.author,
        viewCount: apiData.stats?.views || 0,
        likeCount: apiData.stats?.likes || 0,
        commentCount: apiData.stats?.comments || 0,
        readingTime: apiData.readingTime || 5,
        publishedAt: apiData.publishedAt,
        createdAt: apiData.createdAt,
        isLiked: apiData.isLiked,
        isFavorited: apiData.isFavorited
      }
    } else {
      // 如果API失败，使用列表中的基本信息
      detailContent.value = {
        ...article,
        content: article.description,
        type: 'article',
        viewCount: 0,
        likeCount: 0,
        commentCount: 0,
        readingTime: 5
      }
    }
  } catch (err) {
    console.error('获取文章详情失败:', err)
    // 使用列表中的基本信息
    detailContent.value = {
      ...article,
      content: article.description,
      type: 'article',
      viewCount: 0,
      likeCount: 0,
      commentCount: 0,
      readingTime: 5
    }
  } finally {
    loadingDetail.value = false
  }
}

// 关闭详情弹窗
const closeDetailModal = () => {
  showDetailModal.value = false
  detailContent.value = null
}

// 处理点赞
const handleLike = (content, isLiked) => {
  console.log('点赞:', content.id, isLiked)
  // 这里可以调用API更新点赞状态
}

// 处理分享
const handleShare = (content) => {
  console.log('分享:', content.id)
}

onMounted(() => {
  fetchArticles()
})
</script>

<style scoped>
.article-list {
  margin-top: 32px;
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.loading,
.error,
.empty {
  padding: 40px;
  text-align: center;
  color: #666666;
  font-size: 14px;
}

.error {
  color: #ff4444;
}
</style>

