# AI PM Builder's Template

**Enterprise AI Governance & Lifecycle Management Framework**

**Author**: Jerome Davis — Executive Architect | AI Governance & Strategy

---

A governance-first, multi-agent development framework for building AI applications using agentic coding platforms (Claude Code, Google Antigravity). This repo serves as both the **reusable template** and a **portfolio of projects** built with it.

## What This Is

A complete consulting-grade toolkit for AI project governance and execution, including:

- **14 Specialized AI Agents** — From Requirements BA through Program Analyst, each with defined roles, self-correction protocols, documentation responsibilities, and Director interview procedures
- **22 Governance Templates** — Audit-ready artifacts covering CPMAI v7 lifecycle, CSRMC modernization, ISO 42001, and NIST AI RMF
- **5 Mandatory Directives** — AI governance framework, self-annealing protocol, human reporting protocol, Director interview protocol, and branding guide
- **Self-Annealing Quality System** — 4-phase error detection and correction loop (Validate → Execute → Verify → Correct)
- **Algorithmic Authority Brand System** — Full Cyber-Secure Futurism design guide with hex values, typography, component specs, and AI prompt templates

## Quick Start

### Start a New Project
```bash
./new-project.sh my-project-name
```
This scaffolds a complete project instance under `projects/my-project-name/` with execution, governance, memory, and orchestration directories — without touching the template layer.

### Launch an Agent Session
```bash
# Claude Code
claude
> "Read CLAUDE.md and .agent/souls/scrum-master.md, then take on the Scrum Master role."

# Google Anti-Gravity
> "Read GEMINI.md and .agent/souls/scrum-master.md, then take on the Scrum Master role."
```

## Repository Structure

```
├── .agent/                         # Agent fleet configuration
│   ├── AGENT-ROSTER.md             # 14-agent roster with workflow sequences
│   ├── coordination/               # Cross-agent coordination artifacts
│   └── souls/                      # Individual agent SOUL files (14 agents)
│
├── directives/                     # GOVERNANCE LAYER (the template core)
│   ├── ai-governance-framework.md  # Master governance reference
│   ├── branding-guide.md           # Algorithmic Authority visual/verbal identity
│   ├── director-interview-protocol.md
│   ├── human-reporting-protocol.md
│   ├── self-annealing-protocol.md
│   ├── compliance/                 # Project compliance artifacts
│   ├── requirements/               # Project requirements artifacts
│   ├── stories/                    # User stories
│   └── templates/                  # 22 governance artifact templates
│       └── TEMPLATE-INDEX.md       # Master template inventory
│
├── projects/                       # PROJECT INSTANCES (portfolio)
│   ├── .project-template/          # Scaffold copied for each new project
│   └── [project-name]/             # Each project lives in isolation
│       ├── PROJECT.md              # Project identity, demo links, tech stack
│       ├── execution/              # Code and implementation artifacts
│       ├── governance/             # Project-specific governance evidence
│       ├── memory/                 # Project-specific agent memory
│       └── orchestration/          # Project-specific task board
│
├── orchestration/                  # Sprint planning templates
├── memory/                         # Long-term cross-project learnings
│
├── CLAUDE.md                       # Claude Code shared context
├── GEMINI.md                       # Anti-Gravity shared context
├── PORTFOLIO.md                    # Project showcase index
├── QUICK-START-GUIDE.md            # Comprehensive setup guide
├── QUICK-REFERENCE.md              # Daily workflow reference
└── new-project.sh                  # Project scaffolding script
```

## Standards Coverage

| Standard | Coverage |
|----------|----------|
| CPMAI v7 | Full 6-phase lifecycle with hard phase gates |
| ISO/IEC 42001 | AIMS clauses 4–10, Annex A controls |
| NIST AI RMF 1.0 | Govern, Map, Measure, Manage functions |
| NIST SP 800-53 Rev 5 | Security and privacy controls per phase |
| DoD CSRMC | All 8 modernization elements (MRP, CRPR, AEP, CCV, ACVR, Telemetry, Reciprocity, Resilience) |
| NIST SP 1270 | Bias identification and mitigation |
| NIST AI 100-1 | Generative AI security considerations |
| OMB M-24-10 | Federal AI governance expectations |

## Agent Fleet

| Agent | Domain | Primary Function |
|-------|--------|-----------------|
| Scrum Master | Coordination | Sprint planning, blocker resolution, Director interface |
| Requirements BA | Business Analysis | Stakeholder requirements elicitation |
| User Story BA | Business Analysis | Requirements to user stories |
| Architecture SE | Systems Engineering | System design, ADRs, threat modeling |
| Documentation SE | Systems Engineering | Documentation quality, ISO 42001 Clause 7.5 |
| Database Engineer | Data Engineering | Schema design, data lineage, data governance |
| Backend Developer | Development | API development, secure coding |
| Frontend Developer | Development | UI implementation, brand compliance |
| UI/UX Designer | Design | Interface design, human oversight, accessibility |
| QA Engineer | Quality | Functional testing, acceptance validation |
| Automation Test Engineer | Quality | Test automation, CCV rulesets |
| Pipeline DevOps | Operations | CI/CD pipelines, deployment security |
| Performance DevOps | Operations | Telemetry, performance monitoring |
| Program Analyst | Governance | CPMAI enforcement, phase gates, evidence orchestration |

## Portfolio

See [PORTFOLIO.md](PORTFOLIO.md) for the full project showcase.

---

**Created**: 2026-02-05
**Last Updated**: 2026-02-09
**Owner**: Jerome Davis
**Framework Version**: Enterprise AI Governance & Lifecycle Management Framework v1.1.1
**Platforms**: Claude Code, Google Antigravity
