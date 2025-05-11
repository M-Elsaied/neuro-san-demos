#!/bin/bash

echo "🔁 Starting Flask Web Client using Render-assigned port: $PORT"
export NEURO_SAN_WEB_CLIENT_PORT=$PORT
export NEURO_SAN_SERVER_HOST=localhost
export NEURO_SAN_SERVER_PORT=30013
export AGENT_MANIFEST_FILE=registries/manifest.hocon
export AGENT_TOOL_PATH=coded_tools
export AGENT_MANIFEST_UPDATE_PERIOD_SECONDS=5

# Start Neuro-SAN backend in background
python -u -m neuro_san.service.agent_main_loop --port $NEURO_SAN_SERVER_PORT &

# Start Flask web client in foreground (this is the exposed service)
python -u -m neuro_san_web_client.app \
  --server-host $NEURO_SAN_SERVER_HOST \
  --server-port $NEURO_SAN_SERVER_PORT \
  --web-client-port $PORT \
  --thinking-file /tmp/agent_thinking.txt
