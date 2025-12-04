/**
 * ContentCard 组件测试
 */
import { describe, it, expect } from 'vitest'
import { mount } from '@vue/test-utils'
import ContentCard from '@/components/ContentCard.vue'

describe('ContentCard', () => {
  const defaultProps = {
    title: '测试标题',
    description: '这是测试描述',
    image: 'https://example.com/image.jpg'
  }

  it('正确渲染标题', () => {
    const wrapper = mount(ContentCard, {
      props: defaultProps
    })
    
    expect(wrapper.find('.card-title').text()).toBe('测试标题')
  })

  it('正确渲染描述', () => {
    const wrapper = mount(ContentCard, {
      props: defaultProps
    })
    
    expect(wrapper.find('.card-description').text()).toBe('这是测试描述')
  })

  it('正确设置图片源', () => {
    const wrapper = mount(ContentCard, {
      props: defaultProps
    })
    
    const img = wrapper.find('.card-image')
    expect(img.attributes('src')).toBe('https://example.com/image.jpg')
    expect(img.attributes('alt')).toBe('测试标题')
  })

  it('显示 AI 标签', () => {
    const wrapper = mount(ContentCard, {
      props: defaultProps
    })
    
    expect(wrapper.find('.ai-tag').text()).toBe('AI生成')
  })

  it('应用正确的 CSS 类', () => {
    const wrapper = mount(ContentCard, {
      props: defaultProps
    })
    
    expect(wrapper.classes()).toContain('content-card')
  })

  it('处理长标题', () => {
    const wrapper = mount(ContentCard, {
      props: {
        ...defaultProps,
        title: '这是一个非常非常非常非常非常非常长的标题，需要被截断显示'
      }
    })
    
    expect(wrapper.find('.card-title').exists()).toBe(true)
  })

  it('处理长描述', () => {
    const wrapper = mount(ContentCard, {
      props: {
        ...defaultProps,
        description: '这是一个非常非常非常非常非常非常长的描述，需要被截断显示。'.repeat(5)
      }
    })
    
    expect(wrapper.find('.card-description').exists()).toBe(true)
  })
})

