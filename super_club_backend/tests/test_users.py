"""
用户 API 测试
"""
import pytest
from fastapi import status


class TestGetProfile:
    """获取用户信息测试"""
    
    def test_get_profile_success(self, client, test_user, auth_headers):
        """测试正常获取用户信息"""
        response = client.get("/api/user/profile", headers=auth_headers)
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["success"] is True
        assert data["data"]["email"] == "test@example.com"
        assert data["data"]["name"] == "测试用户"
        assert "stats" in data["data"]
    
    def test_get_profile_unauthorized(self, client, db):
        """测试未授权访问"""
        response = client.get("/api/user/profile")
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
    def test_get_profile_invalid_token(self, client, db):
        """测试无效令牌"""
        response = client.get(
            "/api/user/profile",
            headers={"Authorization": "Bearer invalid_token"}
        )
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED


class TestUpdateProfile:
    """更新用户信息测试"""
    
    def test_update_profile_name(self, client, test_user, auth_headers):
        """测试更新用户名"""
        response = client.put("/api/user/profile", json={
            "name": "新名字"
        }, headers=auth_headers)
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["data"]["name"] == "新名字"
    
    def test_update_profile_bio(self, client, test_user, auth_headers):
        """测试更新个人简介"""
        response = client.put("/api/user/profile", json={
            "bio": "这是我的个人简介"
        }, headers=auth_headers)
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["data"]["bio"] == "这是我的个人简介"
    
    def test_update_profile_multiple_fields(self, client, test_user, auth_headers):
        """测试同时更新多个字段"""
        response = client.put("/api/user/profile", json={
            "name": "更新后的名字",
            "company": "某公司",
            "position": "工程师",
            "phone": "13900139999"
        }, headers=auth_headers)
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["data"]["name"] == "更新后的名字"
        assert data["data"]["company"] == "某公司"
        assert data["data"]["position"] == "工程师"
        assert data["data"]["phone"] == "13900139999"
    
    def test_update_profile_unauthorized(self, client, db):
        """测试未授权更新"""
        response = client.put("/api/user/profile", json={
            "name": "新名字"
        })
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED


class TestFavorites:
    """收藏功能测试"""
    
    def test_get_favorites_empty(self, client, test_user, auth_headers):
        """测试空收藏列表"""
        response = client.get("/api/user/favorites", headers=auth_headers)
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["success"] is True
        assert len(data["data"]["items"]) == 0
    
    def test_add_favorite(self, client, test_user, test_article, auth_headers):
        """测试添加收藏"""
        response = client.post("/api/user/favorites", json={
            "type": "content",
            "resourceId": str(test_article.id)
        }, headers=auth_headers)
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["success"] is True
        assert data["data"]["type"] == "content"
    
    def test_add_duplicate_favorite(self, client, test_user, test_article, auth_headers):
        """测试重复收藏"""
        # 第一次收藏
        client.post("/api/user/favorites", json={
            "type": "content",
            "resourceId": str(test_article.id)
        }, headers=auth_headers)
        
        # 第二次收藏相同资源
        response = client.post("/api/user/favorites", json={
            "type": "content",
            "resourceId": str(test_article.id)
        }, headers=auth_headers)
        
        assert response.status_code == status.HTTP_409_CONFLICT
    
    def test_delete_favorite(self, client, test_user, test_article, auth_headers, db):
        """测试取消收藏"""
        # 先添加收藏
        add_response = client.post("/api/user/favorites", json={
            "type": "content",
            "resourceId": str(test_article.id)
        }, headers=auth_headers)
        favorite_id = add_response.json()["data"]["id"]
        
        # 取消收藏
        response = client.delete(
            f"/api/user/favorites/{favorite_id}",
            headers=auth_headers
        )
        
        assert response.status_code == status.HTTP_200_OK
        assert "已取消收藏" in response.json()["message"]
    
    def test_delete_nonexistent_favorite(self, client, test_user, auth_headers):
        """测试取消不存在的收藏"""
        import uuid
        fake_id = str(uuid.uuid4())
        
        response = client.delete(
            f"/api/user/favorites/{fake_id}",
            headers=auth_headers
        )
        
        assert response.status_code == status.HTTP_404_NOT_FOUND

