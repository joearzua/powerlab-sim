import json
from pathlib import Path

DEVICE_FILE = Path(__file__).parent / "lab_config.json"

def load_devices():
    if DEVICE_FILE.exists():
        with open(DEVICE_FILE, 'r') as f:
            return json.load(f)
    return []

def save_devices(devices):
    with open(DEVICE_FILE, 'w') as f:
        json.dump(devices, f, indent=4)

def add_device(device_id, device_type, firmware):
    devices = load_devices()
    device = {
        "id": device_id,
        "type": device_type,
        "firmware": firmware,
        "status": "active"
    }
    devices.append(device)
    save_devices(devices)
    print(f"Added device: {device}")

if __name__ == "__main__":
    add_device("CEC001", "CEC", "v1.0.0")
