#!/usr/bin/env python3
"""
管理后台演示设置脚本
创建一个演示用的管理员账户数据
"""
import json
from datetime import datetime

def create_demo_admin_data():
    """创建演示管理员数据"""
    
    # 演示管理员账户信息
    demo_admin = {
        "id": "admin-demo-001",
        "email": "admin@superclub.com",
        "password": "admin123",  # 实际使用时应该加密
        "name": "系统管理员",
        "role": "super_admin",
        "avatar": None,
        "phone": "13800138000",
        "company": "Super Club",
        "position": "系统管理员",
        "membership_level": "vip",
        "is_active": True,
        "verified": True,
        "email_verified": True,
        "created_at": datetime.now().isoformat() + "Z",
        "updated_at": datetime.now().isoformat() + "Z"
    }
    
    # 演示统计数据
    demo_stats = {
        "users": {
            "total": 1234,
            "active": 1180,
            "new_this_month": 89,
            "growth_rate": 7.8
        },
        "projects": {
            "total": 156,
            "active": 89,
            "featured": 12
        },
        "events": {
            "total": 45,
            "upcoming": 8
        },
        "content": {
            "total": 234,
            "published": 189
        }
    }
    
    # 演示活动数据
    demo_activities = [
        {
            "id": "activity_1",
            "type": "user_register",
            "title": "新用户注册：张三",
            "icon": "👤",
            "time": datetime.now().isoformat() + "Z"
        },
        {
            "id": "activity_2", 
            "type": "project_create",
            "title": "新项目发布：AI智能助手",
            "icon": "🚀",
            "time": datetime.now().isoformat() + "Z"
        }
    ]
    
    # 保存到文件
    demo_data = {
        "admin_user": demo_admin,
        "dashboard_stats": demo_stats,
        "recent_activities": demo_activities
    }
    
    with open('demo_admin_data.json', 'w', encoding='utf-8') as f:
        json.dump(demo_data, f, ensure_ascii=False, indent=2)
    
    print("✅ 演示管理员数据已创建")
    print("📧 管理员邮箱: admin@superclub.com")
    print("🔑 管理员密码: admin123")
    print("📄 数据文件: demo_admin_data.json")
    print("\n🎯 访问管理后台:")
    print("1. 启动前端服务: http://127.0.0.1:3000")
    print("2. 访问管理后台登录页: http://127.0.0.1:3000/admin/login")
    print("3. 使用上述账户信息登录")

if __name__ == "__main__":
    create_demo_admin_data()
