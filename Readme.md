# 🕵️‍♂️ Veritas: Autonomous Fact-Checking Agent

**Powered by Google Gemini 3 Pro Preview & Live Web Search**

Veritas is a next-generation **Agentic AI** designed to combat misinformation. Unlike standard chatbots that rely on frozen training data, Veritas uses a cognitive architecture to **Plan**, **Research** the live web, and **Self-Correct** its own findings using Gemini 3's advanced reasoning capabilities.

## 🌟 Why Veritas?
* **🧠 Gemini 3 Intelligence:** built on `gemini-3-pro-preview`, utilizing next-gen "Deep Think" reasoning for complex planning.
* **🌍 Live Internet Access:** Integrates `DuckDuckGo` search tools to fetch real-time events and data.
* **🛡️ Self-Healing Architecture:** Features a dedicated **Reviewer Agent** that critiques and fixes errors before the user sees the result.
* **👁️ Transparent Logic:** The UI visualizes the agent's thinking process, showing you exactly how it reaches a conclusion.

## 🚀 Quick Start

### 1. Prerequisites
* Python 3.9+
* A Google AI Studio API Key (with access to Gemini 3 Preview)

### 2. Installation
```bash
# Clone the repo
git clone [https://github.com/yourusername/veritas-agent.git](https://github.com/yourusername/veritas-agent.git)
cd veritas-agent

# Install dependencies
pip install -r requirements.txt

### 3. Configuration
Create a .env file in the root directory and add your API key:
OR
during uploading zip repo file on share.streamlit.io you will see "advanced settings" there you can put api key.
OR
after deployed app successfully on streamlit.io you can go to manage app -> settings -> secrets there you can put api key.

Code snippet

GEMINI_API_KEY=your_actual_api_key_here

### 4. Run the Agent
Launch the web interface:

Bash


streamlit run app.py

### 3. Testing link
App Testing Link : https://prince-radadiya-aqwyzzmbzh24wtvvmmijti.streamlit.app/


