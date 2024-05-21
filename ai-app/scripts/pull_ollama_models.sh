#!/bin/bash

set -e

CURR_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WS_ROOT="$(dirname ${CURR_DIR})"
NAME="ai-ollama"


echo "Running: docker exec -it $NAME ollama pull llama3 && ollama pull nomic-embed-text"
docker exec -it $NAME ollama pull llama3 && ollama pull nomic-embed-text