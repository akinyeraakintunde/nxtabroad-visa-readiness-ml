from fastapi import FastAPI

app = FastAPI(
    title="NxtAbroad AI API",
    version="0.1.0",
    description="API layer for NxtAbroad AI Visa Readiness & Eligibility Engine",
)

@app.get("/health")
def health():
    return {"status": "ok", "service": "nxtabroad-ai-api"}