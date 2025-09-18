from pydantic import BaseModel, EmailStr
from typing import Optional

class GuestBase(BaseModel):
    first_name: str
    last_name: str
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    nationality: Optional[str] = None
    passport_no: Optional[str] = None

class GuestCreate(GuestBase):
    pass

class GuestUpdate(BaseModel):
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    nationality: Optional[str] = None
    passport_no: Optional[str] = None

class GuestResponse(GuestBase):
    id: str
    
    model_config = {"from_attributes": True}
