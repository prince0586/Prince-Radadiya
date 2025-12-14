import google.generativeai as genai
import json

class Planner:
    def __init__(self, model):
        self.model = model

    def create_plan(self, user_goal):
        """Breaks the user goal into 3 distinct steps."""
        prompt = f"""
        You are a Strategic Planning Agent.
        User Goal: "{user_goal}"
        
        Task: Break this goal into 3 distinct, sequential research sub-tasks.
        Return ONLY a raw JSON list of strings.
        Example: ["Define X", "Search recent news on X", "Analyze impact"]
        """
        
        try:
            response = self.model.generate_content(prompt)
            clean_text = response.text.replace("```json", "").replace("```", "").strip()
            return json.loads(clean_text)
        except Exception as e:
            return ["Gather general background info", "Search for specific details", "Summarize findings"]