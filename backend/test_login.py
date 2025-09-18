import requests
import json

# Test login endpoint
url = "http://localhost:8005/api/v1/auth/login"
credentials = {
    "username": "admin",
    "password": "password123"
}

print("Testing login endpoint...")
print(f"URL: {url}")
print(f"Credentials: {credentials}")

try:
    response = requests.post(url, json=credentials)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
    
    if response.status_code == 200:
        data = response.json()
        print("✅ Login successful!")
        print(f"Access Token: {data.get('access_token', 'N/A')[:50]}...")
        print(f"Role: {data.get('role', 'N/A')}")
        print(f"User ID: {data.get('user_id', 'N/A')}")
    else:
        print("❌ Login failed!")
        
except Exception as e:
    print(f"❌ Error: {e}")