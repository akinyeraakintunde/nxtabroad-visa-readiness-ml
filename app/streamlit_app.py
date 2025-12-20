import streamlit as st
from backend.decision_engine import ApplicantProfile, assess_readiness

st.set_page_config(page_title="NxtAbroad AI – Visa Readiness Demo", page_icon="🧭")

st.title("🧭 NxtAbroad AI – Visa Readiness Agent (Demo)")
st.write("Enter a profile and get an explainable readiness score (rules-first).")

with st.form("visa_form"):
    highest_qualification = st.selectbox(
        "Highest Qualification",
        ["MSc", "BSc", "HND", "Diploma", "Other"]
    )
    destination_country = st.selectbox(
        "Destination Country",
        ["UK", "Canada", "Ireland", "Other"]
    )
    available_funds_gbp = st.number_input(
        "Available Funds (GBP)",
        min_value=0.0, value=12000.0, step=500.0
    )
    work_experience_years = st.number_input(
        "Work Experience (Years)",
        min_value=0.0, value=4.0, step=0.5
    )
    english_test_done = st.checkbox("English test completed (IELTS/approved)", value=True)

    submitted = st.form_submit_button("Assess Readiness")

if submitted:
    profile = ApplicantProfile(
        highest_qualification=highest_qualification,
        destination_country=destination_country,
        available_funds_gbp=float(available_funds_gbp),
        work_experience_years=float(work_experience_years),
        english_test_done=bool(english_test_done),
    )

    result = assess_readiness(profile)

    st.subheader("Result")
    st.metric("Readiness Score", f"{result['readiness_score']}/100")
    st.write("**Risk Level:**", result["risk_level"])

    st.subheader("Key Reasons")
    for r in result["key_reasons"]:
        st.write("•", r)

    st.subheader("Recommendations")
    if result["recommendations"]:
        for rec in result["recommendations"]:
            st.write("•", rec)
    else:
        st.write("No major recommendations. Maintain documentation quality and timelines.")

    with st.expander("Show inputs used"):
        st.json(result["inputs_used"])