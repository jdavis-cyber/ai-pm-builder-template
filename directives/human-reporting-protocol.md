# Human Reporting Protocol

## Purpose

The human director is the ultimate authority on project direction, priority, and quality standards. This directive establishes a lightweight but firm reporting chain that keeps the human director informed at every meaningful milestone, provides clear approval gates for decisions that affect project direction, and ensures the Scrum Master serves as the single point of contact between the agent fleet and the human director.

The goal is visibility and governance, not bureaucracy. The human director should always be able to brief external parties on current project status without having to dig through memory files or task boards. The Scrum Master makes that possible by delivering structured, timely updates.

## Reporting Chain

All agents report their status to the Scrum Master through the existing memory file and task board system. The Scrum Master then distills that information into structured briefings for the human director. No agent communicates project status directly to external parties — that's the human director's role, enabled by the Scrum Master's reporting.

```text
┌──────────────────────────────────────────────────┐
│                  AGENT FLEET                       │
│  Requirements BA ─┐                                │
│  User Story BA ───┤                                │
│  Architecture SE ─┤                                │
│  Database Eng ────┤                                │
│  Backend Dev ─────┼──► SCRUM MASTER ──► HUMAN      │
│  Frontend Dev ────┤    (distills &      DIRECTOR   │
│  UI/UX Designer ──┤     reports)        (approves  │
│  Documentation SE ┤                      & directs)│
│  QA Engineer ─────┤                                │
│  Automation Test ─┤                                │
│  Pipeline DevOps ─┤                                │
│  Performance Dev ─┘                                │
└──────────────────────────────────────────────────┘
```

## Reporting Touchpoints

The Scrum Master reports to the human director at five defined touchpoints. These are not optional.

### 1. Task Completion Briefing

**When**: Every time a task moves to "Done" on the task board.

**Format**: Brief summary written to today's memory file, tagged for the human director.

**Content**:

```markdown
### Director Briefing: Task Complete
**Task**: [TASK-ID] — [Task Name]
**Agent**: [Who completed it]
**What was delivered**: [1-2 sentence summary of the output]
**Artifacts**: [File paths to deliverables]
**Self-Review**: [Pass/Fail — summary of verify phase results]
**Corrections Applied**: [None, or brief description]
**Impact**: [What this unblocks or enables next]
**Needs Your Attention**: [Yes/No — if yes, what decision or review is needed]
```

**Why**: You should never discover completed work by stumbling across it. Every completed task is an opportunity to course-correct early if the output isn't what you expected.

### 2. Sprint Start Briefing

**When**: Beginning of each sprint, after sprint planning is complete.

**Format**: Structured summary in the sprint section of the task board and today's memory file.

**Content**:

```markdown
### Director Briefing: Sprint Kickoff
**Sprint**: [Number/Name]
**Sprint Goal**: [What we're trying to accomplish in plain language]
**Duration**: [Start date — End date]
**Committed Work**:
- [TASK-ID]: [Name] — [Agent] — [Estimate]
- [TASK-ID]: [Name] — [Agent] — [Estimate]
**Total Capacity**: [X hours/points committed of Y available]
**Key Dependencies**: [Which tasks block others]
**Risks**: [Anything that might derail the sprint]
**Decisions Needed From You**: [Any pending decisions that could block work]
```

**Why**: You set the direction. Sprint planning is where you confirm the team is building what matters most. If priorities have shifted, this is where you redirect.

### 3. Blocker Escalation

**When**: Immediately when a blocker cannot be resolved by the Scrum Master within 2 hours, OR when a blocker requires a decision outside the agent fleet's authority.

**Format**: Urgent entry in today's memory file, tagged for the human director.

**Content**:

```markdown
### Director Escalation: Blocker
**Severity**: [Critical — blocks multiple agents / High — blocks one agent / Medium — slows work]
**Affected Task(s)**: [TASK-ID(s)]
**Affected Agent(s)**: [Who is blocked]
**What's Blocking**: [Clear description of the obstacle]
**What I've Tried**: [Scrum Master's attempted resolution]
**What I Need From You**: [Specific decision, resource, or action needed]
**Impact If Unresolved**: [What happens if this sits — cascading delays, missed sprint goal, etc.]
**Suggested Resolution**: [Scrum Master's recommendation, if applicable]
```

**Why**: You're the escalation path when the system can't self-resolve. But you should receive a clear problem statement with options, not a vague "we're stuck."

### 4. Sprint Completion Briefing

**When**: End of each sprint, before the retrospective.

**Format**: Structured summary in the task board retrospective section and today's memory file.

**Content**:

```markdown
### Director Briefing: Sprint Complete
**Sprint**: [Number/Name]
**Sprint Goal**: [Achieved / Partially Achieved / Not Achieved]
**Goal Assessment**: [1-2 sentences on why]

**Completed This Sprint**:
- [TASK-ID]: [Name] — [Agent] — [Outcome summary]

**Not Completed (Carried Over)**:
- [TASK-ID]: [Name] — [Why it didn't finish] — [New estimate]

**Blocked (Unresolved)**:
- [TASK-ID]: [Name] — [What's still blocking it]

**Sprint Metrics**:
- Velocity: [Points/hours completed]
- Cycle Time: [Average hours per task]
- Blocker Rate: [Count]
- Self-Annealing: [Self-catch rate, corrections, circuit breaker events]

**Key Decisions Made This Sprint**: [List any significant technical or scope decisions]
**Risks Heading Into Next Sprint**: [Anything you should know]
**Recommended Priorities for Next Sprint**: [Scrum Master's suggestion — you decide]
```

**Why**: This is your executive summary. You should be able to read this single briefing and confidently explain to any external party what was accomplished, what wasn't, and what's next.

### 5. Circuit Breaker Notification

**When**: Immediately when the self-annealing circuit breaker is triggered (see `directives/self-annealing-protocol.md`).

**Format**: Urgent entry in today's memory file, tagged for the human director.

**Content**:

```markdown
### Director Alert: Circuit Breaker Triggered
**Date**: [YYYY-MM-DD]
**Affected Agents**: [Who is paused]
**Affected Tasks**: [TASK-IDs]
**Pattern Detected**: [What systemic error triggered the circuit breaker]
**Root Cause (if known)**: [What's causing the recurring failure]
**Work Paused**: [What's on hold until this is resolved]
**Resolution Plan**: [How the team intends to fix it]
**Your Input Needed**: [Yes/No — if yes, what]
**Estimated Impact**: [Timeline delay, scope reduction, etc.]
```

**Why**: Circuit breakers indicate systemic problems, not individual task failures. You need to know when the system hits a structural issue because it may require a strategic decision from you — change scope, adjust approach, or accept a delay.

## Approval Gates

Certain decisions require your explicit approval before the team proceeds. The Scrum Master is responsible for identifying when an approval gate is reached and presenting you with the decision.

### Hard Stops (The "Red Light" Protocol)

Unlike standard approval gates where work might continue in parallel, a **Hard Stop** halts all forward progress on the affected track.

| Trigger Event | Action | Resolution Owner |
| :--- | :--- | :--- |
| **Phase Gate Failure** | **STOP**: No work on next-phase tasks. | Program Analyst |
| **Missing Prerequisite** | **STOP**: Agent refuses task assignment. | Scrum Master |
| **Scope Creep** | **STOP**: Unplanned feature added mid-sprint. | Scrum Master |
| **Circuit Breaker** | **STOP**: Recurring error pattern detected. | Scrum Master |

**Protocol**: When a Hard Stop occurs, the Scrum Master tags the memory file with `### STOP WORK ORDER` and notifies the Director immediately.

### Decisions That Require Human Approval

| Decision Type | Why It Needs Approval | Who Presents It |
| :--- | :--- | :--- |
| **Sprint scope and priorities** | You decide what gets built and in what order | Scrum Master at sprint start |
| **Architecture direction changes** | Major technical pivots affect timeline and cost | Scrum Master, with Architecture SE context |
| **Scope additions mid-sprint** | Adding work means something else gets dropped or delayed | Scrum Master when scope creep is detected |
| **Rollback decisions** | Rolling back completed work has downstream impact | Scrum Master, per self-annealing protocol |
| **Circuit breaker resolution approach** | Systemic issues may require strategic redirection | Scrum Master when circuit breaker fires |
| **External dependency decisions** | Choosing vendors, services, or integrations that carry cost or commitment | Scrum Master, with relevant agent's analysis |
| **Go/no-go for deployment** | Production deployments carry risk | Scrum Master, with QA and DevOps input |

### Decisions That Do NOT Require Human Approval

These are within the agent fleet's authority and should proceed without waiting:

- Task assignment and sequencing (Scrum Master)
- Technical implementation choices within approved architecture (Developers)
- Test strategy and coverage decisions (QA and Automation Test)
- Documentation format and organization (Documentation SE)
- Self-annealing corrections within an agent's domain (Any agent)
- Blocker resolution the Scrum Master can handle (Scrum Master)

### How Approval Works

1. The Scrum Master writes an approval request in today's memory file with the decision context, options, recommendation, and impact of each option.
2. The Scrum Master tags it clearly: `### Awaiting Director Approval`
3. Work that depends on the decision is marked as "Blocked — Awaiting director decision" on the task board.
4. The human director reviews and responds. The decision is documented in the memory file.
5. The Scrum Master unblocks the dependent work and communicates the decision to affected agents.

**No agent proceeds past an approval gate without documented approval from the human director.**

## How the Human Director Communicates Back

When you make a decision, provide direction, or give feedback:

- **In a live session**: Tell the Scrum Master directly. They'll document it in the memory file and communicate it to affected agents.
- **Between sessions**: Write your decision or direction in today's memory file tagged with `### Director Decision` so the Scrum Master picks it up at their next session initialization.
- **Priority changes**: Update the task board directly, or tell the Scrum Master to reprioritize. Either works.

Your communication doesn't need to follow a template. Just be clear about what you've decided, what you want prioritized, or what needs to change. The Scrum Master will translate your direction into task board updates and agent assignments.

## Briefing Format for External Parties

When you need to brief someone outside the project, pull from the most recent Sprint Completion Briefing. It's designed to give you everything you need:

- **What are we building?** → Sprint Goal
- **What's done?** → Completed This Sprint
- **What's in progress?** → Current sprint's In Progress tasks
- **Any problems?** → Blocker and risk sections
- **What's next?** → Recommended Priorities for Next Sprint

If you need a more detailed briefing on a specific feature or decision, ask the Scrum Master to compile a feature-level summary pulling from relevant task completions, architecture decisions, and test results.

## Anti-Patterns

**Don't** let agents bypass the Scrum Master to bring you status updates or requests. The single-point-of-contact model exists to prevent information overload and ensure consistent, structured reporting.

**Don't** let reporting become a bottleneck. The Scrum Master reports asynchronously through memory files. You review at your pace. Agents don't wait for you to read the briefing before continuing their work (unless they're at an approval gate).

**Don't** skip sprint start or sprint completion briefings. These are your primary governance touchpoints. Without them, you lose the ability to steer.

**Don't** make the Scrum Master guess what you need to know. If there's a specific area you want more visibility into, tell them to add it to their reporting.

**Don't** approve by silence. If a decision is waiting for you, the Scrum Master needs an explicit response. "Proceed as recommended" is fine. No response leaves work blocked.

---

**Directive Version**: 1.0
**Last Updated**: 2026-02-06
**Maintained By**: Scrum Master (reports), Human Director (approves)
**Applies To**: Scrum Master (primary), all agents (awareness)
