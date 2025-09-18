from pydantic import BaseModel
from app.models.order import OrderStatus, OrderType
from typing import Optional

class OrderBase(BaseModel):
    guest_id: str
    order_type: OrderType
    amount: float
    description: Optional[str] = None

class OrderCreate(OrderBase):
    pass

class OrderUpdate(BaseModel):
    order_type: OrderType | None = None
    status: OrderStatus | None = None
    amount: float | None = None
    description: str | None = None

class OrderResponse(OrderBase):
    id: str
    status: OrderStatus
    
    model_config = {"from_attributes": True}