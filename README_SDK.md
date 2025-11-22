# NxtAbroad AI – Python SDK Client

This document explains how to use the Python client (`api_client.py`) to interact with the NxtAbroad AI Visa Readiness & Eligibility Intelligence Engine through its FastAPI endpoint.

The SDK provides a clean, reusable interface for integrating the scoring engine into automation pipelines, dashboards, internal tools, or external applications.

-------------------------------------------------------------

## 1. Overview

The Python SDK enables:

- Sending one or multiple applicant profiles to the `/predict` API endpoint
- Receiving structured scoring results (scores, readiness band, explanations)
- Loading request data from JSON files
- Catching and handling API-level errors
- Smooth, programmatic integration into larger systems

The client acts as a lightweight, production-ready integration layer.

-------------------------------------------------------------

## 2. Installation

Ensure project dependencies are installed:

pip install -r requirements.txt

No additional installation of the SDK is required.

-------------------------------------------------------------

## 3. Basic Usage

from api_client import NxtAbroadAIClient

client = NxtAbroadAIClient(base_url="http://127.0.0.1:8000")

profiles = [
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

result = client.predict(profiles)
print(result)

-------------------------------------------------------------

## 4. Load JSON Request From File

data = client.load_json("data/sample_request.json")
result = client.predict(data["profiles"])

Useful for batch scoring and automated pipelines.

-------------------------------------------------------------

## 5. Error Handling

try:
    result = client.predict(profiles)
except Exception as e:
    print("API Error:", e)

The client automatically raises exceptions for:

- API validation errors  
- Incorrect input structure  
- Non-200 HTTP responses  

-------------------------------------------------------------

## 6. Calling a Remote Server

client = NxtAbroadAIClient(
    base_url="https://api.nxtabroad-ai.com"
)

Works seamlessly with:

- Render  
- Railway  
- AWS ECS / Fargate  
- Azure App Service  
- Docker deployments  

-------------------------------------------------------------

## 7. File Locations

Python SDK:
api_client.py

FastAPI server:
api/demo_fastapi.py

Sample request and response:
data/sample_request.json  
data/sample_response.json

-------------------------------------------------------------

## 8. SDK Methods

### NxtAbroadAIClient.predict(profiles: list) → dict  
Sends profiles to the API and returns scoring output.

### NxtAbroadAIClient.load_json(path: str) → dict  
Loads JSON from disk for API submission.

-------------------------------------------------------------

## 9. Author

Ibrahim Akintunde Akinyera  
Founder · Machine Learning Engineer · Cybersecurity & Risk Analytics  
NxtAbroad Limited (UK–Nigeria)

GitHub: https://github.com/akinyeraakintunde  
Portfolio: https://akinyeraakintunde.github.io/Ibrahim-Akinyera/