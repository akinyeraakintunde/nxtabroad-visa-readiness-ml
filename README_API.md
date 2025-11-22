# NxtAbroad AI – Visa Readiness API Documentation

This document describes the API interface for the NxtAbroad AI Visa Readiness Engine. The API exposes a scoring endpoint that evaluates academic, financial, documentation, and credibility indicators and returns a Visa Readiness Score (Low / Medium / High) with explanations.

The API is built with FastAPI and Pydantic.

-------------------------------------------------------------

## 1. Overview

Endpoint:
POST /predict

Purpose:
- Accept one or more applicant profiles
- Validate and normalise fields
- Apply all rule categories (academic, financial, documentation, credibility)
- Return readiness scores including explanations

-------------------------------------------------------------

## 2. How to Run the API Locally

Install dependencies:

pip install -r requirements.txt

Run the API with Uvicorn:

uvicorn demo_fastapi:app --reload

API URL:
http://127.0.0.1:8000

Swagger UI:
http://127.0.0.1:8000/docs

-------------------------------------------------------------

## 3. Request Format

Endpoint:
POST /predict

Content-Type:
application/json

JSON Body Structure:

{
  "profiles": [
    {
      "profile_id": "STU001",
      "destination_country": "UK",
      "level_of_study": "Masters",
      "course_match": "Strong",
      "degree_classification": "First Class",
      "study_gap_years": 0,
      "has_english_test": "Yes",
      "english_test_type": "IELTS Academic",
      "english_overall_score": 7.5,
      "pof_required_gbp": 18400,
      "pof_available_gbp": 26000,
      "bank_statement_months": 6,
      "sponsor_type": "Self",
      "recent_large_deposit": "No",
      "documents_complete": "Yes",
      "documents_quality_score": 92,
      "previous_visa_refusal": "No",
      "travel_history_level": "Strong",
      "personal_statement_quality": "Strong",
      "dependants_count": 0,
      "target_intake": "2026-01",
      "advisor_location": "Ibadan"
    }
  ]
}

(Also available in data/sample_request.json)

-------------------------------------------------------------

## 4. Response Format

Example successful response:

{
  "results": [
    {
      "profile_id": "STU001",
      "academic_score": 92,
      "financial_score": 94,
      "documentation_score": 95,
      "credibility_score": 90,
      "overall_score": 93,
      "readiness_band": "High",
      "explanations": [
        "Academic strength: First Class.",
        "Funds meet or exceed requirement.",
        "Documentation complete.",
        "Strong travel history.",
        "Strong personal statement."
      ]
    }
  ]
}

(Also available in data/sample_response.json)

-------------------------------------------------------------

## 5. Error Handling

Missing fields → 422 Unprocessable Entity  
Invalid data types → FastAPI validation errors  
Invalid structures → Detailed JSON validation report

-------------------------------------------------------------

## 6. Code Structure

demo_fastapi.py  
- Defines the FastAPI app  
- Implements /predict endpoint  
- Uses Pydantic models for validation  
- Calls rules_engine + utils for scoring logic  

Depends on:
- rules_engine.py  
- utils.py  

-------------------------------------------------------------

## 7. Example cURL Request

curl -X POST "http://127.0.0.1:8000/predict" \
     -H "Content-Type: application/json" \
     -d @data/sample_request.json

-------------------------------------------------------------

## 8. Example Python Client

import requests, json

url = "http://127.0.0.1:8000/predict"
payload = json.load(open("data/sample_request.json"))

response = requests.post(url, json=payload)
print(response.json())

-------------------------------------------------------------

## 9. Future API Enhancements

- API Key or JWT authentication
- Cloud deployment (AWS, Render, Azure)
- Logging and analytics dashboard
- ML-enhanced risk prediction

-------------------------------------------------------------

## 10. Author

Ibrahim Akintunde Akinyera  
Founder · Machine Learning Engineer · Cybersecurity & Risk Analytics  
NxtAbroad Limited (UK–Nigeria)

GitHub: https://github.com/akinyeraakintunde  
Portfolio: https://akinyeraakintunde.github.io/Ibrahim-Akinyera/
