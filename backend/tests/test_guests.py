# Guest Management Tests

import pytest
from fastapi.testclient import TestClient

def test_create_guest(client: TestClient, auth_headers):
    """Test creating a new guest"""
    guest_data = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@email.com",
        "phone": "+1234567890",
        "nationality": "US",
        "passport_no": "US123456789"
    }
    
    response = client.post("/api/v1/guests/", json=guest_data, headers=auth_headers)
    assert response.status_code == 201
    data = response.json()
    assert data["first_name"] == guest_data["first_name"]
    assert data["last_name"] == guest_data["last_name"]
    assert data["email"] == guest_data["email"]

def test_list_guests(client: TestClient, auth_headers):
    """Test listing all guests"""
    response = client.get("/api/v1/guests/", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_get_guest(client: TestClient, auth_headers):
    """Test getting a specific guest"""
    # First create a guest
    guest_data = {
        "first_name": "Jane",
        "last_name": "Smith",
        "email": "jane.smith@email.com",
        "phone": "+1987654321"
    }
    
    create_response = client.post("/api/v1/guests/", json=guest_data, headers=auth_headers)
    guest_id = create_response.json()["id"]
    
    # Get the guest
    response = client.get(f"/api/v1/guests/{guest_id}", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert data["first_name"] == guest_data["first_name"]

def test_update_guest(client: TestClient, auth_headers):
    """Test updating guest information"""
    # First create a guest
    guest_data = {
        "first_name": "Bob",
        "last_name": "Wilson",
        "email": "bob.wilson@email.com"
    }
    
    create_response = client.post("/api/v1/guests/", json=guest_data, headers=auth_headers)
    guest_id = create_response.json()["id"]
    
    # Update the guest
    update_data = {"phone": "+1555123456", "nationality": "CA"}
    response = client.patch(f"/api/v1/guests/{guest_id}", json=update_data, headers=auth_headers)
    
    assert response.status_code == 200
    data = response.json()
    assert data["phone"] == "+1555123456"
    assert data["nationality"] == "CA"

def test_delete_guest(client: TestClient, auth_headers):
    """Test deleting a guest"""
    # First create a guest
    guest_data = {
        "first_name": "Charlie",
        "last_name": "Brown",
        "email": "charlie.brown@email.com"
    }
    
    create_response = client.post("/api/v1/guests/", json=guest_data, headers=auth_headers)
    guest_id = create_response.json()["id"]
    
    # Delete the guest
    response = client.delete(f"/api/v1/guests/{guest_id}", headers=auth_headers)
    assert response.status_code == 204
    
    # Verify it's deleted
    get_response = client.get(f"/api/v1/guests/{guest_id}", headers=auth_headers)
    assert get_response.status_code == 404

def test_search_guests_by_name(client: TestClient, auth_headers):
    """Test searching guests by name"""
    # Create test guests
    guests = [
        {"first_name": "Alice", "last_name": "Johnson", "email": "alice@email.com"},
        {"first_name": "Alice", "last_name": "Williams", "email": "alice.w@email.com"},
        {"first_name": "Bob", "last_name": "Johnson", "email": "bob.j@email.com"}
    ]
    
    for guest in guests:
        client.post("/api/v1/guests/", json=guest, headers=auth_headers)
    
    # Search by first name
    response = client.get("/api/v1/guests/?search=Alice", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    
    # Search by last name
    response = client.get("/api/v1/guests/?search=Johnson", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2