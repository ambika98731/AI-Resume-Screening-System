from pydantic import BaseModel


class MatchingRequest(BaseModel):
    resume_text: str
    job_description: str