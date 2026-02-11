from __future__ import annotations

from typing import Any, Dict, List


def recommend_response(enriched: Dict[str, Any], verdict: Dict[str, Any]) -> Dict[str, Any]:
    """
    Purpose: Provide analyst-reviewed response recommendations (no autonomous action).
    """
    actions: List[str] = []
    mitre: List[Dict[str, str]] = []

    if verdict["label"] in ("Suspicious", "Malicious"):
        actions.extend(
            [
                "Create/Update case and attach generated report (JSON) as evidence",
                "Validate parent/child process lineage and confirm execution context",
                "Check if the user account shows additional anomalous activity in the same time window",
                "Collect triage artifacts (process list, autoruns, recent PowerShell history if available)",
            ]
        )
        mitre.append({"technique": "T1059.001", "name": "Command and Scripting Interpreter: PowerShell"})

    if verdict["label"] == "Malicious":
        actions.extend(
            [
                "Escalate to incident response per SOP for potential malicious PowerShell activity",
                "Consider isolating host via approved tooling after analyst approval",
            ]
        )

    return {
        "analyst_note": "Recommendations are decision support only; analyst approval required for any containment.",
        "actions": actions,
        "mitre_attack": mitre,
    }
