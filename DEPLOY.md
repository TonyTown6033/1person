# Super Club 部署指南

## 📋 前置要求

- Docker 20.10+
- Docker Compose 2.0+
- 服务器开放端口：3000（前端）、8001（后端API）
- 建议配置：2核CPU、4GB内存、40GB硬盘

## 🚀 快速部署

### 1. 上传项目到服务器

```bash
# 方式1: 使用 git
git clone <your-repo-url> /opt/superclub
cd /opt/superclub

# 方式2: 使用 scp 上传
scp -r ./1Person root@your-server:/opt/superclub
ssh root@your-server
cd /opt/superclub
```

### 2. 配置环境变量

```bash
# 复制示例配置
cp env.example .env

# 编辑配置
nano .env  # 或 vim .env
```

**⚠️ 必须修改以下配置：**

```bash
# 1. 数据库密码（使用强密码）
MYSQL_ROOT_PASSWORD=YourStrongPassword123!

# 2. JWT 密钥（生成随机字符串）
SECRET_KEY=$(openssl rand -hex 32)

# 3. 后端 API 地址（改为你的服务器公网IP）
VITE_API_BASE_URL=http://你的服务器IP:8001/api

# 4. CORS 配置（改为你的前端地址）
CORS_ORIGINS=http://你的服务器IP:3000
```

### 3. 启动服务

```bash
# 构建并启动所有服务（首次需要较长时间）
docker-compose up -d --build

# 查看启动日志
docker-compose logs -f

# 查看服务状态
docker-compose ps
```

### 4. 创建管理员账号

```bash
# 等待服务完全启动后执行
docker exec -it superclub-backend python create_admin.py
```

按提示输入管理员邮箱和密码。

### 5. 验证部署

```bash
# 检查后端健康状态
curl http://localhost:8001/health

# 检查前端
curl http://localhost:3000
```

## 🌐 访问地址

| 服务 | 地址 |
|------|------|
| **前端首页** | http://服务器IP:3000 |
| **管理后台** | http://服务器IP:3000/admin/login |
| **后端 API** | http://服务器IP:8001/api |
| **API 文档** | http://服务器IP:8001/docs |

## 📦 服务管理命令

```bash
# 启动服务
docker-compose up -d

# 停止服务
docker-compose down

# 重启服务
docker-compose restart

# 重启单个服务
docker-compose restart backend
docker-compose restart frontend
docker-compose restart mysql

# 查看日志
docker-compose logs -f              # 所有服务
docker-compose logs -f backend      # 仅后端
docker-compose logs -f mysql        # 仅数据库

# 进入容器
docker exec -it superclub-backend bash
docker exec -it superclub-mysql mysql -uroot -p
```

## 🔄 更新部署

```bash
cd /opt/superclub

# 拉取最新代码
git pull

# 重新构建并启动
docker-compose up -d --build
```

## 💾 数据备份与恢复

### 备份数据库

```bash
# 创建备份目录
mkdir -p /opt/superclub/backups

# 备份（替换 YOUR_PASSWORD）
docker exec superclub-mysql mysqldump -uroot -pYOUR_PASSWORD super_club > /opt/superclub/backups/backup_$(date +%Y%m%d_%H%M%S).sql

# 设置定时备份（每天凌晨3点）
echo "0 3 * * * docker exec superclub-mysql mysqldump -uroot -pYOUR_PASSWORD super_club > /opt/superclub/backups/backup_\$(date +\%Y\%m\%d).sql" | crontab -
```

### 恢复数据库

```bash
docker exec -i superclub-mysql mysql -uroot -pYOUR_PASSWORD super_club < /opt/superclub/backups/backup_xxx.sql
```

## 🔒 安全配置

### 防火墙（Ubuntu/Debian）

```bash
# 安装 ufw
apt install ufw -y

# 允许 SSH
ufw allow 22

# 允许前端
ufw allow 3000

# 允许后端 API
ufw allow 8001

# 启用防火墙
ufw enable

# 查看状态
ufw status
```

### 防火墙（CentOS/RHEL）

```bash
# 开放端口
firewall-cmd --permanent --add-port=3000/tcp
firewall-cmd --permanent --add-port=8001/tcp
firewall-cmd --reload
```

## 🐛 常见问题

### 1. 数据库连接失败

```bash
# 检查 MySQL 容器状态
docker-compose ps mysql
docker-compose logs mysql

# 重启后端（等 MySQL 完全启动）
docker-compose restart backend
```

### 2. 前端无法访问后端 API

- 检查 `.env` 中 `VITE_API_BASE_URL` 是否正确
- 检查防火墙是否开放 8001 端口
- 检查 CORS 配置

```bash
# 测试后端是否可访问
curl http://服务器IP:8001/health
```

### 3. 容器启动失败

```bash
# 查看详细日志
docker-compose logs --tail=100 backend

# 检查端口占用
netstat -tlnp | grep -E "3000|8001|3306"
```

### 4. 完全重置

```bash
# 停止并删除所有容器和数据
docker-compose down -v

# 删除构建缓存
docker system prune -a

# 重新部署
docker-compose up -d --build
```

## 📊 架构图

```
                    ┌─────────────────────────────────────┐
                    │           公网访问                   │
                    └─────────────────────────────────────┘
                                    │
                    ┌───────────────┴───────────────┐
                    │                               │
                    ▼                               ▼
            ┌───────────────┐               ┌───────────────┐
            │   Frontend    │               │   Backend     │
            │  Port: 3000   │    ─────▶     │  Port: 8001   │
            │   Vue.js      │               │   FastAPI     │
            └───────────────┘               └───────────────┘
                                                   │
                                                   ▼
                                            ┌───────────────┐
                                            │    MySQL      │
                                            │  Port: 3306   │
                                            │  (内网访问)    │
                                            └───────────────┘

容器网络: superclub-network
数据持久化: mysql_data (Docker Volume)
```

## 📝 配置说明

| 环境变量 | 说明 | 默认值 |
|---------|------|--------|
| `MYSQL_ROOT_PASSWORD` | MySQL root 密码 | root123456 |
| `MYSQL_DATABASE` | 数据库名称 | super_club |
| `SECRET_KEY` | JWT 加密密钥 | - |
| `BACKEND_PORT` | 后端端口 | 8001 |
| `FRONTEND_PORT` | 前端端口 | 3000 |
| `VITE_API_BASE_URL` | 后端 API 地址 | - |
| `CORS_ORIGINS` | CORS 允许源 | * |
