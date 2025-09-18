import requests
import json

# Base URL for the API
BASE_URL = "http://localhost:8000"

def test_endpoints():
    """Test all main endpoints"""
    print("Testing Hotel Management System API Endpoints")
    print("=" * 50)
    
    # Test root endpoint
    print("1. Testing root endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/")
        print(f"   Status: {response.status_code}")
        print(f"   Success: {response.status_code == 200}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Test health endpoint
    print("\n2. Testing health endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/health")
        print(f"   Status: {response.status_code}")
        print(f"   Success: {response.status_code == 200}")
        if response.status_code == 200:
            data = response.json()
            print(f"   Message: {data.get('message', 'N/A')}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Test API v1 root
    print("\n3. Testing API v1 root...")
    try:
        response = requests.get(f"{BASE_URL}/api/v1/")
        print(f"   Status: {response.status_code}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Test auth endpoints
    print("\n4. Testing auth endpoints...")
    try:
        response = requests.get(f"{BASE_URL}/api/v1/auth/")
        print(f"   Auth endpoint status: {response.status_code}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Test rooms endpoints
    print("\n5. Testing rooms endpoints...")
    try:
        response = requests.get(f"{BASE_URL}/api/v1/rooms/")
        print(f"   Rooms endpoint status: {response.status_code}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Test guests endpoints
    print("\n6. Testing guests endpoints...")
    try:
        response = requests.get(f"{BASE_URL}/api/v1/guests/")
        print(f"   Guests endpoint status: {response.status_code}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Test orders endpoints
    print("\n7. Testing orders endpoints...")
    try:
        response = requests.get(f"{BASE_URL}/api/v1/orders/")
        print(f"   Orders endpoint status: {response.status_code}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Test docs
    print("\n8. Testing documentation...")
    try:
        response = requests.get(f"{BASE_URL}/docs")
        print(f"   Docs status: {response.status_code}")
        print(f"   Docs accessible: {response.status_code == 200}")
    except Exception as e:
        print(f"   Error: {e}")
    
    print("\n" + "=" * 50)
    print("API testing completed!")

if __name__ == "__main__":
    test_endpoints()