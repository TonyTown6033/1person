"""
认证 API 测试
"""
import pytest
from fastapi import status


class TestRegister:
    """用户注册测试"""
    
    def test_register_success(self, client, db):
        """测试正常注册"""
        response = client.post("/api/auth/register", json={
            "email": "newuser@example.com",
            "password": "Password123",
            "name": "新用户",
            "phone": "13900139000"
        })
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["success"] is True
        assert data["data"]["user"]["email"] == "newuser@example.com"
        assert data["data"]["user"]["name"] == "新用户"
        assert "accessToken" in data["data"]["tokens"]
        assert "refreshToken" in data["data"]["tokens"]
    
    def test_register_duplicate_email(self, client, test_user):
        """测试重复邮箱注册"""
        response = client.post("/api/auth/register", json={
            "email": "test@example.com",  # 已存在的邮箱
            "password": "Password123",
            "name": "另一个用户"
        })
        
        assert response.status_code == status.HTTP_409_CONFLICT
        assert "已被注册" in response.json()["detail"]
    
    def test_register_invalid_email(self, client, db):
        """测试无效邮箱格式"""
        response = client.post("/api/auth/register", json={
            "email": "invalid-email",
            "password": "Password123",
            "name": "用户"
        })
        
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    
    def test_register_short_password(self, client, db):
        """测试密码过短"""
        response = client.post("/api/auth/register", json={
            "email": "test@example.com",
            "password": "short",  # 少于8个字符
            "name": "用户"
        })
        
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    
    def test_register_missing_name(self, client, db):
        """测试缺少必填字段"""
        response = client.post("/api/auth/register", json={
            "email": "test@example.com",
            "password": "Password123"
            # 缺少 name
        })
        
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


class TestLogin:
    """用户登录测试"""
    
    def test_login_success(self, client, test_user):
        """测试正常登录"""
        response = client.post("/api/auth/login", json={
            "email": "test@example.com",
            "password": "Test123456"
        })
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["success"] is True
        assert data["data"]["user"]["email"] == "test@example.com"
        assert "accessToken" in data["data"]["tokens"]
        assert "refreshToken" in data["data"]["tokens"]
        assert "expiresIn" in data["data"]["tokens"]
    
    def test_login_wrong_password(self, client, test_user):
        """测试密码错误"""
        response = client.post("/api/auth/login", json={
            "email": "test@example.com",
            "password": "WrongPassword"
        })
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert "密码错误" in response.json()["detail"]
    
    def test_login_nonexistent_user(self, client, db):
        """测试用户不存在"""
        response = client.post("/api/auth/login", json={
            "email": "nonexistent@example.com",
            "password": "Password123"
        })
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
    def test_login_inactive_user(self, client, db):
        """测试禁用用户登录"""
        from app.models.user import User
        from app.core.security import get_password_hash
        
        # 创建禁用用户
        user = User(
            email="inactive@example.com",
            password_hash=get_password_hash("Password123"),
            name="禁用用户",
            is_active=False
        )
        db.add(user)
        db.commit()
        
        response = client.post("/api/auth/login", json={
            "email": "inactive@example.com",
            "password": "Password123"
        })
        
        assert response.status_code == status.HTTP_403_FORBIDDEN
        assert "已被禁用" in response.json()["detail"]


class TestRefreshToken:
    """刷新令牌测试"""
    
    def test_refresh_token_success(self, client, test_user):
        """测试正常刷新令牌"""
        # 先登录获取 refresh token
        login_response = client.post("/api/auth/login", json={
            "email": "test@example.com",
            "password": "Test123456"
        })
        refresh_token = login_response.json()["data"]["tokens"]["refreshToken"]
        
        # 使用 refresh token 刷新
        response = client.post("/api/auth/refresh", json={
            "refreshToken": refresh_token
        })
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert "accessToken" in data["data"]
        assert "expiresIn" in data["data"]
    
    def test_refresh_token_invalid(self, client, db):
        """测试无效的刷新令牌"""
        response = client.post("/api/auth/refresh", json={
            "refreshToken": "invalid_token"
        })
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED


class TestLogout:
    """登出测试"""
    
    def test_logout_success(self, client, db):
        """测试正常登出"""
        response = client.post("/api/auth/logout")
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["success"] is True
        assert "退出成功" in data["message"]

