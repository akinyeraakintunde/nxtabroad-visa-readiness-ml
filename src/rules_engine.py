"""
rules_engine.py
Core rules engine for NxtAbroad AI – Visa Readiness & Eligibility Intelligence Engine.
Author: Ibrahim Akintunde Akinyera
"""

# -----------------------------
# Academic Rules
# -----------------------------

def academic_rules(profile):
    score = 0
    reasons = []

    # Degree classification scoring
    degree_map = {
        "First Class": 90,
        "Distinction": 88,
        "Upper Second": 80,
        "HND Upper": 75,
        "Lower Second": 65,
        "HND Lower": 60,
        "Third Class": 55
    }

    degree = profile.get("degree_classification", "").strip()
    if degree in degree_map:
        score += degree_map[degree]
        reasons.append(f"Academic strength: {degree}.")
    else:
        score += 60
        reasons.append("Unrecognised degree type (default score).")

    # Study gap scoring
    gap = int(profile.get("study_gap_years", 0))
    if gap <= 1:
        score += 10
    elif 2 <= gap <= 4:
        score += 5
        reasons.append("Moderate study gap.")
    else:
        score -= 5
        reasons.append("Long study gap, needs justification.")

    # English requirement scoring
    if profile.get("has_english_test", "").lower() == "yes":
        english_score = float(profile.get("english_overall_score", 0))
        if english_score >= 7.0:
            score += 10
        elif english_score >= 6.0:
            score += 6
        else:
            score += 2
            reasons.append("Low English proficiency score.")
    else:
        score -= 5
        reasons.append("No English test provided.")

    return max(score, 0), reasons


# -----------------------------
# Financial Rules
# -----------------------------

def financial_rules(profile):
    score = 0
    reasons = []

    required = float(profile.get("pof_required_gbp", 0))
    available = float(profile.get("pof_available_gbp", 0))

    # Funds check
    if available >= required:
        score += 40
        reasons.append("Funds meet or exceed requirement.")
    elif required * 0.85 <= available < required:
        score += 20
        reasons.append("Funds slightly below requirement.")
    else:
        score += 5
        reasons.append("Insufficient proof of funds.")

    # Bank statement duration
    months = int(profile.get("bank_statement_months", 0))
    if months >= 6:
        score += 15
    elif months >= 3:
        score += 8
    else:
        score += 2
        reasons.append("Short bank history.")

    # Large deposits flag
    if profile.get("recent_large_deposit", "").lower() == "yes":
        score -= 5
        reasons.append("Recent unexplained deposit detected.")

    return max(score, 0), reasons


# -----------------------------
# Documentation Rules
# -----------------------------

def documentation_rules(profile):
    score = 0
    reasons = []

    # Document completeness
    if profile.get("documents_complete", "").lower() == "yes":
        score += 25
    else:
        score += 10
        reasons.append("Documentation incomplete.")

    # Quality score (0–100)
    quality = int(profile.get("documents_quality_score", 0))
    score += quality * 0.2

    return max(score, 0), reasons


# -----------------------------
# Credibility Rules
# -----------------------------

def credibility_rules(profile):
    score = 0
    reasons = []

    # Previous refusals
    if profile.get("previous_visa_refusal", "").lower() == "yes":
        score -= 15
        reasons.append("Previous visa refusal.")

    # Travel history
    travel = profile.get("travel_history_level", "").strip().lower()
    if travel == "strong":
        score += 15
    elif travel == "limited":
        score += 5
    else:
        score += 1
        reasons.append("Weak or no travel history.")

    # Personal statement quality
    ps_map = {
        "Strong": 15,
        "Limited": 8,
        "None": 0
    }

    ps = profile.get("personal_statement_quality", "").strip()
    score += ps_map.get(ps, 0)

    # Dependants
    dependants = int(profile.get("dependants_count", 0))
    if dependants >= 2:
        score -= 5
        reasons.append("Multiple dependants increase risk.")

    return max(score, 0), reasons


# -----------------------------
# MAIN RULES ENGINE
# -----------------------------

def run_all_rules(profile):
    academic, acad_reasons = academic_rules(profile)
    financial, fin_reasons = financial_rules(profile)
    docs, doc_reasons = documentation_rules(profile)
    credibility, cred_reasons = credibility_rules(profile)

    total = academic + financial + docs + credibility

    reasons = acad_reasons + fin_reasons + doc_reasons + cred_reasons

    return {
        "academic_score": academic,
        "financial_score": financial,
        "documentation_score": docs,
        "credibility_score": credibility,
        "total_score": total,
        "reasons": reasons
    }