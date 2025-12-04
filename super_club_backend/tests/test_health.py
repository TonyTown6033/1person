"""
健康检查和基础端点测试
"""
import pytest
from fastapi import status


class TestHealthCheck:
    """健康检查测试"""
    
    def test_health_check(self, client, db):
        """测试健康检查端点"""
        response = client.get("/health")
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["status"] == "healthy"
    
    def test_root_endpoint(self, client, db):
        """测试根端点"""
        response = client.get("/")
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert "message" in data
        assert "Super Club API" in data["message"]
        assert "version" in data


class TestAPIDocumentation:
    """API 文档测试"""
    
    def test_docs_available(self, client, db):
        """测试 Swagger 文档可访问"""
        response = client.get("/docs")
        
        assert response.status_code == status.HTTP_200_OK
    
    def test_redoc_available(self, client, db):
        """测试 ReDoc 文档可访问"""
        response = client.get("/redoc")
        
        assert response.status_code == status.HTTP_200_OK
    
    def test_openapi_schema(self, client, db):
        """测试 OpenAPI schema"""
        response = client.get("/openapi.json")
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert "openapi" in data
        assert "info" in data
        assert data["info"]["title"] == "Super Club API"

