# dev-toolkit-35

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

dev-toolkit-35 is a Python toolkit designed for indie game developers building 2D experiences. It provides practical utilities that handle asset processing and content generation to speed up development.

## Features
- Procedural map generator using simplex noise to create varied terrain and layouts
- Sprite atlas packer that combines images into efficient sheets while preserving metadata
- Game loop profiler for measuring CPU usage and identifying slow functions during playtests
- Batch asset converter supporting common formats like PNG, JPG, and TGA for game imports

## Installation

Install the package directly with pip:
```bash
pip install dev-toolkit-35
```

Clone and install from source:
```bash
git clone https://github.com/Developer/dev-toolkit-35.git
cd dev-toolkit-35
pip install -e .
```

## Basic Usage
```python
from dev_toolkit_35 import MapGenerator

generator = MapGenerator(128, 128, seed=42)
level = generator.generate()
level.export("level.json")
```