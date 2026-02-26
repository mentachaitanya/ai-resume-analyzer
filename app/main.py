from fastapi import FastAPI
from app.models.schemas import ResumeRequest, AnalyzeResponse
from app.services.gpt_service import analyze_resume

app = FastAPI(
    title="AI Resume Analyzer",
    description="LLM-powered Resume vs Job Description Matching System",
    version="1.0.0"
)

@app.post("/analyze", response_model=AnalyzeResponse)
def analyze(data: ResumeRequest):
    return analyze_resume(
        data.resume_text,
        data.job_description
    )