from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from app.models.schemas import ResumeRequest, AnalyzeResponse, TailorResponse
from app.services.gpt_service import analyze_resume, tailor_resume
from app.services.pdf_parser import extract_text_from_pdf

app = FastAPI(
    title="AI Resume Analyzer",
    description="LLM-powered Resume vs Job Description Matching System",
    version="2.0.0"
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


@app.post("/analyze-pdf", response_model=AnalyzeResponse)
def analyze_pdf(
    file: UploadFile = File(...),
    job_description: str = ""
):
    resume_text = extract_text_from_pdf(file.file)

    return analyze_resume(
        resume_text,
        job_description
    )


@app.post("/tailor", response_model=TailorResponse)
def tailor(data: ResumeRequest):
    return tailor_resume(
        data.resume_text,
        data.job_description
    )


@app.post("/tailor-pdf", response_model=TailorResponse)
def tailor_pdf(
    file: UploadFile = File(...),
    job_description: str = ""
):
    resume_text = extract_text_from_pdf(file.file)
    return tailor_resume(
        resume_text,
        job_description
    )