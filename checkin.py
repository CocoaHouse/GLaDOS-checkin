import os
import requests

BASE_URL = "https://glados.cloud"

def checkin(user_label, auth, cookie):
    url = f"{BASE_URL}/api/user/checkin"

    headers = {
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json;charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/124.0.0.0 Safari/537.36",

        # Critical for new rules (origin / referer check)
        "Origin": BASE_URL,
        "Referer": f"{BASE_URL}/console/checkin",
    }

    # Only attach when present to avoid malformed headers.
    if auth:
        headers["Authorization"] = auth
    if cookie:
        headers["Cookie"] = cookie

    data = {"token": "glados.cloud"}

    s = requests.Session()
    resp = s.post(url, headers=headers, json=data, timeout=30)

    print(f"=== {user_label} ===")
    print("Status:", resp.status_code)
    ct = resp.headers.get("Content-Type", "")
    print("Content-Type:", ct)
    try:
        print("Response:", resp.json())
    except Exception:
        print("Raw Response:", resp.text[:2000])
    print("")

if __name__ == "__main__":
    checkin(
        "User (Me)",
        os.environ.get("GLADOS_AUTH"),
        os.environ.get("GLADOS_COOKIE"),
    )
