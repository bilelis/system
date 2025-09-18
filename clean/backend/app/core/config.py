from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List
import json

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="allow"  # Allow extra environment variables
    )
    
    # Database settings
    DATABASE_URL: str = "sqlite:///./hotel_management.db"
    
    # JWT settings
    JWT_SECRET_KEY: str = "hotel-management-system-secret-key-2025"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440  # 24 hours
    
    # CORS settings
    ALLOW_ORIGINS: List[str] = ["http://localhost:5173", "http://localhost:8080"]
    
    # Debug mode
    DEBUG: bool = True
    
    # Environment
    ENVIRONMENT: str = "development"

settings = Settings()