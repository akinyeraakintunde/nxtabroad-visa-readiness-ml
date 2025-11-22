# System Architecture

The NxtAbroad AI engine is composed of:

- **Rules Engine** – Encodes visa and admission logic.
- **Scorer** – Aggregates scores and assigns readiness bands.
- **FastAPI Layer** – Exposes the scoring engine as `/predict`.
- **Client SDK** – Python API client for integration.

See also: `docs/figures/architecture.png` and `docs/figures/scoring_flow.png`.