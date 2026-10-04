#!/bin/bash
# Cafe Roulette local server runner script using uv

# Ensure uv virtual environment exists
if [ ! -d ".venv" ]; then
    echo "📦 uv 가상환경(.venv)을 생성합니다..."
    uv venv
fi

# Run HTTP server with uv
echo "⚡ uv를 사용하여 서빙 스크립트를 실행합니다..."
uv run python serve.py "$@"
