from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List
import json

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="allow"  # Allow extra environment variables
    )
    # Database settings
    DATABASE_URL: str = "postgresql://postgres:password@localhost:5432/hotel_management"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str = "hotel_management"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "password"
    
    # Supabase settings
    SUPABASE_URL: str = "your-supabase-url"
    SUPABASE_ANON_KEY: str = "your-supabase-anon-key"
    SUPABASE_SERVICE_ROLE_KEY: str = "your-supabase-service-role-key"
    
    # JWT settings
    JWT_SECRET_KEY: str = "your-super-secret-jwt-key-change-this-in-production"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440  # 24 hours
    
    # OpenAI settings
    OPENAI_API_KEY: str = "your-openai-api-key-here"
    
    # Google Gemini API settings
    GEMINI_API_KEY: str = "your-gemini-api-key-here"
    
    # TestSprite API settings
    TESTSPRITE_API_KEY: str = "your-testsprite-api-key-here"
    
    # CORS settings
    ALLOW_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:5173", "http://127.0.0.1:3000", "http://127.0.0.1:5173"]
    
    # Debug mode
    DEBUG: bool = True
    
    # Bilel Control Panel
    BILEL_ACCESS_CODE: str = "1234"
    
    # Environment
    ENVIRONMENT: str = "development"
    
    @classmethod
    def parse_env_var(cls, field_name: str, raw_val: str):
        if field_name == "ALLOW_ORIGINS":
            try:
                return json.loads(raw_val)
            except json.JSONDecodeError:
                return raw_val.split(',')
        return raw_val

settings = Settings()