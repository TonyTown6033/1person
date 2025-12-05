#!/usr/bin/env python3
"""
简单插入脚本 - 直接连接数据库插入文章
依赖尽量精简：主要是 psycopg2 + python-dotenv（可选）
"""
import psycopg2
from datetime import datetime
import uuid
import sys
import os
from dotenv import load_dotenv

# 优先从环境变量 / .env 中读取数据库配置，避免在代码里硬编码真实连接串
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    print("❌ 未找到 DATABASE_URL 配置，请在环境变量或 .env 中设置，例如：")
    print("   DATABASE_URL=postgresql://user:password@host:5432/dbname")
    sys.exit(1)

# 测试文章数据
articles = [
    {
        "title": "如何做一个合理的管理者",
        "description": "作为管理者，你的贡献来自于你的判断力与影响力，你的职责不是亲力亲为地背负所有猴子，而是要提供动力让其他人发挥所长。",
        "content": "articles/article-1.md",
        "department": "人力部",
        "tags": ["管理", "领导力", "团队"],
        "cover_image": "https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=800&h=400&fit=crop"
    },
    {
        "title": "为什么领导没时间，下属没事做？",
        "description": "一旦你接受了这些本不属于你的猴子，一个更严重的问题便随之而来：你为什么越努力，反而越忙乱？",
        "content": "articles/article-2.md",
        "department": "人力部",
        "tags": ["管理", "效率", "授权"],
        "cover_image": "https://images.unsplash.com/photo-1497366216548-37526070297c?w=800&h=400&fit=crop"
    },
    {
        "title": "如何培养用户的使用习惯？",
        "description": "成功的习惯养成类产品，本质上是将用户面临的问题与产品提供的解决方案，通过一次又一次的循环，紧密地联系在一起。",
        "content": "articles/article-3.md",
        "department": "品牌部",
        "tags": ["产品", "用户习惯", "增长"],
        "cover_image": "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=800&h=400&fit=crop"
    },
    {
        "title": "让产品成为用户生活中不可或缺的一部分",
        "description": "在这个注意力稀缺的时代，如何让你的产品成为用户生活中不可或缺的一部分？",
        "content": "articles/article-4.md",
        "department": "品牌部",
        "tags": ["产品", "用户体验", "价值"],
        "cover_image": "https://images.unsplash.com/photo-1542744173-8e7e53415bb0?w=800&h=400&fit=crop"
    }
]

def insert_articles():
    """插入文章到数据库"""
    try:
        # 连接数据库
        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor()
        
        print("✅ 数据库连接成功")
        
        # 1. 获取或创建测试用户
        print("\n📝 步骤 1: 检查测试用户...")
        cur.execute("""
            SELECT id FROM users WHERE email = 'test@example.com' LIMIT 1
        """)
        user_row = cur.fetchone()
        
        if user_row:
            user_id = user_row[0]
            print(f"   ✅ 找到用户，ID: {user_id}")
        else:
            # 创建用户
            user_id = str(uuid.uuid4())
            cur.execute("""
                INSERT INTO users (id, email, password_hash, name, avatar, is_active, created_at, updated_at)
                VALUES (%s, %s, %s, %s, %s, %s, NOW(), NOW())
            """, (
                user_id,
                'test@example.com',
                '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5GyY5Y5Y5Y5Y5',  # test123
                '测试用户',
                'https://api.dicebear.com/7.x/avataaars/svg?seed=test',
                True
            ))
            print(f"   ✅ 创建用户，ID: {user_id}")
        
        # 2. 清理旧文章（可选）
        print("\n📝 步骤 2: 清理旧测试文章...")
        cur.execute("""
            DELETE FROM contents 
            WHERE title IN %s
        """, (tuple([a["title"] for a in articles]),))
        deleted = cur.rowcount
        if deleted > 0:
            print(f"   ✅ 删除了 {deleted} 篇旧文章")
        
        # 3. 插入新文章
        print("\n📝 步骤 3: 插入新文章...")
        inserted_count = 0
        
        for article in articles:
            article_id = str(uuid.uuid4())
            cur.execute("""
                INSERT INTO contents (
                    id, title, description, content, type, department, author_id,
                    cover_image, tags, is_published, published_at, reading_time,
                    view_count, like_count, comment_count, favorite_count,
                    created_at, updated_at
                ) VALUES (
                    %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, NOW(), %s,
                    %s, %s, %s, %s,
                    NOW(), NOW()
                )
            """, (
                article_id,
                article["title"],
                article["description"],
                article["content"],  # Markdown 文件路径
                "article",
                article["department"],
                user_id,
                article["cover_image"],
                article["tags"],
                True,  # is_published
                5,  # reading_time
                0, 0, 0, 0  # counts
            ))
            inserted_count += 1
            print(f"   ✅ {article['title']}")
        
        # 提交事务
        conn.commit()
        
        print(f"\n✅ 成功插入 {inserted_count} 篇文章！")
        print("\n📱 现在可以访问前端查看文章：")
        print("   http://localhost:5173")
        
        # 查询插入的文章
        print("\n📋 插入的文章列表：")
        cur.execute("""
            SELECT id, title, department 
            FROM contents 
            WHERE title IN %s
            ORDER BY created_at DESC
        """, (tuple([a["title"] for a in articles]),))
        
        for row in cur.fetchall():
            print(f"   - {row[1]} ({row[2]})")
            print(f"     访问: http://localhost:5173/articles/{row[0]}")
        
        cur.close()
        conn.close()
        
        return True
        
    except psycopg2.Error as e:
        print(f"❌ 数据库错误: {e}")
        if conn:
            conn.rollback()
        return False
    except Exception as e:
        print(f"❌ 错误: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("🚀 开始插入测试文章...")
    print("=" * 60)
    success = insert_articles()
    print("=" * 60)
    if success:
        print("✅ 完成！")
    else:
        print("❌ 失败！")
        sys.exit(1)







