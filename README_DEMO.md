# NxtAbroad AI – Visa Readiness Agent (Demo)

This repository contains a **rules-first, explainable AI agent** designed to assess student visa readiness.
It demonstrates how an enterprise-style AI agent can validate inputs, apply decision logic, orchestrate checks,
and return clear, auditable outcomes.

This demo is intentionally built without black-box ML to prioritise **clarity, governance, and explainability**.
The architecture is ML-ready and mirrors Copilot-style agent patterns.

---

## What This Demo Does

The NxtAbroad AI agent:
- Accepts structured applicant inputs
- Applies rule-based decision logic
- Produces a readiness score (0–100)
- Assigns a risk level (Low / Medium / High)
- Explains *why* the decision was made
- Provides next-step recommendations

This is designed as a **decision-support agent**, not an autonomous system.

---

## Architecture Overview
User Input (Web Form)
↓
Input Validation
↓
Decision Engine (Rules-first)
↓
Orchestration Logic
↓
Explainable Output
---

## Tech Stack

- **Backend:** Python, FastAPI
- **UI:** Streamlit
- **Logic:** Rules-first decision engine (ML-ready)
- **Deployment:** Local or cloud (Render / Railway)

---

## How to Run Locally

### 1) Install dependencies

pip install -r requirements.txt

___
## 2) Run the API 

uvicorn backend.main:app --reload

API endpoints:
	•	Health check: http://127.0.0.1:8000/health
	•	API docs: http://127.0.0.1:8000/docs

## 3) Run the Streamlit UI
streamlit run app/streamlit_app.py

Why Rules-First?

This approach ensures:
	•	Deterministic behaviour
	•	Explainable decisions
	•	Reduced hallucination risk
	•	Enterprise and compliance suitability

Machine learning models can be introduced later as supporting signals, not opaque decision-makers.

Intended Use

This demo is built for:
	•	Recruiter demos
	•	Technical interviews
	•	Architecture discussions
	•	Agent / Copilot-style system explanations

It is not a production immigration advisory system.

Author

Ibrahim Akintunde Akinyera
AI / ML Engineer · Agent Engineer · Cybersecurity & Risk Engineering
GitHub: https://github.com/akinyeraakintunde

---

### ✅ After this
Once you paste and commit this file, reply **DONE**.

Next we will:
➡️ **Deploy it live (Step 7)**  
➡️ Get you a **real URL recruiters can click**  
➡️ Add a **“Live Demo” badge to your GitHub**

You’re doing very well — this is now a **real agent**, not theory.