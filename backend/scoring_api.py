from fastapi import APIRouter
from pydantic import BaseModel, Field
from typing import Any, Dict, List, Optional

router = APIRouter(tags=["Scoring"])

class ApplicantPayload(BaseModel):
    # Keep it flexible: your engine can ignore fields it doesn't need
    target_country: str = Field(default="UK", description="e.g., UK or Canada")
    profile: Dict[str, Any] = Field(default_factory=dict, description="Applicant details")
    documents: List[Dict[str, Any]] = Field(default_factory=list, description="Document metadata")

@router.post("/score")
def score_applicant(payload: ApplicantPayload):
    """
    MVP scoring endpoint.
    In the next step, we will connect this to your existing engine function.
    For now, it returns a working placeholder response (so the API is usable).
    """
    # TODO: replace with real engine call (we’ll do that next)
    return {
        "score": 75,
        "band": "AMBER",
        "flags": [
            {"type": "MISSING_DOCUMENT", "severity": "MEDIUM", "message": "One or more documents missing"}
        ],
        "explanations": [
            "Profile received successfully",
            "Scoring engine integration is next",
        ],
        "received": payload.model_dump()
    }