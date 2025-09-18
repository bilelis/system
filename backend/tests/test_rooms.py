# Room Management Tests

import pytest
from fastapi.testclient import TestClient

def test_list_rooms(client: TestClient, auth_headers):
    """Test listing all rooms"""
    response = client.get("/api/v1/rooms/", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_create_room(client: TestClient, auth_headers):
    """Test creating a new room"""
    room_data = {
        "room_number": "TEST101",
        "room_type": "Standard",
        "floor": 1,
        "rate_per_night": 100.00,
        "capacity": 2,
        "features": {"wifi": True, "tv": True}
    }
    
    response = client.post("/api/v1/rooms/", json=room_data, headers=auth_headers)
    assert response.status_code == 201
    data = response.json()
    assert data["room_number"] == room_data["room_number"]
    assert data["room_type"] == room_data["room_type"]

def test_create_duplicate_room(client: TestClient, auth_headers):
    """Test creating room with duplicate number"""
    room_data = {
        "room_number": "DUP101",
        "room_type": "Standard",
        "floor": 1,
        "rate_per_night": 100.00,
        "capacity": 2
    }
    
    # Create first room
    client.post("/api/v1/rooms/", json=room_data, headers=auth_headers)
    
    # Try to create duplicate
    response = client.post("/api/v1/rooms/", json=room_data, headers=auth_headers)
    assert response.status_code == 400
    assert "Room number already exists" in response.json()["detail"]

def test_get_room(client: TestClient, auth_headers):
    """Test getting a specific room"""
    # First create a room
    room_data = {
        "room_number": "GET101",
        "room_type": "Standard",
        "floor": 1,
        "rate_per_night": 100.00,
        "capacity": 2
    }
    
    create_response = client.post("/api/v1/rooms/", json=room_data, headers=auth_headers)
    room_id = create_response.json()["id"]
    
    # Get the room
    response = client.get(f"/api/v1/rooms/{room_id}", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert data["room_number"] == room_data["room_number"]

def test_get_nonexistent_room(client: TestClient, auth_headers):
    """Test getting a room that doesn't exist"""
    fake_id = "00000000-0000-0000-0000-000000000000"
    response = client.get(f"/api/v1/rooms/{fake_id}", headers=auth_headers)
    assert response.status_code == 404

def test_update_room(client: TestClient, auth_headers):
    """Test updating a room"""
    # First create a room
    room_data = {
        "room_number": "UPD101",
        "room_type": "Standard",
        "floor": 1,
        "rate_per_night": 100.00,
        "capacity": 2
    }
    
    create_response = client.post("/api/v1/rooms/", json=room_data, headers=auth_headers)
    room_id = create_response.json()["id"]
    
    # Update the room
    update_data = {"rate_per_night": 150.00, "status": "maintenance"}
    response = client.patch(f"/api/v1/rooms/{room_id}", json=update_data, headers=auth_headers)
    
    assert response.status_code == 200
    data = response.json()
    assert data["rate_per_night"] == 150.00
    assert data["status"] == "maintenance"

def test_delete_room(client: TestClient, auth_headers):
    """Test deleting a room"""
    # First create a room
    room_data = {
        "room_number": "DEL101",
        "room_type": "Standard",
        "floor": 1,
        "rate_per_night": 100.00,
        "capacity": 2
    }
    
    create_response = client.post("/api/v1/rooms/", json=room_data, headers=auth_headers)
    room_id = create_response.json()["id"]
    
    # Delete the room
    response = client.delete(f"/api/v1/rooms/{room_id}", headers=auth_headers)
    assert response.status_code == 204
    
    # Verify it's deleted
    get_response = client.get(f"/api/v1/rooms/{room_id}", headers=auth_headers)
    assert get_response.status_code == 404

def test_filter_rooms_by_status(client: TestClient, auth_headers):
    """Test filtering rooms by status"""
    response = client.get("/api/v1/rooms/?status=available", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    for room in data:
        assert room["status"] == "available"

def test_filter_rooms_by_floor(client: TestClient, auth_headers):
    """Test filtering rooms by floor"""
    response = client.get("/api/v1/rooms/?floor=1", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    for room in data:
        assert room["floor"] == 1