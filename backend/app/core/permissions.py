from functools import wraps
from typing import List
from fastapi import HTTPException, status
from app.models.user import User, UserRole

def check_permissions(allowed_roles: List[UserRole]):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, current_user: User, **kwargs):
            if current_user.role not in allowed_roles:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Operation not permitted"
                )
            return await func(*args, current_user=current_user, **kwargs)
        return wrapper
    return decorator