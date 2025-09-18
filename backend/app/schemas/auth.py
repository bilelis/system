from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional
from app.models.user import UserRole
import uuid

class Token(BaseModel):
    access_token: str
    token_type: str
    role: UserRole
    user_id: str

class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str
    role: UserRole

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: str
    
    @field_validator('id')
    @classmethod
    def validate_id(cls, v):
        if isinstance(v, uuid.UUID):
            return str(v)
        return v
    
    model_config = {"from_attributes": True}