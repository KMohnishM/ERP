import openai
from django.conf import settings

class ERPIntelligenceService:
    def __init__(self):
        self.api_key = getattr(settings, 'OPENAI_API_KEY', None)
        openai.api_key = self.api_key

    def generate_financial_summary(self, transaction_data):
        """Generates an AI summary for financial transactions."""
        prompt = f"Summarize the following financial data and identify trends or anomalies: {transaction_data}"
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

    def optimize_workflow(self, workflow_history):
        """Suggests improvements to approval bottlenecks."""
        prompt = f"Analyze these workflow bottlenecks and suggest optimizations: {workflow_history}"
        # ... logic to call AI and return suggestions
        return "Recommended: Combine Step 2 and 3 for Purchase Requests under $500."
