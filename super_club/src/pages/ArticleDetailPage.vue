<template>
  <div class="article-detail-page">
    <div v-if="loading" class="loading-container">
      <div class="loading-spinner">加载中...</div>
    </div>
    
    <div v-else-if="error" class="error-container">
      <p class="error-message">{{ error }}</p>
      <button @click="goBack" class="back-button">返回</button>
    </div>
    
    <article v-else-if="article" class="article-container">
      <!-- 返回按钮 -->
      <button @click="goBack" class="back-button-top">
        <svg class="back-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M19 12H5M12 19l-7-7 7-7"/>
        </svg>
        返回
      </button>

      <!-- 文章头部 -->
      <header class="article-header">
        <div class="article-meta">
          <span class="department-tag">{{ article.department }}</span>
          <span class="reading-time">{{ article.readingTime }} 分钟阅读</span>
        </div>
        <h1 class="article-title">{{ article.title }}</h1>
        <div class="article-author-info">
          <img :src="article.author.avatar" :alt="article.author.name" class="author-avatar" />
          <div class="author-details">
            <span class="author-name">{{ article.author.name }}</span>
            <span class="publish-date">{{ formatDate(article.publishedAt) }}</span>
          </div>
        </div>
        <div v-if="article.coverImage" class="article-cover">
          <img :src="article.coverImage" :alt="article.title" />
        </div>
      </header>

      <!-- 文章内容 -->
      <div class="article-content-wrapper">
        <div 
          class="article-content markdown-body" 
          v-html="renderedContent"
        ></div>
      </div>

      <!-- 文章底部 -->
      <footer class="article-footer">
        <div class="article-tags" v-if="article.tags && article.tags.length > 0">
          <span 
            v-for="tag in article.tags" 
            :key="tag" 
            class="tag"
          >{{ tag }}</span>
        </div>
        
        <div class="article-actions">
          <button 
            @click="toggleLike" 
            :class="['action-button', { liked: article.isLiked }]"
          >
            <svg class="action-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/>
            </svg>
            <span>{{ article.stats.likes }}</span>
          </button>
          
          <button class="action-button">
            <svg class="action-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
            </svg>
            <span>{{ article.stats.comments }}</span>
          </button>
        </div>
      </footer>
    </article>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { marked } from 'marked'
import { contentAPI } from '@/api'
import { componentLogger } from '@/utils/logger'
import hljs from 'highlight.js'

const route = useRoute()
const router = useRouter()

const article = ref(null)
const loading = ref(true)
const error = ref(null)

// 配置 marked
marked.setOptions({
  highlight: function(code, lang) {
    if (lang && hljs.getLanguage(lang)) {
      try {
        return hljs.highlight(code, { language: lang }).value
      } catch (err) {
        console.error('代码高亮错误:', err)
      }
    }
    return hljs.highlightAuto(code).value
  },
  breaks: true,
  gfm: true
})

// 渲染 markdown 内容
const renderedContent = computed(() => {
  if (!article.value || !article.value.content) return ''
  
  // 如果内容已经是 HTML，直接返回
  if (article.value.content.startsWith('<')) {
    return article.value.content
  }
  
  // 如果是 markdown，转换为 HTML
  return marked.parse(article.value.content)
})

// 格式化日期
const formatDate = (dateString) => {
  if (!dateString) return ''
  const date = new Date(dateString)
  return date.toLocaleDateString('zh-CN', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  })
}

// 获取文章详情
const fetchArticleDetail = async () => {
  try {
    loading.value = true
    error.value = null
    
    const articleId = route.params.id
    componentLogger.info(`开始获取文章详情: ${articleId}`)
    
    if (!articleId) {
      const error = new Error('文章ID不存在')
      componentLogger.error('文章ID不存在', error)
      throw error
    }
    
    const response = await contentAPI.getArticleDetail(articleId)
    componentLogger.debug('文章详情响应', { id: articleId, hasContent: !!response.content })
    
    article.value = response
    
    componentLogger.info(`成功获取文章详情: ${response.title}`)
  } catch (err) {
    componentLogger.error('获取文章详情失败', err)
    error.value = err.message || '加载文章失败，请稍后重试'
  } finally {
    loading.value = false
  }
}

// 切换点赞状态
const toggleLike = async () => {
  if (!article.value) return
  
  try {
    if (article.value.isLiked) {
      await contentAPI.unlikeArticle(article.value.id)
      article.value.isLiked = false
      article.value.stats.likes = Math.max(0, article.value.stats.likes - 1)
    } else {
      await contentAPI.likeArticle(article.value.id)
      article.value.isLiked = true
      article.value.stats.likes += 1
    }
  } catch (err) {
    console.error('点赞操作失败:', err)
  }
}

// 返回上一页
const goBack = () => {
  router.back()
}

onMounted(() => {
  fetchArticleDetail()
})
</script>

<style scoped>
.article-detail-page {
  flex: 1;
  padding: 40px 48px;
  background-color: #ffffff;
  overflow-y: auto;
  height: 100vh;
  min-width: 0;
}

.loading-container,
.error-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 60vh;
  gap: 20px;
}

.loading-spinner {
  font-size: 16px;
  color: #666666;
}

.error-message {
  color: #ff4444;
  font-size: 16px;
}

.back-button,
.back-button-top {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 8px 16px;
  background-color: #f5f5f5;
  border: 1px solid #e0e0e0;
  border-radius: 6px;
  color: #000000;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.2s;
}

.back-button:hover,
.back-button-top:hover {
  background-color: #e8e8e8;
}

.back-button-top {
  margin-bottom: 32px;
}

.back-icon {
  width: 16px;
  height: 16px;
}

.article-container {
  max-width: 800px;
  margin: 0 auto;
}

.article-header {
  margin-bottom: 48px;
}

.article-meta {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 16px;
}

.department-tag {
  display: inline-block;
  padding: 6px 12px;
  background-color: #f5f5f5;
  color: #666666;
  border-radius: 6px;
  font-size: 13px;
  font-weight: 500;
}

.reading-time {
  font-size: 14px;
  color: #666666;
}

.article-title {
  font-size: 42px;
  font-weight: 700;
  color: #000000;
  line-height: 1.2;
  margin: 0 0 24px 0;
  letter-spacing: -0.5px;
}

.article-author-info {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 32px;
}

.author-avatar {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  object-fit: cover;
}

.author-details {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.author-name {
  font-size: 16px;
  font-weight: 600;
  color: #000000;
}

.publish-date {
  font-size: 14px;
  color: #666666;
}

.article-cover {
  width: 100%;
  border-radius: 12px;
  overflow: hidden;
  margin-bottom: 32px;
}

.article-cover img {
  width: 100%;
  height: auto;
  display: block;
}

.article-content-wrapper {
  margin-bottom: 48px;
}

.article-content {
  font-size: 16px;
  line-height: 1.8;
  color: #333333;
}

/* Markdown 样式 */
:deep(.markdown-body) {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
}

:deep(.markdown-body h1) {
  font-size: 32px;
  font-weight: 700;
  margin: 32px 0 16px 0;
  color: #000000;
  border-bottom: 2px solid #e0e0e0;
  padding-bottom: 8px;
}

:deep(.markdown-body h2) {
  font-size: 28px;
  font-weight: 700;
  margin: 28px 0 14px 0;
  color: #000000;
}

:deep(.markdown-body h3) {
  font-size: 24px;
  font-weight: 600;
  margin: 24px 0 12px 0;
  color: #000000;
}

:deep(.markdown-body h4) {
  font-size: 20px;
  font-weight: 600;
  margin: 20px 0 10px 0;
  color: #000000;
}

:deep(.markdown-body p) {
  margin: 16px 0;
  color: #333333;
}

:deep(.markdown-body ul),
:deep(.markdown-body ol) {
  margin: 16px 0;
  padding-left: 32px;
}

:deep(.markdown-body li) {
  margin: 8px 0;
  color: #333333;
}

:deep(.markdown-body blockquote) {
  margin: 16px 0;
  padding: 16px 20px;
  background-color: #f8f8f8;
  border-left: 4px solid #333333;
  border-radius: 4px;
}

:deep(.markdown-body blockquote p) {
  margin: 0;
  color: #666666;
  font-style: italic;
}

:deep(.markdown-body code) {
  background-color: #f5f5f5;
  padding: 2px 6px;
  border-radius: 4px;
  font-size: 14px;
  font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
  color: #e83e8c;
}

:deep(.markdown-body pre) {
  background-color: #1e1e1e;
  padding: 20px;
  border-radius: 8px;
  overflow-x: auto;
  margin: 20px 0;
}

:deep(.markdown-body pre code) {
  background-color: transparent;
  padding: 0;
  color: #d4d4d4;
  font-size: 14px;
  line-height: 1.6;
}

/* 代码高亮样式 */
:deep(.markdown-body pre code.hljs) {
  display: block;
  overflow-x: auto;
  padding: 0;
}

:deep(.markdown-body .hljs-keyword),
:deep(.markdown-body .hljs-selector-tag),
:deep(.markdown-body .hljs-literal),
:deep(.markdown-body .hljs-title),
:deep(.markdown-body .hljs-section),
:deep(.markdown-body .hljs-doctag),
:deep(.markdown-body .hljs-type),
:deep(.markdown-body .hljs-name),
:deep(.markdown-body .hljs-strong) {
  color: #c678dd;
}

:deep(.markdown-body .hljs-string),
:deep(.markdown-body .hljs-title),
:deep(.markdown-body .hljs-section),
:deep(.markdown-body .hljs-built_in),
:deep(.markdown-body .hljs-literal),
:deep(.markdown-body .hljs-type),
:deep(.markdown-body .hljs-addition),
:deep(.markdown-body .hljs-tag),
:deep(.markdown-body .hljs-quote),
:deep(.markdown-body .hljs-name),
:deep(.markdown-body .hljs-selector-id),
:deep(.markdown-body .hljs-selector-class) {
  color: #98c379;
}

:deep(.markdown-body .hljs-comment),
:deep(.markdown-body .hljs-deletion),
:deep(.markdown-body .hljs-meta) {
  color: #5c6370;
}

:deep(.markdown-body .hljs-number),
:deep(.markdown-body .hljs-regexp),
:deep(.markdown-body .hljs-symbol),
:deep(.markdown-body .hljs-variable),
:deep(.markdown-body .hljs-template-variable),
:deep(.markdown-body .hljs-link),
:deep(.markdown-body .hljs-selector-attr),
:deep(.markdown-body .hljs-selector-pseudo) {
  color: #e06c75;
}

:deep(.markdown-body .hljs-function),
:deep(.markdown-body .hljs-attr) {
  color: #61afef;
}

:deep(.markdown-body img) {
  max-width: 100%;
  height: auto;
  border-radius: 8px;
  margin: 24px 0;
}

:deep(.markdown-body a) {
  color: #333333;
  text-decoration: underline;
  text-decoration-color: #999999;
  transition: color 0.2s;
}

:deep(.markdown-body a:hover) {
  color: #000000;
  text-decoration-color: #000000;
}

:deep(.markdown-body table) {
  width: 100%;
  border-collapse: collapse;
  margin: 20px 0;
}

:deep(.markdown-body th),
:deep(.markdown-body td) {
  padding: 12px;
  border: 1px solid #e0e0e0;
  text-align: left;
}

:deep(.markdown-body th) {
  background-color: #f5f5f5;
  font-weight: 600;
}

:deep(.markdown-body hr) {
  border: none;
  border-top: 1px solid #e0e0e0;
  margin: 32px 0;
}

.article-footer {
  padding-top: 32px;
  border-top: 1px solid #e0e0e0;
}

.article-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 24px;
}

.tag {
  display: inline-block;
  padding: 6px 12px;
  background-color: #f5f5f5;
  color: #666666;
  border-radius: 6px;
  font-size: 13px;
}

.article-actions {
  display: flex;
  gap: 16px;
}

.action-button {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 10px 20px;
  background-color: #f5f5f5;
  border: 1px solid #e0e0e0;
  border-radius: 6px;
  color: #000000;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.2s;
}

.action-button:hover {
  background-color: #e8e8e8;
}

.action-button.liked {
  background-color: #ff4444;
  color: #ffffff;
  border-color: #ff4444;
}

.action-icon {
  width: 18px;
  height: 18px;
}

/* 移动端适配 */
@media (max-width: 768px) {
  .article-detail-page {
    padding: 16px;
    padding-top: 80px;
    padding-bottom: 80px;
  }

  .article-title {
    font-size: 28px;
  }

  .article-content {
    font-size: 15px;
  }

  :deep(.markdown-body h1) {
    font-size: 24px;
  }

  :deep(.markdown-body h2) {
    font-size: 22px;
  }

  :deep(.markdown-body h3) {
    font-size: 20px;
  }
}
</style>

