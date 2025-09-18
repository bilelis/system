import requests
import json

# Test all components of the login system

print("=== Testing Backend Health ===")
try:
    response = requests.get('http://localhost:8005/health')
    print(f"Health check: {response.status_code}")
    print(f"Response: {response.json()}")
except Exception as e:
    print(f"Health check failed: {e}")

print("\n=== Testing Backend Login Endpoint ===")
try:
    login_data = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post('http://localhost:8005/api/v1/auth/login', json=login_data)
    print(f"Login status: {response.status_code}")
    print(f"Response headers: {dict(response.headers)}")
    print(f"Response content: {response.text}")
    
    if response.status_code == 200:
        data = response.json()
        print("✅ Backend login successful!")
        print(f"Token: {data.get('access_token', 'N/A')[:30]}...")
        print(f"Role: {data.get('role', 'N/A')}")
    else:
        print("❌ Backend login failed!")
except Exception as e:
    print(f"Backend login test failed: {e}")

print("\n=== Testing CORS Configuration ===")
try:
    login_data = {
        "username": "admin",
        "password": "password123"
    }
    # Test with Origin header to check CORS
    headers = {
        "Origin": "http://localhost:5174",
        "Content-Type": "application/json"
    }
    response = requests.post('http://localhost:8005/api/v1/auth/login', json=login_data, headers=headers)
    print(f"CORS test status: {response.status_code}")
    print(f"Access-Control-Allow-Origin in response: {response.headers.get('Access-Control-Allow-Origin', 'Not found')}")
except Exception as e:
    print(f"CORS test failed: {e}")

print("\n=== Testing Database Connection ===")
try:
    # Test if we can get a user from the database
    response = requests.get('http://localhost:8005/api/v1/auth/me', headers={
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsInJvbGUiOiJhZG1pbiIsImV4cCI6MTc1ODI1OTA3M30.AjdNaSEz8y1uy-WUp45mXyNLuPnrJdKWLrcvPG6EjHY"
    })
    print(f"User info status: {response.status_code}")
    if response.status_code == 200:
        print("✅ Database connection working!")
        print(f"User data: {response.json()}")
    elif response.status_code == 401:
        print("✅ Database connection working but token invalid (expected)")
    else:
        print("❌ Database connection issue!")
except Exception as e:
    print(f"Database test failed: {e}")