import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

MODEL = "openai/gpt-4o-mini"  # You can change model later


def analyze_resume(resume_text: str, job_description: str) -> dict:

    prompt = f"""
Analyze the resume against the job description.

Return strictly valid JSON:
{{
  "match_percentage": number,
  "missing_skills": [],
  "strengths": [],
  "improvement_suggestions": []
}}

Resume:
{resume_text[:800]}

Job Description:
{job_description[:800]}
"""

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are a recruitment AI assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
        )

        content = response.choices[0].message.content.strip()

        return json.loads(content)

    except Exception:
        return {
            "match_percentage": 75,
            "missing_skills": ["Cloud deployment"],
            "strengths": ["Python", "REST APIs"],
            "improvement_suggestions": ["Add production deployment"],
            "note": "Mock fallback response"
        }