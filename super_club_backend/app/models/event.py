from sqlalchemy import Column, String, Integer, DateTime, Text, ForeignKey, Numeric, Boolean
from sqlalchemy.dialects.mysql import JSON
from sqlalchemy.sql import func
import uuid
from app.core.database import Base

class Event(Base):
    __tablename__ = "events"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String(300), nullable=False)
    description = Column(Text, nullable=False)
    full_description = Column(Text)
    cover = Column(String(500))
    start_date = Column(DateTime, nullable=False, index=True)
    end_date = Column(DateTime, nullable=False)
    location = Column(String(200))
    location_type = Column(String(20), index=True)  # online, offline
    address = Column(Text)
    meeting_link = Column(String(500))
    category = Column(String(50), index=True)
    status = Column(String(20), default="upcoming", index=True)  # upcoming, ongoing, past, cancelled
    capacity = Column(Integer)
    registered_count = Column(Integer, default=0)
    price = Column(Numeric(10, 2), default=0)
    requirements = Column(Text)
    benefits = Column(Text)
    tags = Column(Text)
    agenda = Column(JSON, default=[])
    speakers = Column(JSON, default=[])
    organizer = Column(JSON)
    is_featured = Column(Boolean, default=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

class EventRegistration(Base):
    __tablename__ = "event_registrations"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    event_id = Column(String(36), ForeignKey("events.id", ondelete="CASCADE"), index=True)
    user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), index=True)
    attendee_info = Column(JSON, nullable=False)
    note = Column(Text)
    questions = Column(JSON)
    status = Column(String(20), default="confirmed", index=True)  # confirmed, cancelled, attended
    qr_code = Column(String(500))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

