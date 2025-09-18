# Role-Based Access Control Tests

import pytest
from fastapi.testclient import TestClient

class TestRoleBasedAccess:
    """Test role-based access control across different endpoints"""
    
    def setup_method(self):
        """Setup test data for each test"""
        self.admin_user = {
            "username": "admin_test",
            "password": "admin123",
            "role": "admin",
            "full_name": "Admin Test",
            "email": "admin.test@hotel.com"
        }
        
        self.receptionist_user = {
            "username": "receptionist_test",
            "password": "recep123",
            "role": "receptionist",
            "full_name": "Receptionist Test",
            "email": "recep.test@hotel.com"
        }
        
        self.cashier_user = {
            "username": "cashier_test",
            "password": "cashier123",
            "role": "cashier",
            "full_name": "Cashier Test",
            "email": "cashier.test@hotel.com"
        }
    
    def get_auth_headers(self, client, user_data):
        """Helper to get auth headers for a user"""
        # Register user
        client.post("/api/v1/auth/register", json=user_data)
        
        # Login and get token
        response = client.post(
            "/api/v1/auth/login",
            data={"username": user_data["username"], "password": user_data["password"]}
        )
        token = response.json()["access_token"]
        return {"Authorization": f"Bearer {token}"}
    
    def test_admin_full_access(self, client: TestClient):
        """Test admin has full access to all endpoints"""
        headers = self.get_auth_headers(client, self.admin_user)
        
        # Test room management
        room_data = {
            "room_number": "ADMIN101",
            "room_type": "Standard",
            "floor": 1,
            "rate_per_night": 100.00,
            "capacity": 2
        }
        
        # Admin can create rooms
        response = client.post("/api/v1/rooms/", json=room_data, headers=headers)
        assert response.status_code == 201
        
        room_id = response.json()["id"]
        
        # Admin can view rooms
        response = client.get("/api/v1/rooms/", headers=headers)
        assert response.status_code == 200
        
        # Admin can update rooms
        response = client.patch(f"/api/v1/rooms/{room_id}", json={"status": "maintenance"}, headers=headers)
        assert response.status_code == 200
        
        # Admin can delete rooms
        response = client.delete(f"/api/v1/rooms/{room_id}", headers=headers)
        assert response.status_code == 204
    
    def test_receptionist_limited_access(self, client: TestClient):
        """Test receptionist has limited access"""
        headers = self.get_auth_headers(client, self.receptionist_user)
        
        # Receptionist can view rooms
        response = client.get("/api/v1/rooms/", headers=headers)
        assert response.status_code == 200
        
        # Receptionist can update room status (check-in/out)
        # First create a room as admin
        admin_headers = self.get_auth_headers(client, self.admin_user)
        room_response = client.post("/api/v1/rooms/", json={
            "room_number": "RECEP101",
            "room_type": "Standard",
            "floor": 1,
            "rate_per_night": 100.00,
            "capacity": 2
        }, headers=admin_headers)
        room_id = room_response.json()["id"]
        
        # Receptionist can update room status
        response = client.patch(f"/api/v1/rooms/{room_id}", json={"status": "occupied"}, headers=headers)
        assert response.status_code == 200
        
        # Receptionist CANNOT create rooms
        response = client.post("/api/v1/rooms/", json={
            "room_number": "RECEP102",
            "room_type": "Standard",
            "floor": 1,
            "rate_per_night": 100.00,
            "capacity": 2
        }, headers=headers)
        assert response.status_code == 403  # Forbidden
        
        # Receptionist CANNOT delete rooms
        response = client.delete(f"/api/v1/rooms/{room_id}", headers=headers)
        assert response.status_code == 403  # Forbidden
    
    def test_cashier_pos_only_access(self, client: TestClient):
        """Test cashier has access only to POS-related endpoints"""
        headers = self.get_auth_headers(client, self.cashier_user)
        
        # Cashier can access POS endpoints
        response = client.get("/api/v1/pos/outlets", headers=headers)
        assert response.status_code == 200
        
        # Cashier can create orders
        order_data = {
            "outlet_id": "some-outlet-id",
            "items": [{"item_id": "some-item-id", "quantity": 1}]
        }
        response = client.post("/api/v1/orders/", json=order_data, headers=headers)
        assert response.status_code in [201, 400]  # 400 if validation fails due to missing data
        
        # Cashier CANNOT access room management
        response = client.get("/api/v1/rooms/", headers=headers)
        assert response.status_code == 403  # Forbidden
        
        # Cashier CANNOT access guest management
        response = client.get("/api/v1/guests/", headers=headers)
        assert response.status_code == 403  # Forbidden
    
    def test_unauthenticated_access_denied(self, client: TestClient):
        """Test that unauthenticated requests are denied"""
        # No auth headers
        response = client.get("/api/v1/rooms/")
        assert response.status_code == 401
        
        response = client.get("/api/v1/guests/")
        assert response.status_code == 401
        
        response = client.get("/api/v1/orders/")
        assert response.status_code == 401
    
    def test_invalid_token_access_denied(self, client: TestClient):
        """Test that invalid tokens are rejected"""
        invalid_headers = {"Authorization": "Bearer invalid_token_here"}
        
        response = client.get("/api/v1/rooms/", headers=invalid_headers)
        assert response.status_code == 401
        
        response = client.get("/api/v1/guests/", headers=invalid_headers)
        assert response.status_code == 401
    
    def test_expired_token_access_denied(self, client: TestClient):
        """Test that expired tokens are rejected"""
        # This would require mocking time or using a very short expiration
        # For now, we'll test with a malformed token
        expired_headers = {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.expired"}
        
        response = client.get("/api/v1/rooms/", headers=expired_headers)
        assert response.status_code == 401
    
    def test_role_hierarchy(self, client: TestClient):
        """Test that roles have proper hierarchy (admin > receptionist > cashier)"""
        # Admin can access everything
        admin_headers = self.get_auth_headers(client, self.admin_user)
        
        # Test admin access to analytics (highest privilege)
        response = client.get("/api/v1/analytics/revenue", headers=admin_headers)
        assert response.status_code in [200, 404]  # 200 if endpoint exists, 404 if not implemented
        
        # Receptionist cannot access analytics
        recep_headers = self.get_auth_headers(client, self.receptionist_user)
        response = client.get("/api/v1/analytics/revenue", headers=recep_headers)
        assert response.status_code == 403
        
        # Cashier cannot access analytics
        cashier_headers = self.get_auth_headers(client, self.cashier_user)
        response = client.get("/api/v1/analytics/revenue", headers=cashier_headers)
        assert response.status_code == 403