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
    # Use a larger chunk of text, gpt-4o-mini has 128k context
    resume_chunk = resume_text[:50000]
    jd_chunk = job_description[:50000]

    prompt = f"""
Deeply analyze the following Resume against the Job Description.

SCORING RULES:
1. PRECISION: If a skill is listed in the Resume (even in a simple 'Skills' list), it is a MATCH. Do not mark it as missing.
2. EVIDENCE: Identify exact mentions.
3. FAIRNESS: Be critical of seniority gaps but inclusive of technical keywords.

Return strictly valid JSON:
{{
  "match_percentage": number,
  "missing_skills": ["Skills from JD not found anywhere in resume"],
  "strengths": ["Strongest matches between Resume and JD"],
  "improvement_suggestions": ["Actionable steps to improve matching"]
}}

Resume:
{resume_chunk}

Job Description:
{jd_chunk}
"""

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are a professional Recruitment Analyst. You perform deep semantic analysis of resumes. Always respond in valid JSON."},
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
- NEVER invent skills, education, or responsibilities that are not in the original resume.
- CRITICAL: Do NOT add quantifiable metrics (percentages, numbers, users) unless they exist in the source resume.
- Use formula: [Power Action Verb] + [Technical Context] + [Scale or Scope] + [Measurable Impact] ONLY if factual details permit.
- If details are sparse, do NOT fabricate them. Keep it brief.
- Classify requirements into Must-Have, High-Impact, Nice-to-Have.
- ACCURACY: If a skill exists in the resume's 'Skills' section, status must be 'Yes' or 'Partial', NEVER 'No'.
- SCALE: Evaluate if the candidate has worked at the required scale (e.g., millions of users).

Return strictly valid JSON:
{{
  "jd_intelligence": {{
    "must_have": ["Direct technical requirements from JD"],
    "high_impact": ["Soft skills or desirable traits from JD"],
    "nice_to_have": ["Bonus skills from JD"],
    "seniority_signals": "Description of seniority level expected",
    "hidden_expectations": ["What the recruiter is looking for but didn't explicitly say"]
  }},
  "gap_matrix": [
    {{
      "requirement": "skill/duty",
      "status": "Yes/Partial/No",
      "evidence": "Mention from resume or reason for partial/no",
      "severity": "Low/Medium/High"
    }}
  ],
  "red_flags": ["Repetition, lack of metrics, gaps, or domain mismatch"],
  "tailored_resume": "STRATEGIC REWRITE: A full Markdown formatted resume. REWRITE the profile summary and bullet points to emphasize relevant skills from the JD. DO NOT add skills, degrees, or metrics that are not in the source text. If a section is sparse, leave it sparse.",
  "scores": {{
    "keyword_match": 0-100,
    "semantic_alignment": 0-100,
    "seniority_alignment": 0-100,
    "strategic_match": 0-100
  }},
  "hiring_probability": "Low/Medium/High",
  "confidence_explanation": "Detailed explanation of why this match score was given",
  "strategic_roadmap": {{
    "skills_to_learn": ["Specific skills from JD that are missing"],
    "projects_to_build": ["Mini-projects to demonstrate missing skills"],
    "positioning_advice": "How to talk about this pivot in an interview"
  }}
}}

Resume:
{resume_text[:50000]}

Job Description:
{job_description[:50000]}
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
