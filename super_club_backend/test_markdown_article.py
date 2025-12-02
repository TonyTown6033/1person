#!/usr/bin/env python3
"""
测试脚本：创建包含 Markdown 文件的测试文章
"""
import sys
import os
from datetime import datetime
from pathlib import Path

# 添加项目路径
sys.path.insert(0, str(Path(__file__).parent))

from app.core.database import SessionLocal, engine
from app.models.content import Content
from app.models.user import User
from app.models import Base
import uuid

# 创建数据库表
Base.metadata.create_all(bind=engine)

def create_test_article():
    """创建测试文章"""
    db = SessionLocal()
    
    try:
        # 检查是否已有测试用户
        test_user = db.query(User).filter(User.email == "test@example.com").first()
        
        if not test_user:
            # 创建测试用户
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
        
        # 检查是否已有测试文章
        existing_article = db.query(Content).filter(
            Content.title == "测试文章：Markdown 渲染功能"
        ).first()
        
        if existing_article:
            print(f"⚠️  测试文章已存在，ID: {existing_article.id}")
            print(f"   访问: http://localhost:5173/articles/{existing_article.id}")
            return str(existing_article.id)
        
        # 创建测试文章（使用文件路径）
        article = Content(
            id=uuid.uuid4(),
            title="测试文章：Markdown 渲染功能",
            description="这是一篇测试文章，用于验证 Markdown 渲染功能是否正常工作。",
            content="articles/test-article.md",  # Markdown 文件路径
            type="article",
            department="技术部",
            author_id=test_user.id,
            cover_image="https://images.unsplash.com/photo-1497366216548-37526070297c?w=800&h=400&fit=crop",
            tags=["测试", "Markdown", "功能验证"],
            is_published=True,
            published_at=datetime.now(),
            reading_time=5,
            view_count=0,
            like_count=0,
            comment_count=0,
            favorite_count=0
        )
        
        db.add(article)
        db.commit()
        db.refresh(article)
        
        print(f"✅ 创建测试文章成功！")
        print(f"   文章ID: {article.id}")
        print(f"   标题: {article.title}")
        print(f"   Markdown 文件: {article.content}")
        print(f"\n📝 访问文章详情页:")
        print(f"   http://localhost:5173/articles/{article.id}")
        print(f"\n📝 或者通过 API 访问:")
        print(f"   http://localhost:8001/api/content/articles/{article.id}")
        
        return str(article.id)
        
    except Exception as e:
        db.rollback()
        print(f"❌ 创建测试文章失败: {e}")
        import traceback
        traceback.print_exc()
        return None
    finally:
        db.close()

if __name__ == "__main__":
    print("🚀 开始创建测试文章...")
    print("-" * 50)
    article_id = create_test_article()
    print("-" * 50)
    if article_id:
        print("✅ 测试数据创建完成！")
    else:
        print("❌ 测试数据创建失败！")

