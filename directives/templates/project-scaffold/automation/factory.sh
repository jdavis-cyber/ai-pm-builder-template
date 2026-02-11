#!/bin/bash

# Factory Runner Wrapper
# Usage: ./automation/factory.sh

# Configuration
# Set your preferred CLI tool here (e.g., "claude", "ollama run llama3", "llm").
# Leave empty for "Assisted Mode" (copy/paste).
LLM_COMMAND="" 

echo "🏭 Factory Runner: Starting Continuous Loop..."
echo "Press [CTRL+C] to stop."

while true; do
    echo "---------------------------------------------------"
    echo "🔎 Scanning Task Board..."
    
    # 1. Generate the Prompt
    PROMPT=$(python3 automation/run_factory.py)

    # Check if prompt is empty (no tasks)
    if [ -z "$PROMPT" ]; then
        echo "✅ No pending tasks found. Waiting 10 seconds..."
        sleep 10
        continue
    fi

    echo "🤖 Next Task Identified:"
    echo "$PROMPT"
    echo "---------------------------------------------------"

    # 2. Execute or Assist
    if [ -n "$LLM_COMMAND" ]; then
        echo "🚀 Autonomous Mode: Sending to $LLM_COMMAND..."
        
        # Pipe prompt to LLM and capture output (optional: tee to log)
        echo "$PROMPT" | $LLM_COMMAND
        
        echo "✅ Task execution complete."
        echo "⏳ Cooling down for 5 seconds..."
        sleep 5
    else
        echo "📋 Assisted Mode: Prompt generated above."
        echo "👉 Action: Copy the prompt above, paste into your Agent, and perform the task."
        echo "👉 Then marks the task as [x] in tasks.md to continue."
        echo "⏸️  Pausing loop. Press [Enter] when ready for the next task..."
        read -r
    fi
done
