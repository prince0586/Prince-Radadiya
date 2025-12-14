import streamlit as st
import os
import time
from dotenv import load_dotenv
import google.generativeai as genai

# Local imports
from src.memory import Memory
from src.planner import Planner
from src.executor import Executor
from src.reviewer import Reviewer

# Page Config
st.set_page_config(page_title="Veritas AI (Gemini 3)", page_icon="🕵️‍♂️", layout="wide")

# Load Secrets
load_dotenv()
if "GEMINI_API_KEY" not in os.environ:
    st.error("Please set GEMINI_API_KEY in .env file")
    st.stop()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# --- UPDATE START ---
# Using the latest Gemini 3 Pro Preview model
# This model has enhanced reasoning ("Deep Think") and agentic capabilities.
model = genai.GenerativeModel('gemini-3-pro-preview')
# --- UPDATE END ---

# Custom CSS
st.markdown("""
<style>
    .stApp { background-color: #0E1117; color: #FAFAFA; }
    .report-box { border: 1px solid #4CAF50; padding: 20px; border-radius: 10px; background-color: #1E1E1E; }
    .critique-box { border: 1px solid #FF4B4B; padding: 15px; border-radius: 10px; background-color: #2D1E1E; margin-bottom: 20px; }
</style>
""", unsafe_allow_html=True)

# UI Header
st.title("🕵️‍♂️ Veritas: Autonomous Fact-Checking Agent")
st.caption("Powered by **Gemini 3 Pro Preview** & DuckDuckGo Search")

# Input
user_query = st.text_input("Enter a claim to investigate:", placeholder="e.g., 'Is it true that sharks are immune to cancer?'")

if st.button("🚀 Start Investigation"):
    if not user_query:
        st.warning("Please enter a topic.")
    else:
        # Init Modules
        memory = Memory()
        planner = Planner(model)
        executor = Executor(model)
        reviewer = Reviewer(model)
        
        # PHASE 1: PLANNING
        with st.status("🧠 Phase 1: Strategic Planning (Gemini 3)...", expanded=True) as status:
            plan = planner.create_plan(user_query)
            for task in plan:
                st.write(f"• {task}")
            status.update(label="✅ Planning Complete", state="complete", expanded=False)
        
        # PHASE 2: EXECUTION
        with st.status("🌍 Phase 2: Live Research...", expanded=True) as status:
            progress = st.progress(0)
            for i, task in enumerate(plan):
                st.write(f"**Investigating:** {task}")
                context = memory.get_context()
                result = executor.execute_task(task, context)
                memory.store_finding(task, result)
                with st.expander(f"Findings for Step {i+1}"):
                    st.info(result)
                progress.progress((i + 1) / len(plan))
            status.update(label="✅ Research Complete", state="complete", expanded=False)

        # PHASE 3: REFLECTION
        st.divider()
        st.subheader("🧐 Phase 3: Gemini 3 Reflection")
        with st.spinner("Gemini 3 is reviewing logic and bias..."):
            critique = reviewer.review_findings(user_query, memory.get_full_report())
        st.markdown(f'<div class="critique-box"><h4>⚠️ Reviewer Notes</h4>{critique}</div>', unsafe_allow_html=True)

        # PHASE 4: REPORT
        st.subheader("📑 Final Verified Report")
        with st.spinner("Compiling final document..."):
            final_report = executor.generate_final_response(user_query, memory.get_full_report(), critique)
        st.markdown(f'<div class="report-box">{final_report}</div>', unsafe_allow_html=True)