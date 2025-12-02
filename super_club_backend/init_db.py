#!/usr/bin/env python3
"""
数据库初始化脚本
创建所有表结构
"""
from app.core.database import engine, Base
from app.models import (
    User, Talent, TalentSkill, Project, ProjectInterest,
    Event, EventRegistration, Connection, Content, Comment,
    Favorite, Like, Invitation, Carousel, Notification
)

def init_db():
    """初始化数据库表"""
    print("正在创建数据库表...")
    Base.metadata.create_all(bind=engine)
    print("数据库表创建完成！")

if __name__ == "__main__":
    init_db()

