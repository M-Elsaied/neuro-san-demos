#!/bin/bash

echo "🔁 Starting Neuro-SAN with nsflow (FastAPI client)"

# Use Render's assigned port for nsflow
export NSFLOW_PORT=$PORT
export NEURO_SAN_SERVER_HOST=localhost
export NEURO_SAN_SERVER_PORT=30013
export AGENT_MANIFEST_FILE=registries/manifest.hocon
export AGENT_TOOL_PATH=coded_tools
export AGENT_MANIFEST_UPDATE_PERIOD_SECONDS=5

# Start everything using run.py (will launch both server + nsflow)
python -m run
