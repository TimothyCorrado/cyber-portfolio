from __future__ import annotations

import json
from pathlib import Path
from datetime import datetime, timezone
from typing import Any, Dict

from agents.parser import parse_event
from agents.enricher import enrich_event
from agents.classifier import classify_event
from agents.responder import recommend_response


ROOT = Path(__file__).resolve().parents[1]
SAMPLE = ROOT / "data" / "sample_logs" / "sample.json"
REPORTS = ROOT / "reports"


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main() -> int:
    REPORTS.mkdir(parents=True, exist_ok=True)

    raw: Dict[str, Any] = json.loads(SAMPLE.read_text(encoding="utf-8-sig"))
    parsed = parse_event(raw)
    enriched = enrich_event(parsed)
    verdict = classify_event(enriched)
    response = recommend_response(enriched, verdict)

    out = {
        "generated_at": utc_now_iso(),
        "input": raw,
        "parsed": parsed,
        "enriched": enriched,
        "verdict": verdict,
        "recommended_response": response,
    }

    report_path = REPORTS / f"triage_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    report_path.write_text(json.dumps(out, indent=2), encoding="utf-8-sig")

    print(f"[OK] Wrote report: {report_path}")
    print(f"[OK] Verdict: {verdict['label']} (risk={verdict['risk_score']})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

