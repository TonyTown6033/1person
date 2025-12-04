"""
活动 API 测试
"""
import pytest
from fastapi import status
from datetime import datetime, timedelta


class TestGetEvents:
    """获取活动列表测试"""
    
    def test_get_events_empty(self, client, db):
        """测试空活动列表"""
        response = client.get("/api/events")
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["success"] is True
    
    def test_get_events_with_pagination(self, client, db, test_user):
        """测试活动分页"""
        from app.models.event import Event
        
        # 创建多个未来的活动，确保都满足 start_date > now 过滤条件
        for i in range(10):
            now = datetime.now()
            event = Event(
                title=f"活动{i}",
                description=f"描述{i}",
                location="北京",
                start_date=now + timedelta(days=i + 1),
                end_date=now + timedelta(days=i + 1, hours=2),
                status="upcoming"
            )
            db.add(event)
        db.commit()
        
        response = client.get("/api/events?page=1&limit=5")
        data = response.json()
        
        assert len(data["data"]["items"]) == 5
        assert data["data"]["pagination"]["total"] == 10


class TestEventCarousel:
    """活动轮播图测试"""
    
    def test_get_carousel(self, client, db):
        """测试获取活动轮播图"""
        response = client.get("/api/events/carousel")
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["success"] is True


class TestEventRegistration:
    """活动报名测试"""
    
    def test_register_event_unauthorized(self, client, db):
        """测试未授权报名"""
        response = client.post("/api/events/1/register")
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

