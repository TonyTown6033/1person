from sqlalchemy import Column, String, Integer, DateTime, Text, ForeignKey, Numeric, Boolean
from sqlalchemy.dialects.mysql import JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import uuid
from app.core.database import Base

class Project(Base):
    __tablename__ = "projects"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    owner_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), index=True)
    name = Column(String(200), nullable=False)
    type = Column(String(100))
    description = Column(Text, nullable=False)
    full_description = Column(Text)
    logo = Column(String(500))
    cover_image = Column(String(500))
    tags = Column(Text)
    category = Column(String(50), index=True)
    status = Column(String(20), default="active", index=True)  # active, recruiting, paused, completed
    view_count = Column(Integer, default=0)
    interest_count = Column(Integer, default=0)
    collaboration_count = Column(Integer, default=0)
    contact = Column(JSON)
    needs = Column(JSON, default=[])
    milestones = Column(JSON, default=[])
    team = Column(JSON, default=[])
    is_featured = Column(Boolean, default=False, index=True)
    created_at = Column(DateTime, server_default=func.now(), index=True)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    
    owner = relationship("User", backref="projects")

class ProjectInterest(Base):
    __tablename__ = "project_interests"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    project_id = Column(String(36), ForeignKey("projects.id", ondelete="CASCADE"), index=True)
    user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), index=True)
    message = Column(Text)
    capability = Column(Text)
    contact = Column(JSON)
    status = Column(String(20), default="pending", index=True)  # pending, accepted, rejected
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    
    project = relationship("Project", backref="interests")
    user = relationship("User", backref="project_interests")

