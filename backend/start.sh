#!/bin/sh
uvicorn backend.main:app --host 0.0.0.0 --port $PORT --proxy-headers
