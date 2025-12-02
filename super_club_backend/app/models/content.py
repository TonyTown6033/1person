from sqlalchemy import Column, String, Integer, DateTime, Text, ForeignKey, Boolean

from sqlalchemy.sql import func
import uuid
from app.core.database import Base

class Content(Base):
    __tablename__ = "contents"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String(300), nullable=False)
    description = Column(Text)
    excerpt = Column(Text)
    content = Column(Text)
    image = Column(String(500))
    cover_image = Column(String(500))
    type = Column(String(20), index=True)  # article, video, course, case
    department = Column(String(50), index=True)
    author_id = Column(String(36), ForeignKey("users.id"), index=True)
    tags = Column(Text)
    view_count = Column(Integer, default=0)
    like_count = Column(Integer, default=0)
    comment_count = Column(Integer, default=0)
    favorite_count = Column(Integer, default=0)
    reading_time = Column(Integer)
    published_at = Column(DateTime, index=True)
    is_published = Column(Boolean, default=False, index=True)
    is_featured = Column(Boolean, default=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

class Comment(Base):
    __tablename__ = "comments"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    content_id = Column(String(36), ForeignKey("contents.id", ondelete="CASCADE"), index=True)
    user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), index=True)
    parent_id = Column(String(36), ForeignKey("comments.id", ondelete="CASCADE"), index=True)
    content = Column(Text, nullable=False)
    like_count = Column(Integer, default=0)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now(), index=True)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

