"""
demo_fastapi.py
FastAPI scoring endpoint for NxtAbroad AI.
Author: Ibrahim Akintunde Akinyera
"""

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict, Any

from rules_engine import run_all_rules
from utils import normalise_profile

app = FastAPI(
    title="NxtAbroad AI – Visa Readiness API",
    description="API for scoring visa readiness profiles using rule-based evaluation.",
    version="1.0.0"
)


# ----------------------------------------------------------
# Pydantic Models (input validation)
# ----------------------------------------------------------

class Profile(BaseModel):
    profile_id: str
    destination_country: str
    level_of_study: str
    course_match: str
    degree_classification: str
    study_gap_years: int
    has_english_test: str
    english_test_type: str
    english_overall_score: float
    pof_required_gbp: float
    pof_available_gbp: float
    bank_statement_months: int
    sponsor_type: str
    recent_large_deposit: str
    documents_complete: str
    documents_quality_score: float
    previous_visa_refusal: str
    travel_history_level: str
    personal_statement_quality: str
    dependants_count: int
    target_intake: str
    advisor_location: str


class ProfileRequest(BaseModel):
    profiles: List[Profile]


# ----------------------------------------------------------
# Scoring Logic Wrapper
# ----------------------------------------------------------

def score_single_profile(profile: Dict[str, Any]) -> Dict[str, Any]:
    raw = dict(profile)
    clean = normalise_profile(raw)
    result = run_all_rules(clean)

    total = result["total_score"]
    if total >= 80:
        readiness = "High"
    elif total >= 65:
        readiness = "Medium"
    else:
        readiness = "Low"

    return {
        "profile_id": clean["profile_id"],
        "academic_score": result["academic_score"],
        "financial_score": result["financial_score"],
        "documentation_score": result["documentation_score"],
        "credibility_score": result["credibility_score"],
        "overall_score": total,
        "readiness_band": readiness,
        "explanations": result["reasons"]
    }


# ----------------------------------------------------------
# API Endpoint
# ----------------------------------------------------------

@app.post("/predict")
def predict(request: ProfileRequest):
    output = []

    for profile in request.profiles:
        scored = score_single_profile(profile.dict())
        output.append(scored)

    return {"results": output}


# ----------------------------------------------------------
# Local Run Instructions
# ----------------------------------------------------------

# To run the API locally:
#
#   uvicorn demo_fastapi:app --reload
#
# Visit documentation at:
#
#   http://127.0.0.1:8000/docs
#
