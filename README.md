# The AI Factory: Agentic Development Framework

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Governance: CPMAI](https://img.shields.io/badge/Governance-CPMAI%20v7-blue)](https://www.cognilytica.com/)
[![Team: 14 Agents](https://img.shields.io/badge/Team-14%20Agents-green)](.agent/AGENT-ROSTER.md)

**Executive Architect | AI Governance & Strategy**

## 🏗️ What is "The Factory"?

This repository is **not a software project**. It is a **Software Company in a Box**.

It contains the "DNA" of a high-performance, compliant, and autonomous AI development team. It provides the **Governance Directives**, **Team Structure**, and **Process Orchestration** required to build enterprise-grade AI applications safely and efficiently.

### 🎯 Who is this for?

- **AI Architects & CTOs**: Who need a standardized, governed framework for Generative AI development.
- **Enterprise Developers**: Who want to move beyond "vibes-based coding" to structured, engineering-grade agentic workflows.
- **Consultants**: Who need a repeatable, compliant methodology for delivering AI client work.

---

## 👥 The Team (14 Agent Souls)

The core of The Factory is its staff. We have defined 14 specialized "Agent Souls" in `.agent/souls/`. These are not generic assistants; they are role-specific personas with distinct responsibilities, tools, and constraints.

| Domain | Role | Responsibility |
| :--- | :--- | :--- |
| **Product** | **Requirements BA** | Elicits requirements, identifies stakeholders. |
| | **User Story BA** | Converts requirements into technical User Stories (Gherkin/AC). |
| **Engineering** | **Architecture SE** | Designs system architecture, technology selection. |
| | **Documentation SE** | Maintains "Living Documentation" and technical specs. |
| **Development** | **Frontend Dev** | UI/UX implementation, accessibility, client-side logic. |
| | **Backend Dev** | API design, server-side logic, integrations. |
| | **Database Eng** | Schema design, SQL optimization, data integrity. |
| **Design** | **UI/UX Designer** | Wireframes, user flows, design system enforcement. |
| **Quality** | **QA Engineer** | Manual testing, exploratory testing, bug reporting. |
| | **Automation Eng** | CI test suites, E2E testing frameworks. |
| **DevOps** | **Pipeline DevOps** | CI/CD construction, build automation. |
| | **Performance DevOps** | Observability, load testing, resource optimization. |
| **Management** | **Scrum Master** | Orchestration, blocker resolution, velocity tracking. |
| **Governance** | **Program Analyst** | **The Auditor**. Enforces CPMAI/ISO compliance and phase gates. |

---

## 📜 The Directives (Governance Layer)

The "Factory" operates under immutable laws defined in the `directives/` directory. No agent can override these.

### 1. Enterprise AI Governance (`directives/ai-governance-framework.md`)

A synthesis of **NIST AI RMF**, **ISO 42001**, and **CPMAI v7**. It mandates:

- **6-Phase Lifecycle**: Business Understanding $\to$ Operationalization.
- **Hard Phase Gates**: Work cannot proceed without specific evidence (e.g., *Bias Assessment*, *Threat Model*).

### 2. Self-Annealing Protocol (`directives/self-annealing-protocol.md`)

The "Immune System" of the factory. Every agent must follow the 4-step loop for every task:

1. **Validate**: Pre-flight checks (Do I have what I need?).
2. **Execute**: Perform the work.
3. **Verify**: Self-review against requirements and strict constraints.
4. **Correct**: Loop back and fix errors *before* handoff.

---

## ⚙️ The Orchestration (Process Layer)

How do 14 agents work together without chaos? We use a **Hub-and-Spoke** repository model.

### The "Factory vs. Product" Model

1. **The Hub (This Repo)**:
    - Holds the *Team* (Souls) and *Rules* (Directives).
    - Acts as the "Headquarters".

2. **The Spokes (Product Repos)**:
    - Independent repositories for applications (e.g., `ebook-forge`, `risk-app`).
    - Created by copying the **Factory Scaffold**.

### Workflow: Starting a New Project

Don't clone this repo to build an app. Use it to *spawn* a project.

```bash
# 1. Create a new repository folder
mkdir ../my-awesome-app
cd ../my-awesome-app
git init

# 2. Inject the Factory DNA (The Scaffold)
cp -r ../jdavis-cyber-workspace/directives/templates/project-scaffold/* .

# 3. Code!
# Now your agents (Claude/Gemini) will read your local GEMINI.md, 
# which points them back to the Factory for their instructions.
```

---

## 🧠 Memory & Continuous Learning

The Factory never forgets.

- **`memory/MEMORY.md`**: Cross-project learnings. If the Database Engineer discovers a better way to index PostgreSQL, they record it here. All future projects benefit.
- **`projects/[app]/memory/`**: Project-specific context.

---

**Built with ❤️ by Jerome Davis**
*Powered by Google Antigravity & Anthropic Claude*
