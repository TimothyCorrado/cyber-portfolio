from agents.classifier import classify_event

def test_classifier_flags_encoded_powershell_as_suspicious_or_worse():
    enriched = {
        "timestamp": "2026-02-10T14:30:00Z",
        "host": "WIN10-LAB",
        "user": "timmy",
        "event_type": "process_create",
        "process": {"command_line": "powershell.exe -nop -w hidden -enc AAAA"},
        "network": {"dst_ip": "185.199.108.153"},
        "enrichment": {
            "ip_reputation": {"dst_ip": "185.199.108.153", "reputation": "suspicious", "source": "mock"},
            "heuristics": {"has_encoded_command": True, "has_hidden_window": True},
        },
    }
    verdict = classify_event(enriched)
    assert verdict["risk_score"] >= 35
    assert verdict["label"] in ("Suspicious", "Malicious")
    assert any("encoded" in r.lower() for r in verdict["reasons"])
