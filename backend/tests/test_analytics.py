# Analytics and Reporting Tests

import pytest
from fastapi.testclient import TestClient
from datetime import datetime, timedelta

class TestAnalytics:
    """Test analytics and reporting endpoints"""
    
    def test_revenue_today(self, client: TestClient, auth_headers):
        """Test today's revenue calculation"""
        response = client.get("/api/v1/analytics/revenue/today", headers=auth_headers)
        assert response.status_code == 200
        data = response.json()
        assert "total_revenue" in data
        assert "currency" in data
        assert isinstance(data["total_revenue"], (int, float))
    
    def test_revenue_by_date_range(self, client: TestClient, auth_headers):
        """Test revenue calculation for date range"""
        start_date = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
        end_date = datetime.now().strftime("%Y-%m-%d")
        
        response = client.get(
            f"/api/v1/analytics/revenue?start_date={start_date}&end_date={end_date}",
            headers=auth_headers
        )
        assert response.status_code == 200
        data = response.json()
        assert "total_revenue" in data
        assert "date_range" in data
        assert data["date_range"]["start"] == start_date
        assert data["date_range"]["end"] == end_date
    
    def test_occupancy_rate(self, client: TestClient, auth_headers):
        """Test hotel occupancy rate calculation"""
        response = client.get("/api/v1/analytics/occupancy", headers=auth_headers)
        assert response.status_code == 200
        data = response.json()
        assert "occupancy_rate" in data
        assert "total_rooms" in data
        assert "occupied_rooms" in data
        assert 0 <= data["occupancy_rate"] <= 100
    
    def test_top_selling_items(self, client: TestClient, auth_headers):
        """Test top selling items across all outlets"""
        response = client.get("/api/v1/analytics/top-items", headers=auth_headers)
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        
        for item in data:
            assert "item_name" in item
            assert "quantity_sold" in item
            assert "revenue" in item
            assert "outlet_name" in item
    
    def test_guest_spending_analysis(self, client: TestClient, auth_headers):
        """Test guest spending patterns"""
        response = client.get("/api/v1/analytics/guest-spending", headers=auth_headers)
        assert response.status_code == 200
        data = response.json()
        assert "average_spending" in data
        assert "total_guests" in data
        assert "spending_distribution" in data
    
    def test_revenue_split_by_outlet(self, client: TestClient, auth_headers):
        """Test revenue breakdown by outlet"""
        response = client.get("/api/v1/analytics/revenue-by-outlet", headers=auth_headers)
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        
        for outlet_revenue in data:
            assert "outlet_name" in outlet_revenue
            assert "revenue" in outlet_revenue
            assert "percentage" in outlet_revenue
            assert 0 <= outlet_revenue["percentage"] <= 100
    
    def test_average_revenue_per_room(self, client: TestClient, auth_headers):
        """Test ARPR (Average Revenue Per Room) calculation"""
        response = client.get("/api/v1/analytics/arpr", headers=auth_headers)
        assert response.status_code == 200
        data = response.json()
        assert "arpr" in data
        assert "period" in data
        assert isinstance(data["arpr"], (int, float))
    
    def test_monthly_revenue_trend(self, client: TestClient, auth_headers):
        """Test monthly revenue trend analysis"""
        response = client.get("/api/v1/analytics/revenue/monthly", headers=auth_headers)
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        
        for month_data in data:
            assert "month" in month_data
            assert "revenue" in month_data
            assert "year" in month_data
    
    def test_peak_hours_analysis(self, client: TestClient, auth_headers):
        """Test peak hours analysis for outlets"""
        response = client.get("/api/v1/analytics/peak-hours", headers=auth_headers)
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        
        for hour_data in data:
            assert "hour" in hour_data
            assert "order_count" in hour_data
            assert "revenue" in hour_data
            assert 0 <= hour_data["hour"] <= 23
    
    def test_guest_loyalty_metrics(self, client: TestClient, auth_headers):
        """Test guest loyalty and repeat visit metrics"""
        response = client.get("/api/v1/analytics/guest-loyalty", headers=auth_headers)
        assert response.status_code == 200
        data = response.json()
        assert "repeat_guests" in data
        assert "new_guests" in data
        assert "loyalty_rate" in data
        assert 0 <= data["loyalty_rate"] <= 100
    
    def test_room_type_performance(self, client: TestClient, auth_headers):
        """Test performance analysis by room type"""
        response = client.get("/api/v1/analytics/room-performance", headers=auth_headers)
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        
        for room_type_data in data:
            assert "room_type" in room_type_data
            assert "occupancy_rate" in room_type_data
            assert "average_rate" in room_type_data
            assert "revenue" in room_type_data
    
    def test_daily_summary_dashboard(self, client: TestClient, auth_headers):
        """Test comprehensive daily summary for dashboard"""
        response = client.get("/api/v1/analytics/dashboard/daily", headers=auth_headers)
        assert response.status_code == 200
        data = response.json()
        
        # Check all KPIs are present
        assert "revenue_today" in data
        assert "occupancy_rate" in data
        assert "new_guests" in data
        assert "orders_count" in data
        assert "average_order_value" in data
        assert "top_selling_item" in data
    
    def test_export_analytics_data(self, client: TestClient, auth_headers):
        """Test exporting analytics data"""
        # Test CSV export
        response = client.get("/api/v1/analytics/export/csv?report=revenue", headers=auth_headers)
        assert response.status_code == 200
        assert response.headers["content-type"] == "text/csv"
        
        # Test Excel export
        response = client.get("/api/v1/analytics/export/excel?report=occupancy", headers=auth_headers)
        assert response.status_code == 200
        assert "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" in response.headers["content-type"]
    
    def test_analytics_date_validation(self, client: TestClient, auth_headers):
        """Test date validation in analytics endpoints"""
        # Invalid date format
        response = client.get("/api/v1/analytics/revenue?start_date=invalid", headers=auth_headers)
        assert response.status_code == 400
        
        # Future date
        future_date = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")
        response = client.get(f"/api/v1/analytics/revenue?start_date={future_date}", headers=auth_headers)
        assert response.status_code == 400
    
    def test_analytics_permissions(self, client: TestClient):
        """Test that analytics endpoints require proper permissions"""
        # Create cashier user (limited access)
        cashier_user = {
            "username": "analytics_cashier",
            "password": "cashier123",
            "role": "cashier",
            "full_name": "Analytics Cashier",
            "email": "analytics.cashier@hotel.com"
        }
        
        client.post("/api/v1/auth/register", json=cashier_user)
        login_response = client.post(
            "/api/v1/auth/login",
            data={"username": cashier_user["username"], "password": cashier_user["password"]}
        )
        cashier_headers = {"Authorization": f"Bearer {login_response.json()['access_token']}"}
        
        # Cashier should not access analytics
        response = client.get("/api/v1/analytics/revenue/today", headers=cashier_headers)
        assert response.status_code == 403