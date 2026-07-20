import json

from app.ai.llm import client
from app.ai.prompts import SYSTEM_PROMPT


class TicketAnalyzer:

    @staticmethod
    def analyze(title: str, description: str):

        prompt = f"""
Title:
{title}

Description:
{description}
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"{SYSTEM_PROMPT}\n\n{prompt}",
        )

        text = response.text.strip()

        # Remove markdown if Gemini wraps JSON in ```json
        if text.startswith("```json"):
            text = text.replace("```json", "").replace("```", "").strip()

        elif text.startswith("```"):
            text = text.replace("```", "").strip()

        return json.loads(text)