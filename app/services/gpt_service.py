import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_resume(resume_text: str, job_description: str):

    prompt = f"""
You are an AI recruitment assistant.

Analyze the resume against the job description.

Return STRICTLY in JSON format:
{{
  "match_percentage": number,
  "missing_skills": [],
  "strengths": [],
  "improvement_suggestions": []
}}

Resume:
{resume_text}

Job Description:
{job_description}
"""

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )

    content = response.text

    try:
        return json.loads(content)
    except:
        return {"raw_output": content}