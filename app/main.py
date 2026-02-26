from fastapi import FastAPI, HTTPException
from app.models.schemas import ResumeRequest
from app.services.gpt_service import analyze_resume

app = FastAPI(
    title="AI Resume Analyzer",
    description="GPT-powered Resume vs Job Description Matching System",
    version="1.0.0"
)

@app.post("/analyze")
async def analyze(data: ResumeRequest):
    try:
        result = await analyze_resume(
            data.resume_text,
            data.job_description
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))