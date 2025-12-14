import google.generativeai as genai
import json

class Reviewer:
    def __init__(self, model):
        self.model = model

    def review_findings(self, original_goal, memory_data):
        prompt = f"""
        You are a Quality Assurance AI.
        User Goal: "{original_goal}"
        Collected Data: {json.dumps(memory_data, indent=2)}
        
        Task: 
        1. Check if the data fully answers the goal.
        2. Identify bias, missing context, or logic gaps.
        
        Output: A concise set of critique notes (max 3 bullet points).
        """
        response = self.model.generate_content(prompt)
        return response.text.strip()