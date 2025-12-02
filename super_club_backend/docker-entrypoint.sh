#!/bin/bash
set -e

echo "等待数据库就绪..."
sleep 5

echo "启动 Super Club API 服务..."

# 启动应用（表会自动创建）
exec uvicorn app.main:app --host 0.0.0.0 --port 8000

