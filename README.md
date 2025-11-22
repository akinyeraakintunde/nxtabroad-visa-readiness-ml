# NxtAbroad AI – Visa Readiness & Eligibility Intelligence Engine

Evidence 1 – UK Global Talent Visa (Mandatory Criterion – Innovation)

NxtAbroad AI is an intelligent rules-driven scoring engine designed to evaluate student eligibility, documentation quality, and visa readiness for international study routes including the United Kingdom, Canada, Europe, and the UAE.

The system was fully conceived, architected, and engineered by Ibrahim Akintunde Akinyera, Founder of NxtAbroad Limited (UK–Nigeria). It is actively used as a core decision-support tool inside NxtAbroad’s education and immigration advisory operations.

-------------------------------------------------------------

## 1. Project Overview

Traditional student-recruitment and visa counselling processes are highly manual, inconsistent, and difficult to scale. Advisors interpret complex immigration rules differently, documentation checks vary across offices, and students receive conflicting opinions about their chances of success.

NxtAbroad AI addresses this by converting visa policies, institutional admission rules, and internal risk guidelines into a transparent, repeatable scoring framework. The engine:

- Analyses academic history, English language proficiency, program fit, and destination preferences
- Evaluates financial strength and proof-of-funds against country-specific rules
- Assesses risk indicators (previous refusals, documentation gaps, complex profiles)
- Produces a Visa Readiness Score (Low / Medium / High) with clear explanations

This repository captures the core scoring engine, supporting scripts, diagrams, and Tech Nation evidence documents.

-------------------------------------------------------------

## 2. Key Features

- Rules-Driven Visa Readiness Engine  
  Encodes admission and visa policies into modular Python rules for different destinations and study levels.

- Transparent Scoring & Explanations  
  Outputs a readiness band plus structured reasons (e.g., “Funds below UKVI minimum”, “High academic alignment with target programme”).

- Multi-Country Support  
  Designed for UK, Canada, Europe, and UAE routes with configurable rule sets.

- Operational Focus  
  Tested with real-world cases at NxtAbroad Limited, ensuring practical alignment with advisor workflows.

- Evidence-Ready Documentation  
  Includes Tech Nation evidence write-up, architecture diagrams, and synthetic sample profiles.

-------------------------------------------------------------

## 3. System Architecture

High-level architecture of NxtAbroad AI:

Sample Leads (CSV / Form / CRM)
        |
        v
+-----------------------+
|   NxtAbroad AI Core   |
|                       |
|  +-----------------+  |
|  |  Rules Engine   |  |
|  +-----------------+  |
|  |  Lead Scorer    |  |
|  +-----------------+  |
+-----------------------+
        |
        v
Readiness Report (Low / Medium / High)

Scoring Flow (see docs/figures/scoring_flow.png):

1. Load candidate profile(s)
2. Apply academic rules
3. Apply financial rules
4. Apply risk rules
5. Combine into readiness score + explanations

-------------------------------------------------------------

## 4. Repository Structure

nxtabroad-visa-readiness-ml/
├── data/
│   └── raw/
│       └── sample_profiles.csv                # Synthetic visa-style inputs
│
├── docs/
│   └── figures/
│       ├── architecture.png                   # System architecture diagram
│       └── scoring_flow.png                   # Rule and scoring flow diagram
│
├── src/
│   ├── rules_engine.py                        # Core rule logic
│   ├── scorer.py                               # Aggregates rule outputs
│   └── utils.py                                # Helper functions (validation, I/O)
│
├── models/                                     # Reserved for future ML models
│
├── README.md                                   # This file
├── TECH_NATION_EVIDENCE.md                     # Tech Nation narrative document
├── requirements.txt                            # Python dependencies
└── LICENSE                                     # MIT License

-------------------------------------------------------------

## 5. Quickstart

### Environment Setup

git clone https://github.com/akinyeraakintunde/nxtabroad-visa-readiness-ml.git
cd nxtabroad-visa-readiness-ml

python -m venv venv
source venv/bin/activate           # Windows: venv\Scripts\activate

pip install -r requirements.txt

### Run Sample Scoring

python src/scorer.py \
    --input data/raw/sample_profiles.csv \
    --output data/processed/readiness_report.csv

This will:

1. Load sample profiles  
2. Apply academic, financial, and risk rules  
3. Produce readiness bands (Low / Medium / High)  
4. Export a CSV with scores + explanations

-------------------------------------------------------------

## 6. Rules & Scoring Logic

Academic Rules:
- Validates degree level vs. programme
- Checks grade band and study gap
- Flags weak academic alignment

Financial Rules:
- Verifies funds vs. minimum thresholds
- Validates 28/30/90-day savings windows
- Flags marginal or unstable finances

Risk & Compliance Rules:
- Checks previous refusals
- Assesses sponsor legitimacy
- Evaluates intent and career alignment

Each rule returns a numeric score + explanations.  
Final Visa Readiness Score = weighted aggregate of all rules.

-------------------------------------------------------------

## 7. Example Output

Example from readiness_report.csv:

candidate_id,route,country,readiness_score,readiness_band,explanations  
ABR001,Postgraduate,UK,0.82,High,"Strong academic fit; Funds above UKVI minimum; No previous refusals"  
NXT014,Undergraduate,Canada,0.46,Medium,"Acceptable grades but marginal funds; Recommend improving proof-of-funds"  
NXT021,Postgraduate,UK,0.23,Low,"Previous refusal; Insufficient savings history; High overall risk"

-------------------------------------------------------------

## 8. How This Supports the UK Global Talent Visa

This project is submitted as Evidence 1 (Mandatory Criterion – Innovation) and demonstrates:

- Founder-led innovation  
- Technical depth in designing a rule-based scoring engine  
- Real operational impact inside NxtAbroad Limited  
- Clear documentation, diagrams, and sample data  
- Strong practical understanding of visa rules and digital transformation

See:

- TECH_NATION_EVIDENCE.md  
- Evidence_1_NxtAbroad_AI_Ibrahim_Akinyera.pdf

-------------------------------------------------------------

## 9. Future Roadmap

- Add a web dashboard for advisors  
- Integrate ML-based risk prediction  
- Expand to more countries and rule sets  
- Convert into a FastAPI scoring service  

-------------------------------------------------------------

## 10. License and Contact

MIT License (demonstration use only; operational versions remain proprietary to NxtAbroad Limited).

Author: Ibrahim Akintunde Akinyera  
Company: NxtAbroad Limited (UK–Nigeria)  
GitHub: https://github.com/akinyeraakintunde  
Portfolio: https://akinyeraakintunde.github.io/Ibrahim-Akinyera/