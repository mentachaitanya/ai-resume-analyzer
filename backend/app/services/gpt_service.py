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
                {"role": "system", "content": "You are a recruitment AI assistant. You must respond ONLY with a valid JSON object."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
        )

        content = response.choices[0].message.content.strip()

        # Clean JSON if model wrapped it in markdown
        if content.startswith("```json"):
            content = content.replace("```json", "").replace("```", "").strip()
        elif content.startswith("```"):
            content = content.replace("```", "").strip()

        return json.loads(content)

    except Exception as e:
        print(f"ERROR in analyze_resume: {str(e)}")
        return {
            "match_percentage": 75,
            "missing_skills": ["Cloud deployment"],
            "strengths": ["Python", "REST APIs"],
            "improvement_suggestions": ["Add production deployment"],
            "note": f"Mock fallback response due to: {str(e)}"
        }


def tailor_resume(resume_text: str, job_description: str) -> dict:
    prompt = f"""
You are an Elite Resume Strategist, Senior Technical Recruiter, and ATS Optimization Architect combined.

MISSION: Analyze the JD and resume to generate a strategic, high-accuracy rewrite WITHOUT fabricating experience.

RULES:
- NEVER invent skills or responsibilities.
- Use formula: [Power Action Verb] + [Technical Context] + [Scale or Scope] + [Measurable Impact].
- classify requirements into Must-Have, High-Impact, Nice-to-Have.

Return strictly valid JSON:
{{
  "jd_intelligence": {{
    "must_have": [],
    "high_impact": [],
    "nice_to_have": [],
    "seniority_signals": "description",
    "hidden_expectations": []
  }},
  "gap_matrix": [
    {{
      "requirement": "skill/duty",
      "status": "Yes/Partial/No",
      "evidence": "from resume",
      "severity": "Low/Medium/High"
    }}
  ],
  "red_flags": ["repetition", "lack of metrics", "etc"],
  "tailored_resume": "Markdown formatted full resume",
  "scores": {{
    "keyword_match": 0-100,
    "semantic_alignment": 0-100,
    "seniority_alignment": 0-100,
    "strategic_match": 0-100
  }},
  "hiring_probability": "Low/Medium/High",
  "confidence_explanation": "why",
  "strategic_roadmap": {{
    "skills_to_learn": [],
    "projects_to_build": [],
    "positioning_advice": "text"
  }}
}}

Resume:
{resume_text[:2500]}

Job Description:
{job_description[:2500]}
"""
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are a world-class Elite Career Strategist. Output ONLY valid JSON."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
        )

        content = response.choices[0].message.content.strip()
        if content.startswith("```json"):
            content = content.replace("```json", "").replace("```", "").strip()

        return json.loads(content)

    except Exception as e:
        print(f"ERROR in elite_tailor: {str(e)}")
        # Return structured fallback
        return {{
            "jd_intelligence": {{"must_have": ["Error"]}},
            "gap_matrix": [],
            "red_flags": [str(e)],
            "tailored_resume": "Error processing request.",
            "scores": {{"strategic_match": 0}},
            "hiring_probability": "N/A",
            "confidence_explanation": "API Error",
            "strategic_roadmap": {{"skills_to_learn": []}}
        }}
