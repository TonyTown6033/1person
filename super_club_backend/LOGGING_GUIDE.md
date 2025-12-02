# 日志系统使用指南

## 📋 概述

项目已集成完整的日志系统，包括后端（Python）和前端（JavaScript）日志。

## 🔧 后端日志系统

### 日志文件位置

所有日志文件存储在 `logs/` 目录下：

- `app.log` - 所有日志（DEBUG 及以上级别）
- `error.log` - 仅错误日志（ERROR 及以上级别）
- `api.log` - API 请求日志

### 日志级别

- **DEBUG**: 详细的调试信息
- **INFO**: 一般信息（默认）
- **WARNING**: 警告信息
- **ERROR**: 错误信息
- **CRITICAL**: 严重错误

### 使用示例

```python
from app.core.logging import logger

# 基本日志
logger.info("操作成功")
logger.warning("需要注意的问题")
logger.error("发生错误", exc_info=True)

# 带上下文的日志
logger.info(f"用户 {user_id} 执行了操作", extra={"user_id": user_id})

# API 日志
from app.core.logging import log_api_request
log_api_request("GET", "/api/articles", 200, 0.123, user_id="123", ip="127.0.0.1")
```

### 配置日志级别

在 `app/main.py` 中修改：

```python
setup_logger("super_club", level="DEBUG", use_json=False)
```

### 日志格式

**标准格式**：
```
2024-11-15 13:00:00 - super_club - INFO - 消息内容
```

**详细格式**（文件日志）：
```
2024-11-15 13:00:00 - super_club - INFO - [content.py:99] - get_articles() - 获取文章列表
```

**JSON 格式**（可选）：
```json
{
  "timestamp": "2024-11-15T13:00:00",
  "level": "INFO",
  "logger": "super_club",
  "message": "获取文章列表",
  "module": "content",
  "function": "get_articles",
  "line": 99
}
```

## 🎨 前端日志系统

### 使用示例

```javascript
import logger, { apiLogger, componentLogger } from '@/utils/logger'

// 基本日志
logger.info('操作成功')
logger.warn('警告信息')
logger.error('错误信息', error)

// API 日志（已在 request.js 中自动记录）
apiLogger.logApiRequest('GET', '/api/articles')
apiLogger.logApiResponse('GET', '/api/articles', 200, 150)

// 组件日志
componentLogger.info('组件加载完成')
componentLogger.error('组件错误', error)
```

### 日志级别

在开发环境默认是 `DEBUG`，生产环境是 `INFO`。

### 查看日志

1. **浏览器控制台**：所有日志会输出到浏览器控制台
2. **获取日志**：
```javascript
import logger from '@/utils/logger'
const logs = logger.getLogs()
console.log(logs)
```

3. **导出日志**：
```javascript
const logsJson = logger.exportLogs()
// 可以下载或发送到服务器
```

## 📊 日志功能

### 自动记录

以下操作会自动记录日志：

1. **API 请求**：所有 API 请求和响应
2. **错误**：所有异常和错误
3. **数据库操作**：关键数据库操作
4. **文件操作**：Markdown 文件读取等

### 中间件日志

后端自动记录：

- 请求方法、路径、参数
- 响应状态码、处理时间
- 客户端 IP、用户 ID（如果已登录）
- 异常信息

## 🔍 问题定位

### 查看 API 请求日志

```bash
# 查看所有 API 请求
tail -f logs/api.log

# 查看错误请求
grep "ERROR\|WARNING" logs/api.log
```

### 查看错误日志

```bash
# 查看所有错误
tail -f logs/error.log

# 搜索特定错误
grep "文章" logs/error.log
```

### 查看完整日志

```bash
# 实时查看
tail -f logs/app.log

# 查看最近 100 行
tail -n 100 logs/app.log
```

### 前端日志

1. 打开浏览器开发者工具（F12）
2. 查看 Console 标签
3. 使用过滤器查看特定级别的日志

## 🛠️ 配置

### 后端配置

在 `app/core/logging.py` 中：

```python
# 修改日志级别
setup_logger("super_club", level="DEBUG")

# 使用 JSON 格式
setup_logger("super_club", level="INFO", use_json=True)

# 修改日志文件大小
maxBytes=10 * 1024 * 1024  # 10MB
backupCount=5  # 保留5个备份文件
```

### 前端配置

在 `src/utils/logger.js` 中：

```javascript
// 修改日志级别
const logger = new Logger('App', 'DEBUG')

// 修改最大日志数量
this.maxLogs = 200
```

## 📝 最佳实践

1. **使用合适的日志级别**
   - DEBUG: 详细的调试信息
   - INFO: 重要的业务流程
   - WARN: 需要注意但不影响功能
   - ERROR: 错误和异常

2. **记录关键信息**
   - 用户操作
   - API 请求/响应
   - 数据库操作
   - 文件操作
   - 异常和错误

3. **不要记录敏感信息**
   - 密码、token
   - 个人隐私信息
   - 敏感业务数据

4. **定期清理日志**
   - 日志文件会自动轮转
   - 可以手动删除旧日志

## 🚨 常见问题

### Q: 日志文件太大怎么办？

A: 日志系统已配置自动轮转，单个文件最大 10MB，保留 5 个备份。

### Q: 如何查看特定时间的日志？

A: 使用 grep 过滤：
```bash
grep "2024-11-15 13:" logs/app.log
```

### Q: 生产环境如何配置日志？

A: 建议：
- 日志级别设置为 INFO 或 WARN
- 使用 JSON 格式便于日志收集
- 配置日志收集服务（如 ELK、Sentry）

### Q: 前端日志如何发送到服务器？

A: 在 `logger.js` 的 `sendErrorToServer` 方法中配置错误收集服务。

## 📚 相关文件

- 后端日志配置: `app/core/logging.py`
- 后端中间件: `app/core/middleware.py`
- 前端日志工具: `src/utils/logger.js`
- 日志目录: `logs/`







