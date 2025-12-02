from sqlalchemy import Column, String, DateTime, Text, ForeignKey, Boolean

from sqlalchemy.sql import func
import uuid
from app.core.database import Base

class Notification(Base):
    __tablename__ = "notifications"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), index=True)
    type = Column(String(50), nullable=False)  # invitation, connection, event, system
    title = Column(String(200), nullable=False)
    content = Column(Text)
    link = Column(String(500))
    is_read = Column(Boolean, default=False, index=True)
    created_at = Column(DateTime, server_default=func.now(), index=True)

