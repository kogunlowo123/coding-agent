#!/bin/bash
set -euo pipefail
echo "Setting up Coding Agent..."
pip install -e ".[dev]"
echo "Setup complete!"
