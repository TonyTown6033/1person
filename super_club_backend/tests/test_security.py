"""
安全模块单元测试
"""
import pytest
from datetime import timedelta
from app.core.security import (
    get_password_hash,
    verify_password,
    create_access_token,
    create_refresh_token,
    decode_token
)


class TestPasswordHashing:
    """密码哈希测试"""
    
    def test_hash_password(self):
        """测试密码哈希生成"""
        password = "TestPassword123"
        hashed = get_password_hash(password)
        
        # 哈希值应该不等于原密码
        assert hashed != password
        # 哈希值应该以 $2b$ 开头 (bcrypt)
        assert hashed.startswith("$2b$")
    
    def test_verify_password_correct(self):
        """测试正确密码验证"""
        password = "TestPassword123"
        hashed = get_password_hash(password)
        
        assert verify_password(password, hashed) is True
    
    def test_verify_password_incorrect(self):
        """测试错误密码验证"""
        password = "TestPassword123"
        hashed = get_password_hash(password)
        
        assert verify_password("WrongPassword", hashed) is False
    
    def test_hash_same_password_different_hash(self):
        """测试相同密码生成不同哈希"""
        password = "TestPassword123"
        hash1 = get_password_hash(password)
        hash2 = get_password_hash(password)
        
        # 由于盐值不同，同一密码应产生不同哈希
        assert hash1 != hash2
        # 但两个哈希都应该能验证通过
        assert verify_password(password, hash1) is True
        assert verify_password(password, hash2) is True
    
    def test_long_password_handling(self):
        """测试长密码处理（bcrypt 限制 72 字节）"""
        # 创建一个超过 72 字节的密码
        long_password = "a" * 100
        hashed = get_password_hash(long_password)
        
        # 应该能正确验证
        assert verify_password(long_password, hashed) is True
    
    def test_unicode_password(self):
        """测试 Unicode 密码"""
        password = "密码测试123"
        hashed = get_password_hash(password)
        
        assert verify_password(password, hashed) is True
        assert verify_password("错误密码", hashed) is False


class TestJWTTokens:
    """JWT 令牌测试"""
    
    def test_create_access_token(self):
        """测试创建访问令牌"""
        data = {"sub": "user123"}
        token = create_access_token(data)
        
        assert token is not None
        assert isinstance(token, str)
        assert len(token) > 0
    
    def test_create_access_token_with_expires(self):
        """测试自定义过期时间"""
        data = {"sub": "user123"}
        expires = timedelta(hours=2)
        token = create_access_token(data, expires_delta=expires)
        
        assert token is not None
    
    def test_create_refresh_token(self):
        """测试创建刷新令牌"""
        data = {"sub": "user123"}
        token = create_refresh_token(data)
        
        assert token is not None
        assert isinstance(token, str)
    
    def test_decode_valid_token(self):
        """测试解码有效令牌"""
        user_id = "user123"
        token = create_access_token({"sub": user_id})
        
        payload = decode_token(token)
        
        assert payload is not None
        assert payload["sub"] == user_id
        assert "exp" in payload
    
    def test_decode_invalid_token(self):
        """测试解码无效令牌"""
        payload = decode_token("invalid.token.here")
        
        assert payload is None
    
    def test_decode_expired_token(self):
        """测试解码过期令牌"""
        from datetime import datetime
        from jose import jwt
        from app.core.config import settings
        
        # 创建一个已过期的令牌
        expired_data = {
            "sub": "user123",
            "exp": datetime.utcnow() - timedelta(hours=1)
        }
        expired_token = jwt.encode(
            expired_data,
            settings.SECRET_KEY,
            algorithm=settings.ALGORITHM
        )
        
        payload = decode_token(expired_token)
        
        assert payload is None
    
    def test_token_payload_integrity(self):
        """测试令牌载荷完整性"""
        original_data = {
            "sub": "user456",
            "role": "admin",
            "extra": "data"
        }
        token = create_access_token(original_data)
        payload = decode_token(token)
        
        assert payload["sub"] == "user456"
        assert payload["role"] == "admin"
        assert payload["extra"] == "data"


class TestSecurityEdgeCases:
    """安全边界情况测试"""
    
    def test_empty_password(self):
        """测试空密码"""
        password = ""
        hashed = get_password_hash(password)
        
        assert verify_password(password, hashed) is True
        assert verify_password("something", hashed) is False
    
    def test_special_characters_password(self):
        """测试特殊字符密码"""
        password = "!@#$%^&*()_+-=[]{}|;':\",./<>?"
        hashed = get_password_hash(password)
        
        assert verify_password(password, hashed) is True
    
    def test_whitespace_password(self):
        """测试空白字符密码"""
        password = "   password with spaces   "
        hashed = get_password_hash(password)
        
        assert verify_password(password, hashed) is True
        # 不同空白应该验证失败
        assert verify_password("password with spaces", hashed) is False

