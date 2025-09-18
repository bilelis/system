from sqlalchemy import Column, String, Integer, Enum, Numeric, JSON, DateTime, UUID
from sqlalchemy.sql import func
import enum
import uuid
from app.db.session import Base

class RoomStatus(str, enum.Enum):
    available = "available"
    occupied = "occupied"
    maintenance = "maintenance"
    cleaning = "cleaning"

class Room(Base):
    __tablename__ = "rooms"
    
    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    room_number = Column(String(10), unique=True, nullable=False)
    room_type = Column(String(50), nullable=False)
    floor = Column(Integer, nullable=False)
    status = Column(Enum(RoomStatus), default=RoomStatus.available)
    rate_per_night = Column(Numeric(10, 2), nullable=False)
    capacity = Column(Integer, nullable=False)
    features = Column(JSON)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())