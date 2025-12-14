import google.generativeai as genai
import json
from duckduckgo_search import DDGS

class Executor:
    def __init__(self, model):
        self.model = model
        self.search_tool = DDGS()

    def perform_web_search(self, query):
        """Fetches real-time search results."""
        try:
            # Get top 3 results
            results = self.search_tool.text(query, max_results=3)
            if not results:
                return "No search results found."
            
            search_summary = ""
            for r in results:
                search_summary += f"- Title: {r['title']}\n  Snippet: {r['body']}\n"
            return search_summary
        except Exception as e:
            return f"Search Error: {e}"

    def execute_task(self, task, context):
        """Decides if search is needed, searches, then synthesizes."""
        
        # 1. Search the web
        raw_search_data = self.perform_web_search(task)

        # 2. Synthesize with LLM
        prompt = f"""
        You are a Research Executor Agent.
        Task: {task}
        Context: {context}
        
        REAL-TIME WEB SEARCH RESULTS:
        {raw_search_data}
        
        Instructions:
        1. Answer the task using the WEB SEARCH RESULTS.
        2. Keep it factual and concise (max 3 sentences).
        """
        
        response = self.model.generate_content(prompt)
        return response.text.strip()

    def generate_final_response(self, original_goal, memory_data, critique_notes):
        prompt = f"""
        You are the Final Reporter.
        Original Goal: {original_goal}
        Collected Data: {json.dumps(memory_data, indent=2)}
        
        *** CRITICAL QUALITY CONTROL NOTES (Must Address) ***
        {critique_notes}
        
        Task: Write a final, coherent report. Explicitly fix any issues raised in the notes.
        """
        response = self.model.generate_content(prompt)
        return response.text