#!/usr/bin/env python3
"""
Simple Authentication Test Script

This script demonstrates the complete authentication flow using the new simple endpoints.
"""

import requests
import json

def test_simple_authentication():
    """Test the simple authentication flow"""
    base_url = "http://localhost:8005/api/v1/simple-auth"
    
    print("=== Simple Authentication Test ===\n")
    
    # Test 1: Health check
    print("1. Testing backend health...")
    try:
        response = requests.get("http://localhost:8005/health")
        if response.status_code == 200:
            print("   ✅ Backend is running")
        else:
            print(f"   ❌ Backend health check failed: {response.status_code}")
            return
    except Exception as e:
        print(f"   ❌ Backend not accessible: {e}")
        return
    
    # Test 2: Simple login
    print("\n2. Testing simple login...")
    login_data = {
        "username": "admin",
        "password": "password123"
    }
    
    try:
        response = requests.post(f"{base_url}/simple-login", json=login_data)
        if response.status_code == 200:
            login_result = response.json()
            token = login_result["access_token"]
            user = login_result["user"]
            print("   ✅ Login successful!")
            print(f"   Token: {token[:30]}...")
            print(f"   User: {user['username']} ({user['role']})")
        else:
            print(f"   ❌ Login failed: {response.status_code}")
            print(f"   Response: {response.text}")
            return
    except Exception as e:
        print(f"   ❌ Login request failed: {e}")
        return
    
    # Test 3: Get user info
    print("\n3. Testing user info retrieval...")
    try:
        response = requests.get(f"{base_url}/simple-user?token={token}")
        if response.status_code == 200:
            user_info = response.json()
            print("   ✅ User info retrieved successfully!")
            print(f"   ID: {user_info['id']}")
            print(f"   Username: {user_info['username']}")
            print(f"   Email: {user_info['email']}")
            print(f"   Full Name: {user_info['full_name']}")
            print(f"   Role: {user_info['role']}")
        else:
            print(f"   ❌ Failed to get user info: {response.status_code}")
            print(f"   Response: {response.text}")
    except Exception as e:
        print(f"   ❌ User info request failed: {e}")
    
    # Test 4: Invalid credentials
    print("\n4. Testing invalid credentials...")
    invalid_login_data = {
        "username": "admin",
        "password": "wrongpassword"
    }
    
    try:
        response = requests.post(f"{base_url}/simple-login", json=invalid_login_data)
        if response.status_code == 401:
            print("   ✅ Correctly rejected invalid credentials")
        else:
            print(f"   ❌ Unexpected response for invalid credentials: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Request failed: {e}")
    
    print("\n=== Test Complete ===")

if __name__ == "__main__":
    test_simple_authentication()