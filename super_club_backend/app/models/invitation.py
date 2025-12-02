from sqlalchemy import Column, String, Integer, DateTime, Text, ForeignKey

from sqlalchemy.sql import func
import uuid
from app.core.database import Base

class Invitation(Base):
    __tablename__ = "invitations"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    talent_id = Column(String(36), ForeignKey("talents.id", ondelete="CASCADE"), index=True)
    user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), index=True)
    message = Column(Text)
    preferred_date = Column(DateTime, index=True)
    topic = Column(String(200))
    duration = Column(Integer)  # 分钟
    status = Column(String(20), default="pending", index=True)  # pending, accepted, rejected, completed
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

