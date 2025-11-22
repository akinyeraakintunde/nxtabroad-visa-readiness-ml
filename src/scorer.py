"""
scorer.py
Aggregates rule outputs from rules_engine.py to produce a final Visa Readiness Score.
Author: Ibrahim Akintunde Akinyera
"""

import csv
import argparse
from rules_engine import run_all_rules


# ----------------------------------------------------------
# Calculate readiness band based on total score
# ----------------------------------------------------------

def readiness_band(total_score):
    """
    Maps total numeric score to readiness band:
    - High (strong candidate)
    - Medium (admissible with conditions)
    - Low (high refusal risk)
    """

    if total_score >= 80:
        return "High"
    elif total_score >= 65:
        return "Medium"
    else:
        return "Low"


# ----------------------------------------------------------
# Process a single candidate profile
# ----------------------------------------------------------

def score_profile(profile_dict):
    """
    Accepts a profile (dict), runs all rule categories,
    returns final scores and readiness band.
    """

    results = run_all_rules(profile_dict)
    total = results["total_score"]
    band = readiness_band(total)

    return {
        "academic_score": results["academic_score"],
        "financial_score": results["financial_score"],
        "documentation_score": results["documentation_score"],
        "credibility_score": results["credibility_score"],
        "overall_score": total,
        "readiness_band": band,
        "explanations": "; ".join(results["reasons"])
    }


# ----------------------------------------------------------
# Load CSV → Score Each Profile → Write Output CSV
# ----------------------------------------------------------

def process_csv(input_path, output_path):
    """
    Loads candidate profiles from CSV, scores each one,
    and saves processed results to a new CSV file.
    """

    with open(input_path, "r", encoding="utf-8-sig") as infile:
        reader = csv.DictReader(infile)
        profiles = list(reader)

    output_rows = []

    for profile in profiles:
        candidate_id = profile.get("profile_id", "UNKNOWN")
        result = score_profile(profile)

        output_rows.append({
            "profile_id": candidate_id,
            "academic_score": result["academic_score"],
            "financial_score": result["financial_score"],
            "documentation_score": result["documentation_score"],
            "credibility_score": result["credibility_score"],
            "overall_score": result["overall_score"],
            "readiness_band": result["readiness_band"],
            "explanations": result["explanations"]
        })

    # Write output CSV
    with open(output_path, "w", newline="", encoding="utf-8") as outfile:
        fieldnames = [
            "profile_id",
            "academic_score",
            "financial_score",
            "documentation_score",
            "credibility_score",
            "overall_score",
            "readiness_band",
            "explanations"
        ]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(output_rows)

    print(f"Processed {len(output_rows)} profiles → saved to {output_path}")


# ----------------------------------------------------------
# Command-line Interface
# ----------------------------------------------------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="NxtAbroad AI Scoring Engine")

    parser.add_argument(
        "--input",
        type=str,
        required=True,
        help="Path to input CSV file containing raw candidate profiles"
    )

    parser.add_argument(
        "--output",
        type=str,
        required=True,
        help="Path to output CSV file for readiness scores"
    )

    args = parser.parse_args()

    process_csv(args.input, args.output)