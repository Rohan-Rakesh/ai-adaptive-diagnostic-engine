from openai import OpenAI
from app.core.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)


def generate_study_plan(missed_topics):

    prompt = f"""
Student finished an adaptive GRE diagnostic test.

Weak topics:
{missed_topics}

Generate a concise 3 step study plan to improve performance.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
