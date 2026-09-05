# dev-toolkit-35

`dev-toolkit-35` is a specialized Python library designed to streamline game development workflows by automating asset processing and telemetry integration. It provides a robust suite of utilities to bridge the gap between engine-agnostic data structures and production-ready game builds.

## Features

*   **Asset Pipeline Optimization:** Automates texture compression and mesh decimation for various target platforms using multi-threaded batch processing.
*   **Telemetry Event Manager:** A plug-and-play middleware that captures and buffers player metrics, supporting integration with external analytics backends.
*   **Dynamic Data Serializer:** Simplifies game state serialization with high-performance JSON/Binary schema enforcement, ensuring consistent save file structures.
*   **Environment Config Sync:** Synchronizes local developer build settings across distributed teams to ensure uniform build artifacts.

## Installation

Ensure you have Python 3.9+ installed. Install the toolkit via pip:

```bash
pip install dev-toolkit-35
```

For contributors or local development builds:

```bash
git clone https://github.com/Developer/dev-toolkit-35.git
cd dev-toolkit-35
pip install -e .
```

## Basic Usage

Initialize the telemetry client to begin tracking session events within your game loop:

```python
from dev_toolkit import TelemetryClient

# Initialize client with project credentials
client = TelemetryClient(api_key="your_key_here", environment="production")

# Track a custom game event
client.log_event("player_level_up", {"level": 10, "class": "mage"})

# Flush buffer to backend
client.flush()
```

## License

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.