/**
 * ArticleItem 组件测试
 */
import { describe, it, expect, vi } from 'vitest'
import { mount } from '@vue/test-utils'
import ArticleItem from '@/components/ArticleItem.vue'

describe('ArticleItem', () => {
  const mockArticle = {
    id: '1',
    title: '测试文章标题',
    description: '这是文章描述内容',
    image: 'https://example.com/article.jpg',
    department: '技术部'
  }

  it('正确渲染文章标题', () => {
    const wrapper = mount(ArticleItem, {
      props: { article: mockArticle }
    })
    
    expect(wrapper.find('.article-title').text()).toBe('测试文章标题')
  })

  it('正确渲染文章描述', () => {
    const wrapper = mount(ArticleItem, {
      props: { article: mockArticle }
    })
    
    expect(wrapper.find('.article-description').text()).toBe('这是文章描述内容')
  })

  it('正确渲染部门标签', () => {
    const wrapper = mount(ArticleItem, {
      props: { article: mockArticle }
    })
    
    expect(wrapper.find('.department-tag').text()).toBe('技术部')
  })

  it('正确设置图片', () => {
    const wrapper = mount(ArticleItem, {
      props: { article: mockArticle }
    })
    
    const img = wrapper.find('.article-image img')
    expect(img.attributes('src')).toBe('https://example.com/article.jpg')
    expect(img.attributes('alt')).toBe('测试文章标题')
  })

  it('点击时触发 view-detail 事件', async () => {
    const wrapper = mount(ArticleItem, {
      props: { article: mockArticle }
    })
    
    await wrapper.trigger('click')
    
    expect(wrapper.emitted('view-detail')).toBeTruthy()
    expect(wrapper.emitted('view-detail')[0]).toEqual([mockArticle])
  })

  it('鼠标悬停时有正确样式类', () => {
    const wrapper = mount(ArticleItem, {
      props: { article: mockArticle }
    })
    
    expect(wrapper.classes()).toContain('article-item')
  })

  it('处理不同部门', () => {
    const departments = ['战略部', '品牌部', '销售部', '人力部', '财法部']
    
    departments.forEach(dept => {
      const wrapper = mount(ArticleItem, {
        props: {
          article: { ...mockArticle, department: dept }
        }
      })
      expect(wrapper.find('.department-tag').text()).toBe(dept)
    })
  })

  it('处理空描述', () => {
    const wrapper = mount(ArticleItem, {
      props: {
        article: { ...mockArticle, description: '' }
      }
    })
    
    expect(wrapper.find('.article-description').text()).toBe('')
  })
})

