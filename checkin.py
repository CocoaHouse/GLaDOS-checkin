import os
import requests

url = "https://glados.rocks/api/user/checkin"

headers = {
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json;charset=UTF-8",
    "Authorization": os.environ.get("GLADOS_AUTH"),
    "Cookie": os.environ.get("GLADOS_COOKIE"),
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/124.0.0.0 Safari/537.36"
}

data = {
    "token": "glados.one"
}

response = requests.post(url, headers=headers, json=data)

print("Status:", response.status_code)
print("Response:", response.text)
