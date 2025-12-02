# 快速插入测试文章

## 📝 已创建的文件

### Markdown 文章（5篇）
- `articles/article-1.md` - 如何做一个合理的管理者
- `articles/article-2.md` - 为什么领导没时间，下属没事做？
- `articles/article-3.md` - 如何培养用户的使用习惯？
- `articles/article-4.md` - 让产品成为用户生活中不可或缺的一部分
- `articles/test-article.md` - 测试文章（功能演示）

### SQL 脚本
- `insert_test_articles.sql` - 插入4篇测试文章的 SQL 脚本

## 🚀 插入数据的方法

### 方法一：直接执行 SQL（推荐）

如果你有数据库访问权限：

```bash
# 使用 psql
psql -U postgres -d your_database_name -f insert_test_articles.sql

# 或者通过数据库管理工具（如 pgAdmin、DBeaver）执行
# 打开 insert_test_articles.sql 文件，复制内容执行
```

### 方法二：通过 API 创建

如果后端服务正在运行，可以通过 API 创建：

```bash
# 1. 先注册用户（如果还没有）
curl -X POST http://localhost:8001/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "test123",
    "name": "测试用户"
  }'

# 2. 登录获取 token
curl -X POST http://localhost:8001/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "test123"
  }'

# 3. 使用 token 创建文章
curl -X POST http://localhost:8001/api/content/articles \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{
    "title": "如何做一个合理的管理者",
    "description": "作为管理者，你的贡献来自于你的判断力与影响力...",
    "content": "articles/article-1.md",
    "type": "article",
    "department": "人力部",
    "is_published": true
  }'
```

### 方法三：使用 Python 脚本（需要安装依赖）

```bash
cd super_club_backend
python3 insert_test_articles.py
```

## ✅ 验证数据

插入后，可以通过以下方式验证：

### 1. 查询数据库
```sql
SELECT id, title, department, content 
FROM contents 
WHERE is_published = true
ORDER BY created_at DESC;
```

### 2. 访问 API
```bash
# 获取文章列表
curl http://localhost:8001/api/content/articles

# 获取文章详情（替换 {id} 为实际文章ID）
curl http://localhost:8001/api/content/articles/{id}
```

### 3. 访问前端
打开浏览器访问：`http://localhost:5173`

应该能看到文章列表，点击文章可以查看 Markdown 渲染效果。

## 📋 文章信息

| 标题 | 部门 | Markdown 文件 | 标签 |
|------|------|--------------|------|
| 如何做一个合理的管理者 | 人力部 | article-1.md | 管理、领导力、团队 |
| 为什么领导没时间，下属没事做？ | 人力部 | article-2.md | 管理、效率、授权 |
| 如何培养用户的使用习惯？ | 品牌部 | article-3.md | 产品、用户习惯、增长 |
| 让产品成为用户生活中不可或缺的一部分 | 品牌部 | article-4.md | 产品、用户体验、价值 |

## 🎯 测试 Markdown 渲染

插入数据后：

1. 访问前端：`http://localhost:5173`
2. 在文章列表中点击任意文章
3. 应该能看到：
   - ✅ Markdown 正确渲染为 HTML
   - ✅ 代码块有语法高亮
   - ✅ 表格、列表格式正确
   - ✅ 图片和链接正常显示

## 💡 提示

- 如果文章内容显示为文件路径而不是内容，检查后端是否正确读取了文件
- 如果 Markdown 没有渲染，检查前端是否正确加载了 `marked` 库
- 如果代码没有高亮，检查 `highlight.js` 是否正确配置







