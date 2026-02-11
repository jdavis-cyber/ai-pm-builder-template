# The AI Factory: Agentic Development Framework

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Governance: CPMAI](https://img.shields.io/badge/Governance-CPMAI%20v7-blue)](https://www.pmi.org/certifications/ai-project-management-cpmai)
[![Team: 14 Agents](https://img.shields.io/badge/Team-14%20Agents-green)](.agent/AGENT-ROSTER.md)

**A governance-first framework for orchestrating autonomous AI development teams.**

---

## What is "The Factory"?

This repository is **not a software project**. It is a **Software Company in a Box**.

It contains the DNA of a high-performance, compliant, and autonomous AI development team: the **Governance Directives**, **Team Structure (Souls)**, **Process Orchestration**, and **Automation Scripts** required to build enterprise-grade applications safely and efficiently.

### Who is this for?

- **AI Architects & CTOs**: Who need a standardized, governed framework for Generative AI development.
- **Enterprise Developers**: Who want to move beyond ad-hoc prompting to structured, engineering-grade agentic workflows.
- **Consultants & PMs**: Who need a repeatable, compliant methodology for delivering AI-driven client work — even without coding experience.

---

## Core Architecture

The Factory uses a **Hub-and-Spoke** model:

| Layer | Purpose | Location |
|:---|:---|:---|
| **The Hub (This Repo)** | Team definitions, governance rules, templates | Factory root |
| **The Spokes (Products)** | Individual apps built by the team | Separate repos, spawned from the scaffold |

```
ai-pm-builder-template/          # The Hub (Factory)
├── .agent/
│   ├── souls/                   # 14 Agent identity files
│   ├── AGENT-ROSTER.md          # Team roster
│   └── coordination/            # Handoff protocols
├── directives/
│   ├── ai-governance-framework.md
│   ├── self-annealing-protocol.md
│   ├── human-reporting-protocol.md
│   ├── director-interview-protocol.md
│   └── templates/
│       ├── project-scaffold/    # 👈 Copy this to start a new project
│       └── [26 governance templates]
├── orchestration/               # Cross-project task templates
├── memory/                      # Cross-project learnings
├── CLAUDE.md                    # Agent context (Claude Code)
├── GEMINI.md                    # Agent context (Antigravity)
└── README.md                    # You are here
```

---

## The Team (14 Agent Souls)

Every soul file in `.agent/souls/` defines a specialized agent with distinct responsibilities, tools, verification checks, and behavioral constraints.

| Domain | Agent | Focus |
|:---|:---|:---|
| **Product** | Requirements BA | Stakeholder interviews, requirements elicitation |
| | User Story BA | Gherkin/AC user stories, acceptance criteria |
| **Engineering** | Architecture SE | System design, technology selection, diagrams |
| | Documentation SE | Living documentation, technical specs |
| **Development** | Backend Dev | APIs, server-side logic, integrations |
| | Frontend Dev | UI implementation, accessibility, client-side logic |
| | Database Engineer | Schema design, query optimization, data integrity |
| **Design** | UI/UX Designer | Wireframes, user flows, design systems |
| **Quality** | QA Engineer | Manual & exploratory testing, bug reporting |
| | Automation Engineer | CI test suites, E2E frameworks |
| **DevOps** | Pipeline DevOps | CI/CD construction, build automation |
| | Performance DevOps | Observability, load testing, optimization |
| **Management** | Scrum Master | Orchestration, velocity tracking, Session Zero |
| **Governance** | Program Analyst | CPMAI/ISO compliance, phase gate enforcement |

---

## Governance Layer

The Factory operates under immutable directives in `directives/`. No agent can override these.

### Enterprise AI Governance

A synthesis of **NIST AI RMF**, **ISO 42001**, and **CPMAI v7** mandating a 6-phase lifecycle with hard phase gates. Work cannot proceed without specific evidence (Bias Assessment, Threat Model, etc.).

### Self-Annealing Protocol

The "immune system" of the Factory. Every agent follows a 4-step loop for every task:

1. **Validate** — Pre-flight checks (Do I have what I need?)
2. **Execute** — Perform the work
3. **Verify** — Self-review against requirements
4. **Correct** — Fix errors *before* handoff

### Double-Lock Protocol

Two hard stops prevent agents from skipping steps:

- **Lock 1 (Scrum Master)**: No task starts without upstream artifacts present ("Definition of Ready")
- **Lock 2 (Program Analyst)**: No phase advances without a passed Phase Gate

---

## Automation Layer

The Factory includes a **Runner Script** that automates the agent orchestration loop.

### Quick Start

```bash
# From inside a spawned project:
./automation/factory.sh
```

### Two Operating Modes

| Mode | How It Works | Best For |
|:---|:---|:---|
| **Assisted** (default) | Script finds the next task, generates the prompt, and pauses. You paste it into your agent. | Non-coders, manual control |
| **Autonomous** | Script pipes prompts directly to your CLI tool (`claude`, `gemini`, etc.) in a continuous loop. | Hands-free execution |

### Session Zero (Scrum Master)

On first project initialization, the Scrum Master automatically:

1. Asks the Director which LLM CLI they use
2. Edits `automation/factory.sh` to configure the tool (no manual script editing)
3. Initializes `PROJECT.md` and the task board
4. Assigns the Requirements BA as the first task

---

## ROI Tracking

The system tracks the "Value Delta" between human and AI effort:

- **Human Estimate**: The Scrum Master estimates tasks at "Senior Developer" pace
- **Agent Actual**: Agents log their real execution time
- **Velocity Multiplier**: `Human Estimate / Agent Actual` — reported every sprint

---

## Starting a New Project

Don't clone this repo to build an app. Use it to **spawn** a project:

```bash
# 1. Create a new project
mkdir ../my-awesome-app && cd ../my-awesome-app
git init

# 2. Inject the Factory DNA
cp -r ../ai-pm-builder-template/directives/templates/project-scaffold/* .
cp -r ../ai-pm-builder-template/directives/templates/project-scaffold/.* . 2>/dev/null

# 3. Summon the Scrum Master
# "Act as the Scrum Master. Read .agent/souls/scrum-master.md and GEMINI.md.
#  Initialize this project for a [your app idea]."
```

The Scrum Master will configure your automation, populate the task board, and the team is ready to work.

### Spawned Project Structure (Hybrid)

```
my-awesome-app/                  # Code at root (developer-first)
├── backend/
├── frontend/
├── database/
├── .agent/                      # Hidden agent machinery
│   ├── souls/                   # Agent identities
│   ├── memory/                  # Handoff logs
│   └── tasks.md                 # Task board
├── .governance/                 # Hidden compliance artifacts
├── automation/
│   ├── factory.sh               # The Runner
│   └── run_factory.py           # The Logic
└── PROJECT.md                   # Project identity card
```

---

## Memory & Continuous Learning

- **`memory/MEMORY.md`** (Factory root): Cross-project learnings — all future projects benefit
- **`.agent/memory/MEMORY.md`** (Each project): Project-specific context and decisions

---

## Built With

- [Google Antigravity](https://antigravity.google/) — Primary agentic IDE
- [Anthropic Claude Code](https://claude.ai/) — Complementary agentic IDE
- [CPMAI v7](https://www.pmi.org/certifications/ai-project-management-cpmai) — AI project methodology

---

**Built by Jerome Davis**
*Executive Architect | AI Governance & Strategy*
