import requests

BASE_URL = "http://127.0.0.1:8000"

# List متاع endpoints باش نجربوهم
endpoints = [
    "/users/me",      # مثال، غيّر حسب المشروع متاعك
    "/rooms",
    "/guests",
    "/orders",
    "/analytics"
]

for ep in endpoints:
    url = BASE_URL + ep
    try:
        response = requests.get(url)
        print(f"Endpoint {ep} => Status: {response.status_code}")
        print(f"Response: {response.json()}\n")
    except Exception as e:
        print(f"Endpoint {ep} => ERROR: {e}\n")
