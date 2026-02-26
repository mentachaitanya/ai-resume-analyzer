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
    jd_intelligence: dict # Hunter Step
    gap_matrix: List[dict] # Matrix Step
    red_flags: List[str] # Critic Step
    tailored_resume: str # Architect Step
    scores: dict # Multi-dimensional scoring
    hiring_probability: str
    confidence_explanation: str
    strategic_roadmap: dict # Improvement Step