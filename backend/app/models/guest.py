from sqlalchemy import Column, String, DateTime, UUID
from sqlalchemy.sql import func
import uuid
from app.db.session import Base

class Guest(Base):
    __tablename__ = "guests"
    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(255))
    phone = Column(String(20))
    nationality = Column(String(50))
    passport_no = Column(String(50))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
