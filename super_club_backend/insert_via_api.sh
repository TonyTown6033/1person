#!/bin/bash

# 通过 API 插入测试文章

API_BASE="http://localhost:8001/api"

echo "🚀 开始通过 API 插入测试文章..."
echo ""

# 1. 注册用户（如果不存在）
echo "📝 步骤 1: 注册测试用户..."
REGISTER_RESPONSE=$(curl -s -X POST "$API_BASE/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "test123",
    "name": "测试用户",
    "phone": "13800138000"
  }')

echo "$REGISTER_RESPONSE" | grep -q "success" && echo "✅ 用户注册成功" || echo "⚠️  用户可能已存在"

# 2. 登录获取 token
echo ""
echo "📝 步骤 2: 登录获取 token..."
LOGIN_RESPONSE=$(curl -s -X POST "$API_BASE/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "test123"
  }')

TOKEN=$(echo "$LOGIN_RESPONSE" | grep -o '"accessToken":"[^"]*' | cut -d'"' -f4)

if [ -z "$TOKEN" ]; then
    echo "❌ 登录失败，无法获取 token"
    echo "响应: $LOGIN_RESPONSE"
    exit 1
fi

echo "✅ 登录成功，Token: ${TOKEN:0:20}..."

# 3. 插入文章
echo ""
echo "📝 步骤 3: 插入测试文章..."

articles=(
  '{"title":"如何做一个合理的管理者","description":"作为管理者，你的贡献来自于你的判断力与影响力，你的职责不是亲力亲为地背负所有猴子，而是要提供动力让其他人发挥所长。","content":"articles/article-1.md","type":"article","department":"人力部","tags":["管理","领导力","团队"],"coverImage":"https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=800&h=400&fit=crop","isPublished":true}'
  '{"title":"为什么领导没时间，下属没事做？","description":"一旦你接受了这些本不属于你的猴子，一个更严重的问题便随之而来：你为什么越努力，反而越忙乱？","content":"articles/article-2.md","type":"article","department":"人力部","tags":["管理","效率","授权"],"coverImage":"https://images.unsplash.com/photo-1497366216548-37526070297c?w=800&h=400&fit=crop","isPublished":true}'
  '{"title":"如何培养用户的使用习惯？","description":"成功的习惯养成类产品，本质上是将用户面临的问题与产品提供的解决方案，通过一次又一次的循环，紧密地联系在一起。","content":"articles/article-3.md","type":"article","department":"品牌部","tags":["产品","用户习惯","增长"],"coverImage":"https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=800&h=400&fit=crop","isPublished":true}'
  '{"title":"让产品成为用户生活中不可或缺的一部分","description":"在这个注意力稀缺的时代，如何让你的产品成为用户生活中不可或缺的一部分？","content":"articles/article-4.md","type":"article","department":"品牌部","tags":["产品","用户体验","价值"],"coverImage":"https://images.unsplash.com/photo-1542744173-8e7e53415bb0?w=800&h=400&fit=crop","isPublished":true}'
)

success_count=0
for article in "${articles[@]}"; do
    RESPONSE=$(curl -s -X POST "$API_BASE/content/articles" \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $TOKEN" \
      -d "$article")
    
    if echo "$RESPONSE" | grep -q "success\|id"; then
        TITLE=$(echo "$article" | grep -o '"title":"[^"]*' | cut -d'"' -f4)
        echo "  ✅ $TITLE"
        ((success_count++))
    else
        TITLE=$(echo "$article" | grep -o '"title":"[^"]*' | cut -d'"' -f4)
        echo "  ❌ $TITLE - 失败: $RESPONSE"
    fi
done

echo ""
echo "✅ 完成！成功插入 $success_count/4 篇文章"
echo ""
echo "📱 现在可以访问前端查看文章："
echo "   http://localhost:5173"







