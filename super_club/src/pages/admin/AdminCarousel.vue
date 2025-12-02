<template>
  <div class="admin-carousel">
    <div class="page-header">
      <div class="header-left">
        <h2>轮播管理</h2>
        <p>管理首页轮播图和推荐内容</p>
      </div>
      <div class="header-right">
        <button @click="showAddModal = true" class="btn-primary">
          <span>🖼️</span>
          添加轮播
        </button>
      </div>
    </div>
    
    <div class="content-placeholder">
      <div class="placeholder-icon">🖼️</div>
      <h3>轮播管理功能</h3>
      <p>此页面将包含轮播图的管理和配置功能</p>
      <ul class="feature-list">
        <li>轮播图上传和编辑</li>
        <li>轮播顺序调整</li>
        <li>链接地址配置</li>
        <li>显示状态控制</li>
        <li>轮播效果预览</li>
      </ul>
    </div>
    
    <div v-if="showAddModal" class="modal-overlay" @click="showAddModal = false">
      <div class="modal-content" @click.stop>
        <div class="modal-header">
          <h3>添加轮播</h3>
          <button @click="showAddModal = false" class="close-btn">✕</button>
        </div>
        <div class="modal-body">
          <p>轮播添加功能正在开发中...</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'

export default {
  name: 'AdminCarousel',
  setup() {
    const showAddModal = ref(false)
    
    return {
      showAddModal
    }
  }
}
</script>

<style scoped>
.admin-carousel {
  max-width: 1400px;
  margin: 0 auto;
}

.page-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 30px;
}

.header-left h2 {
  margin: 0 0 8px 0;
  font-size: 28px;
  font-weight: 600;
  color: #2c3e50;
}

.header-left p {
  margin: 0;
  color: #666;
  font-size: 16px;
}

.btn-primary {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  padding: 12px 20px;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 8px;
  transition: transform 0.2s, box-shadow 0.2s;
}

.btn-primary:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
}

.content-placeholder {
  background: white;
  border-radius: 12px;
  padding: 60px 40px;
  text-align: center;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.placeholder-icon {
  font-size: 64px;
  margin-bottom: 24px;
}

.content-placeholder h3 {
  margin: 0 0 16px 0;
  font-size: 24px;
  color: #2c3e50;
}

.content-placeholder p {
  margin: 0 0 24px 0;
  color: #666;
  font-size: 16px;
}

.feature-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: inline-block;
  text-align: left;
}

.feature-list li {
  padding: 8px 0;
  color: #666;
  position: relative;
  padding-left: 20px;
}

.feature-list li:before {
  content: '✓';
  position: absolute;
  left: 0;
  color: #27ae60;
  font-weight: bold;
}

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.modal-content {
  background: white;
  border-radius: 12px;
  width: 90%;
  max-width: 500px;
}

.modal-header {
  padding: 24px 24px 0 24px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.modal-header h3 {
  margin: 0;
  font-size: 20px;
  font-weight: 600;
  color: #2c3e50;
}

.close-btn {
  background: none;
  border: none;
  font-size: 20px;
  cursor: pointer;
  color: #666;
  padding: 4px;
  border-radius: 4px;
  transition: background-color 0.2s;
}

.close-btn:hover {
  background-color: #f0f0f0;
}

.modal-body {
  padding: 24px;
  text-align: center;
  color: #666;
}
</style>
