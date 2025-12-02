from sqlalchemy import Column, String, Boolean, Integer, DateTime, Text, ForeignKey
from sqlalchemy.dialects.mysql import JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import uuid
from app.core.database import Base

class Talent(Base):
    __tablename__ = "talents"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"))
    name = Column(String(100), nullable=False)
    role = Column(String(200), nullable=False)
    company = Column(String(200), nullable=False)
    location = Column(String(100))
    avatar = Column(String(500))
    description = Column(Text)
    bio = Column(Text)
    tags = Column(Text)
    verified = Column(Boolean, default=False, index=True)
    available = Column(Boolean, default=True, index=True)
    stats = Column(JSON, default={"projects": "0", "experience": "0", "followers": "0"})
    skills = Column(JSON, default=[])
    education = Column(JSON, default=[])
    contact = Column(JSON)
    view_count = Column(Integer, default=0)
    follower_count = Column(Integer, default=0, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    
    user = relationship("User", backref="talents")

class TalentSkill(Base):
    __tablename__ = "talent_skills"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    talent_id = Column(String(36), ForeignKey("talents.id", ondelete="CASCADE"), index=True)
    skill_name = Column(String(100), nullable=False, index=True)
    skill_level = Column(String(20))  # beginner, intermediate, advanced, expert
    created_at = Column(DateTime, server_default=func.now())
    
    talent = relationship("Talent", backref="talent_skills_list")

