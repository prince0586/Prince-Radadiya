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
        
        try:
            # Generate content
            response = self.model.generate_content(prompt)
            
            # Check if response is valid before accessing .text
            if response.parts:
                return response.text.strip()
            else:
                # If blocked by safety filters, return a manual warning
                return "⚠️ The Reviewer detected potential sensitivities and withheld the critique. Proceeding with available data."
                
        except ValueError:
            # This catches the specific "ValueError" from your screenshot
            return "⚠️ Reviewer output was blocked by safety settings. (Standard automated check)."
        except Exception as e:
            return f"⚠️ Reviewer Error: {str(e)}"
