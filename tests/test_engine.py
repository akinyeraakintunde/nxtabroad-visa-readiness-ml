"""
Basic unit tests for NxtAbroad AI rules engine and scorer.
Author: Ibrahim Akintunde Akinyera
"""

import os
import csv
import pytest

from src.rules_engine import run_all_rules
from src.scorer import score_profile


DATA_PATH = os.path.join("data", "raw", "sample_profiles.csv")


def load_first_profile():
    with open(DATA_PATH, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            return row
    return None


def test_sample_profiles_file_exists():
    assert os.path.exists(DATA_PATH), "sample_profiles.csv is missing."


def test_run_all_rules_returns_expected_keys():
    profile = load_first_profile()
    assert profile is not None, "No profile found in sample_profiles.csv."

    result = run_all_rules(profile)

    assert "academic_score" in result
    assert "financial_score" in result
    assert "documentation_score" in result
    assert "credibility_score" in result
    assert "total_score" in result
    assert "reasons" in result
    assert isinstance(result["reasons"], list)


def test_score_profile_output_structure():
    profile = load_first_profile()
    result = score_profile(profile)

    expected_keys = [
        "academic_score",
        "financial_score",
        "documentation_score",
        "credibility_score",
        "overall_score",
        "readiness_band",
        "explanations",
    ]

    for key in expected_keys:
        assert key in result, f"Missing key in score_profile result: {key}"

    assert result["readiness_band"] in ["High", "Medium", "Low"]
    assert isinstance(result["explanations"], str)
