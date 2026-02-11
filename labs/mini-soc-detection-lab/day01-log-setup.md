# 🛡️ Day 1 – Log Setup & Baseline Configuration  
**Tag:** `@SOC-DAY1-LOGSETUP`  
**Goal:** Establish a clean, SIEM-ready telemetry baseline inside a Windows VM.

This document captures the exact configuration steps and validations required to prepare a Windows system for security monitoring.  
Each step produces auditable evidence and follows real SOC engineering practices.

---

## ⚙️ 1. Security Audit Policy Configuration
Configured Windows auditing to capture authentication, process activity, privilege use, and policy change events.  
Audit categories enabled:

- Logon / Logoff  
- Account Logon  
- Account Management  
- Policy Change  
- Privilege Use  
- Object Access (File System)  
- Detailed Tracking (Process Creation)

**Evidence:**  
- `evidence/day01/audit_policy_export.txt` (exported audit settings)

---

## ⚙️ 2. Sysmon Deployment
Installed Sysmon with a hardened XML configuration to improve process visibility beyond native Windows logs.

Monitored events include:

- Process creation  
- Network connections  
- Driver loading  
- Image load activity  
- Registry modifications  

**Evidence:**  
- `evidence/day01/sysmon_config.xml`  
- Sysmon process creation events (Event ID 1) visible in Event Viewer

---

## ⚙️ 3. PowerShell Logging Configuration
Enabled operational logging to support detection of malicious script activity.

Configured:

- Module Logging  
- Script Block Logging  
- (Optional) Transcription

**Evidence:**  
- `evidence/day01/powershell_logging_status.txt`  
- PowerShell ScriptBlock events (4104) verified in Event Viewer

---

## 🔍 4. Baseline Event Generation
Generated known-good events to confirm logging integrity:

- **4625** – Failed logon attempt  
- **4624** – Successful logon  
- **1** – Sysmon process creation  
- **4104** – PowerShell script execution

These events form the baseline for future detection and anomaly analysis.

**Evidence:**  
- `evidence/day01/event-viewer-baseline.png`

---

## 🧪 5. Validation Summary
✔ All required log sources enabled and producing events  
✔ Audit policy exported  
✔ Sysmon installed and verified  
✔ PowerShell logging operational  
✔ Baseline events captured  
✔ Evidence saved to repo structure  

---

# 🎉 Day 1 Status: Completed  
Windows telemetry sources successfully enabled and validated.  
All required evidence has been collected and stored under `/evidence/day01/`.  
This baseline will be used for Day 2 log parsing, enrichment, and early detection engineering.

---