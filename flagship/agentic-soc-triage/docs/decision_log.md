# Decision Log — Agentic SOC Triage

Purpose: Capture key design decisions and rationale for auditability, maintenance, and review in a state government SOC context.

This log explains *why* certain choices were made, not just *what* was built.

---

## D001 — Analyst-in-the-loop (No Autonomous Response)

Decision: The system will only recommend actions; it will not automatically contain or remediate activity.

Rationale: In a state SOC, automated response can disrupt business operations and requires human approval.

Tradeoffs: Slower response time compared to full automation.

Validation: Verified by ensuring the responder only outputs recommendations and performs no actions.

---

## D002 — Heuristic-first Triage Before LLM Decision Support

**Decision:**  

**Rationale:**  

**Tradeoffs:**  

**Validation:**  

---

## D003 — Soft Alignment to NIST CSF (Conceptual, Not Compliance)

**Decision:**  

**Rationale:**  

**Tradeoffs:**  

**Validation:**  

---

## D004 — Deterministic, Reproducible Outputs

**Decision:**  

**Rationale:**  

**Tradeoffs:**  

**Validation:**  

---

## D005 — Pluggable Enrichment Backends (Mock → Approved Sources)

**Decision:**  

**Rationale:**  

**Tradeoffs:**  

**Validation:**  

---

## D006 — Report Format (JSON-first for Ticketing / Review)

**Decision:**  

**Rationale:**  

**Tradeoffs:**  

**Validation:**  
