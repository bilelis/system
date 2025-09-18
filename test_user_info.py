import requests
import json

# Test the user info endpoint with proper error handling

print("=== Testing User Info Endpoint ===")
try:
    # First, let's get a fresh token
    login_data = {
        "username": "admin",
        "password": "password123"
    }
    login_response = requests.post('http://localhost:8005/api/v1/auth/login', json=login_data)
    
    if login_response.status_code == 200:
        token_data = login_response.json()
        access_token = token_data.get('access_token')
        print(f"Got token: {access_token[:30]}...")
        
        # Now test the user info endpoint
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        response = requests.get('http://localhost:8005/api/v1/auth/me', headers=headers)
        print(f"User info status: {response.status_code}")
        print(f"Response headers: {dict(response.headers)}")
        print(f"Response content: {response.text}")
        
        if response.status_code == 200:
            print("✅ User info retrieved successfully!")
            print(f"User data: {response.json()}")
        else:
            print("❌ Failed to get user info!")
    else:
        print(f"Failed to login: {login_response.status_code}")
        print(f"Response: {login_response.text}")
        
except Exception as e:
    print(f"User info test failed: {e}")
    import traceback
    traceback.print_exc()