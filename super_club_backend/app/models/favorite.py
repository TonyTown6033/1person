from sqlalchemy import Column, String, DateTime, ForeignKey

from sqlalchemy.sql import func
import uuid
from app.core.database import Base

class Favorite(Base):
    __tablename__ = "favorites"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), index=True)
    resource_type = Column(String(20), nullable=False)  # talent, project, event, content
    resource_id = Column(String(36), nullable=False)
    created_at = Column(DateTime, server_default=func.now(), index=True)

