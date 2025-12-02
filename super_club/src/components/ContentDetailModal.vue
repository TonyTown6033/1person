<template>
  <Teleport to="body">
    <div v-if="visible" class="content-detail-overlay" @click="handleClose">
      <div class="content-detail-modal" @click.stop>
        <!-- 关闭按钮 -->
        <button class="close-btn" @click="handleClose">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M18 6L6 18M6 6l12 12"/>
          </svg>
        </button>

        <!-- 加载状态 -->
        <div v-if="loading" class="loading-container">
          <div class="loading-spinner"></div>
          <p>加载中...</p>
        </div>

        <!-- 内容详情 -->
        <div v-else-if="content" class="detail-container">
          <!-- 封面图 -->
          <div v-if="content.coverImage" class="cover-section">
            <img :src="content.coverImage" :alt="content.title" />
          </div>

          <!-- 内容主体 -->
          <div class="content-body">
            <!-- 标题 -->
            <h1 class="content-title">{{ content.title }}</h1>

            <!-- 元信息 -->
            <div class="meta-info">
              <div class="author-info" v-if="content.author">
                <div class="author-avatar">
                  <img v-if="content.author.avatar" :src="content.author.avatar" :alt="content.author.name" />
                  <span v-else class="avatar-placeholder">{{ (content.author.name || '未')[0] }}</span>
                </div>
                <span class="author-name">{{ content.author.name || '未知作者' }}</span>
              </div>
              <span class="meta-divider">·</span>
              <span class="publish-time">{{ formatDate(content.publishedAt || content.createdAt) }}</span>
              <span class="meta-divider">·</span>
              <span class="reading-time">{{ content.readingTime || 5 }} 分钟阅读</span>
            </div>

            <!-- 标签和分类 -->
            <div class="tags-section">
              <span class="type-tag" :class="content.type">
                {{ getTypeLabel(content.type) }}
              </span>
              <span v-if="content.department" class="department-tag">
                {{ content.department }}
              </span>
              <span v-for="tag in (content.tags || [])" :key="tag" class="content-tag">
                {{ tag }}
              </span>
            </div>

            <!-- 摘要 -->
            <div v-if="content.excerpt || content.description" class="excerpt-section">
              <p>{{ content.excerpt || content.description }}</p>
            </div>

            <!-- 正文 -->
            <div class="article-content-wrapper">
              <div v-if="content.content" class="article-content" v-html="formatContent(content.content)"></div>
              <div v-else class="no-content">
                <p>暂无正文内容</p>
              </div>
            </div>

            <!-- 统计数据 -->
            <div class="stats-section">
              <div class="stat-item">
                <span class="stat-icon">👁</span>
                <span class="stat-value">{{ content.viewCount || 0 }}</span>
                <span class="stat-label">阅读</span>
              </div>
              <div class="stat-item">
                <span class="stat-icon">❤️</span>
                <span class="stat-value">{{ content.likeCount || 0 }}</span>
                <span class="stat-label">点赞</span>
              </div>
              <div class="stat-item">
                <span class="stat-icon">💬</span>
                <span class="stat-value">{{ content.commentCount || 0 }}</span>
                <span class="stat-label">评论</span>
              </div>
            </div>

            <!-- 操作按钮（管理模式） -->
            <div v-if="isAdmin" class="admin-actions">
              <button @click="$emit('edit', content)" class="action-btn edit-btn">
                ✏️ 编辑内容
              </button>
              <button @click="$emit('toggle-publish', content)" class="action-btn publish-btn">
                {{ content.isPublished ? '📤 取消发布' : '📥 发布内容' }}
              </button>
            </div>

            <!-- 操作按钮（用户模式） -->
            <div v-else class="user-actions">
              <button @click="handleLike" class="action-btn like-btn" :class="{ liked: isLiked }">
                {{ isLiked ? '❤️' : '🤍' }} {{ isLiked ? '已点赞' : '点赞' }}
              </button>
              <button @click="handleShare" class="action-btn share-btn">
                📤 分享
              </button>
            </div>
          </div>
        </div>

        <!-- 错误状态 -->
        <div v-else class="error-container">
          <p>😔 加载失败，请重试</p>
          <button @click="$emit('retry')" class="retry-btn">重新加载</button>
        </div>
      </div>
    </div>
  </Teleport>
</template>

<script>
import { ref, watch } from 'vue'

export default {
  name: 'ContentDetailModal',
  props: {
    visible: {
      type: Boolean,
      default: false
    },
    content: {
      type: Object,
      default: null
    },
    loading: {
      type: Boolean,
      default: false
    },
    isAdmin: {
      type: Boolean,
      default: false
    }
  },
  emits: ['close', 'edit', 'toggle-publish', 'like', 'share', 'retry'],
  setup(props, { emit }) {
    const isLiked = ref(false)

    // 监听内容变化，重置点赞状态
    watch(() => props.content, (newContent) => {
      if (newContent) {
        // 可以从localStorage或API获取点赞状态
        isLiked.value = false
      }
    })

    const handleClose = () => {
      emit('close')
    }

    const handleLike = () => {
      isLiked.value = !isLiked.value
      emit('like', props.content, isLiked.value)
    }

    const handleShare = () => {
      // 复制链接到剪贴板
      if (props.content) {
        const url = `${window.location.origin}/articles/${props.content.id}`
        navigator.clipboard.writeText(url).then(() => {
          alert('链接已复制到剪贴板')
        }).catch(() => {
          alert('复制失败，请手动复制')
        })
      }
      emit('share', props.content)
    }

    const formatDate = (dateStr) => {
      if (!dateStr) return ''
      const date = new Date(dateStr)
      const now = new Date()
      const diff = now - date
      const days = Math.floor(diff / (1000 * 60 * 60 * 24))
      
      if (days === 0) {
        const hours = Math.floor(diff / (1000 * 60 * 60))
        if (hours === 0) {
          const minutes = Math.floor(diff / (1000 * 60))
          return minutes <= 0 ? '刚刚' : `${minutes} 分钟前`
        }
        return `${hours} 小时前`
      } else if (days < 7) {
        return `${days} 天前`
      } else {
        return date.toLocaleDateString('zh-CN', {
          year: 'numeric',
          month: 'long',
          day: 'numeric'
        })
      }
    }

    const getTypeLabel = (type) => {
      const labels = {
        article: '文章',
        video: '视频',
        course: '课程'
      }
      return labels[type] || type || '文章'
    }

    const formatContent = (content) => {
      if (!content) return ''
      // Markdown 简单转换
      let html = content
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        // 标题
        .replace(/^### (.+)$/gm, '<h4>$1</h4>')
        .replace(/^## (.+)$/gm, '<h3>$1</h3>')
        .replace(/^# (.+)$/gm, '<h2>$1</h2>')
        // 粗体和斜体
        .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
        .replace(/\*(.+?)\*/g, '<em>$1</em>')
        // 代码
        .replace(/`(.+?)`/g, '<code>$1</code>')
        // 链接
        .replace(/\[(.+?)\]\((.+?)\)/g, '<a href="$2" target="_blank">$1</a>')
        // 列表
        .replace(/^\- (.+)$/gm, '<li>$1</li>')
        // 换行
        .replace(/\n\n/g, '</p><p>')
        .replace(/\n/g, '<br>')
      
      return `<p>${html}</p>`
    }

    return {
      isLiked,
      handleClose,
      handleLike,
      handleShare,
      formatDate,
      getTypeLabel,
      formatContent
    }
  }
}
</script>

<style scoped>
.content-detail-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.6);
  backdrop-filter: blur(4px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
  padding: 20px;
  animation: fadeIn 0.2s ease;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

.content-detail-modal {
  background: white;
  border-radius: 16px;
  width: 100%;
  max-width: 800px;
  max-height: 90vh;
  overflow: hidden;
  position: relative;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
  animation: slideUp 0.3s ease;
}

@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.close-btn {
  position: absolute;
  top: 16px;
  right: 16px;
  width: 40px;
  height: 40px;
  border: none;
  background: rgba(255, 255, 255, 0.9);
  border-radius: 50%;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 10;
  transition: all 0.2s;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.close-btn:hover {
  background: white;
  transform: scale(1.1);
}

.close-btn svg {
  width: 20px;
  height: 20px;
  color: #333;
}

/* 加载状态 */
.loading-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 80px 40px;
  color: #666;
}

.loading-spinner {
  width: 48px;
  height: 48px;
  border: 3px solid #f0f0f0;
  border-top-color: #667eea;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-bottom: 16px;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

/* 错误状态 */
.error-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 80px 40px;
  color: #666;
}

.retry-btn {
  margin-top: 16px;
  padding: 10px 20px;
  background: #667eea;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
}

/* 内容区域 */
.detail-container {
  overflow-y: auto;
  max-height: 90vh;
}

.cover-section {
  width: 100%;
  height: 300px;
  overflow: hidden;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.cover-section img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.content-body {
  padding: 32px;
}

.content-title {
  font-size: 28px;
  font-weight: 700;
  color: #1a1a2e;
  line-height: 1.4;
  margin: 0 0 20px 0;
}

/* 元信息 */
.meta-info {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 20px;
  font-size: 14px;
  color: #666;
}

.author-info {
  display: flex;
  align-items: center;
  gap: 8px;
}

.author-avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  overflow: hidden;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.author-avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.avatar-placeholder {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: 600;
  font-size: 14px;
}

.author-name {
  font-weight: 500;
  color: #333;
}

.meta-divider {
  color: #ddd;
}

/* 标签 */
.tags-section {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 24px;
}

.type-tag {
  padding: 4px 12px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 600;
}

.type-tag.article {
  background: #e3f2fd;
  color: #1976d2;
}

.type-tag.video {
  background: #fce4ec;
  color: #c2185b;
}

.type-tag.course {
  background: #fff3e0;
  color: #f57c00;
}

.department-tag {
  padding: 4px 12px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 500;
  background: #f3e5f5;
  color: #7b1fa2;
}

.content-tag {
  padding: 4px 12px;
  border-radius: 16px;
  font-size: 12px;
  background: #f5f5f5;
  color: #666;
}

/* 摘要 */
.excerpt-section {
  background: linear-gradient(135deg, #f8f9ff 0%, #f5f0ff 100%);
  border-left: 4px solid #667eea;
  padding: 20px 24px;
  border-radius: 0 12px 12px 0;
  margin-bottom: 24px;
}

.excerpt-section p {
  margin: 0;
  font-size: 15px;
  line-height: 1.7;
  color: #555;
  font-style: italic;
}

/* 正文 */
.article-content-wrapper {
  margin-bottom: 32px;
  min-height: 100px;
}

.article-content {
  font-size: 16px;
  line-height: 1.8;
  color: #333;
}

.no-content {
  padding: 40px;
  text-align: center;
  color: #999;
  background: #f8f9fa;
  border-radius: 8px;
}

.article-content :deep(h2) {
  font-size: 22px;
  font-weight: 700;
  color: #1a1a2e;
  margin: 32px 0 16px 0;
  padding-bottom: 8px;
  border-bottom: 2px solid #f0f0f0;
}

.article-content :deep(h3) {
  font-size: 18px;
  font-weight: 600;
  color: #1a1a2e;
  margin: 24px 0 12px 0;
}

.article-content :deep(h4) {
  font-size: 16px;
  font-weight: 600;
  color: #1a1a2e;
  margin: 20px 0 10px 0;
}

.article-content :deep(p) {
  margin: 0 0 16px 0;
}

.article-content :deep(code) {
  background: #f5f5f5;
  padding: 2px 8px;
  border-radius: 4px;
  font-family: 'Monaco', 'Menlo', 'Consolas', monospace;
  font-size: 14px;
  color: #e74c3c;
}

.article-content :deep(strong) {
  font-weight: 600;
  color: #1a1a2e;
}

.article-content :deep(em) {
  font-style: italic;
  color: #666;
}

.article-content :deep(a) {
  color: #667eea;
  text-decoration: none;
}

.article-content :deep(a:hover) {
  text-decoration: underline;
}

.article-content :deep(li) {
  margin: 8px 0;
  padding-left: 8px;
}

/* 统计 */
.stats-section {
  display: flex;
  justify-content: center;
  gap: 48px;
  padding: 24px;
  background: #f8f9fa;
  border-radius: 12px;
  margin-bottom: 24px;
}

.stat-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
}

.stat-icon {
  font-size: 24px;
}

.stat-value {
  font-size: 20px;
  font-weight: 700;
  color: #1a1a2e;
}

.stat-label {
  font-size: 12px;
  color: #666;
}

/* 操作按钮 */
.admin-actions,
.user-actions {
  display: flex;
  justify-content: center;
  gap: 16px;
  padding-top: 24px;
  border-top: 1px solid #f0f0f0;
}

.action-btn {
  padding: 12px 24px;
  border: none;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 8px;
  transition: all 0.2s;
}

.edit-btn {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

.edit-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
}

.publish-btn {
  background: #f0f0f0;
  color: #333;
}

.publish-btn:hover {
  background: #e0e0e0;
}

.like-btn {
  background: #fff0f0;
  color: #e74c3c;
}

.like-btn.liked {
  background: #e74c3c;
  color: white;
}

.like-btn:hover {
  transform: scale(1.05);
}

.share-btn {
  background: #e3f2fd;
  color: #1976d2;
}

.share-btn:hover {
  background: #bbdefb;
}

/* 响应式 */
@media (max-width: 768px) {
  .content-detail-modal {
    max-width: 100%;
    max-height: 100vh;
    border-radius: 0;
  }

  .cover-section {
    height: 200px;
  }

  .content-body {
    padding: 20px;
  }

  .content-title {
    font-size: 22px;
  }

  .meta-info {
    font-size: 13px;
  }

  .stats-section {
    gap: 24px;
  }

  .admin-actions,
  .user-actions {
    flex-direction: column;
  }

  .action-btn {
    width: 100%;
    justify-content: center;
  }
}
</style>

