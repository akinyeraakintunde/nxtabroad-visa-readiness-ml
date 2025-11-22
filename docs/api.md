# NxtAbroad Visa Readiness Engine – API Documentation

This document describes the REST API provided by the NxtAbroad Visa Readiness ML Engine. The API exposes machine-learning scoring, rules-engine evaluation, and health-check endpoints to support integrations with NxtAbroad internal systems, dashboards, and partner platforms.

---

## 1. Base URL

Local development:
http://localhost:8000

Docker deployment:
http://localhost:8001

---

## 2. Endpoints Overview

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /health | API health/status check |
| POST | /score | Full Visa Readiness Score (ML + Rules) |
| POST | /predict | Predict visa readiness class only |
| GET | /schema | Retrieve OpenAPI schema |

---

## 3. Request Format

Content-Type: application/json

Example request body:

{
  "name": "John Doe",
  "age": 24,
  "country": "Nigeria",
  "education_background": "BSc Computer Science",
  "grade": "Second Class Upper",
  "english_score": 6.5,
  "funds_available_gbp": 13500,
  "has_tb_test": true,
  "immigration_history": "None",
  "documents": {
    "passport": true,
    "sop": true,
    "cas_documents": true,
    "bank_statements": true
  },
  "timeline_months_before_start": 6,
  "selected_school_ranking": 78
}

---

## 4. API Endpoints in Detail

### 4.1 GET /health

Response:

{
  "status": "ok",
  "message": "NxtAbroad Visa Readiness API is running"
}

---

### 4.2 POST /score

Runs the full scoring pipeline:
- ML prediction
- Rules engine evaluation
- Weighted scoring
- Final readiness score
- Explanations

Response:

{
  "score": 87,
  "category": "Visa-Ready",
  "explanations": [
    "Strong Proof of Funds provided",
    "Good academic background",
    "Early application timeline",
    "All major documents submitted"
  ]
}

---

### 4.3 POST /predict

Returns the ML model’s predicted visa readiness category only.

Response:

{
  "prediction": "Visa-Ready",
  "probability": 0.92
}

---

### 4.4 GET /schema

Returns the complete OpenAPI definition for generating SDKs or clients.  
Stored locally as: openapi_schema.json

---

## 5. Error Handling

Error responses follow:

{
  "error": true,
  "message": "Invalid input: missing required field 'grade'"
}

HTTP Status Codes:
- 200 OK
- 400 Invalid request
- 500 Internal server error

---

## 6. Postman Collection

Import the file:
postman_collection.json

Includes ready-made:
- /predict
- /score
- /health

---

## 7. Running the API Locally

### Option A — Python

pip install -r requirements.txt
uvicorn api.demo_fastapi:app --reload

### Option B — Docker

docker-compose up --build

---

## 8. Security Notes

- No real PII included; all data is synthetic.
- JWT authentication is recommended for production.
- HTTPS should be enforced in deployed environments.

---

## 9. Versioning

Current API Version:
v1.0.0

---

## 10. Contact

Ibrahim Akintunde Akinyera  
Machine Learning & Cybersecurity Engineer  
Founder, NxtAbroad Limited  
Email: info@nxtabroad.com  
Portfolio: https://akinyeraakintunde.github.io/Ibrahim-Akinyera/