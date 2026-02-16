# Structural Integrity & Sequential Governance Protocol

**Protocol Version**: 2.0 (The "Traffic Cop" Revision)
**Date**: 2026-02-16
**Author**: Jerome Davis / Antigravity
**Enforced By**: Scrum Master (Phase Authority), Program Analyst (Compliance Author)

## 1. The Core Shift: Authority vs. Authoring

To prevent "Phase Skipping" and ensure "Go/No-Go" decisions are evidence-based, this workspace operates on a strict separation of powers:

| Role | Authority / Mandate |
| :--- | :--- |
| **Human Director (PM/PO)** | Product Owner. The ultimate authority on "What" and "Why." Signs off on Phase Gates. |
| **Scrum Master (Traffic Cop)** | **The Gatekeeper.** Holds the physical power to block all building until both Product Discovery and Compliance Documentation are finalized. |
| **Program Analyst (Author)** | **The Historian.** Responsible for translating the technical extraction into the formalized CPMAI/ISO governance artifacts. |
| **Specialists (Intel Sources)** | Responsible for "Knowledge Deposition." They must document every nuance in the shared Hub before a task is "Done." |

---

## 2. The Shared Discovery Hub (`/docs`)

All agents MUST treat the root-level `/docs` folder as the primary "Truth Depot." No knowledge stays in an agent's session; it must be materialized here.

```text
/docs/
├── interviews/       # RAW specialist interview summaries with the PM/PO.
├── product/          # The Master PRD (BAs) and Feature Roadmaps.
├── architecture/     # ADRs, DB Schemas, and API Contract Specs.
├── design/           # UX flows, Style Guides, and Design System tokens.
├── qa/               # Test strategies, edge-case logs, and validation plans.
└── verification/     # MANDATORY verification artifacts for EVERY task.
```

---

## 3. The "No Document, No Decision" Rule

The Scrum Master is forbidden from presenting a phase for "Human Review" if any of the following are missing:

1. **The Synthesis**: The PRD and technical specs for that phase in the `/docs` folder.
2. **The Governance**: The corresponding CPMAI phase artifacts (authored by the Program Analyst) in `.governance/`.
3. **The Verification**: A `verify.md` artifact from every participating agent documenting their self-annealing checks.

---

## 4. Sequential Discovery Protocol (Session 0)

To prevent "Military Hallucinations" (incorrect assumptions about theme/intent), the project MUST begin with the **Specialist Interview Line**:

1. **PM/PO Interview (Sequential)**:
    * UI/UX Designer first (Feel/Soul).
    * Architect/DB second (Bones/Memory).
    * QA/Security third (Safety/Edges).
2. **Synthesis**:
    * BAs synthesize the interviews into a **Robust PRD**.
    * Program Analyst synthesizes the BAs' PRD into the **Mission Risk Profile**.
3. **Planning Review**:
    * Scrum Master + BAs present the Sprint Plan (derived from PRD).
    * **STOP POINT**: No coding or scaffold-building happens until the PM signs off on the PRD and Sprint Plan.

---

## 5. Hard-Linked Self-Annealing

To tighten the "Verify" loop, the `verify.md` artifact must contain:

* [ ] **Acceptance Criteria Check**: Evidence-based check of EVERY AC.
* [ ] **Dependency Audit**: Confirmation that no upstream data was ignored.
* [ ] **Regression Check**: Confirmation that the new logic doesn't bypass existing governance.
* [ ] **Failure Mode Analysis**: One documented "What if this fails?" scenario.

---

## 6. Sequence of Instruction

Agents must follow these files in this PRECISE order. If an agent skips a file, the Scrum Master must flag it as a "Process Violation."

1. **PROJECT.md**: Understand the current Mission.
2. **GEMINI.md**: Read the Operational Mode (Lite/Full) and Startup Protocol.
3. **structural-integrity-protocol.md**: [THIS FILE] Understand the Gate requirements.
4. **ai-governance-framework.md**: Understand the Compliance obligations.
5. **tasks.md**: Check if the current Phase Gate is OPEN.

**IF GATE IS CLOSED: ALL AGENTS STOP BUILDING AND SWITCH TO DISCOVERY/DOCUMENTATION.**
