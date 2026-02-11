# Agentic SOC Triage

## Overview
Agent-based SOC triage pipeline designed to **assist security analysts** with alert ingestion, contextual enrichment, risk scoring, and response recommendations.

This project emphasizes **responsible, reviewable automation** suitable for **state government SOC environments**, where analyst oversight, auditability, and operational trust are critical.

---

## Operational Context
- **Environment:** State government SOC
- **Design Model:** Analyst-in-the-loop
- **Automation Role:** Decision support only (no autonomous response)
- **Status:** Active development (2026)

---

## What This Project Demonstrates
- Practical SOC workflow automation (parse → enrich → triage → recommend)
- Clear separation of responsibilities via agent design
- Risk-based decision support with explainable output
- Government-aware design (oversight, audit readiness, clarity)

---

## Architecture (Day-1 MVP)

```text
Log Input
   ↓
Parser Agent
   ↓
Enrichment Agent
   ↓
Classification Agent
   ↓
Response Recommendation Agent
   ↓
SOC Triage Report (JSON)
