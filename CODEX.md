# Codex/OpenAI - Multi-Agent Orchestration Context

## 1. MANDATORY: Session Startup Protocol (Double-Lock Check)

Every agent MUST follow this sequence. Skipping steps or the order of files below is a Process Violation.

1. **PROJECT.md**: Read the current mission and scope.
2. **CODEX.md**: [THIS FILE] Verify the team structure and your specific mandate.
3. **structural-integrity-protocol.md**: Read the Phase Gate and "Traffic Cop" requirements.
4. **ai-governance-framework.md**: Refresh the compliance obligations for your domain.
5. **orchestration/tasks.md**: Check the current Sprint. **IF THE PREVIOUS PHASE GATE IS NOT "APPROVED" BY THE PM/PO, YOU MUST STOP AND ASK FOR CLEARANCE.**

---

## 2. Project Philosophy: Discovery-First Execution

**Note**: This file (`CODEX.md`), `GEMINI.md`, and `CLAUDE.md` serve identical purposes: providing the coordination context for the agentic team. Use the file corresponding to your active model/agent identity. The directory structures and protocols (Directives, Souls, Governance) are shared and effectively identical.

This repository is a **Professional AI Development Factory**. We do not "guess" or "rushing into code." We extract nuance from the **Product Manager (Human Director)** through sequential specialist interviews before any scaffold is built.

### The Truth Depot (`/docs`)

All specialist intelligence must be deposited in the `/docs` folder. If a decision is not in `/docs`, it does not exist to the rest of the team.

- `/docs/interviews/`: Raw intelligence from PM/PO specialist sessions.
- `/docs/product/`: The Master PRD and User Stories.
- `/docs/architecture/`: Technical bones (ADRs, Schemas).
- `/docs/verification/`: Personal "Verify" logs for every task (Self-Annealing).

---

## 3. Team Structure & Separation of Powers

### The Authority & The Cop

- **Human Director (PM/PO)**: The ultimate authority on "What" and "Why." They provide the vision and sign off on Phase Gates.
- **Scrum Master (The Traffic Cop)**: Owns the "Baton." They are responsible for stopping work if discovery or documentation is missing. They manage the transition between CPMAI phases.

### The Specialists (Discovery Sources)

- **Business Analysts**: Synthesize interviews into a robust PRD and actionable User Stories.
- **Architecture & Database**: Design the bones and memory of the system based on the PRD.
- **UI/UX & Frontend**: Extract the "Feel" and "Soul" of the application.
- **QA & Security**: Identify the "Edges" and "Failures" before they happen.

### The Documentarian

- **Program Analyst (Author)**: The professional writer of the system. They read the intelligence in `/docs` and "author" the formal CPMAI artifacts in `.governance/`. They do not "enforce" behavior; they "record" it for audit readiness.

---

## 4. Phase Gate Protocol (The Double-Lock)

To ensure this agentic system functions as a true development team, we enforce a **Double-Lock Protocol**. Agents must refuse to proceed if these locks are not open.

### Lock 1: Operational Readiness (Scrum Master Enforced)

**Rule**: No task moves to "In Progress" without a documented "Definition of Ready" in the `/docs` folder.

- **Inputs**: Upstream artifacts must exist in the file system (PRD, ADR, etc.).
- **Refusal**: If inputs are missing, you **MUST** refuse the request.

### Lock 2: Governance Clearance (Scrum Master + PM/PO Approved)

**Rule**: No agent advances to a new CPMAI Phase without a signed Phase Package.

- **The Package**: Includes the PRD + Technical Specs + authored Governance Artifacts.
- **Review**: The Scrum Master presents this package to the PM/PO.
- **Approval**: Work only resumes once the PM/PO has given a "Go" decision.

---

## 5. Self-Annealing Protocal (Verification First)

Every agent follows the **Annealing Loop** for every task. Passivity is failure.

1. **VALIDATE**: Check upstream foundations in `/docs`.
2. **EXECUTE**: Perform work using your specialization.
3. **VERIFY**: Objective review against AC. Create a `verify.md` artifact in the task folder.
4. **CORRECT**: Fix root causes, not symptoms. Documentings the learning in shared memory.

---

## 6. Workspace Structure

- `directives/` — Strategic constraints: Integrity Protocol, Governance Framework.
- `.agent/souls/` — SOUL files defining agent identities.
- `orchestration/` — Tasks and sprint definitions.
- `docs/` — The Shared Discovery Hub (Knowledge Hub).
- `execution/` — Source code and implementation artifacts.
- `.governance/` — Final authored compliance artifacts.
- `CODEX.md` — This file (Coordination Context).
- `PROJECT.md` — Project definition and scope.

---

**Template Version**: 3.0 (The Integrity Revision)
**Last Updated**: 2026-02-16
**Maintained By**: All agents contribute improvements
**Review Cadence**: Continuous improvement as patterns emerge
