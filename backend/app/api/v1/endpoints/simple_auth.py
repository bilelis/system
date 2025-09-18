from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import timedelta
from typing import Any
from app.core.security import verify_password, create_access_token
from app.core.config import settings
from app.models.user import User
from app.db.session import get_db
from pydantic import BaseModel

router = APIRouter()

# Simple login request model
class SimpleLoginRequest(BaseModel):
    username: str
    password: str

class SimpleUserResponse(BaseModel):
    id: str
    username: str
    email: str
    full_name: str
    role: str

class SimpleTokenResponse(BaseModel):
    access_token: str
    token_type: str
    user: SimpleUserResponse

@router.post("/simple-login", response_model=SimpleTokenResponse)
async def simple_login(
    request: SimpleLoginRequest,
    db: Session = Depends(get_db)
) -> Any:
    """Simple login endpoint that bypasses complex dependencies"""
    try:
        # Check user exists
        user = db.query(User).filter(User.username == request.username).first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password"
            )
        
        # Check password
        if not verify_password(request.password, str(user.password_hash)):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password"
            )
        
        # Convert user to simple response model
        user_response = SimpleUserResponse(
            id=str(user.id),
            username=str(user.username),
            email=str(user.email),
            full_name=str(user.full_name),
            role=str(user.role)
        )
        
        # Generate JWT token
        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.username, "role": user.role},
            expires_delta=access_token_expires
        )
        
        return SimpleTokenResponse(
            access_token=access_token,
            token_type="bearer",
            user=user_response
        )
    except HTTPException:
        # Re-raise HTTP exceptions
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Login failed: {str(e)}"
        )

@router.get("/simple-user")
async def get_simple_user(
    token: str,
    db: Session = Depends(get_db)
) -> Any:
    """Simple user info endpoint"""
    try:
        from app.core.security import decode_access_token
        
        payload = decode_access_token(token)
        if payload is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token"
            )
        
        username = payload.get("sub")
        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token"
            )
        
        user = db.query(User).filter(User.username == username).first()
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User not found"
            )
        
        return SimpleUserResponse(
            id=str(user.id),
            username=str(user.username),
            email=str(user.email),
            full_name=str(user.full_name),
            role=str(user.role)
        )
    except HTTPException:
        # Re-raise HTTP exceptions
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get user info: {str(e)}"
        )