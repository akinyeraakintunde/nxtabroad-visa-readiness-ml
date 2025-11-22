"""
utils.py
Utility functions for data validation, safe parsing,
and profile normalisation for NxtAbroad AI.
Author: Ibrahim Akintunde Akinyera
"""


# ----------------------------------------------------------
# Safe type conversion helpers
# ----------------------------------------------------------

def safe_int(value, default=0):
    try:
        return int(value)
    except:
        return default


def safe_float(value, default=0.0):
    try:
        return float(value)
    except:
        return default


def safe_str(value, default=""):
    if value is None:
        return default
    return str(value).strip()


# ----------------------------------------------------------
# Normalise a profile row so rules never break
# ----------------------------------------------------------

EXPECTED_FIELDS = [
    "profile_id",
    "destination_country",
    "level_of_study",
    "course_match",
    "degree_classification",
    "study_gap_years",
    "has_english_test",
    "english_test_type",
    "english_overall_score",
    "pof_required_gbp",
    "pof_available_gbp",
    "bank_statement_months",
    "sponsor_type",
    "recent_large_deposit",
    "documents_complete",
    "documents_quality_score",
    "previous_visa_refusal",
    "travel_history_level",
    "personal_statement_quality",
    "dependants_count",
    "target_intake",
    "advisor_location"
]


def normalise_profile(raw):
    """
    Normalises a CSV dict row into a clean dictionary 
    so rules_engine can safely process it.
    """

    profile = {}

    for field in EXPECTED_FIELDS:
        value = raw.get(field, "")

        # Convert some fields specially
        if field in ["study_gap_years", "bank_statement_months", "dependants_count"]:
            profile[field] = safe_int(value)

        elif field in ["english_overall_score", "pof_required_gbp", "pof_available_gbp", "documents_quality_score"]:
            profile[field] = safe_float(value)

        else:
            profile[field] = safe_str(value)

    return profile


# ----------------------------------------------------------
# Example helper: log output cleanly
# ----------------------------------------------------------

def print_profile_result(profile_id, result):
    """
    Clean console logger (optional).
    """
    print("--------------------------------------------------")
    print(f"Profile ID: {profile_id}")
    print(f"Academic Score:      {result['academic_score']}")
    print(f"Financial Score:     {result['financial_score']}")
    print(f"Documentation Score: {result['documentation_score']}")
    print(f"Credibility Score:   {result['credibility_score']}")
    print(f"Overall Score:       {result['overall_score']}")
    print(f"Readiness Band:      {result['readiness_band']}")
    print(f"Notes: {result['explanations']}")
    print("--------------------------------------------------\n")