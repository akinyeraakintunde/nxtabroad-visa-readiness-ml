from dataclasses import dataclass
from typing import Dict, List, Tuple


@dataclass
class ApplicantProfile:
    highest_qualification: str  # e.g., "BSc", "MSc", "HND", "Diploma"
    destination_country: str    # e.g., "UK", "Canada", "Ireland"
    available_funds_gbp: float  # in GBP for v1 demo (simple)
    work_experience_years: float
    english_test_done: bool


def _clamp(x: float, lo: float = 0.0, hi: float = 100.0) -> float:
    return max(lo, min(hi, x))


def assess_readiness(profile: ApplicantProfile) -> Dict:
    """
    Rules-first scoring engine (v1):
    - Produces readiness_score (0-100), risk_level, reasons, recommendations
    - Intentionally simple, explainable, and demo-friendly
    """

    score = 50.0  # start neutral
    risk = 0.0
    reasons: List[str] = []
    recommendations: List[str] = []

    # 1) Qualification signal (simple)
    q = profile.highest_qualification.strip().lower()
    if q in ["msc", "master", "masters", "m.sc", "m.sc."]:
        score += 15
        reasons.append("Strong academic profile (Master’s level).")
    elif q in ["bsc", "b.sc", "b.sc.", "bachelor", "bachelors"]:
        score += 10
        reasons.append("Solid academic profile (Bachelor’s level).")
    elif q in ["hnd", "diploma"]:
        score += 3
        reasons.append("Academic profile is acceptable, but may require stronger supporting evidence.")
        recommendations.append("Strengthen Statement of Purpose and supporting documents.")
    else:
        score -= 5
        risk += 10
        reasons.append("Academic profile is unclear or not standardised.")
        recommendations.append("Provide clearer education history and transcripts.")

    # 2) Funds threshold (demo assumption)
    # Keep it simple: UK-style demonstration threshold for readiness
    if profile.available_funds_gbp >= 12000:
        score += 15
        reasons.append("Funds appear sufficient for initial visa readiness checks.")
    elif 8000 <= profile.available_funds_gbp < 12000:
        score += 5
        risk += 10
        reasons.append("Funds are borderline; may be acceptable depending on route and tuition/deposit.")
        recommendations.append("Increase available funds buffer or provide stronger financial evidence.")
    else:
        score -= 10
        risk += 25
        reasons.append("Funds appear insufficient for a safe application profile.")
        recommendations.append("Increase funds and/or prepare stronger sponsor evidence.")

    # 3) English test (binary for v1)
    if profile.english_test_done:
        score += 10
        reasons.append("English proficiency evidence confirmed.")
    else:
        risk += 15
        reasons.append("English proficiency evidence not confirmed yet.")
        recommendations.append("Book IELTS/UKVI IELTS or provide approved alternative evidence.")

    # 4) Work experience (simple)
    if profile.work_experience_years >= 5:
        score += 10
        reasons.append("Strong work history supports credibility and intent.")
    elif 2 <= profile.work_experience_years < 5:
        score += 5
        reasons.append("Work experience supports credibility.")
    else:
        score -= 3
        reasons.append("Limited work experience; ensure documentation and SOP are very clear.")
        recommendations.append("Strengthen SOP and demonstrate clear academic/career progression.")

    # 5) Destination nudges (light logic)
    dest = profile.destination_country.strip().lower()
    if dest in ["uk", "united kingdom"]:
        reasons.append("Destination: UK (ensure UKVI-compliant documentation and timelines).")
        recommendations.append("Prepare UKVI-compliant document checklist and financial evidence.")
    elif dest in ["canada"]:
        reasons.append("Destination: Canada (consider SDS vs non-SDS and proof of funds strategy).")
        recommendations.append("Confirm SDS eligibility and plan proof of funds accordingly.")
    else:
        reasons.append(f"Destination: {profile.destination_country} (ensure local requirements are met).")

    # Risk level mapping
    score = _clamp(score - (risk * 0.3))  # risk reduces score
    if risk >= 40:
        risk_level = "High"
    elif risk >= 20:
        risk_level = "Medium"
    else:
        risk_level = "Low"

    # Keep top reasons tidy
    top_reasons = reasons[:5]
    top_recommendations = list(dict.fromkeys(recommendations))[:5]  # unique, preserve order

    return {
        "readiness_score": round(score, 1),
        "risk_level": risk_level,
        "key_reasons": top_reasons,
        "recommendations": top_recommendations,
        "inputs_used": {
            "highest_qualification": profile.highest_qualification,
            "destination_country": profile.destination_country,
            "available_funds_gbp": profile.available_funds_gbp,
            "work_experience_years": profile.work_experience_years,
            "english_test_done": profile.english_test_done,
        }
    }