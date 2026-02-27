from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import FileResponse, StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from app.models.schemas import ResumeRequest, AnalyzeResponse, TailorResponse
from app.services.gpt_service import analyze_resume, tailor_resume
from app.services.pdf_parser import extract_text_from_pdf
from app.services.pdf_generator import generate_resume_pdf
import io
import urllib.parse
from pathlib import Path

# Get the root directory (one level up from backend/)
ROOT_DIR = Path(__file__).resolve().parent.parent.parent
FRONTEND_PATH = ROOT_DIR / "frontend" / "index.html"

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
    return FileResponse(FRONTEND_PATH)


@app.post("/extract-text")
def extract_text(file: UploadFile = File(...)):
    text = extract_text_from_pdf(file.file)
    return {"text": text}


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


@app.post("/download-pdf")
async def download_pdf(resume_text: str = Form(...)):
    # Basic PDF generation from tailored text
    pdf_buffer = generate_resume_pdf(resume_text)
    
    return StreamingResponse(
        pdf_buffer,
        media_type="application/pdf",
        headers={"Content-Disposition": "attachment; filename=Tailored_Resume.pdf"}
    )