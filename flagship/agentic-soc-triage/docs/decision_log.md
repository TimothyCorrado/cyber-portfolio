# Decision Log — Agentic SOC Triage

Purpose: Capture key design decisions and rationale for auditability, maintenance, and review in a state government SOC context.

This log explains *why* certain choices were made, not just *what* was built.

---

## D001 — Analyst-in-the-loop (No Autonomous Response)

**Decision:**  
The system will generate triage findings and response recommendations but will not take autonomous containment or remediation actions.

**Rationale:**  
State government SOC environments require human approval for actions that could disrupt operations or impact users. Analyst oversight ensures accountability and reduces operational risk.

**Tradeoffs:**  
Response actions may take longer compared to fully automated systems.

**Validation:**  
Confirmed by reviewing the responder agent, which outputs recommendations only and performs no direct actions.


---

## D002 — Heuristic-first Triage Before LLM Decision Support

**Decision:**  
Initial triage is performed using transparent heuristic logic before introducing any LLM-based decision support.

**Rationale:**  
Heuristic rules provide predictable, explainable results that are easier to validate and audit in a state SOC environment. LLMs are reserved for higher-level reasoning rather than primary detection.

**Tradeoffs:**  
Heuristic approaches may miss subtle patterns that more advanced models could identify.

**Validation:**  
Verified by reviewing the classifier logic, which bases risk scoring on explicit signals before any AI-assisted reasoning is added.


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
