from sqlalchemy import Column, String, DateTime, Numeric, Text, Enum, UUID, ForeignKey
from sqlalchemy.sql import func
import uuid
import enum
from app.db.session import Base

class OrderStatus(str, enum.Enum):
    pending = "pending"
    preparing = "preparing"
    completed = "completed"
    cancelled = "cancelled"

class Order(Base):
    __tablename__ = "orders"
    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    guest_id = Column(UUID, ForeignKey("guests.id"))
    outlet_id = Column(UUID, ForeignKey("outlets.id"), nullable=False)
    room_id = Column(UUID, ForeignKey("rooms.id"))
    user_id = Column(UUID, ForeignKey("users.id"), nullable=False)
    order_number = Column(String(20), unique=True, nullable=False)
    status = Column(Enum(OrderStatus), default=OrderStatus.pending)
    total_amount = Column(Numeric(10,2), nullable=False)
    notes = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
