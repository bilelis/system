from pydantic import BaseModel
from typing import Dict, Optional
from decimal import Decimal
from app.models.room import RoomStatus

class RoomBase(BaseModel):
    room_number: str
    room_type: str
    floor: int
    rate_per_night: Decimal
    capacity: int
    features: Dict

class RoomCreate(RoomBase):
    pass

class RoomUpdate(BaseModel):
    room_type: Optional[str] = None
    status: Optional[RoomStatus] = None
    rate_per_night: Optional[Decimal] = None
    capacity: Optional[int] = None
    features: Optional[Dict] = None

class RoomResponse(RoomBase):
    id: str
    status: RoomStatus
    
    model_config = {"from_attributes": True}