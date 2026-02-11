#!/usr/bin/env python3
"""
Factory Runner — The Autonomous Agent Loop.

Parses .agent/tasks.md (table format) to find the next open task,
determines the correct agent role, and generates a ready-to-use prompt.

Usage:
    python3 automation/run_factory.py
"""

import os
import re
import sys

# Configuration
TASKS_FILE = ".agent/tasks.md"
MEMORY_DIR = ".agent/memory"
SOULS_DIR = ".agent/souls"

# Role keyword mappings
ROLE_MAP = {
    "Requirements BA": "requirements-ba",
    "User Story BA": "user-story-ba",
    "Architecture SE": "architecture-se",
    "Documentation SE": "documentation-se",
    "Database Engineer": "database-engineer",
    "Database Eng": "database-engineer",
    "Backend Developer": "backend-developer",
    "Backend Dev": "backend-developer",
    "Frontend Developer": "frontend-developer",
    "Frontend Dev": "frontend-developer",
    "UI/UX Designer": "ui-ux-designer",
    "QA Engineer": "qa-engineer",
    "Automation Eng": "automation-test-engineer",
    "Automation Test Engineer": "automation-test-engineer",
    "Pipeline DevOps": "pipeline-devops",
    "Performance DevOps": "performance-devops",
    "Scrum Master": "scrum-master",
    "Program Analyst": "program-analyst",
}

KEYWORD_FALLBACK = {
    "requirement": "requirements-ba",
    "stakeholder": "requirements-ba",
    "user story": "user-story-ba",
    "gherkin": "user-story-ba",
    "architecture": "architecture-se",
    "diagram": "architecture-se",
    "database": "database-engineer",
    "schema": "database-engineer",
    "sql": "database-engineer",
    "frontend": "frontend-developer",
    "ui": "frontend-developer",
    "css": "frontend-developer",
    "backend": "backend-developer",
    "api": "backend-developer",
    "test": "qa-engineer",
    "qa": "qa-engineer",
    "pipeline": "pipeline-devops",
    "ci/cd": "pipeline-devops",
    "document": "documentation-se",
    "governance": "program-analyst",
    "compliance": "program-analyst",
}


def find_tasks_file():
    """Locates the tasks.md file."""
    if os.path.exists(TASKS_FILE):
        return TASKS_FILE
    if os.path.exists(f"directives/templates/project-scaffold/{TASKS_FILE}"):
        return f"directives/templates/project-scaffold/{TASKS_FILE}"
    return None


def get_next_task_from_table(tasks_path):
    """
    Parses the scaffold's table-format tasks.md.
    Looks for rows in the 'Backlog' or 'In Progress' sections and returns
    the first task that has a 'Backlog' or 'To Do' status.
    """
    with open(tasks_path, "r") as f:
        lines = f.readlines()

    in_backlog = False
    in_progress = False

    for line in lines:
        stripped = line.strip()

        # Track which section we're in
        if stripped.startswith("## Backlog"):
            in_backlog = True
            in_progress = False
            continue
        elif stripped.startswith("## In Progress"):
            in_backlog = False
            in_progress = True
            continue
        elif stripped.startswith("## Done"):
            in_backlog = False
            in_progress = False
            continue

        # Parse table rows (skip headers and separators)
        if (in_backlog or in_progress) and stripped.startswith("|") and not stripped.startswith("|---") and "Task ID" not in stripped:
            cells = [c.strip() for c in stripped.split("|")[1:-1]]
            if len(cells) >= 5:
                task_id = cells[0]
                title = cells[1]
                assigned_to = cells[2]
                status = cells[4] if len(cells) > 4 else "Backlog"

                # Skip placeholder rows
                if "[Title]" in title or not title:
                    continue

                # Return first actionable task
                if status.lower() in ("backlog", "to do", "todo", "open", "ready"):
                    return task_id, title, assigned_to

    return None, None, None


def get_next_task_from_checkboxes(tasks_path):
    """
    Fallback parser for checkbox-format tasks.md (- [ ] style).
    """
    with open(tasks_path, "r") as f:
        lines = f.readlines()

    current_parent = "General Task"

    for line in lines:
        if line.strip().startswith("- [ ]") and not line.startswith("  "):
            current_parent = line.strip()[5:].strip()
            current_parent = re.sub(r"<!--.*?-->", "", current_parent).strip()

        if "- [ ]" in line:
            task_text = line.split("- [ ]")[1].strip()
            task_text = re.sub(r"<!--.*?-->", "", task_text).strip()
            return None, task_text, current_parent

    return None, None, None


def resolve_role(assigned_to, title=""):
    """Resolves the agent role from the assigned-to field or title keywords."""
    # Direct match first
    if assigned_to and assigned_to in ROLE_MAP:
        return ROLE_MAP[assigned_to]

    # Keyword fallback from title
    search_text = f"{assigned_to} {title}".lower()
    for keyword, role in KEYWORD_FALLBACK.items():
        if keyword in search_text:
            return role

    return "scrum-master"  # Default


def generate_prompt(role, task_id, title, assigned_to):
    """Constructs the prompt for the agent."""
    soul_path = f"{SOULS_DIR}/{role}.md"
    display_name = role.replace("-", " ").title()

    prompt = f"""Act as the **{display_name}**.
Read your soul file `{soul_path}` and `GEMINI.md`.
Check `{TASKS_FILE}` and `{MEMORY_DIR}/` for context.

Your assigned task is:
"""
    if task_id:
        prompt += f"**{task_id}**: {title}\n"
    else:
        prompt += f"**{title}**\n"

    prompt += f"""
Execute this task following the Self-Annealing Protocol:
1. **Validate** — Confirm you have all inputs needed.
2. **Execute** — Perform the work.
3. **Verify** — Self-review against acceptance criteria.
4. **Correct** — Fix any issues found.

When finished:
1. Update the task status to "Done" in `{TASKS_FILE}`.
2. Write a handoff entry in `.agent/memory/` with your completion summary.
3. Log your execution time as `Agent Actual: [X] minutes`.
"""
    return prompt


def main():
    tasks_path = find_tasks_file()
    if not tasks_path:
        print(f"Error: Could not find {TASKS_FILE}")
        sys.exit(1)

    # Try table format first, then checkbox fallback
    task_id, title, assigned_to = get_next_task_from_table(tasks_path)

    if not title:
        task_id, title, assigned_to = get_next_task_from_checkboxes(tasks_path)

    if not title:
        print("✅ No pending tasks found in tasks.md!")
        sys.exit(0)

    role = resolve_role(assigned_to or "", title or "")
    prompt = generate_prompt(role, task_id, title, assigned_to)

    print(prompt)


if __name__ == "__main__":
    main()
