# POS System Tests

import pytest
from fastapi.testclient import TestClient

class TestPOSSystem:
    """Test Point of Sale system functionality"""
    
    def test_get_outlets(self, client: TestClient, auth_headers):
        """Test getting all outlets"""
        response = client.get("/api/v1/pos/outlets", headers=auth_headers)
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        
        # Check if seeded outlets exist
        outlet_names = [outlet["name"] for outlet in data]
        assert "Bar" in outlet_names
        assert "Restaurant1" in outlet_names
        assert "Restaurant2" in outlet_names
    
    def test_get_outlet_items(self, client: TestClient, auth_headers):
        """Test getting items for a specific outlet"""
        # First get outlets
        outlets_response = client.get("/api/v1/pos/outlets", headers=auth_headers)
        outlets = outlets_response.json()
        
        if outlets:
            outlet_id = outlets[0]["id"]
            response = client.get(f"/api/v1/pos/outlets/{outlet_id}/items", headers=auth_headers)
            assert response.status_code == 200
            data = response.json()
            assert isinstance(data, list)
    
    def test_create_order(self, client: TestClient, auth_headers):
        """Test creating a new POS order"""
        # Get outlets and items first
        outlets_response = client.get("/api/v1/pos/outlets", headers=auth_headers)
        outlets = outlets_response.json()
        
        if outlets:
            outlet_id = outlets[0]["id"]
            items_response = client.get(f"/api/v1/pos/outlets/{outlet_id}/items", headers=auth_headers)
            items = items_response.json()
            
            if items:
                order_data = {
                    "outlet_id": outlet_id,
                    "guest_id": None,  # Walk-in customer
                    "items": [
                        {
                            "item_id": items[0]["id"],
                            "quantity": 2,
                            "unit_price": items[0]["price"]
                        }
                    ],
                    "discount": 0,
                    "tax": 0.1
                }
                
                response = client.post("/api/v1/orders/", json=order_data, headers=auth_headers)
                assert response.status_code == 201
                data = response.json()
                assert data["outlet_id"] == outlet_id
                assert len(data["items"]) == 1
                assert data["status"] == "pending"
    
    def test_update_order_status(self, client: TestClient, auth_headers):
        """Test updating order status (preparing, completed, etc.)"""
        # First create an order
        outlets_response = client.get("/api/v1/pos/outlets", headers=auth_headers)
        outlets = outlets_response.json()
        
        if outlets:
            outlet_id = outlets[0]["id"]
            items_response = client.get(f"/api/v1/pos/outlets/{outlet_id}/items", headers=auth_headers)
            items = items_response.json()
            
            if items:
                order_data = {
                    "outlet_id": outlet_id,
                    "items": [{"item_id": items[0]["id"], "quantity": 1, "unit_price": items[0]["price"]}]
                }
                
                create_response = client.post("/api/v1/orders/", json=order_data, headers=auth_headers)
                order_id = create_response.json()["id"]
                
                # Update order status
                response = client.patch(f"/api/v1/orders/{order_id}", json={"status": "preparing"}, headers=auth_headers)
                assert response.status_code == 200
                assert response.json()["status"] == "preparing"
                
                # Complete the order
                response = client.patch(f"/api/v1/orders/{order_id}", json={"status": "completed"}, headers=auth_headers)
                assert response.status_code == 200
                assert response.json()["status"] == "completed"
    
    def test_link_order_to_guest(self, client: TestClient, auth_headers):
        """Test linking an order to a guest"""
        # First create a guest
        guest_data = {
            "first_name": "POS",
            "last_name": "Customer",
            "email": "pos.customer@hotel.com"
        }
        guest_response = client.post("/api/v1/guests/", json=guest_data, headers=auth_headers)
        guest_id = guest_response.json()["id"]
        
        # Create order with guest
        outlets_response = client.get("/api/v1/pos/outlets", headers=auth_headers)
        outlets = outlets_response.json()
        
        if outlets:
            outlet_id = outlets[0]["id"]
            items_response = client.get(f"/api/v1/pos/outlets/{outlet_id}/items", headers=auth_headers)
            items = items_response.json()
            
            if items:
                order_data = {
                    "outlet_id": outlet_id,
                    "guest_id": guest_id,
                    "items": [{"item_id": items[0]["id"], "quantity": 1, "unit_price": items[0]["price"]}]
                }
                
                response = client.post("/api/v1/orders/", json=order_data, headers=auth_headers)
                assert response.status_code == 201
                data = response.json()
                assert data["guest_id"] == guest_id
    
    def test_calculate_order_total(self, client: TestClient, auth_headers):
        """Test order total calculation with tax and discount"""
        outlets_response = client.get("/api/v1/pos/outlets", headers=auth_headers)
        outlets = outlets_response.json()
        
        if outlets:
            outlet_id = outlets[0]["id"]
            items_response = client.get(f"/api/v1/pos/outlets/{outlet_id}/items", headers=auth_headers)
            items = items_response.json()
            
            if items:
                item_price = items[0]["price"]
                quantity = 2
                discount = 5.0  # $5 discount
                tax_rate = 0.1  # 10% tax
                
                order_data = {
                    "outlet_id": outlet_id,
                    "items": [{"item_id": items[0]["id"], "quantity": quantity, "unit_price": item_price}],
                    "discount": discount,
                    "tax": tax_rate
                }
                
                response = client.post("/api/v1/orders/", json=order_data, headers=auth_headers)
                assert response.status_code == 201
                data = response.json()
                
                # Calculate expected total
                subtotal = item_price * quantity
                total_after_discount = subtotal - discount
                expected_total = total_after_discount * (1 + tax_rate)
                
                assert abs(data["total"] - expected_total) < 0.01  # Allow for rounding differences
    
    def test_cancel_order(self, client: TestClient, auth_headers):
        """Test cancelling an order"""
        # Create an order first
        outlets_response = client.get("/api/v1/pos/outlets", headers=auth_headers)
        outlets = outlets_response.json()
        
        if outlets:
            outlet_id = outlets[0]["id"]
            items_response = client.get(f"/api/v1/pos/outlets/{outlet_id}/items", headers=auth_headers)
            items = items_response.json()
            
            if items:
                order_data = {
                    "outlet_id": outlet_id,
                    "items": [{"item_id": items[0]["id"], "quantity": 1, "unit_price": items[0]["price"]}]
                }
                
                create_response = client.post("/api/v1/orders/", json=order_data, headers=auth_headers)
                order_id = create_response.json()["id"]
                
                # Cancel the order
                response = client.patch(f"/api/v1/orders/{order_id}", json={"status": "cancelled"}, headers=auth_headers)
                assert response.status_code == 200
                assert response.json()["status"] == "cancelled"
    
    def test_get_orders_by_outlet(self, client: TestClient, auth_headers):
        """Test filtering orders by outlet"""
        response = client.get("/api/v1/orders/", headers=auth_headers)
        assert response.status_code == 200
        
        outlets_response = client.get("/api/v1/pos/outlets", headers=auth_headers)
        outlets = outlets_response.json()
        
        if outlets:
            outlet_id = outlets[0]["id"]
            response = client.get(f"/api/v1/orders/?outlet_id={outlet_id}", headers=auth_headers)
            assert response.status_code == 200
            data = response.json()
            for order in data:
                assert order["outlet_id"] == outlet_id
    
    def test_get_orders_by_status(self, client: TestClient, auth_headers):
        """Test filtering orders by status"""
        response = client.get("/api/v1/orders/?status=pending", headers=auth_headers)
        assert response.status_code == 200
        data = response.json()
        for order in data:
            assert order["status"] == "pending"