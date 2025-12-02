# 测试文章：Markdown 渲染功能

这是一篇测试文章，用于验证 Markdown 渲染功能是否正常工作。

## 功能特性

### 1. 基础格式

这是**粗体文本**，这是*斜体文本*，这是~~删除线~~。

这是一个包含[链接](https://example.com)的段落。

### 2. 列表

#### 无序列表
- 项目 1
- 项目 2
  - 子项目 2.1
  - 子项目 2.2
- 项目 3

#### 有序列表
1. 第一项
2. 第二项
3. 第三项

### 3. 代码块

#### Python 代码示例

```python
def hello_world():
    """打印 Hello World"""
    print("Hello, World!")
    return True

# 调用函数
result = hello_world()
```

#### JavaScript 代码示例

```javascript
function greet(name) {
    return `Hello, ${name}!`;
}

const message = greet('Super Club');
console.log(message);
```

#### SQL 查询示例

```sql
SELECT 
    id,
    title,
    content,
    created_at
FROM contents
WHERE is_published = true
ORDER BY created_at DESC
LIMIT 10;
```

### 4. 引用块

> 这是一段引用文字。
> 
> 可以包含多行内容。
> 
> 用于突出显示重要信息。

### 5. 表格

| 功能 | 状态 | 说明 |
|------|------|------|
| Markdown 渲染 | ✅ | 已实现 |
| 代码高亮 | ✅ | 已实现 |
| 响应式布局 | ✅ | 已实现 |
| Notion 集成 | 🚧 | 计划中 |

### 6. 水平线

---

### 7. 图片

![示例图片](https://images.unsplash.com/photo-1497366216548-37526070297c?w=800&h=400&fit=crop)

### 8. 任务列表

- [x] 完成 Markdown 渲染
- [x] 实现代码高亮
- [x] 添加响应式布局
- [ ] 集成 Notion API
- [ ] 添加评论功能

## 总结

这篇文章展示了 Markdown 的各种语法特性，包括：

- ✅ 标题层级
- ✅ 文本格式
- ✅ 列表
- ✅ 代码块（带语法高亮）
- ✅ 引用
- ✅ 表格
- ✅ 链接和图片

希望这个功能能够帮助你更好地展示文章内容！

