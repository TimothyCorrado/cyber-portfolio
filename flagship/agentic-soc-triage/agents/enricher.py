from __future__ import annotations

from typing import Any, Dict


def enrich_event(parsed: Dict[str, Any]) -> Dict[str, Any]:
    """
    Purpose: Add context (mocked Day-1) to support analyst decision-making.
    State/Gov-friendly: Enrichment is deterministic and reviewable.
    """
    dst_ip = (parsed.get("network") or {}).get("dst_ip")
    cmd = (parsed.get("process") or {}).get("command_line", "")

    # Mock reputation and heuristics (replace with real sources in Phase 2)
    rep = {"dst_ip": dst_ip, "reputation": "unknown", "source": "mock"}
    if dst_ip and dst_ip.startswith("185."):
        rep["reputation"] = "suspicious"

    heuristics = {
        "has_encoded_command": (" -enc " in cmd.lower()) or (" -encodedcommand " in cmd.lower()),
        "has_hidden_window": ("-w hidden" in cmd.lower()) or ("-windowstyle hidden" in cmd.lower()),
    }

    enriched = dict(parsed)
    enriched["enrichment"] = {"ip_reputation": rep, "heuristics": heuristics}
    return enriched
