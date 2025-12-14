---

### 2. `ARCHITECTURE.md`
*The technical blueprint. This proves you built a system, not just a script.*

```markdown
# 🏗️ System Architecture

Veritas moves beyond simple "Prompt-Response" loops by implementing a **Cognitive Cyclic Architecture**.

## 🔄 Data Flow Diagram

```mermaid
User Goal
    │
    ▼
[ 🧠 Planner Agent ] ──(Gemini 3 Reasoning)──> Decomposes Goal into Tasks
    │
    ▼
[ 🌍 Executor Agent ] <──(Loop)──> [ 🔎 DuckDuckGo Search Tool ]
    │                                      │
    │ (Synthesizes Live Data)              │
    ▼                                      ▼
[ 📝 Memory Module ] <─────────────────────┘
    │
    ▼
[ ⚖️ Reviewer Agent ] ──(Self-Reflection)──> Identifies Gaps/Bias
    │
    ▼
[ 📑 Final Reporter ] ──(Critique + Context)──> Verified Answer
🧩 Core Components
1. The Planner (src/planner.py)
Model: gemini-3-pro-preview

Role: Uses advanced reasoning to break vague user queries (e.g., "Is the new iPhone worth it?") into concrete, researchable sub-tasks.

Logic: Prevents the agent from getting overwhelmed by complex prompts.

2. The Executor (src/executor.py)
Role: The "Hands" of the agent.

Tool Use: Autonomously calls the DuckDuckGo Search API when internal knowledge is insufficient.

Context Awareness: Reads from src/memory.py to ensure new searches build upon previous findings.

3. The Reviewer (src/reviewer.py)
Role: The "Conscience" of the agent.

Method: Implements a Reflection Pattern. It reads the gathered data before the final report is written and checks for:

Logical Inconsistencies.

Missing verification for bold claims.

Potential hallucinations.

4. The Tech Stack
LLM: Google Gemini 3 Pro Preview (Selected for Agentic Optimization).

Orchestration: Python & Streamlit.

Search: DuckDuckGo (DDGS).

