#!/usr/bin/env python3
"""
插入测试文章到数据库
直接使用 SQL 语句，避免依赖问题
"""
import sys
import os
from datetime import datetime
from pathlib import Path

# 添加项目路径
sys.path.insert(0, str(Path(__file__).parent))

try:
    from app.core.database import SessionLocal, engine
    from app.models.content import Content
    from app.models.user import User
    from app.models import Base
    import uuid
    from sqlalchemy import text
    
    # 创建数据库表
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    
    try:
        # 1. 获取或创建测试用户
        test_user = db.query(User).filter(User.email == "test@example.com").first()
        
        if not test_user:
            from app.core.security import get_password_hash
            test_user = User(
                id=uuid.uuid4(),
                email="test@example.com",
                password_hash=get_password_hash("test123"),
                name="测试用户",
                avatar="https://api.dicebear.com/7.x/avataaars/svg?seed=test",
                is_active=True
            )
            db.add(test_user)
            db.commit()
            db.refresh(test_user)
            print(f"✅ 创建测试用户: {test_user.email}")
        else:
            print(f"✅ 使用现有用户: {test_user.email}")
        
        # 2. 检查并删除已存在的测试文章
        existing_articles = db.query(Content).filter(
            Content.title.like("测试%")
        ).all()
        
        if existing_articles:
            for article in existing_articles:
                db.delete(article)
            db.commit()
            print(f"✅ 清理了 {len(existing_articles)} 篇旧文章")
        
        # 3. 创建测试文章
        articles_data = [
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
        
        created_articles = []
        for article_data in articles_data:
            article = Content(
                id=uuid.uuid4(),
                title=article_data["title"],
                description=article_data["description"],
                content=article_data["content"],  # Markdown 文件路径
                type="article",
                department=article_data["department"],
                author_id=test_user.id,
                cover_image=article_data["cover_image"],
                tags=article_data["tags"],
                is_published=True,
                published_at=datetime.now(),
                reading_time=5,
                view_count=0,
                like_count=0,
                comment_count=0,
                favorite_count=0
            )
            db.add(article)
            created_articles.append(article)
        
        db.commit()
        
        print(f"\n✅ 成功创建 {len(created_articles)} 篇测试文章！")
        print("\n📝 文章列表:")
        for i, article in enumerate(created_articles, 1):
            print(f"   {i}. {article.title}")
            print(f"      ID: {article.id}")
            print(f"      文件: {article.content}")
            print(f"      访问: http://localhost:5173/articles/{article.id}")
            print()
        
        print("✨ 现在可以在前端页面看到这些文章了！")
        
    except Exception as e:
        db.rollback()
        print(f"❌ 插入文章失败: {e}")
        import traceback
        traceback.print_exc()
    finally:
        db.close()
        
except ImportError as e:
    print(f"❌ 导入模块失败: {e}")
    print("\n💡 提示：")
    print("   1. 确保已安装依赖: pip install -r requirements.txt")
    print("   2. 或者使用 SQL 直接插入（见下方）")
    print("\n📝 或者手动执行以下 SQL:")
    print("-" * 60)
    
    # 生成 SQL 语句
    sql_template = """
-- 首先获取或创建用户（假设用户ID为固定值）
INSERT INTO users (id, email, password_hash, name, avatar, is_active, created_at, updated_at)
VALUES (
    '00000000-0000-0000-0000-000000000001',
    'test@example.com',
    '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5GyY5Y5Y5Y5Y5',  -- test123
    '测试用户',
    'https://api.dicebear.com/7.x/avataaars/svg?seed=test',
    true,
    NOW(),
    NOW()
) ON CONFLICT (email) DO NOTHING;

-- 插入文章
INSERT INTO contents (id, title, description, content, type, department, author_id, 
                      cover_image, tags, is_published, published_at, reading_time,
                      view_count, like_count, comment_count, favorite_count, created_at, updated_at)
VALUES 
(
    gen_random_uuid(),
    '如何做一个合理的管理者',
    '作为管理者，你的贡献来自于你的判断力与影响力，你的职责不是亲力亲为地背负所有猴子，而是要提供动力让其他人发挥所长。',
    'articles/article-1.md',
    'article',
    '人力部',
    '00000000-0000-0000-0000-000000000001',
    'https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=800&h=400&fit=crop',
    ARRAY['管理', '领导力', '团队'],
    true,
    NOW(),
    5,
    0, 0, 0, 0,
    NOW(),
    NOW()
),
(
    gen_random_uuid(),
    '为什么领导没时间，下属没事做？',
    '一旦你接受了这些本不属于你的猴子，一个更严重的问题便随之而来：你为什么越努力，反而越忙乱？',
    'articles/article-2.md',
    'article',
    '人力部',
    '00000000-0000-0000-0000-000000000001',
    'https://images.unsplash.com/photo-1497366216548-37526070297c?w=800&h=400&fit=crop',
    ARRAY['管理', '效率', '授权'],
    true,
    NOW(),
    5,
    0, 0, 0, 0,
    NOW(),
    NOW()
),
(
    gen_random_uuid(),
    '如何培养用户的使用习惯？',
    '成功的习惯养成类产品，本质上是将用户面临的问题与产品提供的解决方案，通过一次又一次的循环，紧密地联系在一起。',
    'articles/article-3.md',
    'article',
    '品牌部',
    '00000000-0000-0000-0000-000000000001',
    'https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=800&h=400&fit=crop',
    ARRAY['产品', '用户习惯', '增长'],
    true,
    NOW(),
    5,
    0, 0, 0, 0,
    NOW(),
    NOW()
),
(
    gen_random_uuid(),
    '让产品成为用户生活中不可或缺的一部分',
    '在这个注意力稀缺的时代，如何让你的产品成为用户生活中不可或缺的一部分？',
    'articles/article-4.md',
    'article',
    '品牌部',
    '00000000-0000-0000-0000-000000000001',
    'https://images.unsplash.com/photo-1542744173-8e7e53415bb0?w=800&h=400&fit=crop',
    ARRAY['产品', '用户体验', '价值'],
    true,
    NOW(),
    5,
    0, 0, 0, 0,
    NOW(),
    NOW()
);
"""
    print(sql_template)
    print("-" * 60)







