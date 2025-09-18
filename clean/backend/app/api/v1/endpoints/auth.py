from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import timedelta
from typing import Any
from app.core.security import verify_password, create_access_token, get_password_hash
from app.core.config import settings
from app.models.user import User
from app.db.session import get_db
from app.schemas.auth import Token, UserCreate, UserResponse
from app.api.deps import get_current_active_user

router = APIRouter()

@router.post("/login", response_model=Token)
async def login(
    username: str,
    password: str,
    db: Session = Depends(get_db)
) -> Any:
    # Check user exists and password is correct
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, str(user.password_hash)):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Generate JWT token
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username, "role": user.role},
        expires_delta=access_token_expires
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "role": user.role,
        "user_id": str(user.id)
    }

@router.post("/register", response_model=UserResponse)
async def register(
    user_create: UserCreate,
    db: Session = Depends(get_db)
) -> Any:
    # Check if username exists
    if db.query(User).filter(User.username == user_create.username).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered"
        )
    
    # Check if email exists
    if db.query(User).filter(User.email == user_create.email).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    # Create new user
    user = User(
        username=user_create.username,
        password_hash=get_password_hash(user_create.password),
        role=user_create.role,
        full_name=user_create.full_name,
        email=user_create.email
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    
    return user

@router.get("/me", response_model=UserResponse)
async def read_users_me(
    current_user: User = Depends(get_current_active_user)
) -> Any:
    return current_user