# Backend Testing Suite Configuration

import pytest
import asyncio
from httpx import AsyncClient
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app
from app.db.session import get_db

# Test database configuration
TEST_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/hotel_test"
engine = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    db = None
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        if db:
            db.close()

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture
def test_user():
    return {
        "username": "testuser",
        "password": "testpass123",
        "role": "admin",
        "full_name": "Test User",
        "email": "test@hotel.com"
    }

@pytest.fixture
def auth_token(test_user):
    # Create user
    response = client.post("/api/v1/auth/register", json=test_user)
    
    # Login and get token
    response = client.post(
        "/api/v1/auth/login",
        data={"username": test_user["username"], "password": test_user["password"]}
    )
    return response.json()["access_token"]

@pytest.fixture
def auth_headers(auth_token):
    return {"Authorization": f"Bearer {auth_token}"}