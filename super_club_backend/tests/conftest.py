"""
测试配置文件
"""
import pytest
import json
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from datetime import datetime, timedelta

from app.main import app
from app.core.database import Base, get_db
from app.core.security import get_password_hash, create_access_token
from app.models.user import User
from app.models.content import Content


# 使用 SQLite 内存数据库进行测试
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    """覆盖数据库依赖"""
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


# 覆盖应用的数据库依赖
app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(scope="function")
def db():
    """为每个测试函数创建一个新的数据库会话"""
    # 创建所有表
    Base.metadata.create_all(bind=engine)
    
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        # 清理所有表
        Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def client(db):
    """创建测试客户端"""
    return TestClient(app)


@pytest.fixture
def test_user(db):
    """创建测试用户"""
    user = User(
        email="test@example.com",
        password_hash=get_password_hash("Test123456"),
        name="测试用户",
        phone="13800138000",
        is_active=True,
        role="user"
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@pytest.fixture
def test_admin(db):
    """创建测试管理员"""
    admin = User(
        email="admin@example.com",
        password_hash=get_password_hash("Admin123456"),
        name="管理员",
        is_active=True,
        role="admin"
    )
    db.add(admin)
    db.commit()
    db.refresh(admin)
    return admin


@pytest.fixture
def auth_headers(test_user):
    """生成认证头"""
    access_token = create_access_token(data={"sub": str(test_user.id)})
    return {"Authorization": f"Bearer {access_token}"}


@pytest.fixture
def admin_auth_headers(test_admin):
    """生成管理员认证头"""
    access_token = create_access_token(data={"sub": str(test_admin.id)})
    return {"Authorization": f"Bearer {access_token}"}


@pytest.fixture
def test_article(db, test_user):
    """创建测试文章"""
    article = Content(
        title="测试文章",
        description="这是一篇测试文章",
        content="# 测试文章\n\n这是文章内容。",
        excerpt="这是文章摘要",
        type="article",
        department="技术部",
        author_id=test_user.id,
        cover_image="https://example.com/image.jpg",
        tags=json.dumps(["测试", "技术"]),  # SQLite 需要 JSON 字符串
        is_published=True,
        published_at=datetime.now(),
        reading_time=5,
        view_count=100,
        like_count=10,
        comment_count=5,
        favorite_count=3
    )
    db.add(article)
    db.commit()
    db.refresh(article)
    return article


@pytest.fixture
def sample_users(db):
    """创建多个测试用户"""
    users = []
    for i in range(5):
        user = User(
            email=f"user{i}@example.com",
            password_hash=get_password_hash("Password123"),
            name=f"用户{i}",
            is_active=True
        )
        db.add(user)
        users.append(user)
    db.commit()
    for user in users:
        db.refresh(user)
    return users

