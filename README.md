# AI Governance & Team Framework (The Factory)

**Executive Architect | AI Governance & Strategy**

This repository is the central **AI Development Factory** — containing the team structure, governance directives, and process orchestration for building AI applications. It serves as the "Office" where the 14 specialized AI agents live and work.

**Code and Projects reside in separate repositories.** This repository provides the *capability* to build them.

---

## 🏭 Repository Purpose

This is strictly a **Governance & Orchestration** repository. It contains:

1. **Directives Layer**: Immutable strategic rules, AI governance framework (CPMAI/NIST/ISO).
2. **The Agent Team**: 14 specialized Agent Personas (SOULs) defined in `.agent/souls/`.
3. **Process Templates**: Workflows, phase gate requirements, and project scaffolding.

### 🚫 What is NOT here?

- **Application Code**: Source code for specific applications (e.g., `ebook-forge`) lives in separate, sibling repositories.
- **Project Artifacts**: Run-time artifacts for specific apps live in their own repos.

---

## 📂 Architecture

```
jdavis-cyber-workspace/
├── .agent/                    # The Team
│   ├── AGENT-ROSTER.md        # Roster of all 14 agents
│   └── souls/                 # Individual Agent Personas (The "Employees")
├── directives/                # The Rules
│   ├── ai-governance-framework.md
│   ├── templates/             # Governance & Project Templates
│   │   └── project-scaffold/  # Core structure for new external projects
│   └── ...
├── orchestration/             # The Process
│   └── ...                    # Cross-project coordination
├── memory/                    # The Brain
│   └── MEMORY.md              # Long-term cross-project learnings
├── GEMINI.md                  # Anti-Gravity Context
└── CLAUDE.md                  # Claude Code Context
```

---

## 🚀 How to Use "The Factory"

### 1. Initialize a New Project (External)

To start a new project, you must create a separate repository and copy the **Factory Scaffold** into it:

```bash
# 1. Create your new project folder (outside this repo)
mkdir ../my-new-app
cd ../my-new-app
git init

# 2. Copy the Factory Scaffold
cp -r ../jdavis-cyber-workspace/directives/templates/project-scaffold/* .

# 3. Customize
# Update CLAUDE.md / GEMINI.md in the new repo to reference your local paths.
```

### 2. Activate the Team

Navigate to your **Project Repository** (e.g., `../my-new-app`) and activate an agent:

```bash
cd ../my-new-app
# Start your agent session (Claude/Gemini)
# "Read GEMINI.md and .agent/souls/scrum-master.md..."
```

*(Note: The `new-project.sh` script has been deprecated to enforce manual, conscious repository creation.)*

---

## 🛡️ Governance Framework

Every project built by this Factory inherits the **Enterprise AI Governance Framework**:

- **CPMAI v7 Lifecycle**: 6-phase governance (Business Understanding -> Operationalization).
- **Hard Phase Gates**: Mandatory evidence generation before moving phases.
- **Self-Annealing**: Protocol for autonomous error correction.

---

**Maintainer**: Jerome Davis
*Built with the AI PM Builder's Template*
