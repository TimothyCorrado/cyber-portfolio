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
The project aligns conceptually with NIST CSF functions without claiming formal compliance.

**Rationale:**  
State SOC teams commonly use NIST CSF as a mental model for operations, but personal projects should avoid compliance claims that imply audit or certification.

**Tradeoffs:**  
The project does not map to specific control IDs or provide compliance evidence.

**Validation:**  
Confirmed by reviewing documentation language to ensure it uses “aligns with” rather than “complies with.”

---

## D004 — Deterministic, Reproducible Outputs

**Decision:**  
The pipeline produces deterministic outputs for the same input data.

**Rationale:**  
Deterministic behavior supports analyst trust, repeatable investigations, and audit review in state SOC environments.

**Tradeoffs:**  
Reduced flexibility compared to non-deterministic or adaptive systems.

**Validation:**  
Validated by re-running the pipeline on identical sample data and confirming consistent results.


---

## D005 — Pluggable Enrichment Backends (Mock → Approved Sources)

**Decision:**  
Enrichment logic is designed to support pluggable backends, starting with mocked data sources.

**Rationale:**  
State environments often restrict outbound access and require approved vendors; mocking allows development without violating constraints.

**Tradeoffs:**  
Mocked enrichment limits realism until approved sources are integrated.

**Validation:**  
Validated by isolating enrichment logic in a dedicated agent that can be replaced without changing the pipeline.


---

## D006 — Report Format (JSON-first for Ticketing / Review)

**Decision:**  
The system outputs triage results in a JSON-first report format.

**Rationale:**  
JSON integrates cleanly with ticketing systems, case management tools, and audit workflows common in state SOCs.

**Tradeoffs:**  
Human readability is reduced compared to narrative-only reports.

**Validation:**  
Validated by generating sample reports and confirming fields are suitable for downstream consumption.

