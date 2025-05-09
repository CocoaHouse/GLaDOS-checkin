import os
import requests

def checkin(user_label, auth, cookie):
    url = "https://glados.rocks/api/user/checkin"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": auth,
        "Cookie": cookie,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/124.0.0.0 Safari/537.36"
    }
    data = {
        "token": "glados.one"
    }

    response = requests.post(url, headers=headers, json=data)
    print(f"=== {user_label} ===")
    print("Status:", response.status_code)
    try:
        print("Response:", response.json())
    except:
        print("Raw Response:", response.text)
    print("")


checkin("User1 (Me)", os.environ.get("GLADOS_AUTH"), os.environ.get("GLADOS_COOKIE"))

checkin("User2 (Friend)", os.environ.get("GLADOS_AUTH_USER2"), os.environ.get("GLADOS_COOKIE_USER2"))
