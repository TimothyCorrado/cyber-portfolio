# Cybersecurity Portfolio — Timmy Corrado

## Overview
Hands-on cybersecurity portfolio focused on **SOC operations, detection engineering, and security automation**, progressing from foundational labs to a **state-government-focused agentic SOC triage system**.

This repository is intentionally structured to demonstrate:
- Practical SOC analyst and security engineering skills
- Mature system design and automation thinking
- Responsible, reviewable use of AI in security workflows
- Clear separation between learning labs and production-style work

---

## 📌 Start Here (Recommended Order)

### 🔥 Flagship Project
**Agentic SOC Triage** *(Jan 2026 – Present)*  
Agent-based SOC triage pipeline designed to assist analysts with alert ingestion, contextual enrichment, risk scoring, and response recommendations.

**Operational Context:** State government SOC, analyst-driven, compliance-aware automation  
**AI Role:** Decision support (not model training)

**Status:** Actively developed; expanding toward SOAR-style automation

📂 `flagship/agentic-soc-triage/`

---

### 🏛️ State Government SOC Focus

This flagship project is designed to align with **state government SOC and IT security environments**, where priorities include **operational reliability, audit readiness, analyst oversight, and responsible use of automation**.

**Design Emphasis**
- Analyst-in-the-loop decision support
- Clear audit trails and explainable outcomes
- Practical automation that complements existing SOC workflows
- Risk-aware use of AI in operational settings

**AI Usage Model**
- LLMs are used strictly for **decision support and triage assistance**
- No autonomous containment or enforcement actions
- All recommendations are **reviewable and attributable**
- Human analysts retain final authority

**Explicitly Out of Scope**
- Training or fine-tuning language models
- Black-box or self-modifying AI behavior
- Fully autonomous response without analyst approval

---

### 📘 Standards Alignment (Design-Oriented)

This project is **not intended to meet formal compliance or certification requirements**.  
Instead, it is designed to **align conceptually with NIST cybersecurity guidance** commonly adopted by state government SOC and IT security teams.

**NIST Cybersecurity Framework (CSF) – Conceptual Alignment**
- **Identify:** Structured log ingestion and contextual enrichment support visibility into users, systems, and activity
- **Detect:** Risk-based alert classification and triage logic support timely detection of suspicious behavior
- **Respond:** Analyst-reviewed response recommendations align with controlled incident response practices
- **Recover:** Generated reports and artifacts support post-incident review and continuous improvement

This alignment is **design-focused**, demonstrating familiarity with NIST principles **without asserting formal compliance**.

---

## 🧪 SOC & Detection Labs

These projects demonstrate foundational blue-team and SOC analyst skills.

#### 1. Windows Event Monitor Analyzer *(Dec 2025 – Jan 2026)*
- Windows Event Logs and Sysmon analysis
- Log parsing, filtering, and detection logic
- Security-focused interpretation of host-based telemetry

📂 `labs/windows-event-monitor-analyzer/`

---

#### 2. Mini SOC Detection Lab *(Jan 2026)*
- Simulated SOC alert triage workflow
- Alert validation, investigation, and reporting
- SIEM-style thinking using real telemetry

📂 `labs/mini-soc-detection-lab/`

---

#### 3. Small Business Cybersecurity Toolkit *(Jan 2026)*
- Practical security assessment tools for SMB environments
- Checklists, templates, and defensive guidance
- Focus on real-world constraints and actionable outcomes

📂 `labs/small-biz-cybersecurity-toolkit/`

---

## 🔁 Shared Components
Reusable assets used across projects:
- Event schemas and data contracts
- Sanitized sample logs
- Shared utilities and helpers

📂 `shared/`

---

## 🌐 Other Projects (External)
Not part of this monorepo, but relevant:
- **Security+ Study Journal** – exam preparation and notes  
- **Job Tracker** – personal automation project  
- **Crypto** – technical and financial experimentation  

(See GitHub profile for links.)

---

## 📎 Notes
- Labs are preserved for learning and skill signaling
- Flagship project reflects **production-oriented, government-aware design**
- Repository structure mirrors real-world engineering practices

---

> **Portfolio actively maintained (2026).**
