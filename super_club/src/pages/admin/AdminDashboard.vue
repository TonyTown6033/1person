<template>
  <div class="admin-dashboard">
    <!-- 统计卡片 -->
    <div class="stats-grid">
      <div class="stat-card" v-for="stat in stats" :key="stat.key">
        <div class="stat-icon" :style="{ backgroundColor: stat.color }">
          {{ stat.icon }}
        </div>
        <div class="stat-content">
          <div class="stat-value">{{ stat.value }}</div>
          <div class="stat-label">{{ stat.label }}</div>
          <div class="stat-change" :class="stat.changeType">
            {{ stat.change }}
          </div>
        </div>
      </div>
    </div>
    
    <!-- 图表和表格区域 -->
    <div class="dashboard-grid">
      <!-- 最近活动 -->
      <div class="dashboard-card">
        <div class="card-header">
          <h3>最近活动</h3>
          <button @click="refreshActivities" class="refresh-btn">刷新</button>
        </div>
        <div class="card-content">
          <div v-if="loading.activities" class="loading">加载中...</div>
          <div v-else-if="recentActivities.length === 0" class="empty-state">
            暂无活动数据
          </div>
          <div v-else class="activity-list">
            <div 
              v-for="activity in recentActivities" 
              :key="activity.id"
              class="activity-item"
            >
              <div class="activity-icon">{{ activity.icon }}</div>
              <div class="activity-content">
                <div class="activity-title">{{ activity.title }}</div>
                <div class="activity-time">{{ formatTime(activity.time) }}</div>
              </div>
            </div>
          </div>
        </div>
      </div>
      
      <!-- 系统状态 -->
      <div class="dashboard-card">
        <div class="card-header">
          <h3>系统状态</h3>
        </div>
        <div class="card-content">
          <div class="status-list">
            <div 
              v-for="status in systemStatus" 
              :key="status.name"
              class="status-item"
            >
              <div class="status-name">{{ status.name }}</div>
              <div class="status-value" :class="status.status">
                {{ status.value }}
              </div>
            </div>
          </div>
        </div>
      </div>
      
      <!-- 快速操作 -->
      <div class="dashboard-card">
        <div class="card-header">
          <h3>快速操作</h3>
        </div>
        <div class="card-content">
          <div class="quick-actions">
            <button 
              v-for="action in quickActions" 
              :key="action.name"
              @click="handleQuickAction(action)"
              class="action-btn"
              :style="{ backgroundColor: action.color }"
            >
              <span class="action-icon">{{ action.icon }}</span>
              <span class="action-text">{{ action.name }}</span>
            </button>
          </div>
        </div>
      </div>
      
      <!-- 数据概览 -->
      <div class="dashboard-card full-width">
        <div class="card-header">
          <h3>数据概览</h3>
          <select v-model="selectedPeriod" @change="updateChartData" class="period-select">
            <option value="7d">最近7天</option>
            <option value="30d">最近30天</option>
            <option value="90d">最近90天</option>
          </select>
        </div>
        <div class="card-content">
          <div class="chart-placeholder">
            <div class="chart-info">
              <p>📈 用户增长趋势</p>
              <p>📊 内容发布统计</p>
              <p>🎯 活动参与度</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { adminAPI } from '../../api/admin.js'

export default {
  name: 'AdminDashboard',
  setup() {
    const router = useRouter()
    const loading = ref({
      activities: false
    })
    const selectedPeriod = ref('7d')
    
    // 统计数据
    const stats = ref([
      {
        key: 'users',
        icon: '👥',
        label: '总用户数',
        value: '0',
        change: '+0%',
        changeType: 'positive',
        color: '#3498db'
      },
      {
        key: 'projects',
        icon: '🚀',
        label: '活跃项目',
        value: '0',
        change: '+0%',
        changeType: 'positive',
        color: '#e74c3c'
      },
      {
        key: 'events',
        icon: '📅',
        label: '即将举办',
        value: '0',
        change: '+0%',
        changeType: 'positive',
        color: '#f39c12'
      },
      {
        key: 'content',
        icon: '📝',
        label: '已发布内容',
        value: '0',
        change: '+0%',
        changeType: 'positive',
        color: '#27ae60'
      }
    ])
    
    // 最近活动
    const recentActivities = ref([
      {
        id: 1,
        icon: '👤',
        title: '新用户注册：张三',
        time: new Date(Date.now() - 1000 * 60 * 5)
      },
      {
        id: 2,
        icon: '🚀',
        title: '新项目发布：AI智能助手',
        time: new Date(Date.now() - 1000 * 60 * 15)
      },
      {
        id: 3,
        icon: '📅',
        title: '活动报名：技术分享会',
        time: new Date(Date.now() - 1000 * 60 * 30)
      },
      {
        id: 4,
        icon: '📝',
        title: '内容发布：Vue3最佳实践',
        time: new Date(Date.now() - 1000 * 60 * 45)
      }
    ])
    
    // 系统状态
    const systemStatus = ref([
      { name: '服务器状态', value: '正常', status: 'healthy' },
      { name: '数据库连接', value: '正常', status: 'healthy' },
      { name: '缓存服务', value: '正常', status: 'healthy' },
      { name: '存储空间', value: '78%', status: 'warning' }
    ])
    
    // 快速操作
    const quickActions = ref([
      { name: '添加用户', icon: '👤', color: '#3498db', action: 'add-user' },
      { name: '发布内容', icon: '📝', color: '#27ae60', action: 'add-content' },
      { name: '创建活动', icon: '📅', color: '#f39c12', action: 'add-event' },
      { name: '系统设置', icon: '⚙️', color: '#95a5a6', action: 'settings' }
    ])
    
    const formatTime = (time) => {
      const now = new Date()
      const diff = now - time
      const minutes = Math.floor(diff / (1000 * 60))
      const hours = Math.floor(diff / (1000 * 60 * 60))
      const days = Math.floor(diff / (1000 * 60 * 60 * 24))
      
      if (minutes < 60) {
        return `${minutes}分钟前`
      } else if (hours < 24) {
        return `${hours}小时前`
      } else {
        return `${days}天前`
      }
    }
    
    const refreshActivities = () => {
      loading.value.activities = true
      // 模拟API调用
      setTimeout(() => {
        loading.value.activities = false
      }, 1000)
    }
    
    const updateChartData = () => {
      console.log('更新图表数据:', selectedPeriod.value)
    }
    
    const handleQuickAction = (action) => {
      switch (action.action) {
        case 'add-user':
          router.push('/admin/users')
          break
        case 'add-content':
          router.push('/admin/content')
          break
        case 'add-event':
          router.push('/admin/events')
          break
        case 'settings':
          console.log('打开系统设置')
          break
      }
    }
    
    const loadDashboardData = async () => {
      try {
        // 加载统计数据
        const data = await adminAPI.getDashboardStats()
        
        if (data) {
          // 更新统计卡片数据 - 用户
          stats.value[0].value = (data.users?.total || 0).toLocaleString()
          stats.value[0].change = `+${data.users?.growth_rate || 0}%`
          
          // 项目 - 防止除以0
          const projectsTotal = data.projects?.total || 0
          const projectsActive = data.projects?.active || 0
          stats.value[1].value = projectsActive.toString()
          stats.value[1].change = projectsTotal > 0 
            ? `+${Math.round((projectsActive / projectsTotal) * 100)}%` 
            : '+0%'
          
          // 活动 - 防止除以0
          const eventsTotal = data.events?.total || 0
          const eventsUpcoming = data.events?.upcoming || 0
          stats.value[2].value = eventsUpcoming.toString()
          stats.value[2].change = eventsTotal > 0 
            ? `+${Math.round((eventsUpcoming / eventsTotal) * 100)}%` 
            : '+0%'
          
          // 内容 - 防止除以0
          const contentTotal = data.content?.total || 0
          const contentPublished = data.content?.published || 0
          stats.value[3].value = contentPublished.toString()
          stats.value[3].change = contentTotal > 0 
            ? `+${Math.round((contentPublished / contentTotal) * 100)}%` 
            : '+0%'
        }
        
        // 加载最近活动
        const activitiesData = await adminAPI.getRecentActivities(10)
        if (activitiesData && Array.isArray(activitiesData)) {
          recentActivities.value = activitiesData.map(activity => ({
            id: activity.id,
            icon: activity.icon,
            title: activity.title,
            time: new Date(activity.time)
          }))
        }
      } catch (error) {
        console.error('加载仪表板数据失败:', error)
      }
    }
    
    onMounted(() => {
      loadDashboardData()
    })
    
    return {
      stats,
      recentActivities,
      systemStatus,
      quickActions,
      loading,
      selectedPeriod,
      formatTime,
      refreshActivities,
      updateChartData,
      handleQuickAction
    }
  }
}
</script>

<style scoped>
.admin-dashboard {
  max-width: 1400px;
  margin: 0 auto;
}

/* 统计卡片网格 */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
  margin-bottom: 30px;
}

.stat-card {
  background: white;
  border-radius: 12px;
  padding: 24px;
  display: flex;
  align-items: center;
  gap: 16px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s, box-shadow 0.2s;
}

.stat-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
}

.stat-icon {
  width: 60px;
  height: 60px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
  color: white;
}

.stat-content {
  flex: 1;
}

.stat-value {
  font-size: 28px;
  font-weight: 700;
  color: #2c3e50;
  margin-bottom: 4px;
}

.stat-label {
  font-size: 14px;
  color: #666;
  margin-bottom: 8px;
}

.stat-change {
  font-size: 12px;
  font-weight: 600;
  padding: 4px 8px;
  border-radius: 4px;
  display: inline-block;
}

.stat-change.positive {
  color: #27ae60;
  background-color: #d5f4e6;
}

.stat-change.negative {
  color: #e74c3c;
  background-color: #fdf2f2;
}

/* 仪表板网格 */
.dashboard-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 20px;
}

.dashboard-card {
  background: white;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  overflow: hidden;
}

.dashboard-card.full-width {
  grid-column: 1 / -1;
}

.card-header {
  padding: 20px 24px;
  border-bottom: 1px solid #e1e5e9;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.card-header h3 {
  margin: 0;
  font-size: 18px;
  font-weight: 600;
  color: #2c3e50;
}

.refresh-btn {
  background: none;
  border: 1px solid #ddd;
  padding: 6px 12px;
  border-radius: 6px;
  font-size: 12px;
  cursor: pointer;
  transition: all 0.2s;
}

.refresh-btn:hover {
  background-color: #f8f9fa;
  border-color: #bbb;
}

.period-select {
  padding: 6px 12px;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-size: 14px;
}

.card-content {
  padding: 24px;
}

/* 活动列表 */
.activity-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.activity-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px;
  border-radius: 8px;
  transition: background-color 0.2s;
}

.activity-item:hover {
  background-color: #f8f9fa;
}

.activity-icon {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background-color: #e3f2fd;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 16px;
}

.activity-content {
  flex: 1;
}

.activity-title {
  font-size: 14px;
  font-weight: 500;
  color: #2c3e50;
  margin-bottom: 4px;
}

.activity-time {
  font-size: 12px;
  color: #666;
}

/* 系统状态 */
.status-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.status-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 0;
  border-bottom: 1px solid #f0f0f0;
}

.status-item:last-child {
  border-bottom: none;
}

.status-name {
  font-size: 14px;
  color: #2c3e50;
}

.status-value {
  font-size: 14px;
  font-weight: 500;
  padding: 4px 8px;
  border-radius: 4px;
}

.status-value.healthy {
  color: #27ae60;
  background-color: #d5f4e6;
}

.status-value.warning {
  color: #f39c12;
  background-color: #fef9e7;
}

.status-value.error {
  color: #e74c3c;
  background-color: #fdf2f2;
}

/* 快速操作 */
.quick-actions {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
  gap: 12px;
}

.action-btn {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  padding: 20px 12px;
  border: none;
  border-radius: 8px;
  color: white;
  cursor: pointer;
  transition: transform 0.2s, box-shadow 0.2s;
}

.action-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.action-icon {
  font-size: 20px;
}

.action-text {
  font-size: 12px;
  font-weight: 500;
}

/* 图表占位符 */
.chart-placeholder {
  height: 300px;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #f8f9fa;
  border-radius: 8px;
  border: 2px dashed #ddd;
}

.chart-info {
  text-align: center;
  color: #666;
}

.chart-info p {
  margin: 8px 0;
  font-size: 16px;
}

/* 通用样式 */
.loading {
  text-align: center;
  color: #666;
  padding: 40px;
}

.empty-state {
  text-align: center;
  color: #999;
  padding: 40px;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .stats-grid {
    grid-template-columns: 1fr;
  }
  
  .dashboard-grid {
    grid-template-columns: 1fr;
  }
  
  .quick-actions {
    grid-template-columns: repeat(2, 1fr);
  }
}
</style>
