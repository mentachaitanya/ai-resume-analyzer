from pydantic import BaseModel, Field
from typing import List, Optional

class ResumeRequest(BaseModel):
    resume_text: str = Field(..., min_length=50)
    job_description: str = Field(..., min_length=50)


class AnalyzeResponse(BaseModel):
    match_percentage: float = Field(..., ge=0, le=100)
    missing_skills: List[str] = Field(default_factory=list)
    strengths: List[str] = Field(default_factory=list)
    improvement_suggestions: List[str] = Field(default_factory=list)
    note: Optional[str] = None


class TailorResponse(BaseModel):
    tailored_resume: str
    key_changes: List[str]
    optimization_score: int