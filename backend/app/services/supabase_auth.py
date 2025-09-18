"""
Supabase Authentication Service
خدمة المصادقة باستخدام Supabase Auth
"""

from typing import Optional, Dict, Any
from fastapi import HTTPException, status
from app.services.supabase_client import supabase_service
from app.core.config import settings
import logging

logger = logging.getLogger(__name__)

class SupabaseAuthService:
    """
    Service for managing authentication with Supabase Auth
    """
    
    def __init__(self):
        self.supabase = supabase_service.get_client()
        self.is_available = supabase_service.is_available()
        if not self.is_available:
            logger.warning("Supabase Auth service initialized but Supabase client is not available")
    
    async def sign_up(self, email: str, password: str, user_metadata: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Register a new user with Supabase Auth
        """
        if not self.is_available:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Supabase authentication service is not available"
            )
            
        try:
            response = self.supabase.auth.sign_up({
                "email": email,
                "password": password,
                "options": {
                    "data": user_metadata or {}
                }
            })
            
            if response.user:
                return {
                    "user": response.user,
                    "session": response.session,
                    "message": "User registered successfully"
                }
            else:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Failed to register user"
                )
                
        except Exception as e:
            logger.error(f"Sign up error: {e}")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e)
            )
    
    async def sign_in(self, email: str, password: str) -> Dict[str, Any]:
        """
        Sign in user with Supabase Auth
        """
        try:
            response = self.supabase.auth.sign_in_with_password({
                "email": email,
                "password": password
            })
            
            if response.user and response.session:
                return {
                    "user": response.user,
                    "session": response.session,
                    "access_token": response.session.access_token,
                    "refresh_token": response.session.refresh_token
                }
            else:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid credentials"
                )
                
        except Exception as e:
            logger.error(f"Sign in error: {e}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials"
            )
    
    async def get_user(self, access_token: str) -> Optional[Dict[str, Any]]:
        """
        Get user information from access token
        """
        try:
            # Set the session
            self.supabase.auth.set_session(access_token, "")
            user = self.supabase.auth.get_user()
            
            if user:
                return user.user
            return None
            
        except Exception as e:
            logger.error(f"Get user error: {e}")
            return None
    
    async def refresh_session(self, refresh_token: str) -> Dict[str, Any]:
        """
        Refresh user session
        """
        try:
            response = self.supabase.auth.refresh_session(refresh_token)
            
            if response.session:
                return {
                    "session": response.session,
                    "access_token": response.session.access_token,
                    "refresh_token": response.session.refresh_token
                }
            else:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Failed to refresh session"
                )
                
        except Exception as e:
            logger.error(f"Refresh session error: {e}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Failed to refresh session"
            )
    
    async def sign_out(self, access_token: str) -> bool:
        """
        Sign out user
        """
        try:
            self.supabase.auth.set_session(access_token, "")
            self.supabase.auth.sign_out()
            return True
            
        except Exception as e:
            logger.error(f"Sign out error: {e}")
            return False

# Global instance
supabase_auth_service = SupabaseAuthService()