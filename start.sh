#!/bin/bash

echo "🔁 Starting Neuro-SAN with nsflow (FastAPI client)"
export NEURO_SAN_SERVER_HOST=0.0.0.0
export NEURO_SAN_SERVER_PORT=$PORT #30013
export NSFLOW_PORT=$PORT
export AGENT_MANIFEST_FILE=registries/manifest.hocon
export AGENT_TOOL_PATH=coded_tools
export AGENT_MANIFEST_UPDATE_PERIOD_SECONDS=5

# Start Neuro-SAN backend in the background
python -u -m neuro_san.service.agent_main_loop --port $NEURO_SAN_SERVER_PORT &

# Start nsflow frontend in the foreground
python -u -m uvicorn nsflow.backend.main:app --host 0.0.0.0 --port $PORT
