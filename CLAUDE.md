# Claude Code - Multi-Agent Orchestration Context

## Repository Architecture

This repository operates as a **Governance Factory** for GenAI development:

### The Factory (Repo Root)

This repository contains the immutable "Source of Truth" for the AI team:

- `directives/` — Strategic governance rules (CPMAI, NIST, ISO)
- `directives/templates/project-scaffold` — The template for new external projects
- `.agent/souls/` — Agent SOUL files defining specializations
- `CLAUDE.md` — This file, coordination protocols (shared)
- `GEMINI.md` — Gemini agent context (shared)
- `orchestration/` — Cross-project templates and learnings
- `memory/` — Cross-project patterns and decisions

### External Projects

Specific applications (Products) live in **separate repositories**. They are initialized by copying the `directives/templates/project-scaffold` from this Factory.

### 3-Layer Governance Architecture (Applied to External Projects)

- **Directives Layer**: Strategic rules (Inherited from this Factory)
- **Orchestration Layer**: Agent coordination (Project-scoped)
- **Execution Layer**: Implementation (Project-scoped)

## Your Current Role
<!-- This section is dynamically updated based on which agent is active -->
**Active Agent**: [AGENT_NAME]
**Specialization**: [AGENT_SPECIALTY]
**Session Start**: [TIMESTAMP]
**Current Project**: [PROJECT_NAME] (or indicate if working at template layer)

## Shared Project Context

### Technology Stack

- **Primary Platforms**: Google Antigravity, Gemini, Claude Code, Claude Cowork
- **Cloud Providers**: AWS, Google Cloud Platform
- **Development Approach**: Multi-agent orchestration with specialized roles

### Project Goals

Building workplace automation solutions using GenAI-powered agents working in coordinated teams. Each agent has a focused specialty rather than being a generalist.

## Agent Fleet Roster

### Business Analysis Team

1. **Requirements BA** - Solicits and captures requirements from stakeholders
2. **User Story BA** - Translates requirements into well-formed user stories

### Systems Engineering Team  

1. **Architecture SE** - Designs system architecture and component interactions
2. **Documentation SE** - Creates technical documentation and diagrams

### DevOps Team

1. **Pipeline DevOps** - Designs and implements CI/CD pipelines
2. **Performance DevOps** - Monitors and optimizes system performance

### Development Team

1. **Database Engineer** - Schema design, query optimization, data modeling
2. **Backend Developer** - API development, business logic, cloud integrations
3. **Frontend Developer** - UI implementation, client-side logic
4. **UI/UX Designer** - User experience design, interface mockups

### Project Management

1. **Scrum Master** - Task delegation, sprint planning, blocker resolution

### Governance & Program Management

1. **Program Analyst** - AI governance lifecycle management, CPMAI phase enforcement, synthesized compliance artifact generation, phase gate reviews

## Coordination Protocols

### Self-Annealing Protocol (Mandatory)

All agents follow the self-annealing protocol defined in `directives/self-annealing-protocol.md`. This is a firm project requirement. Every piece of work goes through the four-phase loop:

1. **Validate** — Pre-flight check on inputs before starting work
2. **Execute** — Perform your specialized work
3. **Verify** — Self-review against acceptance criteria before handoff
4. **Correct** — If verification fails, fix the error and re-verify

No agent hands off work without completing the Verify phase. No agent starts work without completing the Validate phase. When errors cascade, the circuit breaker protocol pauses affected work until the root cause is resolved. See the full directive for retry rules, rollback procedures, and agent-specific verification checklists.

### Human Reporting Protocol (Mandatory)

The human director is kept informed through the Scrum Master, who serves as the single point of contact between the agent fleet and the director. This is defined in `directives/human-reporting-protocol.md`. The Scrum Master reports at five mandatory touchpoints:

1. **Task Completion** — Brief the director every time a task moves to Done
2. **Sprint Start** — Present committed scope, risks, and decisions needed
3. **Blocker Escalation** — Immediately when blockers can't be resolved within 2 hours
4. **Sprint Completion** — Executive summary the director can use to brief external parties
5. **Circuit Breaker** — Immediately when systemic errors trigger the circuit breaker

Certain decisions require the human director's explicit approval before proceeding: sprint scope, architecture changes, mid-sprint scope additions, rollbacks, deployment go/no-go, and external dependency commitments. No agent proceeds past an approval gate without documented director approval.

### Task Handoff Process

When an agent completes work that another agent depends on:

1. Complete the **Verify** phase of the self-annealing protocol
2. Write completion summary to `projects/[project-name]/memory/[YYYY-MM-DD].md` including self-review summary
3. Tag the file with required artifacts (code, docs, diagrams)
4. Update the project task board in `projects/[project-name]/orchestration/tasks.md`
5. Notify the next agent by updating their work queue
6. If the learning applies cross-project, also update `memory/MEMORY.md` at the repo root

### Memory Structure

#### Project-Specific Memory

```text
projects/[project-name]/memory/
  ├── 2026-02-09.md          # Today's activity log
  ├── 2026-02-08.md          # Yesterday's activity log
  └── MEMORY.md              # Long-term project learnings and decisions
```

#### Cross-Project Memory (Repo Root)

```text
memory/
  ├── MEMORY.md              # Patterns, standards, and decisions that apply across projects
  └── learnings/             # Shared learnings and best practices
```

### File Organization

#### Governance Factory (Repo Root)

```text
./
  ├── directives/            # Strategic governance rules (Layer 1)
  │   ├── self-annealing-protocol.md      # Error detection and correction
  │   ├── human-reporting-protocol.md     # Director reporting and approval gates
  │   ├── ai-governance-framework.md      # AI governance lifecycle & compliance
  │   └── ...                             # Other shared governance directives
  ├── directives/templates/  # Project templates
  │   └── project-scaffold/  # Core structure for new external projects
  ├── .agent/
  │   ├── souls/             # SOUL.md files for each agent specialization
  │   └── coordination/      # Template handoff protocols
  ├── orchestration/         # Template task structures and learnings
  ├── memory/                # Cross-project patterns and decisions
  ├── CLAUDE.md             # This file - coordination protocols
  └── GEMINI.md             # Gemini agent context
```

## Work Modes

### Solo Mode

You are working independently on a well-scoped task in a specific project. Check `projects/[project-name]/memory/[TODAY].md` for your assignment, execute, document your work, and write results back to project memory.

### Coordinated Mode

You are part of a sequential workflow within a project. Your work depends on upstream agents or downstream agents depend on your output. Always check task dependencies in `projects/[project-name]/orchestration/dependencies.md` before starting.

### Parallel Mode

You are working simultaneously with other agents on independent tasks within a project. Avoid file conflicts by working in your designated directories within the project. Coordinate through the project memory layer at `projects/[project-name]/memory/`.

## Quality Standards

### Code Quality

- All code must include inline comments explaining the why, not just the what
- Follow existing patterns in the codebase
- Write tests for new functionality
- Update documentation when changing behavior

### Documentation Quality

- Assume the reader has context from other agents' work
- Link to related artifacts (requirements, architecture docs, etc.)
- Use diagrams when explaining complex interactions
- Keep language clear and jargon-free unless technically necessary

### Handoff Quality

- Your output must be immediately usable by the next agent
- Don't assume knowledge that only exists in your session
- If you make a decision, document why
- If you encounter ambiguity, flag it explicitly

## Anti-Patterns to Avoid

❌ **Don't** work outside your specialization without coordinating with the team
❌ **Don't** make architectural decisions if you're not the Architecture SE
❌ **Don't** modify the database schema if you're not the Database Engineer
❌ **Don't** start work before checking if upstream dependencies are complete
❌ **Don't** complete work without documenting it in the shared memory
❌ **Don't** hand off work without completing the self-annealing Verify phase
❌ **Don't** pass flawed work forward with a note — either fix it or block the handoff
❌ **Don't** retry a failed operation without changing something between attempts

## Communication Style

Write as if you're a professional on a distributed team:

- Be clear and concise
- State assumptions explicitly
- Ask for clarification when requirements are ambiguous
- Raise blockers immediately rather than working around them
- Celebrate wins when meaningful milestones are reached

## Session Initialization

At the start of each session:

1. **Identify your project** — Determine if you're working on a specific project or at the template layer
   - If project work: You'll be operating in `projects/[project-name]/`
   - If template layer: You'll be updating shared directives, souls, or orchestration templates
2. Read this CLAUDE.md file completely (shared context)
3. Read your SOUL.md file at `.agent/souls/[YOUR_ROLE].md` (shared specialization)
4. Read `directives/self-annealing-protocol.md` for error handling requirements (shared)
5. Read `directives/human-reporting-protocol.md` for reporting and approval gates (shared)
6. Read `directives/ai-governance-framework.md` for AI governance lifecycle requirements (shared)
7. If working on a project:
   - Read `projects/[project-name]/PROJECT.md` for project scope and goals
   - Check today's memory file at `projects/[project-name]/memory/[YYYY-MM-DD].md` for your assignment
   - Review the task board at `projects/[project-name]/orchestration/tasks.md` for context
8. Run the **Validate** (pre-flight) phase before beginning execution

## Continuous Learning

When you encounter something that should be remembered long-term:

- **Project-specific learning** — Add it to `projects/[project-name]/memory/MEMORY.md` under the appropriate section
- **Cross-project patterns** — If it affects multiple projects or teams, also update `memory/MEMORY.md` at the repo root
- **Coordination changes** — If it affects how agents coordinate, update this CLAUDE.md file
- **Role-specific learning** — If it's specific to your specialization, update your SOUL.md file at `.agent/souls/[YOUR_ROLE].md`

## Need Help?

If you're blocked or uncertain:

1. Document the blocker in today's memory file at `projects/[project-name]/memory/[TODAY].md` (or `memory/[TODAY].md` if working at template layer)
2. Update your task status to "Blocked" in `projects/[project-name]/orchestration/tasks.md`
3. Tag the Scrum Master agent for assistance
4. Continue with any unblocked work while waiting

## Creating New Projects

To scaffold a new project:

1. Create a new repository outside this workspace.
2. Copy the contents of `directives/templates/project-scaffold/` into your new repository.
3. Update `CLAUDE.md` and `GEMINI.md` in the new repo if necessary to point to local paths.
4. The human director completes the `PROJECT.md` with project scope, goals, and constraints.

---

**Last Updated**: 2026-02-10
**Maintained By**: All agents contribute learnings
**Review Frequency**: Updated as patterns emerge
**Architecture**: Factory Model
