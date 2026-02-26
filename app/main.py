from fastapi import FastAPI
from fastapi.responses import FileResponse
from app.models.schemas import ResumeRequest, AnalyzeResponse
from app.services.gpt_service import analyze_resume

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="AI Resume Analyzer",
    description="LLM-powered Resume vs Job Description Matching System",
    version="1.0.0"
)

# Enable CORS for the demo frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", include_in_schema=False)
async def read_index():
    return FileResponse("demo.html")

@app.post("/analyze", response_model=AnalyzeResponse)
def analyze(data: ResumeRequest):
    return analyze_resume(
        data.resume_text,
        data.job_description
    )