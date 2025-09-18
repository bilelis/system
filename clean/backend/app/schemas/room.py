from pydantic import BaseModel
from app.models.room import RoomStatus, RoomType

class RoomBase(BaseModel):
    room_number: str
    room_type: RoomType
    floor: int
    rate_per_night: float
    capacity: int
    features: str | None = None

class RoomCreate(RoomBase):
    pass

class RoomUpdate(BaseModel):
    room_type: RoomType | None = None
    floor: int | None = None
    status: RoomStatus | None = None
    rate_per_night: float | None = None
    capacity: int | None = None
    features: str | None = None

class RoomResponse(RoomBase):
    id: str
    status: RoomStatus
    
    model_config = {"from_attributes": True}