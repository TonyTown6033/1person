#!/usr/bin/env python3
"""
创建管理员账户
"""
import uuid
from sqlalchemy import create_engine, text
from app.core.security import get_password_hash
from app.core.config import settings

def create_admin_user():
    """创建管理员用户"""
    engine = create_engine(settings.DATABASE_URL)
    
    try:
        with engine.connect() as connection:
            # 检查管理员是否已存在
            result = connection.execute(text("""
                SELECT id FROM users WHERE email = 'admin@superclub.com'
            """))
            
            if result.fetchone():
                print("管理员账户已存在")
                return
            
            # 创建管理员账户
            admin_id = str(uuid.uuid4())
            password_hash = get_password_hash('admin123')
            
            connection.execute(text("""
                INSERT INTO users (id, email, password_hash, name, role, is_active, verified, email_verified)
                VALUES (:id, :email, :password_hash, :name, :role, :is_active, :verified, :email_verified)
            """), {
                'id': admin_id,
                'email': 'admin@superclub.com',
                'password_hash': password_hash,
                'name': '系统管理员',
                'role': 'super_admin',
                'is_active': True,
                'verified': True,
                'email_verified': True
            })
            
            connection.commit()
            print("✅ 管理员账户创建成功")
            print("📧 邮箱: admin@superclub.com")
            print("🔑 密码: admin123")
            
    except Exception as e:
        print(f"创建管理员账户失败: {e}")

if __name__ == "__main__":
    create_admin_user()
