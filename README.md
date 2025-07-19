# PowerLab Sim [![](https://github.com/joearzua/powerlab-sim/actions/workflows/python-tests.yml/badge.svg?branch=dev)](https://github.com/joearzua/powerlab-sim/actions/workflows/python-tests.yml)

Simulated lab management tool for IBM Power Systems.

## Features

- Add/remove/configure virtual lab devices
- Simulate firmware and OS updates
- Track config changes in JSON
- Docker-based device simulation (in progress)
- CI pipeline using GitHub Actions (in progress)

## Getting Started

```bash
# Run the device manager to add a device to lab_config.json
python backend/device_manager.py

# Simulate device via Docker
./devops/setup_lab.sh
