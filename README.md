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
python backend/device_manager.py

# Use Docker Compose to simulate the device environment
docker-compose up --build
