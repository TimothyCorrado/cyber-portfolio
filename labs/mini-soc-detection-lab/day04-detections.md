# 🛡️ Day 4 – Detection Engineering  
**Tag:** `@SOC-DAY4-DETECTIONS`  
**Date Completed:** 12/06/2025

---

## 🎯 Objective

The focus of Day 4 was transforming collected telemetry (Windows Security + Sysmon) into **actionable detections** using Splunk SPL. These detections form the foundational capability of a SOC: identifying authentication anomalies and malicious process execution patterns.

Deliverables for today include:
- Two authentication detections  
- Two Sysmon-based detections  
- Documented SPL logic  
- Screenshots + evidence  
- Prepared LOLBins detection for future simulation  

---

# ----------------------------------------
# 🔍 1. Authentication Detection – Excessive Failed Logons (Brute Force)

Detects multiple failed authentication attempts within a 5-minute window.

### SPL Detection Logic
```spl
index=main sourcetype="WinEventLog:Security" EventCode=4625
| eval User = coalesce(AccountName, Account_Name, TargetUserName, SubjectUserName)
| bin _time span=5m
| stats count by _time, User, host
| where count >= 5
| sort -count