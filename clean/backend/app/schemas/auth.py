from pydantic import BaseModel, EmailStr
from app.models.user import UserRole

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
    
    model_config = {"from_attributes": True}