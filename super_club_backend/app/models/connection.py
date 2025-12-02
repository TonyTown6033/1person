from sqlalchemy import Column, String, DateTime, Text, ForeignKey

from sqlalchemy.sql import func
import uuid
from app.core.database import Base

class Connection(Base):
    __tablename__ = "connections"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    requester_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), index=True)
    target_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), index=True)
    message = Column(Text)
    purpose = Column(String(50))
    status = Column(String(20), default="pending", index=True)  # pending, connected, rejected
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

