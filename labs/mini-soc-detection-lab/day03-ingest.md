# 🛡️ Day 3 – Log Ingestion & Dataset Export  
**Tag:** `@SOC-DAY3-INGEST`  
**Goal:** Export core Windows telemetry (Security + Sysmon) from Splunk into clean CSV datasets for analysis and detection engineering.

---

## 1. Security Log Dataset (4624 / 4625)

- **Source:** Splunk (`index=main`, `sourcetype="WinEventLog:Security"`)
- **Query:**
  ```spl
  index=main sourcetype="WinEventLog:Security" (EventCode=4624 OR EventCode=4625)