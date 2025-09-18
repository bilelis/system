from sqlalchemy import Column, String, DateTime, Numeric, Enum
from sqlalchemy.sql import func
import enum
from app.db.session import Base

class OrderStatus(str, enum.Enum):
    pending = "pending"
    completed = "completed"
    cancelled = "cancelled"

class OrderType(str, enum.Enum):
    room_booking = "room_booking"
    restaurant = "restaurant"
    spa = "spa"
    other = "other"

class Order(Base):
    __tablename__ = "orders"
    
    id = Column(String, primary_key=True)
    guest_id = Column(String, nullable=False)
    order_type = Column(Enum(OrderType), nullable=False)
    status = Column(Enum(OrderStatus), default=OrderStatus.pending)
    amount = Column(Numeric(10, 2), nullable=False)
    description = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())