from fastapi.responses import HTMLResponse
from fastapi import APIRouter

router = APIRouter()

HTML = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>NxtAbroad AI Demo</title>
  <style>
    body { font-family: Arial, sans-serif; max-width: 800px; margin: 30px auto; padding: 0 16px; }
    .card { padding: 16px; border: 1px solid #ddd; border-radius: 10px; margin-bottom: 16px; }
    label { display: block; margin: 10px 0 6px; font-weight: 600; }
    input, select { width: 100%; padding: 10px; border-radius: 8px; border: 1px solid #ccc; }
    button { margin-top: 14px; padding: 12px 14px; border: none; border-radius: 8px; cursor: pointer; }
    pre { background: #0b0b0b; color: #eaeaea; padding: 12px; border-radius: 10px; overflow: auto; }
    .row { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
    @media (max-width: 600px) { .row { grid-template-columns: 1fr; } }
  </style>
</head>
<body>
  <h1>NxtAbroad AI — Visa Readiness Agent (Demo)</h1>
  <p>This is a lightweight demo UI on top of the FastAPI scoring endpoint.</p>

  <div class="card">
    <div class="row">
      <div>
        <label>Highest Qualification</label>
        <select id="highest_qualification">
          <option>BSc</option>
          <option selected>MSc</option>
          <option>PhD</option>
        </select>
      </div>
      <div>
        <label>Destination Country</label>
        <select id="destination_country">
          <option selected>UK</option>
          <option>Canada</option>
          <option>USA</option>
          <option>Germany</option>
        </select>
      </div>
    </div>

    <div class="row">
      <div>
        <label>Available Funds (GBP)</label>
        <input id="available_funds_gbp" type="number" value="12000" />
      </div>
      <div>
        <label>Work Experience (Years)</label>
        <input id="work_experience_years" type="number" value="4" />
      </div>
    </div>

    <label>English Test Done?</label>
    <select id="english_test_done">
      <option value="false" selected>No</option>
      <option value="true">Yes</option>
    </select>

    <button onclick="runAssess()">Run Assessment</button>
  </div>

  <div class="card">
    <h3>Result</h3>
    <pre id="result">{}</pre>
  </div>

  <p>
    API Docs: <a href="/docs">/docs</a> • Health: <a href="/health">/health</a>
  </p>

  <script>
    async function runAssess() {
      const payload = {
        highest_qualification: document.getElementById("highest_qualification").value,
        destination_country: document.getElementById("destination_country").value,
        available_funds_gbp: Number(document.getElementById("available_funds_gbp").value),
        work_experience_years: Number(document.getElementById("work_experience_years").value),
        english_test_done: document.getElementById("english_test_done").value === "true"
      };

      document.getElementById("result").textContent = "Running...";

      const res = await fetch("/assess", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      });

      const data = await res.json();
      document.getElementById("result").textContent = JSON.stringify(data, null, 2);
    }
  </script>
</body>
</html>
"""

@router.get("/demo", response_class=HTMLResponse)
def demo():
    return HTML