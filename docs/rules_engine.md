# Rules Engine

The rules engine is implemented in `src/rules_engine.py` and includes:

- Academic rules  
- Financial rules  
- Documentation rules  
- Credibility rules  

Each rule returns a numeric contribution and human-readable reasons. The sum of all rule categories becomes the final readiness score.