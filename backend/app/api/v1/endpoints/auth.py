from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from datetime import timedelta
from typing import Any, Optional
from app.core.security import verify_password, create_access_token, get_password_hash
from app.core.config import settings
from app.models.user import User
from app.db.session import get_db
from app.schemas.auth import Token, UserCreate, UserResponse
from app.api.deps import get_current_active_user
from app.services.supabase_auth import supabase_auth_service
from pydantic import BaseModel

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

# Simple login request model
class SimpleLoginRequest(BaseModel):
    username: str
    password: str

@router.post("/test-json")
async def test_json(request: SimpleLoginRequest) -> dict:
    """Test JSON parsing"""
    return {
        "received_username": request.username,
        "received_password": "***",
        "message": "JSON parsing works!"
    }

@router.post("/simple-login")
async def simple_login(
    request: SimpleLoginRequest,
    db: Session = Depends(get_db)
) -> Any:
    """Simple login for testing"""
    try:
        # Check user exists
        user = db.query(User).filter(User.username == request.username).first()
        if not user:
            return {"error": "User not found", "username": request.username}
        
        # Check password
        if not verify_password(request.password, str(user.password_hash)):
            return {"error": "Invalid password"}
        
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
            "user_id": str(user.id),
            "username": user.username
        }
    except Exception as e:
        return {"error": str(e), "type": str(type(e))}

@router.post("/login")
async def login(
    request: SimpleLoginRequest,
    db: Session = Depends(get_db)
) -> dict:
    # Check user exists and password is correct
    user = db.query(User).filter(User.username == request.username).first()
    if not user or not verify_password(request.password, str(user.password_hash)):
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

# === Supabase Auth Endpoints ===

class SupabaseSignUpRequest(BaseModel):
    email: str
    password: str
    full_name: str
    role: str = "receptionist"

class SupabaseSignInRequest(BaseModel):
    email: str
    password: str

@router.post("/supabase/signup", response_model=dict)
async def supabase_signup(
    request: SupabaseSignUpRequest
) -> Any:
    """
    Register user with Supabase Auth
    """
    try:
        user_metadata = {
            "full_name": request.full_name,
            "role": request.role
        }
        
        result = await supabase_auth_service.sign_up(
            email=request.email,
            password=request.password,
            user_metadata=user_metadata
        )
        
        return {
            "message": "User registered successfully",
            "user_id": result["user"].id if result.get("user") else None,
            "email": request.email,
            "requires_verification": True
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Registration failed: {str(e)}"
        )

@router.post("/supabase/signin", response_model=dict)
async def supabase_signin(
    request: SupabaseSignInRequest
) -> Any:
    """
    Sign in user with Supabase Auth
    """
    try:
        result = await supabase_auth_service.sign_in(
            email=request.email,
            password=request.password
        )
        
        return {
            "access_token": result["access_token"],
            "refresh_token": result["refresh_token"],
            "token_type": "bearer",
            "user": {
                "id": result["user"].id,
                "email": result["user"].email,
                "user_metadata": result["user"].user_metadata
            }
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Sign in failed: {str(e)}"
        )

@router.post("/supabase/refresh", response_model=dict)
async def supabase_refresh(
    refresh_token: str
) -> Any:
    """
    Refresh Supabase session
    """
    try:
        result = await supabase_auth_service.refresh_session(refresh_token)
        
        return {
            "access_token": result["access_token"],
            "refresh_token": result["refresh_token"],
            "token_type": "bearer"
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Token refresh failed: {str(e)}"
        )

@router.post("/supabase/signout", response_model=dict)
async def supabase_signout(
    access_token: str
) -> Any:
    """
    Sign out user from Supabase
    """
    try:
        success = await supabase_auth_service.sign_out(access_token)
        
        return {
            "message": "Signed out successfully" if success else "Sign out failed",
            "success": success
        }
        
    except Exception as e:
        return {
            "message": f"Sign out failed: {str(e)}",
            "success": False
        }