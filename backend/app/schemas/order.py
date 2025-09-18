from pydantic import BaseModel
from typing import Optional
from decimal import Decimal
from app.models.order import OrderStatus

class OrderBase(BaseModel):
    guest_id: Optional[str] = None
    outlet_id: str
    room_id: Optional[str] = None
    user_id: str
    order_number: str
    status: Optional[OrderStatus] = None
    total_amount: Decimal
    notes: Optional[str] = None

class OrderCreate(OrderBase):
    pass

class OrderUpdate(BaseModel):
    status: Optional[OrderStatus] = None
    notes: Optional[str] = None

class OrderResponse(OrderBase):
    id: str
    created_at: Optional[str]
    updated_at: Optional[str]
    
    model_config = {"from_attributes": True}