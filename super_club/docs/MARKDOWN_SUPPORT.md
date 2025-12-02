# Markdown 文章支持

## 功能概述

Super Club 现在支持将 Markdown 文件展示为文章的详情页。系统会自动识别并渲染 Markdown 格式的内容，支持代码高亮、表格、列表等常见 Markdown 语法。

## 使用方法

### 方式一：直接在数据库中存储 Markdown 内容

在创建或更新文章时，将 `content` 字段设置为 Markdown 格式的文本：

```python
content = Content(
    title="我的文章标题",
    content="# 这是标题\n\n这是正文内容...",
    # ... 其他字段
)
```

### 方式二：使用 Markdown 文件路径

在创建文章时，将 `content` 字段设置为 Markdown 文件的相对路径：

```python
content = Content(
    title="我的文章标题",
    content="articles/my-article.md",  # 相对路径
    # ... 其他字段
)
```

系统会自动从文件系统读取文件内容。

**文件路径规则：**
- 相对路径：相对于 `super_club_backend` 项目根目录
- 绝对路径：直接使用完整路径
- 支持的文件扩展名：`.md` 或 `.markdown`

**示例：**
```python
# 相对路径（推荐）
content="articles/my-article.md"
content="docs/guides/getting-started.md"

# 绝对路径
content="/path/to/your/article.md"
```

## 前端展示

文章详情页会自动：
1. 检测内容格式（Markdown 或 HTML）
2. 如果是 Markdown，使用 `marked` 库转换为 HTML
3. 使用 `highlight.js` 进行代码高亮
4. 应用美观的样式

## Markdown 功能支持

### 基础语法
- ✅ 标题（H1-H6）
- ✅ 段落
- ✅ 粗体、斜体
- ✅ 链接
- ✅ 图片
- ✅ 列表（有序、无序）
- ✅ 引用
- ✅ 水平线

### 高级语法
- ✅ 代码块（带语法高亮）
- ✅ 表格
- ✅ 任务列表
- ✅ 删除线
- ✅ GitHub Flavored Markdown (GFM)

### 代码高亮支持的语言
- JavaScript/TypeScript
- Python
- Java
- C/C++
- HTML/CSS
- SQL
- 以及其他 highlight.js 支持的语言

## 样式定制

Markdown 渲染样式定义在 `ArticleDetailPage.vue` 中，你可以根据需要调整：

- 字体大小和行高
- 代码块背景色和语法高亮颜色
- 表格样式
- 链接颜色
- 等等

## 与 Notion 集成（未来计划）

### 方案一：Notion API 集成

1. **获取 Notion API Token**
   - 在 Notion 中创建集成（Integration）
   - 获取 API Token

2. **后端添加 Notion API 支持**
   ```python
   # 添加 Notion API 客户端
   from notion_client import Client
   
   notion = Client(auth=NOTION_TOKEN)
   
   # 获取 Notion 页面内容
   page = notion.pages.retrieve(page_id)
   blocks = notion.blocks.children.list(block_id=page_id)
   ```

3. **转换为 Markdown**
   - 使用 `notion-to-md` 库将 Notion 内容转换为 Markdown
   - 存储到数据库或直接返回

### 方案二：Notion 导出 + 文件同步

1. **从 Notion 导出 Markdown**
   - 在 Notion 中导出页面为 Markdown
   - 保存到项目的 `articles/` 目录

2. **使用文件路径方式**
   - 在数据库中设置 `content` 字段为文件路径
   - 系统自动读取并渲染

### 方案三：Webhook 自动同步

1. **设置 Notion Webhook**
   - 当 Notion 页面更新时触发
   - 后端接收更新通知

2. **自动同步**
   - 获取最新内容
   - 转换为 Markdown
   - 更新数据库或文件

## 示例：创建 Markdown 文章

### 1. 创建 Markdown 文件

在 `super_club_backend/articles/` 目录下创建文件：

```markdown
# 文章标题

这是文章的第一段内容。

## 二级标题

这是第二段内容，包含**粗体**和*斜体*。

### 代码示例

```python
def hello_world():
    print("Hello, World!")
```

### 列表

- 项目 1
- 项目 2
- 项目 3

### 表格

| 列1 | 列2 | 列3 |
|-----|-----|-----|
| 数据1 | 数据2 | 数据3 |
```

### 2. 在数据库中创建文章记录

```python
from app.models.content import Content
from datetime import datetime

article = Content(
    title="文章标题",
    content="articles/my-article.md",  # 文件路径
    description="文章描述",
    type="article",
    department="技术部",
    author_id=user_id,
    is_published=True,
    published_at=datetime.now(),
    reading_time=5
)
db.add(article)
db.commit()
```

### 3. 访问文章

前端访问 `/articles/{article_id}` 即可看到渲染后的文章。

## 注意事项

1. **文件编码**：确保 Markdown 文件使用 UTF-8 编码
2. **文件权限**：确保后端服务有读取文件的权限
3. **路径安全**：系统会验证文件路径，防止路径遍历攻击
4. **性能考虑**：大量文章建议使用数据库存储，而非文件系统
5. **缓存策略**：可以考虑添加缓存机制，避免频繁读取文件

## 故障排查

### 问题：文章内容不显示

1. 检查文件路径是否正确
2. 检查文件是否存在
3. 检查文件编码是否为 UTF-8
4. 查看后端日志中的错误信息

### 问题：代码高亮不工作

1. 确保代码块指定了语言：```` ```python ````
2. 检查 highlight.js 是否正确加载
3. 查看浏览器控制台是否有错误

### 问题：样式显示异常

1. 检查 CSS 是否正确加载
2. 检查是否有样式冲突
3. 清除浏览器缓存

## 未来改进

- [ ] 支持实时预览
- [ ] 支持 Markdown 编辑器
- [ ] 支持图片上传和存储
- [ ] 支持数学公式（LaTeX）
- [ ] 支持 Mermaid 图表
- [ ] 支持 Notion API 直接集成
- [ ] 支持自动同步 Notion 内容

