#!/usr/bin/env python3
"""
添加用户角色字段的数据库迁移脚本
"""
import sys
from sqlalchemy import text
from app.core.database import engine
from app.core.logging import logger

def add_user_role_column():
    """添加用户角色字段"""
    try:
        with engine.connect() as connection:
            # 检查角色字段是否已存在
            result = connection.execute(text("""
                SELECT COLUMN_NAME 
                FROM INFORMATION_SCHEMA.COLUMNS 
                WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = 'users' AND COLUMN_NAME = 'role'
            """))
            
            if result.fetchone():
                logger.info("用户角色字段已存在，跳过添加")
                return
            
            # 添加角色字段
            connection.execute(text("""
                ALTER TABLE users 
                ADD COLUMN role VARCHAR(20) DEFAULT 'user'
            """))
            
            # 为现有用户设置默认角色
            connection.execute(text("""
                UPDATE users 
                SET role = 'user' 
                WHERE role IS NULL
            """))
            
            # 创建一个超级管理员账户（如果不存在）
            result = connection.execute(text("""
                SELECT id FROM users WHERE email = 'admin@superclub.com'
            """))
            
            if not result.fetchone():
                from app.core.security import get_password_hash
                import uuid
                
                admin_id = str(uuid.uuid4())
                password_hash = get_password_hash('admin123')
                
                connection.execute(text("""
                    INSERT INTO users (id, email, password_hash, name, role, is_active)
                    VALUES (:id, :email, :password_hash, :name, :role, :is_active)
                """), {
                    'id': admin_id,
                    'email': 'admin@superclub.com',
                    'password_hash': password_hash,
                    'name': '系统管理员',
                    'role': 'super_admin',
                    'is_active': True
                })
                
                logger.info("已创建超级管理员账户: admin@superclub.com / admin123")
            
            connection.commit()
            logger.info("用户角色字段添加成功")
            
    except Exception as e:
        logger.error(f"添加用户角色字段失败: {e}")
        sys.exit(1)

if __name__ == "__main__":
    logger.info("开始添加用户角色字段...")
    add_user_role_column()
    logger.info("迁移完成")
