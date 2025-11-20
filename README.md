# NxtAbroad AI – Visa Readiness & Eligibility Intelligence Engine

NxtAbroad AI is a rules-driven intelligence engine for assessing student eligibility, visa readiness, and documentation strength for international study destinations (UK, Canada, Europe, UAE). It standardises how student applications are evaluated and provides consistent, explainable readiness scores used by NxtAbroad advisors.

The system was conceived, architected, and implemented by Ibrahim Akintunde Akinyera (Founder, NxtAbroad Limited). It also serves as a core evidence component for Ibrahim’s UK Global Talent Visa application under the Mandatory Criterion (Founding an Innovative Digital Product).

------------------------------------------------------------
## 1. Why NxtAbroad AI Exists

Traditional student-visa screening processes rely on manual judgement, inconsistent staff decisions, and spreadsheet-based logic. This often results in:

- avoidable visa refusals  
- inconsistent assessments across advisors or offices  
- slow manual analysis  
- weak documentation checks  
- difficulty scaling operations  

NxtAbroad AI addresses these issues by providing:

- a structured decision framework  
- deterministic rules for each evaluation category  
- clear readiness bands (Low, Medium, High)  
- narrative notes for improved advisor transparency  
- a process that is repeatable, auditable, and scalable  

It has been applied to hundreds of student profiles internally and has significantly improved accuracy and speed.

------------------------------------------------------------
## 2. What the Engine Evaluates

The core engine evaluates:

- Academic Eligibility  
  – qualification level  
  – grade/classification  
  – course compatibility  
  – study gaps  

- Financial Readiness  
  – proof of funds (POF) coverage  
  – account stability  
  – sponsor relationships  
  – recent inflow anomalies  

- Documentation Quality  
  – completeness of required documents  
  – quality of uploads  
  – consistency across supporting evidence  

- Immigration Credibility  
  – previous refusals  
  – travel history  
  – alignment of applicant narrative  

- Visa Readiness Score  
  – continuous score (0–100)  
  – mapped to readiness band (Low / Medium / High)  

------------------------------------------------------------
## 3. Repository Structure

nxtabroad-visa-readiness-ml/  
│  
├── data/  
│   └── sample_profiles/            Example input profiles  
│  
├── docs/  
│   └── figures/  
│       ├── architecture.png        System architecture  
│       └── scoring_flow.png        Scoring flow diagram  
│  
├── models/                         Optional saved rule configs or ML prototypes  
│  
├── src/  
│   ├── rules_engine.py             Core business rules  
│   ├── scoring.py                  Aggregated readiness scoring  
│   └── utils.py                    Helper functions  
│  
├── Evidence_1_NxtAbroad_AI_Ibrahim_Akinyera.pdf  
├── TECH_NATION_EVIDENCE.md  
├── requirements.txt  
└── README.md  

------------------------------------------------------------
## 4. Scoring Model Overview

The scoring model works in four stages:

1. **Rule Evaluation**  
   Each dimension (academic, financial, documentation, credibility) is evaluated using deterministic rules in `rules_engine.py`.

2. **Sub-score Calculation**  
   Each category produces a score (0–100).

3. **Weighted Readiness Score**  
   The scoring engine (`scoring.py`) combines the sub-scores into a final readiness score.

4. **Band Classification**  
   Final results fall into three bands:  
   - 0–39: Low readiness  
   - 40–69: Medium readiness  
   - 70–100: High readiness  

These outputs allow NxtAbroad advisors to take informed, consistent decisions.

------------------------------------------------------------
## 5. Running the Engine

### Install dependencies
pip install -r requirements.txt

### Run the core rules engine
python src/rules_engine.py

### Run the readiness scoring engine
python src/scoring.py

You may customise the input profiles by modifying the sample data under:
data/sample_profiles/

------------------------------------------------------------
## 6. Tech Nation Relevance (Mandatory Criterion)

This project demonstrates:

- technical innovation as a founder  
- ability to translate business knowledge into software  
- system architecture and rules design  
- product development leadership  
- evidence of real-world adoption by NxtAbroad staff  
- an automated scoring engine with practical business value  

Included in this repository:

- Evidence_1 PDF  
- architecture and scoring flow diagrams  
- technical narrative (TECH_NATION_EVIDENCE.md)  
- core scoring logic and rule engine source code  

------------------------------------------------------------
## 7. Future Extensions

The current engine is built to support future upgrades:

- API service for multi-location NxtAbroad teams  
- dashboard analytics  
- NLP-driven Personal Statement quality checks  
- ML-based credibility detection  
- multi-country scoring profiles  

------------------------------------------------------------
## 8. Author

Ibrahim Akintunde Akinyera  
Founder – NxtAbroad Limited  
Machine Learning Engineer | Cybersecurity & Risk Analytics  

Portfolio: https://akinyeraakintunde.github.io/Ibrahim-Akinyera  
GitHub: https://github.com/akinyeraakintunde  
LinkedIn: https://linkedin.com/in/ibrahimakinyera  

------------------------------------------------------------
## 9. License

All rights reserved. Property of NxtAbroad Limited.