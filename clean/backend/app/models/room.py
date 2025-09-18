from sqlalchemy import Column, String, Integer, Enum, DateTime, Numeric
from sqlalchemy.sql import func
import enum
from app.db.session import Base

class RoomStatus(str, enum.Enum):
    available = "available"
    occupied = "occupied"
    maintenance = "maintenance"

class RoomType(str, enum.Enum):
    standard = "Standard"
    deluxe = "Deluxe"
    suite = "Suite"

class Room(Base):
    __tablename__ = "rooms"
    
    id = Column(String, primary_key=True)
    room_number = Column(String(10), unique=True, nullable=False)
    room_type = Column(Enum(RoomType), nullable=False)
    floor = Column(Integer, nullable=False)
    status = Column(Enum(RoomStatus), default=RoomStatus.available)
    rate_per_night = Column(Numeric(10, 2), nullable=False)
    capacity = Column(Integer, nullable=False)
    features = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())