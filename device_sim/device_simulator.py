import os
import time
import requests

DEVICE_ID = os.getenv("DEVICE_ID", "SIM001")
DEVICE_TYPE = os.getenv("DEVICE_TYPE", "CEC")
FIRMWARE = os.getenv("FIRMWARE", "v1.0.0")
BACKEND_URL = os.getenv("BACKEND_URL", "http://backend:5000")

def register_device():
    payload = {
        "id": DEVICE_ID,
        "type": DEVICE_TYPE,
        "firmware": FIRMWARE
    }
    try:
        r = requests.post(f"{BACKEND_URL}/add", json=payload)
        print(f"[{DEVICE_ID}] Registered: {r.status_code} {r.text}")
    except Exception as e:
        print(f"[{DEVICE_ID}] Error: {e}")

if __name__ == "__main__":
    while True:
        register_device()
        time.sleep(10)
