from __future__ import annotations

from typing import Any, Dict


REQUIRED_TOP_LEVEL = ("timestamp", "host", "user", "event_type")


def parse_event(evt: Dict[str, Any]) -> Dict[str, Any]:
    """
    Purpose: Normalize and validate incoming telemetry for repeatable SOC triage.
    Note: This is a minimal Day-1 parser; schema can be hardened over time.
    """
    missing = [k for k in REQUIRED_TOP_LEVEL if k not in evt]
    if missing:
        raise ValueError(f"Missing required fields: {missing}")

    # Normalization: keep only expected sections + passthrough others under 'extras'
    parsed = {
        "timestamp": evt["timestamp"],
        "host": evt["host"],
        "user": evt["user"],
        "event_type": evt["event_type"],
        "process": evt.get("process", {}),
        "network": evt.get("network", {}),
        "extras": {k: v for k, v in evt.items() if k not in (*REQUIRED_TOP_LEVEL, "process", "network")},
    }
    return parsed
