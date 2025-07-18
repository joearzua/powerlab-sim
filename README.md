# PowerLab Sim 🧪

Simulated lab management tool for IBM Power Systems.

## Features

- Add/remove/configure virtual lab devices
- Simulate firmware and OS updates
- Track config changes in JSON
- Docker-based device simulation
- CI pipeline using GitHub Actions

## Getting Started

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/powerlab-sim

# Run the device manager
python backend/device_manager.py

# Simulate device via Docker
./devops/setup_lab.sh
