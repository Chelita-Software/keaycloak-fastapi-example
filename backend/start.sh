#!/bin/sh
uvicorn document_manager_service.main:app --host 0.0.0.0 --port $PORT --proxy-headers
