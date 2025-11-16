import os
import joblib
import numpy as np
import pandas as pd
import streamlit as st


MODEL_PATH = os.path.join("models", "visa_readiness_model.joblib")


@st.cache_resource
def load_model():
    if not os.path.exists(MODEL_PATH):
        return None
    return joblib.load(MODEL_PATH)


def main():
    st.set_page_config(
        page_title="NxtAbroad AI – Visa Readiness Scoring",
        page_icon="🛫",
        layout="centered"
    )

    st.title("NxtAbroad AI – Visa Readiness Engine")
    st.write(
        "Enter applicant details below to get a **visa readiness prediction** "
        "and key risk level (High / Medium / Ready)."
    )

    model = load_model()
    if model is None:
        st.error(
            "No trained model found. Please run `python src/train_model.py` "
            "to create `models/visa_readiness_model.joblib`."
        )
        st.stop()

    st.header("Applicant Profile")

    # --- Input widgets (aligned with the dataset schema) --- #

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", min_value=16, max_value=60, value=24)

        country_of_citizenship = st.selectbox(
            "Country of Citizenship",
            ["Nigeria", "Ghana", "Kenya", "India", "Pakistan"]
        )

        country_of_residence = st.selectbox(
            "Country of Residence",
            ["Nigeria", "Ghana", "Kenya", "India", "Pakistan", "UK", "UAE", "Other"],
            index=0
        )

        target_country = st.selectbox(
            "Target Study Country",
            ["UK", "Canada", "Ireland"]
        )

        education_level_applied = st.selectbox(
            "Education Level Applied For",
            ["Bachelors", "Masters", "Top-up", "Diploma"]
        )

        course_area = st.selectbox(
            "Course Area",
            ["Business", "IT", "Health", "Engineering", "Social Sciences"]
        )

        tuition_fee_total_gbp = st.number_input(
            "Total Tuition Fee (GBP equivalent)",
            min_value=5000.0,
            max_value=40000.0,
            value=18000.0,
            step=500.0
        )

    with col2:
        tuition_deposit_paid_gbp = st.number_input(
            "Tuition Deposit Already Paid (GBP)",
            min_value=0.0,
            max_value=40000.0,
            value=4000.0,
            step=500.0
        )

        proof_of_funds_gbp = st.number_input(
            "Proof of Funds Available (GBP)",
            min_value=0.0,
            max_value=80000.0,
            value=28000.0,
            step=500.0
        )

        funds_held_days = st.number_input(
            "Number of Days Funds Have Been Held",
            min_value=0,
            max_value=365,
            value=30
        )

        has_sponsor = st.selectbox(
            "Does the Applicant Have a Sponsor?",
            ["Yes", "No"]
        )
        has_sponsor_bin = 1 if has_sponsor == "Yes" else 0

        sponsor_type = "Self"
        if has_sponsor_bin == 1:
            sponsor_type = st.selectbox(
                "Sponsor Type",
                ["Parent", "Sibling", "Spouse", "Self", "Other"]
            )

        num_previous_visa_refusals = st.number_input(
            "Number of Previous Visa Refusals",
            min_value=0,
            max_value=5,
            value=0
        )

        previous_study_visa_history = st.selectbox(
            "Previous Successful Study Visa History",
            ["None", "UK", "Canada", "Schengen", "Multiple"]
        )

    st.subheader("Employment & Education Background")

    col3, col4 = st.columns(2)

    with col3:
        employment_status = st.selectbox(
            "Current Employment Status",
            ["Employed", "Self-employed", "Unemployed"]
        )

        employment_duration_months = st.number_input(
            "Duration in Current Job/Business (months)",
            min_value=0,
            max_value=240,
            value=12
        )

    with col4:
        study_gap_years = st.number_input(
            "Study Gap (years since last formal education)",
            min_value=0.0,
            max_value=20.0,
            value=1.0,
            step=0.5
        )

        ielts_overall_score = st.number_input(
            "IELTS (or equivalent) Overall Score",
            min_value=0.0,
            max_value=9.0,
            value=6.5,
            step=0.5
        )
        ielts_each_band_ok = 1 if ielts_overall_score >= 6.0 else 0

    st.subheader("Documentation & Risk Perception")

    col5, col6 = st.columns(2)

    with col5:
        course_alignment_score = st.slider(
            "Course Alignment with Background (1 = poor, 5 = excellent)",
            min_value=1, max_value=5, value=4
        )

        financial_document_quality = st.slider(
            "Financial Document Quality (1 = poor, 5 = excellent)",
            min_value=1, max_value=5, value=4
        )

    with col6:
        documentation_completeness = st.slider(
            "Documentation Completeness (4–10)",
            min_value=4, max_value=10, value=8
        )

        country_risk_level = st.slider(
            "Country Risk Level (1 = low risk, 5 = high risk)",
            min_value=1, max_value=5, value=3
        )

    consultant_manual_flag = st.checkbox(
        "Consultant sees unusual / complex risk (manual flag)",
        value=False
    )
    consultant_manual_flag_bin = 1 if consultant_manual_flag else 0

    # --- Prediction --- #
    if st.button("Predict Visa Readiness"):
        # Build a single-row DataFrame that matches training features
        input_data = {
            "age": [age],
            "country_of_citizenship": [country_of_citizenship],
            "country_of_residence": [country_of_residence],
            "target_country": [target_country],
            "education_level_applied": [education_level_applied],
            "course_area": [course_area],
            "tuition_fee_total_gbp": [tuition_fee_total_gbp],
            "tuition_deposit_paid_gbp": [tuition_deposit_paid_gbp],
            "proof_of_funds_gbp": [proof_of_funds_gbp],
            "funds_held_days": [funds_held_days],
            "has_sponsor": [has_sponsor_bin],
            "sponsor_type": [sponsor_type],
            "num_previous_visa_refusals": [num_previous_visa_refusals],
            "previous_study_visa_history": [previous_study_visa_history],
            "employment_status": [employment_status],
            "employment_duration_months": [employment_duration_months],
            "study_gap_years": [study_gap_years],
            "ielts_overall_score": [ielts_overall_score],
            "ielts_each_band_ok": [ielts_each_band_ok],
            "course_alignment_score": [course_alignment_score],
            "financial_document_quality": [financial_document_quality],
            "documentation_completeness": [documentation_completeness],
            "country_risk_level": [country_risk_level],
            "consultant_manual_flag": [consultant_manual_flag_bin],
        }

        input_df = pd.DataFrame(input_data)

        # Predict class and probabilities
        pred_class = model.predict(input_df)[0]

        # Some models may not support predict_proba; handle safely
        try:
            proba = model.predict_proba(input_df)[0]
        except Exception:
            proba = None

        class_mapping = {
            0: "High Risk",
            1: "Medium Risk",
            2: "Ready"
        }
        class_description = class_mapping.get(pred_class, "Unknown")

        st.markdown("---")
        st.subheader("Prediction Result")

        if pred_class == 2:
            st.success(f"Visa Readiness: **{class_description} (Class {pred_class})**")
        elif pred_class == 1:
            st.warning(f"Visa Readiness: **{class_description} (Class {pred_class})**")
        else:
            st.error(f"Visa Readiness: **{class_description} (Class {pred_class})**")

        if proba is not None:
            st.write("Class Probabilities:")
            prob_df = pd.DataFrame(
                proba.reshape(1, -1),
                columns=["High Risk (0)", "Medium Risk (1)", "Ready (2)"]
            )
            st.dataframe(prob_df.style.format("{:.2f}"))

        st.markdown("### Quick Interpretation")
        if pred_class == 0:
            st.write(
                "- The application currently appears **high risk**.\n"
                "- Check **funds amount and duration**, **study gap**, **visa history**, and **document quality** carefully.\n"
                "- You may need to **delay submission**, increase funds, or strengthen documentation."
            )
        elif pred_class == 1:
            st.write(
                "- The application is **medium risk**.\n"
                "- With stronger documents, clearer explanations and improved alignment, it may become ready.\n"
                "- Focus on **proof of funds**, **sponsor evidence**, and **course justification**."
            )
        else:
            st.write(
                "- The application appears **strong and ready** based on the current inputs.\n"
                "- Still ensure that all documents match official visa requirements and are up to date."
            )


if __name__ == "__main__":
    main()
