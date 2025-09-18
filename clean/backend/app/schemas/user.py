from pydantic import BaseModel, EmailStr
from app.models.user import UserRole

class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str
    role: UserRole

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    email: EmailStr | None = None
    full_name: str | None = None
    role: UserRole | None = None

class UserResponse(UserBase):
    id: str
    
    model_config = {"from_attributes": True}