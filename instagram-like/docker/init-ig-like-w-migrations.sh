#!/bin/bash

echo " Starting migrations..."
alembic upgrade head

echo "\n Init server..."
uvicorn src.entrypoint:app --host 0.0.0.0 --port 8002 --reload

