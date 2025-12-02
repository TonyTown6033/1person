<template>
  <div class="article-item" @click="handleClick">
    <div class="article-image">
      <img :src="article.image" :alt="article.title" />
    </div>
    <div class="article-content">
      <div class="article-meta">
        <span class="department-tag">{{ article.department }}</span>
      </div>
      <h3 class="article-title">{{ article.title }}</h3>
      <p class="article-description">{{ article.description }}</p>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  article: {
    type: Object,
    required: true
  }
})

const emit = defineEmits(['view-detail'])

const handleClick = () => {
  emit('view-detail', props.article)
}
</script>

<style scoped>
.article-item {
  display: flex;
  gap: 20px;
  padding: 20px;
  background-color: #ffffff;
  border-radius: 8px;
  border: 1px solid #f0f0f0;
  transition: box-shadow 0.2s;
  text-decoration: none;
  color: inherit;
  cursor: pointer;
}

.article-item:hover {
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

.article-image {
  width: 160px;
  height: 120px;
  flex-shrink: 0;
  border-radius: 6px;
  overflow: hidden;
  background-color: #f0f0f0;
}

.article-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.article-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.article-meta {
  margin-bottom: 4px;
}

.department-tag {
  display: inline-block;
  padding: 4px 10px;
  background-color: #f5f5f5;
  color: #666666;
  border-radius: 4px;
  font-size: 12px;
}

.article-title {
  font-size: 18px;
  font-weight: 600;
  color: #000000;
  margin: 0;
  line-height: 1.4;
}

.article-description {
  font-size: 14px;
  color: #666666;
  line-height: 1.6;
  margin: 0;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>

