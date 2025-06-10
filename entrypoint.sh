#!/bin/bash
python3 src/fastapi_app/seed_data.py
gunicorn -w 2 -k uvicorn.workers.UvicornWorker fastapi_app.main:app --bind=0.0.0.0:8000