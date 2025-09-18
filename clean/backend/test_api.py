import requests
import json

# Base URL for the API
BASE_URL = "http://localhost:8000"

def test_health_check():
    """Test the health check endpoint"""
    print("Testing health check endpoint...")
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
    print()

def test_root():
    """Test the root endpoint"""
    print("Testing root endpoint...")
    response = requests.get(f"{BASE_URL}/")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
    print()

def test_docs():
    """Test the docs endpoint"""
    print("Testing docs endpoint...")
    response = requests.get(f"{BASE_URL}/docs")
    print(f"Status Code: {response.status_code}")
    print(f"Docs available: {response.status_code == 200}")
    print()

if __name__ == "__main__":
    print("Testing Hotel Management System API")
    print("=" * 40)
    
    try:
        test_health_check()
        test_root()
        test_docs()
        print("All tests completed successfully!")
    except Exception as e:
        print(f"Error during testing: {e}")