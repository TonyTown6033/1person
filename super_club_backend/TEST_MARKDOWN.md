# Markdown 功能测试指南

## ✅ 基础功能测试（已完成）

文件读取功能已通过测试：
- ✅ Markdown 文件存在
- ✅ 文件读取功能正常
- ✅ 相对路径和绝对路径都支持

## 🚀 完整功能测试步骤

### 1. 启动后端服务

```bash
cd /Users/town/Project/1Person/super_club_backend
python3 run.py
```

后端服务将在 `http://localhost:8001` 启动

### 2. 启动前端服务

```bash
cd /Users/town/Project/1Person/super_club
npm run dev
```

前端服务将在 `http://localhost:5173` 启动

### 3. 创建测试数据

#### 方式一：通过 API 创建（需要数据库）

```bash
# 先注册用户
curl -X POST http://localhost:8001/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "test123",
    "name": "测试用户"
  }'

# 登录获取 token
curl -X POST http://localhost:8001/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "test123"
  }'

# 创建文章（使用 Markdown 文件路径）
curl -X POST http://localhost:8001/api/content/articles \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{
    "title": "测试文章：Markdown 渲染功能",
    "content": "articles/test-article.md",
    "type": "article",
    "department": "技术部",
    "is_published": true
  }'
```

#### 方式二：直接测试 API（模拟数据）

访问后端 API 文档：
```
http://localhost:8001/docs
```

### 4. 测试 Markdown 渲染

#### 测试场景 1：直接 Markdown 内容

创建文章时，`content` 字段直接是 Markdown 文本：

```json
{
  "title": "测试文章",
  "content": "# 标题\n\n这是**粗体**文本。\n\n```python\nprint('Hello')\n```",
  "type": "article"
}
```

#### 测试场景 2：Markdown 文件路径

创建文章时，`content` 字段是文件路径：

```json
{
  "title": "测试文章",
  "content": "articles/test-article.md",
  "type": "article"
}
```

### 5. 前端测试

1. 访问首页：`http://localhost:5173`
2. 在文章列表中点击任意文章
3. 应该跳转到 `/articles/{id}` 详情页
4. 检查 Markdown 是否正确渲染：
   - ✅ 标题层级正确
   - ✅ 代码块有语法高亮
   - ✅ 列表格式正确
   - ✅ 表格显示正常
   - ✅ 链接可点击

## 🧪 API 测试

### 测试文件读取功能

```bash
# 测试获取文章详情（应该自动读取文件）
curl http://localhost:8001/api/content/articles/{article_id}
```

响应应该包含完整的 Markdown 内容。

### 测试前端渲染

打开浏览器控制台，检查：
1. 是否有 JavaScript 错误
2. API 请求是否成功
3. Markdown 是否正确转换为 HTML

## 📝 测试检查清单

- [ ] 后端服务正常启动
- [ ] 前端服务正常启动
- [ ] 可以创建测试文章
- [ ] 文章列表显示正常
- [ ] 点击文章可以跳转到详情页
- [ ] Markdown 内容正确渲染
- [ ] 代码块有语法高亮
- [ ] 响应式布局正常（移动端/桌面端）
- [ ] 返回按钮正常工作
- [ ] 点赞功能正常（如果已登录）

## 🐛 常见问题

### 问题 1：文件读取失败

**原因**：文件路径不正确或文件不存在

**解决**：
- 检查文件路径是否正确
- 确保文件在 `super_club_backend/articles/` 目录下
- 检查文件权限

### 问题 2：Markdown 不渲染

**原因**：前端 marked 库未正确加载

**解决**：
- 检查浏览器控制台是否有错误
- 确认 `marked` 和 `highlight.js` 已安装
- 清除浏览器缓存

### 问题 3：代码高亮不工作

**原因**：highlight.js 未正确配置

**解决**：
- 检查代码块是否指定了语言：```` ```python ````
- 查看浏览器控制台错误
- 确认 highlight.js 样式已加载

## 📊 测试结果

测试完成后，记录以下信息：

- 测试时间：___________
- 测试环境：___________
- 浏览器：___________
- 测试结果：✅ 通过 / ❌ 失败
- 发现的问题：___________
- 修复状态：___________

