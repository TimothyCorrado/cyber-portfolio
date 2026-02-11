# 🛡️ Day 5 – Alert Triage & Investigation  
**Tag:** `@SOC-DAY5-TRIAGE`  
**Alert Type:** Excessive Failed Logons (4625)  
**Date:** 12/06/2025

---

## 🔔 Alert Summary
The brute-force detection triggered for a 5-minute window containing multiple failed logons.

**Alert Details**
- **User:** Tim  
- **Host:** DESKTOP-0VN9UV0  
- **Failures in 5-min window:** 2  
- **Timestamp:** 2025-12-05 17:20:00  

This resembles a *mild authentication anomaly* — not a full brute-force but still potentially worth review.

---

## 🔍 Step 1 — Initial Triage Questions (Tier 1)

| Question | Answer |
|---------|--------|
| *Is the account valid and known?* | Yes — “Tim” is a valid local user. |
| *Are failures happening on a single system?* | Yes — DESKTOP-0VN9UV0 only. |
| *Is this volume unusual for this user?* | Unknown — requires baseline context. |
| *Any successful logons after the failures?* | Not identified yet — analyst must check. |
| *Any suspicious source IPs?* | Not applicable — local logon attempt. |
| *Does the host show other suspicious activity?* | Requires Sysmon correlation. |

---

## 🔎 Step 2 — Enrichment

## 🧠 MITRE ATT&CK Mapping

**Technique:**  
- **T1110 – Brute Force**  
  - **T1110.001 – Password Guessing**  
  - **T1110.003 – Password Spraying**

**Justification:**  
Failed logon attempts (Event ID 4625) occurring in a compressed time window may indicate automated password guessing or spraying. In this case, the volume was low and did not indicate actual malicious behavior, but the technique signature aligns with early brute-force activity patterns.

### ✔ Check for successful logons nearby
```spl
index=main sourcetype="WinEventLog:Security" EventCode=4624 User="Tim"
| sort -_time
```
---

## 📁 Evidence Summary (Day 5)

The following screenshots support the triage workflow and represent the alert, raw events, and enrichment steps performed during analysis.

### 1. `failed_logon_bucket.png`
Shows the triggered brute-force detection result from Splunk, indicating:
- User: Tim  
- Host: DESKTOP-0VN9UV0  
- Failure Count: 2 within a 5-minute window  

This screenshot represents the **alert itself**.

---

### 2. `4625_raw_event.png`
Screenshot of the **raw failed logon (EventCode 4625)** including:
- Failure reason  
- Logon type  
- Security ID  
- Process information  
- Workstation name  

Used to understand the context of the failure and validate the alert.

---

### 3. `4624_enrichment.png`
Results of an enrichment search for **successful logons (EventCode 4624)** tied to the same account.  
This determines whether the failed attempts were followed by a successful login, which could indicate credential compromise.

---

### 4. `sysmon_correlation.png`
Sysmon event review around the alert time window (17:15–17:25).  
Used to identify any correlated process execution or suspicious activity that might support malicious intent.

---

### ✔ Evidence Location
All screenshots are stored under:



