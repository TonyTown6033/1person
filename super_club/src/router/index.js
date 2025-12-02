import { createRouter, createWebHistory } from 'vue-router'

import HomePage from '../components/MainContent.vue'
import TalentPage from '../pages/TalentPage.vue'
import LinkPage from '../pages/LinkPage.vue'
import ProjectPage from '../pages/ProjectPage.vue'
import EventsPage from '../pages/EventsPage.vue'
import ProfilePage from '../pages/ProfilePage.vue'
import ArticleDetailPage from '../pages/ArticleDetailPage.vue'

// 管理后台页面
import AdminLogin from '../pages/admin/AdminLogin.vue'
import AdminLayout from '../pages/admin/AdminLayout.vue'
import AdminDashboard from '../pages/admin/AdminDashboard.vue'
import AdminUsers from '../pages/admin/AdminUsers.vue'
import AdminProjects from '../pages/admin/AdminProjects.vue'
import AdminEvents from '../pages/admin/AdminEvents.vue'
import AdminContent from '../pages/admin/AdminContent.vue'
import AdminCarousel from '../pages/admin/AdminCarousel.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomePage
  },
  {
    path: '/talents',
    name: 'talents',
    component: TalentPage
  },
  {
    path: '/links',
    name: 'links',
    component: LinkPage
  },
  {
    path: '/projects',
    name: 'projects',
    component: ProjectPage
  },
  {
    path: '/events',
    name: 'events',
    component: EventsPage
  },
  {
    path: '/profile',
    name: 'profile',
    component: ProfilePage
  },
  {
    path: '/articles/:id',
    name: 'article-detail',
    component: ArticleDetailPage
  },
  // 管理后台路由
  {
    path: '/admin/login',
    name: 'admin-login',
    component: AdminLogin,
    meta: { hideSidebar: true }
  },
  {
    path: '/admin',
    component: AdminLayout,
    meta: { requiresAuth: true },
    children: [
      {
        path: '',
        name: 'admin-dashboard',
        component: AdminDashboard
      },
      {
        path: 'users',
        name: 'admin-users',
        component: AdminUsers
      },
      {
        path: 'projects',
        name: 'admin-projects',
        component: AdminProjects
      },
      {
        path: 'events',
        name: 'admin-events',
        component: AdminEvents
      },
      {
        path: 'content',
        name: 'admin-content',
        component: AdminContent
      },
      {
        path: 'carousel',
        name: 'admin-carousel',
        component: AdminCarousel
      }
    ]
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// 路由守卫
router.beforeEach((to, from, next) => {
  // 检查是否需要认证
  if (to.meta.requiresAuth) {
    const token = localStorage.getItem('admin_token')
    if (!token) {
      next('/admin/login')
      return
    }
  }
  next()
})

export default router

