from pydantic import BaseModel
from typing import Optional

class GuestBase(BaseModel):
    first_name: str
    last_name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    nationality: Optional[str] = None
    passport_no: Optional[str] = None

class GuestCreate(GuestBase):
    pass

class GuestUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    nationality: Optional[str] = None
    passport_no: Optional[str] = None

class GuestResponse(GuestBase):
    id: str
    
    model_config = {"from_attributes": True}