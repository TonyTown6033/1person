from sqlalchemy import Column, String, Boolean, DateTime, Text
from sqlalchemy.sql import func
import uuid
from app.core.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    email = Column(String(255), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    name = Column(String(100), nullable=False)
    avatar = Column(String(500))
    phone = Column(String(20))
    bio = Column(Text)
    company = Column(String(200))
    position = Column(String(100))
    membership_level = Column(String(20), default="free")  # free, premium, vip
    membership_expiry = Column(DateTime)
    role = Column(String(20), default="user")  # user, admin, super_admin
    verified = Column(Boolean, default=False)
    email_verified = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

