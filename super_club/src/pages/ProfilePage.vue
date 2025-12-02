<template>
  <main class="profile-page">
    <section class="profile-header">
      <div class="header-content">
        <div class="user-info">
          <div class="avatar-large">
            <img src="https://api.dicebear.com/7.x/avataaars/svg?seed=greta" alt="greta" />
          </div>
          <div class="user-details">
            <div class="user-name">greta</div>
            <div class="user-badge">Pitch学习室会员</div>
          </div>
        </div>
        <button class="edit-btn">编辑</button>
      </div>
    </section>

    <section class="profile-sections">
      <!-- 我的名片 -->
      <div class="section-card">
        <h2 class="section-title">我的名片</h2>
        <div class="section-items">
          <a href="#" class="section-item">
            <div class="item-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                <circle cx="12" cy="7" r="4"></circle>
                <path d="M16 11h6M19 8v6"></path>
              </svg>
            </div>
            <span class="item-text">我的电子名片</span>
            <svg class="arrow-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M9 18l6-6-6-6"></path>
            </svg>
          </a>
          <a href="#" class="section-item">
            <div class="item-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                <path d="M12 20h9"></path>
                <path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"></path>
              </svg>
            </div>
            <span class="item-text">创建/编辑我的名片</span>
            <svg class="arrow-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M9 18l6-6-6-6"></path>
            </svg>
          </a>
        </div>
      </div>

      <!-- 我的创业项目 -->
      <div class="section-card">
        <h2 class="section-title">我的创业项目</h2>
        <div class="section-items">
          <a href="#" class="section-item">
            <div class="item-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path>
                <polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline>
                <line x1="12" y1="22.08" x2="12" y2="12"></line>
              </svg>
            </div>
            <span class="item-text">我的项目</span>
            <svg class="arrow-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M9 18l6-6-6-6"></path>
            </svg>
          </a>
          <a href="#" class="section-item">
            <div class="item-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                <path d="M12 20h9"></path>
                <path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"></path>
              </svg>
            </div>
            <span class="item-text">我的经验贴</span>
            <svg class="arrow-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M9 18l6-6-6-6"></path>
            </svg>
          </a>
        </div>
      </div>

      <!-- 我的社区互动 -->
      <div class="section-card">
        <h2 class="section-title">我的社区互动</h2>
        <div class="section-items">
          <a href="#" class="section-item">
            <div class="item-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
              </svg>
            </div>
            <span class="item-text">我的收藏</span>
            <svg class="arrow-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M9 18l6-6-6-6"></path>
            </svg>
          </a>
          <a href="#" class="section-item">
            <div class="item-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path>
                <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path>
              </svg>
            </div>
            <span class="item-text">我的链接</span>
            <svg class="arrow-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M9 18l6-6-6-6"></path>
            </svg>
          </a>
          <a href="#" class="section-item">
            <div class="item-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
              </svg>
            </div>
            <span class="item-text">我的评论</span>
            <svg class="arrow-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M9 18l6-6-6-6"></path>
            </svg>
          </a>
        </div>
      </div>
    </section>
  </main>
</template>

<script setup>
// 页面逻辑可以在这里添加
</script>

<style scoped>
.profile-page {
  flex: 1;
  padding: 40px 48px;
  background-color: #ffffff;
  overflow-y: auto;
  height: 100vh;
  min-width: 0;
}

.profile-header {
  margin-bottom: 40px;
}

.header-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
}

.user-info {
  display: flex;
  align-items: center;
  gap: 20px;
}

.avatar-large {
  width: 64px;
  height: 64px;
  border-radius: 50%;
  overflow: hidden;
  background-color: #f0f0f0;
  flex-shrink: 0;
}

.avatar-large img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.user-details {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.user-name {
  font-size: 24px;
  font-weight: 600;
  color: #000000;
}

.user-badge {
  font-size: 14px;
  color: #666666;
}

.edit-btn {
  padding: 10px 20px;
  background-color: #ffffff;
  border: 1px solid #e0e0e0;
  border-radius: 6px;
  color: #000000;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.2s;
}

.edit-btn:hover {
  background-color: #f5f5f5;
  border-color: #cccccc;
}

.profile-sections {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.section-card {
  background-color: #ffffff;
  border: 1px solid #f0f0f0;
  border-radius: 12px;
  padding: 24px;
}

.section-title {
  font-size: 18px;
  font-weight: 600;
  color: #000000;
  margin-bottom: 20px;
}

.section-items {
  display: flex;
  flex-direction: column;
  gap: 0;
}

.section-item {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 16px;
  color: #000000;
  text-decoration: none;
  border-radius: 8px;
  transition: background-color 0.2s;
  position: relative;
}

.section-item:not(:last-child)::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 56px;
  right: 16px;
  height: 1px;
  background-color: #f0f0f0;
}

.section-item:hover {
  background-color: #f5f5f5;
}

.section-item:active {
  background-color: #e8e8e8;
}

.item-icon {
  width: 24px;
  height: 24px;
  color: #000000;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
}

.item-icon svg {
  width: 100%;
  height: 100%;
  stroke: currentColor;
}

.item-text {
  flex: 1;
  font-size: 15px;
  color: #000000;
}

.arrow-icon {
  width: 18px;
  height: 18px;
  color: #999999;
  flex-shrink: 0;
}

/* 移动端样式 */
@media (max-width: 768px) {
  .profile-page {
    padding: 16px;
    padding-top: 80px;
    padding-bottom: 80px;
    height: auto;
    min-height: calc(100vh - 60px);
  }

  .profile-header {
    margin-bottom: 24px;
  }

  .header-content {
    flex-direction: column;
    align-items: flex-start;
    gap: 16px;
  }

  .user-info {
    width: 100%;
  }

  .avatar-large {
    width: 56px;
    height: 56px;
  }

  .user-name {
    font-size: 20px;
  }

  .edit-btn {
    width: 100%;
    padding: 12px 20px;
  }

  .section-card {
    padding: 20px 16px;
  }

  .section-title {
    font-size: 16px;
    margin-bottom: 16px;
  }

  .section-item {
    padding: 14px;
  }

  .item-text {
    font-size: 14px;
  }
}
</style>

