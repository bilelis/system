from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
import os

# Get database URL from settings
DATABASE_URL = settings.DATABASE_URL

# Create engine with error handling
try:
    engine = create_engine(DATABASE_URL)
except ImportError as e:
    if "psycopg2" in str(e):
        # Fallback to SQLite if PostgreSQL driver is not available
        print("Warning: PostgreSQL driver not available, falling back to SQLite")
        DATABASE_URL = "sqlite:///./hotel_management.db"
        engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
    else:
        raise e

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()