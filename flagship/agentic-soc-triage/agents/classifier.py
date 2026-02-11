from __future__ import annotations

from typing import Any, Dict


def classify_event(enriched: Dict[str, Any]) -> Dict[str, Any]:
    """
    Purpose: Produce an evidence-backed risk score for SOC triage.
    Note: Day-1 uses transparent heuristics; LLM decision-support can be added later.
    """
    h = enriched.get("enrichment", {}).get("heuristics", {})
    ip_rep = enriched.get("enrichment", {}).get("ip_reputation", {})
    score = 0
    reasons = []

    if ip_rep.get("reputation") == "suspicious":
        score += 25
        reasons.append("Destination IP reputation flagged suspicious (mock)")

    if h.get("has_encoded_command"):
        score += 40
        reasons.append("PowerShell encoded command observed")

    if h.get("has_hidden_window"):
        score += 20
        reasons.append("Hidden window execution flag observed")

    # Simple label bands
    if score >= 70:
        label = "Malicious"
    elif score >= 35:
        label = "Suspicious"
    else:
        label = "Benign"

    return {"label": label, "risk_score": score, "reasons": reasons}
