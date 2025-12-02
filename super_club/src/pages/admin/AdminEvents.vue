<template>
  <div class="admin-events">
    <div class="page-header">
      <div class="header-left">
        <h2>活动管理</h2>
        <p>管理系统中的所有活动</p>
      </div>
      <div class="header-right">
        <button @click="showAddModal = true" class="btn-primary">
          <span>📅</span>
          添加活动
        </button>
      </div>
    </div>
    
    <div class="content-placeholder">
      <div class="placeholder-icon">📅</div>
      <h3>活动管理功能</h3>
      <p>此页面将包含活动的创建、编辑、删除和状态管理功能</p>
      <ul class="feature-list">
        <li>活动列表展示</li>
        <li>活动状态管理（即将开始、进行中、已结束）</li>
        <li>报名人数统计</li>
        <li>活动分类筛选</li>
        <li>活动详情编辑</li>
      </ul>
    </div>
    
    <!-- 简单的模态框占位 -->
    <div v-if="showAddModal" class="modal-overlay" @click="showAddModal = false">
      <div class="modal-content" @click.stop>
        <div class="modal-header">
          <h3>添加活动</h3>
          <button @click="showAddModal = false" class="close-btn">✕</button>
        </div>
        <div class="modal-body">
          <p>活动添加功能正在开发中...</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'

export default {
  name: 'AdminEvents',
  setup() {
    const showAddModal = ref(false)
    
    return {
      showAddModal
    }
  }
}
</script>

<style scoped>
.admin-events {
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

/* 模态框样式 */
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
