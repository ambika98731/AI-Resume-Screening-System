from pydantic import BaseModel
from datetime import datetime


class AnalysisBase(BaseModel):

    candidate_name: str | None = None

    email: str | None = None

    job_title: str | None = None

    overall_score: float

    semantic_score: float

    matched_skills: str

    missing_skills: str

    summary: str

    recommendation: str


class AnalysisCreate(AnalysisBase):
    pass


class AnalysisResponse(AnalysisBase):

    id: int

    created_at: datetime

    class Config:
        from_attributes = True