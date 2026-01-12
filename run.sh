#!/bin/bash

# 启动项目
echo "启动项目..."
uv run uvicorn src.main:app --host localhost --port 8000 --reload