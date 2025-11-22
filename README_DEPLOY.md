# NxtAbroad AI – Deployment Guide
This document explains how to deploy the NxtAbroad AI Visa Readiness Scoring Engine and API to different environments, including local machines, Docker containers, and cloud platforms.

The goal of this guide is to provide a production-ready, reproducible deployment workflow.

-------------------------------------------------------------

## 1. Project Structure (Summary)

Key components required for deployment:

- src/rules_engine.py  
- src/scorer.py  
- src/utils.py  
- api/demo_fastapi.py (FastAPI scoring endpoint)  
- requirements.txt  
- Dockerfile  
- run_demo.sh  
- data/ (sample data, optional in production)  
- README_API.md  
- openapi_schema.json  

-------------------------------------------------------------

## 2. Local Deployment

### 2.1 Install Dependencies

Create a virtual environment:

python3 -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

### 2.2 Run the API

uvicorn api.demo_fastapi:app --reload

Visit:

http://127.0.0.1:8000/docs

-------------------------------------------------------------

## 3. Deployment with Docker

### 3.1 Build Docker Image

docker build -t nxtabroad-ai .

### 3.2 Run the Container

docker run -p 8000:8000 nxtabroad-ai

Visit the API:

http://localhost:8000/docs

### 3.3 Running in Background

docker run -d -p 8000:8000 nxtabroad-ai

-------------------------------------------------------------

## 4. Deployment with Docker Compose

Create a file named docker-compose.yml:

version: "3.9"

services:
  nxtabroad_ai:
    build: .
    container_name: nxtabroad-ai
    ports:
      - "8000:8000"
    restart: always

Run:

docker-compose up --build -d

-------------------------------------------------------------

## 5. Cloud Deployment Options

### 5.1 Render (Recommended – Simple & Free Tier)

Steps:
1. Push code to GitHub  
2. Log into Render.com  
3. Create a new "Web Service"  
4. Select your repo  
5. Runtime: Docker  
6. Build Command: docker build -t nxtabroad-ai .  
7. Start Command: uvicorn api.demo_fastapi:app --host 0.0.0.0 --port 8000  
8. Deploy  

### 5.2 Railway.app

Steps similar to Render:
- Connect GitHub repo  
- Auto-detect FastAPI  
- Expose port 8000  
- Deploy with container  

### 5.3 AWS ECS or AWS App Runner

Use the Dockerfile:
- Push Docker image to AWS ECR  
- Deploy via ECS Fargate or App Runner  
- Autoscaling and SSL supported  

-------------------------------------------------------------

## 6. Environment Variables (Optional)

Create a file `.env.example` if needed:

API_ENV=production
LOG_LEVEL=info

In FastAPI, load with python-dotenv:

from dotenv import load_dotenv
load_dotenv()

-------------------------------------------------------------

## 7. Health Check Endpoint (Optional)

Add to demo_fastapi.py:

@app.get("/health")
def health():
    return {"status": "ok"}

-------------------------------------------------------------

## 8. Production Recommendation Checklist

- Use Docker for consistent builds  
- Enable HTTPS in cloud environment  
- Add API authentication (API Key / JWT)  
- Add logging and monitoring  
- Set up CI/CD (GitHub Actions recommended)  

-------------------------------------------------------------

## 9. Author

Ibrahim Akintunde Akinyera  
Founder · Machine Learning Engineer · Cybersecurity & Risk Analytics  
NxtAbroad Limited (UK–Nigeria)

GitHub: https://github.com/akinyeraakintunde  
Portfolio: https://akinyeraakintunde.github.io/Ibrahim-Akinyera/
