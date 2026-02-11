from agents.parser import parse_event

def test_parse_event_requires_fields():
    bad = {"host": "WIN10", "user": "timmy", "event_type": "process_create"}  # missing timestamp
    try:
        parse_event(bad)
        assert False, "Expected ValueError for missing required fields"
    except ValueError as e:
        assert "Missing required fields" in str(e)

def test_parse_event_normalizes_structure():
    evt = {
        "timestamp": "2026-02-10T14:30:00Z",
        "host": "WIN10-LAB",
        "user": "timmy",
        "event_type": "process_create",
        "process": {"image": "powershell.exe", "command_line": "powershell.exe -enc AAAA"},
        "extra_field": "kept_in_extras",
    }
    out = parse_event(evt)
    assert out["host"] == "WIN10-LAB"
    assert out["process"]["image"] == "powershell.exe"
    assert out["extras"]["extra_field"] == "kept_in_extras"
