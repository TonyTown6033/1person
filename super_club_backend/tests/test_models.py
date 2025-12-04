"""
数据模型单元测试
"""
import pytest
import json
from datetime import datetime
from app.models.user import User
from app.models.content import Content
from app.core.security import get_password_hash


class TestUserModel:
    """用户模型测试"""
    
    def test_create_user(self, db):
        """测试创建用户"""
        user = User(
            email="model_test@example.com",
            password_hash=get_password_hash("Password123"),
            name="模型测试用户"
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        
        assert user.id is not None
        assert user.email == "model_test@example.com"
        assert user.name == "模型测试用户"
        assert user.created_at is not None
    
    def test_user_default_values(self, db):
        """测试用户默认值"""
        user = User(
            email="default@example.com",
            password_hash="hashed",
            name="默认值测试"
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        
        assert user.is_active is True
        assert user.role == "user"
        assert user.membership_level == "free"
        assert user.verified is False
        assert user.email_verified is False
    
    def test_user_unique_email(self, db):
        """测试邮箱唯一性"""
        user1 = User(
            email="unique@example.com",
            password_hash="hash1",
            name="用户1"
        )
        db.add(user1)
        db.commit()
        
        user2 = User(
            email="unique@example.com",
            password_hash="hash2",
            name="用户2"
        )
        db.add(user2)
        
        with pytest.raises(Exception):  # SQLAlchemy IntegrityError
            db.commit()
    
    def test_user_update(self, db, test_user):
        """测试更新用户"""
        test_user.name = "更新后的名字"
        test_user.bio = "新的个人简介"
        db.commit()
        db.refresh(test_user)
        
        assert test_user.name == "更新后的名字"
        assert test_user.bio == "新的个人简介"
    
    def test_user_optional_fields(self, db):
        """测试用户可选字段"""
        user = User(
            email="optional@example.com",
            password_hash="hash",
            name="可选字段测试",
            phone="13800138000",
            bio="我是开发者",
            company="某公司",
            position="工程师"
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        
        assert user.phone == "13800138000"
        assert user.bio == "我是开发者"
        assert user.company == "某公司"
        assert user.position == "工程师"


class TestContentModel:
    """内容模型测试"""
    
    def test_create_article(self, db, test_user):
        """测试创建文章"""
        article = Content(
            title="测试标题",
            content="测试内容",
            type="article",
            author_id=test_user.id,
            is_published=True,
            published_at=datetime.now()
        )
        db.add(article)
        db.commit()
        db.refresh(article)
        
        assert article.id is not None
        assert article.title == "测试标题"
        assert article.type == "article"
        assert article.author_id == test_user.id
    
    def test_article_default_counts(self, db, test_user):
        """测试文章默认计数"""
        article = Content(
            title="计数测试",
            content="内容",
            type="article",
            author_id=test_user.id
        )
        db.add(article)
        db.commit()
        db.refresh(article)
        
        assert article.view_count == 0
        assert article.like_count == 0
        assert article.comment_count == 0
        assert article.favorite_count == 0
    
    def test_article_with_tags(self, db, test_user):
        """测试文章标签"""
        tags_list = ["Python", "FastAPI", "测试"]
        article = Content(
            title="标签测试",
            content="内容",
            type="article",
            author_id=test_user.id,
            tags=json.dumps(tags_list)  # SQLite 需要 JSON 字符串
        )
        db.add(article)
        db.commit()
        db.refresh(article)
        
        # 验证存储的是 JSON 字符串，可以解析回列表
        assert json.loads(article.tags) == tags_list
    
    def test_article_update_counts(self, db, test_article):
        """测试更新文章计数"""
        test_article.view_count += 1
        test_article.like_count += 1
        db.commit()
        db.refresh(test_article)
        
        assert test_article.view_count == 101  # 原始是100
        assert test_article.like_count == 11   # 原始是10
    
    def test_unpublished_article(self, db, test_user):
        """测试未发布文章"""
        article = Content(
            title="草稿",
            content="内容",
            type="article",
            author_id=test_user.id,
            is_published=False
        )
        db.add(article)
        db.commit()
        db.refresh(article)
        
        assert article.is_published is False
        assert article.published_at is None


class TestContentQuery:
    """内容查询测试"""
    
    def test_query_published_articles(self, db, test_user):
        """测试查询已发布文章"""
        # 创建已发布和未发布文章
        published = Content(
            title="已发布",
            content="内容",
            type="article",
            author_id=test_user.id,
            is_published=True,
            published_at=datetime.now()
        )
        unpublished = Content(
            title="未发布",
            content="内容",
            type="article",
            author_id=test_user.id,
            is_published=False
        )
        db.add_all([published, unpublished])
        db.commit()
        
        # 查询已发布文章
        result = db.query(Content).filter(Content.is_published == True).all()
        
        titles = [c.title for c in result]
        assert "已发布" in titles
        assert "未发布" not in titles
    
    def test_query_by_department(self, db, test_user):
        """测试按部门查询"""
        tech = Content(
            title="技术文章",
            content="内容",
            type="article",
            department="技术部",
            author_id=test_user.id,
            is_published=True,
            published_at=datetime.now()
        )
        hr = Content(
            title="人力文章",
            content="内容",
            type="article",
            department="人力部",
            author_id=test_user.id,
            is_published=True,
            published_at=datetime.now()
        )
        db.add_all([tech, hr])
        db.commit()
        
        result = db.query(Content).filter(Content.department == "技术部").all()
        
        assert len(result) == 1
        assert result[0].title == "技术文章"
    
    def test_query_order_by_published_date(self, db, test_user):
        """测试按发布日期排序"""
        from datetime import timedelta
        
        older = Content(
            title="旧文章",
            content="内容",
            type="article",
            author_id=test_user.id,
            is_published=True,
            published_at=datetime.now() - timedelta(days=7)
        )
        newer = Content(
            title="新文章",
            content="内容",
            type="article",
            author_id=test_user.id,
            is_published=True,
            published_at=datetime.now()
        )
        db.add_all([older, newer])
        db.commit()
        
        result = db.query(Content).filter(
            Content.is_published == True
        ).order_by(Content.published_at.desc()).all()
        
        # 新文章应该在前面
        assert result[0].title == "新文章"

