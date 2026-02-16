#!/usr/bin/env python3
"""
Factory Runner — The Autonomous Agent Loop.

Parses orchestration/tasks.md (rich format) to find the next open task,
determines the correct agent role, and generates a ready-to-use prompt.

Usage:
    python3 automation/run_factory.py
"""

import os
import re
import sys

# Configuration
TASKS_FILE = "orchestration/tasks.md"
MEMORY_DIR = "memory"
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
    return None


def get_next_task_from_rich_format(tasks_path):
    """
    Parses the rich-format orchestration/tasks.md or similiar.
    Looks for tasks under '## Backlog' or '## In Progress'.
    Matches format: '### TASK-XXX: Task Title'
    Extracts 'Assigned To' and description.
    """
    with open(tasks_path, "r") as f:
        lines = f.readlines()

    task_id = None
    title = None
    assigned_to = None
    
    # Simple state machine
    current_section = None # 'Backlog' | 'In Progress' | 'Done' | 'Blocked'
    
    for line in lines:
        stripped = line.strip()
        
        # Section detection
        if stripped.startswith("## Backlog"):
            current_section = "Backlog"
            continue
        elif stripped.startswith("## In Progress"):
            current_section = "In Progress"
            continue
        elif stripped.startswith("## Done") or stripped.startswith("## Blocked"):
            current_section = "Done" # Or blocked, basically stop looking effectively for new work here if we prioritize Backlog/InProgress
            continue

        # We only care about Backlog or In Progress for fetching the NEXT task
        if current_section in ["Backlog", "In Progress"]:
            # Task Header: ### TASK-001: Define Project Requirements
            if stripped.startswith("### TASK-"):
                parts = stripped.replace("###", "").strip().split(":", 1)
                if len(parts) == 2:
                    t_id = parts[0].strip()
                    t_title = parts[1].strip()
                    
                    # We found a task. Is it assigned or actionable? 
                    # For this simple runner, we pick the FIRST one we see.
                    # Ideally we might look for 'Unassigned' or specific agent, but let's grab it.
                    task_id = t_id
                    title = t_title
                    assigned_to = "scrum-master" # Default until we find the line
                    
                    # Look ahead for "Assigned To"
                    # We can return immediately once we find the ID/Title, or scan a few lines for assignment.
                    # But the function needs to return ONE task.
                    # Let's scan forward in list to find details for THIS task.
                    # A better way is to iterate line by line and capture state.
                    pass 
                
            if task_id and stripped.lower().startswith("**assigned to**:"):
                # **Assigned To**: Unassigned (recommend Requirements BA)
                val = stripped.split(":", 1)[1].strip()
                # Clean up "Unassigned (recommend X)" -> "X"
                if "recommend" in val:
                     # Extract what's inside parenthesis or after 'recommend'
                     # heuristic: 'Unassigned (recommend User Story BA)' -> 'User Story BA'
                     match = re.search(r"recommend\s+([A-Za-z\s]+)\)", val)
                     if match:
                         val = match.group(1)
                
                assigned_to = val
                
                # We have ID, Title, Assignment. We are good to go.
                return task_id, title, assigned_to

    return None, None, None


def resolve_role(assigned_to, title=""):
    """Resolves the agent role from the assigned-to field or title keywords."""
    
    clean_assigned = assigned_to.strip()
    
    # Direct match first (exact)
    if clean_assigned in ROLE_MAP:
        return ROLE_MAP[clean_assigned]
        
    # Partial match in ROLE_MAP keys
    for key in ROLE_MAP:
        if key in clean_assigned:
            return ROLE_MAP[key]

    # Keyword fallback from title
    search_text = f"{clean_assigned} {title}".lower()
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
1. Deposit all relevant knowledge (diagrams, specs, interview notes) into the appropriate sub-folder in `/docs/`.
2. Create a `verify.md` artifact in `/docs/verification/` following the template in `directives/templates/verify.md`.
3. Update the task status to "Done" in `{TASKS_FILE}`.
   - Move the task from its current section to `## Done`.
   - Update `**Completed**:` field with today's date.
4. Write a handoff entry in `{MEMORY_DIR}/` with your completion summary.
5. Log your execution time as `Agent Actual: [X] minutes`.
"""
    return prompt


def main():
    tasks_path = find_tasks_file()
    if not tasks_path:
        print(f"Error: Could not find {TASKS_FILE}")
        sys.exit(1)

    # Use the rich format parser
    task_id, title, assigned_to = get_next_task_from_rich_format(tasks_path)

    if not title:
        print("✅ No pending tasks found in orchestrated tasks.md!")
        sys.exit(0)

    role = resolve_role(assigned_to or "", title or "")
    prompt = generate_prompt(role, task_id, title, assigned_to)

    print(prompt)


if __name__ == "__main__":
    main()
