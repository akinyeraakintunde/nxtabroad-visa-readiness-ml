# src/generate_synthetic_data.py

import os
import numpy as np
import pandas as pd


def generate_synthetic_applicants(n_samples: int = 2000, random_state: int = 42) -> pd.DataFrame:
    np.random.seed(random_state)

    # Basic ID
    applicant_id = np.arange(1, n_samples + 1)

    # Age: 18–45 skewed towards mid-20s
    age = np.clip(np.random.normal(loc=26, scale=4.5, size=n_samples), 18, 45).astype(int)

    # Countries
    countries = ["Nigeria", "Ghana", "Kenya", "India", "Pakistan"]
    country_of_citizenship = np.random.choice(countries, size=n_samples, p=[0.55, 0.15, 0.1, 0.1, 0.1])
    country_of_residence = country_of_citizenship  # simple assumption for now

    # Target country
    target_countries = ["UK", "Canada", "Ireland"]
    target_country = np.random.choice(target_countries, size=n_samples, p=[0.6, 0.25, 0.15])

    # Education level
    education_levels = ["Bachelors", "Masters", "Top-up", "Diploma"]
    education_level_applied = np.random.choice(education_levels, size=n_samples, p=[0.4, 0.4, 0.1, 0.1])

    # Course area
    course_areas = ["Business", "IT", "Health", "Engineering", "Social Sciences"]
    course_area = np.random.choice(course_areas, size=n_samples, p=[0.35, 0.25, 0.15, 0.15, 0.1])

    # Tuition fees (GBP equivalent)
    tuition_fee_total_gbp = np.round(
        np.random.normal(loc=18000, scale=3000, size=n_samples).clip(9000, 30000),
        -2
    )

    # Deposit paid (10–50% typically)
    tuition_deposit_paid_gbp = np.round(
        tuition_fee_total_gbp * np.random.uniform(0.1, 0.6, size=n_samples),
        -2
    )

    # Proof of funds (tuition remainder + living costs)
    # living cost assumption 12 months * 1023/1136-ish; we just approximate 12k–16k
    living_costs = np.random.uniform(12000, 18000, size=n_samples)
    required_funds = (tuition_fee_total_gbp - tuition_deposit_paid_gbp) + living_costs

    # Some applicants underfund, some overfund
    proof_of_funds_gbp = np.round(
        required_funds * np.random.normal(loc=1.0, scale=0.25, size=n_samples).clip(0.5, 1.7),
        -2
    )

    # Funds held days (10–120)
    funds_held_days = np.random.randint(10, 121, size=n_samples)

    # Sponsor info
    has_sponsor = np.random.binomial(1, 0.75, size=n_samples)
    sponsor_types = ["Parent", "Sibling", "Spouse", "Self", "Other"]
    sponsor_type = np.where(
        has_sponsor == 1,
        np.random.choice(sponsor_types, size=n_samples, p=[0.6, 0.15, 0.1, 0.1, 0.05]),
        "Self"
    )

    # Visa history
    num_previous_visa_refusals = np.random.choice([0, 1, 2, 3], size=n_samples, p=[0.75, 0.15, 0.07, 0.03])
    previous_study_visa_history = np.random.choice(
        ["None", "UK", "Canada", "Schengen", "Multiple"],
        size=n_samples,
        p=[0.7, 0.1, 0.07, 0.07, 0.06]
    )

    # Employment
    employment_status = np.random.choice(
        ["Employed", "Self-employed", "Unemployed"],
        size=n_samples,
        p=[0.55, 0.2, 0.25]
    )

    employment_duration_months = []
    for status in employment_status:
        if status == "Unemployed":
            employment_duration_months.append(0)
        else:
            employment_duration_months.append(
                int(np.clip(np.random.normal(loc=18, scale=10), 1, 120))
            )
    employment_duration_months = np.array(employment_duration_months)

    # Study gap (0–10 years, skewed low)
    study_gap_years = np.round(
        np.random.gamma(shape=2.0, scale=1.5, size=n_samples).clip(0, 12),
        1
    )

    # IELTS
    ielts_overall_score = np.round(
        np.random.normal(loc=6.5, scale=0.6, size=n_samples).clip(4.5, 8.5),
        1
    )

    ielts_each_band_ok = (ielts_overall_score >= 6.0).astype(int)

    # Course alignment (1–5)
    course_alignment_score = np.random.choice([1, 2, 3, 4, 5], size=n_samples, p=[0.1, 0.15, 0.25, 0.3, 0.2])

    # Financial doc quality (1–5)
    financial_document_quality = np.random.choice([1, 2, 3, 4, 5], size=n_samples, p=[0.1, 0.15, 0.25, 0.3, 0.2])

    # Documentation completeness (1–10, higher = more complete)
    documentation_completeness = np.random.randint(4, 11, size=n_samples)

    # Country risk (1–5)
    country_risk_map = {
        "Nigeria": 4,
        "Ghana": 3,
        "Kenya": 3,
        "India": 2,
        "Pakistan": 3,
    }
    country_risk_level = np.array([country_risk_map[c] for c in country_of_citizenship])

    # Consultant manual flag (rare)
    consultant_manual_flag = np.random.binomial(1, 0.05, size=n_samples)

    # ------- Rule-based label creation (visa_readiness_class) ------- #
    # We'll create a base score and then convert to 0/1/2

    base_score = np.zeros(n_samples, dtype=float)

    # Funds vs required
    funds_ratio = proof_of_funds_gbp / (required_funds + 1e-6)
    base_score += np.where(funds_ratio >= 1.0, 2.0,
                           np.where(funds_ratio >= 0.8, 0.5, -2.0))

    # Funds held days
    base_score += np.where(funds_held_days >= 28, 1.5,
                           np.where(funds_held_days >= 21, 0.5, -1.5))

    # Course alignment & docs
    base_score += (course_alignment_score - 3) * 0.8
    base_score += (financial_document_quality - 3) * 0.8
    base_score += (documentation_completeness - 7) * 0.3

    # Study gap
    base_score += np.where(study_gap_years <= 2, 1.0,
                           np.where(study_gap_years <= 5, 0.0, -1.5))

    # IELTS
    base_score += np.where(ielts_overall_score >= 6.0, 1.0,
                           np.where(ielts_overall_score >= 5.5, 0.0, -1.5))

    # Visa refusals
    base_score += np.where(num_previous_visa_refusals == 0, 1.0,
                           np.where(num_previous_visa_refusals == 1, -0.5, -1.5))

    # Country risk
    base_score += (3 - country_risk_level) * 0.3  # lower risk_level => higher score

    # Manual flag
    base_score += np.where(consultant_manual_flag == 1, -1.0, 0.0)

    # Add a little noise
    base_score += np.random.normal(loc=0.0, scale=0.7, size=n_samples)

    # Convert base_score to classes: 0 = High Risk, 1 = Medium, 2 = Ready
    visa_readiness_class = np.where(
        base_score >= 3.0, 2,
        np.where(base_score >= 1.0, 1, 0)
    )

    df = pd.DataFrame({
        "applicant_id": applicant_id,
        "age": age,
        "country_of_citizenship": country_of_citizenship,
        "country_of_residence": country_of_residence,
        "target_country": target_country,
        "education_level_applied": education_level_applied,
        "course_area": course_area,
        "tuition_fee_total_gbp": tuition_fee_total_gbp,
        "tuition_deposit_paid_gbp": tuition_deposit_paid_gbp,
        "proof_of_funds_gbp": proof_of_funds_gbp,
        "funds_held_days": funds_held_days,
        "has_sponsor": has_sponsor,
        "sponsor_type": sponsor_type,
        "num_previous_visa_refusals": num_previous_visa_refusals,
        "previous_study_visa_history": previous_study_visa_history,
        "employment_status": employment_status,
        "employment_duration_months": employment_duration_months,
        "study_gap_years": study_gap_years,
        "ielts_overall_score": ielts_overall_score,
        "ielts_each_band_ok": ielts_each_band_ok,
        "course_alignment_score": course_alignment_score,
        "financial_document_quality": financial_document_quality,
        "documentation_completeness": documentation_completeness,
        "country_risk_level": country_risk_level,
        "consultant_manual_flag": consultant_manual_flag,
        "visa_readiness_class": visa_readiness_class,
    })

    return df


def main():
    # Ensure directories exist
    processed_dir = os.path.join("data", "processed")
    os.makedirs(processed_dir, exist_ok=True)

    df = generate_synthetic_applicants(n_samples=3000, random_state=42)
    output_path = os.path.join(processed_dir, "visa_readiness_data.csv")
    df.to_csv(output_path, index=False)

    print(f"Saved synthetic dataset to: {output_path}")
    print(df.head())


if __name__ == "__main__":
    main()

