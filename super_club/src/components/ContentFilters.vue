<template>
  <div class="content-filters">
    <div class="main-tabs">
      <button 
        v-for="tab in mainTabs" 
        :key="tab"
        :class="['main-tab', { active: activeMainTab === tab }]"
        @click="activeMainTab = tab"
      >
        {{ tab }}
      </button>
    </div>

    <div class="filter-section">
      <div class="filter-label">部门筛选</div>
      <div class="filter-buttons">
        <button 
          v-for="dept in departments" 
          :key="dept"
          :class="['filter-btn', { active: activeDepartment === dept }]"
          @click="activeDepartment = dept"
        >
          {{ dept }}
        </button>
      </div>
    </div>

    <div class="filter-section">
      <div class="filter-label">内容类型</div>
      <div class="filter-buttons">
        <button 
          v-for="type in contentTypes" 
          :key="type"
          :class="['filter-btn', { active: activeContentType === type }]"
          @click="activeContentType = type"
        >
          {{ type }}
        </button>
      </div>
    </div>

    <div class="search-section">
      <div class="search-box">
        <svg class="search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="11" cy="11" r="8"></circle>
          <path d="m21 21-4.35-4.35"></path>
        </svg>
        <input type="text" placeholder="搜索..." class="search-input" />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const activeMainTab = ref('全部文章')
const activeDepartment = ref('不限')
const activeContentType = ref('不限')

const mainTabs = ['全部文章', '资料分享', '行业数据库']
const departments = ['不限', '战略部', '品牌部', '销售部', '财法部', '人力部', '技术部']
const contentTypes = ['不限', '书籍播客', '大佬思维', '案例拆解', '运营笔记', '时事观点']
</script>

<style scoped>
.content-filters {
  margin-top: 48px;
}

.main-tabs {
  display: flex;
  gap: 0;
  border-bottom: 1px solid #e0e0e0;
  margin-bottom: 32px;
}

.main-tab {
  padding: 12px 24px;
  background: none;
  border: none;
  font-size: 16px;
  color: #666666;
  cursor: pointer;
  position: relative;
  transition: color 0.2s;
  border-bottom: 2px solid transparent;
}

.main-tab:hover {
  color: #000000;
}

.main-tab.active {
  color: #000000;
  border-bottom-color: #000000;
}

.filter-section {
  margin-bottom: 24px;
}

.filter-label {
  font-size: 14px;
  color: #666666;
  margin-bottom: 12px;
}

.filter-buttons {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}

.filter-btn {
  padding: 8px 16px;
  background-color: #f5f5f5;
  border: 1px solid #e0e0e0;
  border-radius: 6px;
  font-size: 14px;
  color: #000000;
  cursor: pointer;
  transition: all 0.2s;
}

.filter-btn:hover {
  background-color: #eeeeee;
}

.filter-btn.active {
  background-color: #333333;
  color: #ffffff;
  border-color: #333333;
}

.search-section {
  margin-top: 32px;
}

.search-box {
  position: relative;
  max-width: 400px;
}

.search-icon {
  position: absolute;
  left: 12px;
  top: 50%;
  transform: translateY(-50%);
  width: 18px;
  height: 18px;
  color: #999999;
}

.search-input {
  width: 100%;
  padding: 12px 12px 12px 40px;
  border: 1px solid #e0e0e0;
  border-radius: 6px;
  font-size: 14px;
  background-color: #ffffff;
  transition: border-color 0.2s;
}

.search-input:focus {
  outline: none;
  border-color: #333333;
}
</style>

