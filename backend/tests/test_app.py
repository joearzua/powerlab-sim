
import unittest
import json
from pathlib import Path
from backend.app import app, device_manager


TEST_FILE = Path(__file__).parent.parent / "lab_config.json"


class TestAppRoutes(unittest.TestCase):
    def setUp(self):
        # Set up a test client
        self.client = app.test_client()
        # Clean the config file
        if TEST_FILE.exists():
            TEST_FILE.unlink()
        with open(TEST_FILE, 'w') as f:
            json.dump([], f)

    def test_add_device_route(self):
        payload = {
            "id": "FLASK001",
            "type": "CEC",
            "firmware": "v0.1"
        }
        response = self.client.post('/add', json=payload)
        self.assertEqual(response.status_code, 200)

        # Check it was added
        devices = device_manager.load_devices()
        self.assertEqual(len(devices), 1)
        self.assertEqual(devices[0]["id"], "FLASK001")

    def test_remove_device_route(self):
        # Add first
        device_manager.add_device("TODELETE", "CEC", "v0.1")

        # Now remove via API
        response = self.client.post('/remove', json={"id": "TODELETE"})
        self.assertEqual(response.status_code, 200)

        # Check it's gone
        devices = device_manager.load_devices()
        self.assertEqual(len(devices), 0)

    def test_update_firmware_route(self):
        device_manager.add_device("FWTEST", "CEC", "v0.1")

        response = self.client.post('/update_firmware', json={
            "id": "FWTEST",
            "firmware": "v2.0"
        })
        self.assertEqual(response.status_code, 200)

        devices = device_manager.load_devices()
        self.assertEqual(devices[0]["firmware"], "v2.0")

    def test_get_devices_route(self):
        device_manager.add_device("GETTEST", "CEC", "v1.0")
        response = self.client.get('/devices')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIsInstance(data, list)
        self.assertEqual(data[0]["id"], "GETTEST")


if __name__ == '__main__':
    unittest.main()
