# Verification Artifact: [Task Name]

**Agent**: [Your Role Name]
**Date**: [YYYY-MM-DD]
**Task Path**: [Path to task/feature]

## 1. Acceptance Criteria Check

List every AC for this task and provide evidence/confirmation of validation.

| Acceptance Criterion | Result (Pass/Fail) | Evidence/Notes |
| :--- | :--- | :--- |
| AC 1: [Description] | [Pass/Fail] | [E.g., "Tested with input X, got output Y"] |
| AC 2: [Description] | [Pass/Fail] | [E.g., "Verified field Z exists in schema"] |

## 2. Dependency Audit

- [ ] **Upstream Validation**: I have verified that all upstream inputs (PRD, ADRs, Designs) located in `/docs/` were used as the source of truth.
- [ ] **Cross-Functional Check**: I have verified that my changes do not break contracts established by other specialists (e.g., API contracts, DB schemas).

## 3. Structural Integrity & Governance

- [ ] **Knowledge Deposition**: All relevant intelligence (diagrams, specs, notes) has been deposited into the appropriate sub-folder in `/docs/`.
- [ ] **Governance Alignment**: My implementation aligns with the `ai-governance-framework.md` requirements for this domain.

## 4. Failure Mode Analysis (Self-Annealing)

**Worst-Case Scenario**: What happens if this logic/component fails?
> [Provide a brief description of the failure mode and the mitigation/recovery strategy implemented.]

**Self-Correction Record**:
> [If you found and fixed any errors during this task, document them here as part of the annealing loop.]

---
*This artifact is required for Phase Gate clearance.*
