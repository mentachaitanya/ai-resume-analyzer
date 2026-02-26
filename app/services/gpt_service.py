import os
import json
import re
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def analyze_resume(resume_text: str, job_description: str) -> dict:
    prompt = f"""
Analyze the resume against the job description.

Return valid JSON with:
match_percentage,
missing_skills,
strengths,
improvement_suggestions.

Resume:
{resume_text[:800]}

Job Description:
{job_description[:800]}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
        )

        content = response.text.strip()

        content = re.sub(r"^```json|```$", "", content).strip()

        return json.loads(content)

    except Exception:
        # Fallback for testing / quota issues
        return {
            "match_percentage": 75,
            "missing_skills": ["Cloud deployment"],
            "strengths": ["Python", "REST APIs"],
            "improvement_suggestions": ["Add AI-based project"],
            "note": "Mock fallback response"
        }