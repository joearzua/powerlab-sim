import unittest
import json
from pathlib import Path
from backend import device_manager

TEST_FILE = Path(__file__).parent.parent / "lab_config.json"


class TestDeviceManager(unittest.TestCase):

    def setUp(self):
        # Clean slate before each test
        if TEST_FILE.exists():
            TEST_FILE.unlink()
        with open(TEST_FILE, 'w', encoding='utf-8') as f:
            json.dump([], f)

    def test_add_device(self):
        device_manager.add_device("TEST001", "CEC", "v1.0.0")
        devices = device_manager.load_devices()
        self.assertEqual(len(devices), 1)
        self.assertEqual(devices[0]["id"], "TEST001")

    def test_remove_device(self):
        device_manager.add_device("TEST001", "CEC", "v1.0.0")
        device_manager.remove_device("TEST001")
        devices = device_manager.load_devices()
        self.assertEqual(len(devices), 0)

    def test_update_firmware(self):
        device_manager.add_device("TEST001", "CEC", "v1.0.0")
        device_manager.update_firmware("TEST001", "v2.1.3")
        devices = device_manager.load_devices()
        self.assertEqual(devices[0]["firmware"], "v2.1.3")


if __name__ == "__main__":
    unittest.main()
