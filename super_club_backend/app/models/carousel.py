from sqlalchemy import Column, String, Integer, DateTime, Boolean

from sqlalchemy.sql import func
import uuid
from app.core.database import Base

class Carousel(Base):
    __tablename__ = "carousels"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    page = Column(String(50), nullable=False, index=True)  # events, links, home
    image = Column(String(500), nullable=False)
    title = Column(String(200))
    subtitle = Column(String(200))
    link = Column(String(500))
    order_num = Column(Integer, default=0, index=True)
    is_active = Column(Boolean, default=True, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

