# PowerLab Sim [![](https://github.com/joearzua/powerlab-sim/actions/workflows/python-tests.yml/badge.svg?branch=dev)](https://github.com/joearzua/powerlab-sim/actions/workflows/python-tests.yml)

Simulated lab management tool for IBM Power Systems.

## Features

- Add/remove/configure virtual lab devices
- Simulate firmware and OS updates
- Track config changes in JSON
- Simulate virtual lab devices via Docker and Flask API
- Continuous Integration: Automated tests run on every push using GitHub Actions

## Getting Started

```bash
# Add a device to lab_config.json using the device manager script
~/powerlab-sim-main> python backend/device_manager.py
Added device: {'id': 'CEC001', 'type': 'CEC', 'firmware': 'v1.0.0', 'status': 'active'}

# Use Docker Compose to simulate the device environment
~/powerlab-sim-main> docker-compose up --build
[+] Running 4/4
  backend                     Built                 0.0s
  device_sim                  Built                 0.0s
  Container powerlab_backend  Recreated             0.2s
  Container device_simulator  Recreated             0.1s
Attaching to device_simulator, powerlab_backend
powerlab_backend  |  * Serving Flask app 'app.py'
