#!/bin/bash

echo "--------------------------------------------"
echo " NxtAbroad AI – Visa Readiness API Demo"
echo "--------------------------------------------"

echo "Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Starting FastAPI service..."
echo "Visit: http://127.0.0.1:8000/docs"
echo "Press CTRL + C to stop."

uvicorn api.demo_fastapi:app --reload --host 127.0.0.1 --port 8000
