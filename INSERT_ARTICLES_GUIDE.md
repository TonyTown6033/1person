# 📝 插入测试文章指南

## ✅ 已准备的文件

- ✅ 4 篇 Markdown 测试文章（`super_club_backend/articles/article-1.md` ~ `article-4.md`）
- ✅ SQL 插入脚本（`super_club_backend/insert_test_articles.sql`）
- ✅ Python 插入脚本（`super_club_backend/insert_articles_simple.py`）

## 🚀 方法一：直接执行 SQL（最简单，推荐）

### 步骤：

1. **打开数据库管理工具**
   - pgAdmin
   - DBeaver
   - 或其他 PostgreSQL 客户端

2. **连接到数据库**
   - 数据库地址：`test-db-postgresql.ns-tmbwyn2v.svc:5432`
   - 数据库名：`postgres`
   - 用户名：`postgres`
   - 密码：`tbrn2kq9`

3. **执行 SQL 文件**
   - 打开文件：`super_club_backend/insert_test_articles.sql`
   - 复制全部内容
   - 在数据库工具中执行

### 或者使用命令行：

```bash
psql -h test-db-postgresql.ns-tmbwyn2v.svc -p 5432 -U postgres -d postgres -f super_club_backend/insert_test_articles.sql
```

## 🚀 方法二：通过 API（需要后端服务运行）

### 步骤：

1. **注册用户**（如果还没有）
```bash
curl -X POST http://localhost:8001/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "test123",
    "name": "测试用户"
  }'
```

2. **登录获取 token**
```bash
curl -X POST http://localhost:8001/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "test123"
  }'
```

3. **使用 token 创建文章**
```bash
# 替换 YOUR_TOKEN 为上面获取的 token
curl -X POST http://localhost:8001/api/content/articles \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{
    "title": "如何做一个合理的管理者",
    "description": "作为管理者，你的贡献来自于你的判断力与影响力...",
    "content": "articles/article-1.md",
    "type": "article",
    "department": "人力部",
    "tags": ["管理", "领导力", "团队"],
    "coverImage": "https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=800&h=400&fit=crop",
    "isPublished": true
  }'
```

重复步骤 3，创建其他 3 篇文章。

## 🚀 方法三：使用 Python 脚本（需要安装依赖）

### 步骤：

1. **安装依赖**
```bash
pip install psycopg2-binary
```

2. **执行脚本**
```bash
cd super_club_backend
python3 insert_articles_simple.py
```

## 📋 文章列表

插入后，你将看到以下 4 篇文章：

| 标题 | 部门 | Markdown 文件 |
|------|------|--------------|
| 如何做一个合理的管理者 | 人力部 | article-1.md |
| 为什么领导没时间，下属没事做？ | 人力部 | article-2.md |
| 如何培养用户的使用习惯？ | 品牌部 | article-3.md |
| 让产品成为用户生活中不可或缺的一部分 | 品牌部 | article-4.md |

## ✅ 验证插入结果

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
```

### 3. 访问前端
打开浏览器访问：`http://localhost:5173`

应该能看到文章列表，点击文章可以查看 Markdown 渲染效果。

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

- **推荐使用方法一（SQL）**：最简单直接
- 如果数据库连接有问题，检查网络连接和数据库服务状态
- 如果文章内容显示为文件路径，检查后端是否正确读取了文件
- 如果 Markdown 没有渲染，检查前端是否正确加载了 `marked` 库

## 🆘 遇到问题？

1. **数据库连接失败**
   - 检查数据库服务是否运行
   - 检查网络连接
   - 验证数据库凭据

2. **API 调用失败**
   - 检查后端服务是否运行：`curl http://localhost:8001/health`
   - 检查 token 是否有效
   - 查看后端日志

3. **前端不显示文章**
   - 检查前端服务是否运行：`curl http://localhost:5173`
   - 检查浏览器控制台是否有错误
   - 验证 API 是否返回数据







