#!/usr/bin/env python3
"""
API 接口测试脚本
"""
import requests
import json
from datetime import datetime

BASE_URL = "http://localhost:8001"

def print_response(title, response):
    """打印响应"""
    print(f"\n{'='*60}")
    print(f"{title}")
    print(f"{'='*60}")
    print(f"状态码: {response.status_code}")
    try:
        data = response.json()
        print(f"响应: {json.dumps(data, indent=2, ensure_ascii=False)}")
    except:
        print(f"响应: {response.text}")
    print()

def test_health():
    """测试健康检查"""
    print_response("1. 健康检查", requests.get(f"{BASE_URL}/health"))

def test_root():
    """测试根路径"""
    print_response("2. 根路径", requests.get(f"{BASE_URL}/"))

def test_register():
    """测试用户注册"""
    data = {
        "email": f"test_{datetime.now().strftime('%Y%m%d%H%M%S')}@example.com",
        "password": "Test123456",
        "name": "测试用户",
        "phone": "13800138000"
    }
    print_response("3. 用户注册", requests.post(f"{BASE_URL}/api/auth/register", json=data))

def test_login():
    """测试用户登录"""
    data = {
        "email": "test@example.com",
        "password": "Test123456"
    }
    response = requests.post(f"{BASE_URL}/api/auth/login", json=data)
    print_response("4. 用户登录", response)
    if response.status_code == 200:
        try:
            return response.json()["data"]["tokens"]["accessToken"]
        except:
            pass
    return None

def test_get_events(token=None):
    """测试获取活动列表"""
    headers = {}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    print_response("5. 获取活动列表", requests.get(f"{BASE_URL}/api/events?page=1&limit=5", headers=headers))

def test_get_talents(token=None):
    """测试获取人才列表"""
    headers = {}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    print_response("6. 获取人才列表", requests.get(f"{BASE_URL}/api/talents?page=1&limit=5", headers=headers))

def test_get_talent_stats():
    """测试人才统计"""
    print_response("7. 人才统计", requests.get(f"{BASE_URL}/api/talents/stats"))

def test_get_projects(token=None):
    """测试获取项目列表"""
    headers = {}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    print_response("8. 获取项目列表", requests.get(f"{BASE_URL}/api/projects?page=1&limit=5", headers=headers))

def test_get_content_cards():
    """测试获取内容卡片"""
    print_response("9. 获取内容卡片", requests.get(f"{BASE_URL}/api/content/cards?page=1&limit=2"))

def test_get_carousels():
    """测试轮播图"""
    print_response("10. 活动轮播图", requests.get(f"{BASE_URL}/api/events/carousel"))
    print_response("11. 链接轮播图", requests.get(f"{BASE_URL}/api/links/carousel"))

if __name__ == "__main__":
    print("\n开始测试 API 接口...\n")
    
    # 基础接口测试
    test_health()
    test_root()
    
    # 注册和登录
    test_register()
    token = test_login()
    
    # 需要认证的接口
    if token:
        test_get_events(token)
        test_get_talents(token)
        test_get_projects(token)
    else:
        print("\n注意: 登录失败，跳过需要认证的接口测试")
    
    # 公开接口
    test_get_talent_stats()
    test_get_content_cards()
    test_get_carousels()
    
    print("\n测试完成！")

