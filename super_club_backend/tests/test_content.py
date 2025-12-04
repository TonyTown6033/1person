"""
内容 API 测试
"""
import pytest
from fastapi import status
from datetime import datetime


class TestGetContentCards:
    """获取内容卡片测试"""
    
    def test_get_cards_empty(self, client, db):
        """测试空内容列表"""
        response = client.get("/api/content/cards")
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["success"] is True
        assert "items" in data["data"]
        assert "pagination" in data["data"]
    
    def test_get_cards_with_content(self, client, test_article):
        """测试有内容时获取卡片"""
        response = client.get("/api/content/cards")
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert len(data["data"]["items"]) >= 1
    
    def test_get_cards_pagination(self, client, db, test_user):
        """测试分页功能"""
        # 创建多篇文章
        from app.models.content import Content
        for i in range(10):
            content = Content(
                title=f"测试文章{i}",
                description=f"描述{i}",
                content=f"内容{i}",
                type="article",
                author_id=test_user.id,
                is_published=True,
                published_at=datetime.now()
            )
            db.add(content)
        db.commit()
        
        # 测试第一页
        response = client.get("/api/content/cards?page=1&limit=5")
        data = response.json()
        assert len(data["data"]["items"]) == 5
        assert data["data"]["pagination"]["page"] == 1
        assert data["data"]["pagination"]["totalPages"] == 2
    
    def test_get_cards_filter_by_department(self, client, test_article):
        """测试按部门筛选"""
        response = client.get("/api/content/cards?department=技术部")
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        for item in data["data"]["items"]:
            assert item["department"] == "技术部"
    
    def test_get_cards_filter_by_type(self, client, test_article):
        """测试按类型筛选"""
        response = client.get("/api/content/cards?type=article")
        
        assert response.status_code == status.HTTP_200_OK
    
    def test_get_cards_search(self, client, test_article):
        """测试搜索功能"""
        response = client.get("/api/content/cards?search=测试")
        
        assert response.status_code == status.HTTP_200_OK


class TestGetArticles:
    """获取文章列表测试"""
    
    def test_get_articles_success(self, client, test_article):
        """测试获取文章列表"""
        response = client.get("/api/content/articles")
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["success"] is True
        assert "items" in data["data"]
    
    def test_get_articles_pagination(self, client, db, test_user):
        """测试文章分页"""
        from app.models.content import Content
        
        # 创建多篇文章
        for i in range(15):
            content = Content(
                title=f"文章{i}",
                content=f"内容{i}",
                type="article",
                author_id=test_user.id,
                is_published=True,
                published_at=datetime.now()
            )
            db.add(content)
        db.commit()
        
        response = client.get("/api/content/articles?page=1&limit=10")
        data = response.json()
        
        assert len(data["data"]["items"]) == 10
        assert data["data"]["pagination"]["total"] == 15


class TestGetArticleDetail:
    """获取文章详情测试"""
    
    def test_get_article_detail_success(self, client, test_article):
        """测试获取文章详情"""
        response = client.get(f"/api/content/articles/{test_article.id}")
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["success"] is True
        assert data["data"]["title"] == "测试文章"
        assert "content" in data["data"]
        assert "author" in data["data"]
        assert "stats" in data["data"]
    
    def test_get_article_increases_view_count(self, client, test_article, db):
        """测试访问文章增加浏览量"""
        initial_views = test_article.view_count
        
        client.get(f"/api/content/articles/{test_article.id}")
        
        # 刷新对象
        db.refresh(test_article)
        assert test_article.view_count == initial_views + 1
    
    def test_get_article_nonexistent(self, client, db):
        """测试获取不存在的文章"""
        import uuid
        fake_id = str(uuid.uuid4())
        
        response = client.get(f"/api/content/articles/{fake_id}")
        
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert "文章不存在" in response.json()["detail"]


class TestCreateArticle:
    """创建文章测试"""
    
    def test_create_article_success(self, client, test_user, auth_headers):
        """测试创建文章"""
        response = client.post("/api/content/articles", json={
            "title": "新文章",
            "content": "# 标题\n\n这是内容",
            "description": "这是描述",
            "department": "技术部",
            # 注意：SQLite 测试环境不支持 JSON 列表，不传 tags
            "isPublished": True,
            "readingTime": 5
        }, headers=auth_headers)
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["success"] is True
        assert data["data"]["title"] == "新文章"
        assert "id" in data["data"]
    
    def test_create_article_unauthorized(self, client, db):
        """测试未授权创建文章"""
        response = client.post("/api/content/articles", json={
            "title": "新文章",
            "content": "内容"
        })
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED


class TestArticleLike:
    """文章点赞测试"""
    
    def test_like_article_success(self, client, test_user, test_article, auth_headers):
        """测试点赞文章"""
        response = client.post(
            f"/api/content/articles/{test_article.id}/like",
            headers=auth_headers
        )
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["data"]["isLiked"] is True
    
    def test_like_article_twice(self, client, test_user, test_article, auth_headers):
        """测试重复点赞"""
        # 第一次点赞
        client.post(
            f"/api/content/articles/{test_article.id}/like",
            headers=auth_headers
        )
        
        # 第二次点赞
        response = client.post(
            f"/api/content/articles/{test_article.id}/like",
            headers=auth_headers
        )
        
        assert response.status_code == status.HTTP_409_CONFLICT
    
    def test_unlike_article_success(self, client, test_user, test_article, auth_headers):
        """测试取消点赞"""
        # 先点赞
        client.post(
            f"/api/content/articles/{test_article.id}/like",
            headers=auth_headers
        )
        
        # 取消点赞
        response = client.delete(
            f"/api/content/articles/{test_article.id}/like",
            headers=auth_headers
        )
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["data"]["isLiked"] is False


class TestArticleComments:
    """文章评论测试"""
    
    def test_create_comment_success(self, client, test_user, test_article, auth_headers):
        """测试创建评论"""
        response = client.post(
            f"/api/content/articles/{test_article.id}/comments",
            json={"content": "这是一条评论"},
            headers=auth_headers
        )
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["data"]["content"] == "这是一条评论"
        assert "author" in data["data"]
    
    def test_get_comments_empty(self, client, test_article):
        """测试空评论列表"""
        response = client.get(f"/api/content/articles/{test_article.id}/comments")
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert "items" in data["data"]
    
    def test_create_comment_unauthorized(self, client, test_article):
        """测试未授权评论"""
        response = client.post(
            f"/api/content/articles/{test_article.id}/comments",
            json={"content": "评论"}
        )
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

