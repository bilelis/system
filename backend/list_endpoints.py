import requests

# Get OpenAPI schema
try:
    response = requests.get("http://localhost:8000/openapi.json")
    if response.status_code == 200:
        data = response.json()
        print("Available endpoints:")
        for path, methods in data.get("paths", {}).items():
            for method in methods.keys():
                print(f"  {method.upper()} {path}")
    else:
        print(f"Failed to get schema: {response.status_code}")
except Exception as e:
    print(f"Error: {e}")