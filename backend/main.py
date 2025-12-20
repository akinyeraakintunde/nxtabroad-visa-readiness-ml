from fastapi import FastAPI
from pydantic import BaseModel, Field

from backend.decision_engine import ApplicantProfile, assess_readiness
from backend.demo_page import router as demo_router
app = FastAPI(
    title="NxtAbroad AI – Visa Readiness Agent (Demo)",
    version="1.0.0",
    description="Rules-first, explainable visa readiness scoring agent."
)
app.include_router(demo_router)
class AssessRequest(BaseModel):
    highest_qualification: str = Field(..., example="MSc")
    destination_country: str = Field(..., example="UK")
    available_funds_gbp: float = Field(..., example=12000)
    work_experience_years: float = Field(..., example=4)
    english_test_done: bool = Field(..., example=True)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/assess")
def assess(payload: AssessRequest):
    profile = ApplicantProfile(
        highest_qualification=payload.highest_qualification,
        destination_country=payload.destination_country,
        available_funds_gbp=payload.available_funds_gbp,
        work_experience_years=payload.work_experience_years,
        english_test_done=payload.english_test_done
    )
    return assess_readiness(profile)
    
    @app.get("/")
def root():
    return {
        "name": "NxtAbroad AI – Visa Readiness Agent (Demo)",
        "docs": "/docs",
        "health": "/health"
    }