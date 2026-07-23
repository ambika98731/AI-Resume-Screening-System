from fastapi import APIRouter, Body

from app.services.parser_service import parse_resume
from app.services.jd_parser_service import parse_job_description
from app.services.matching_service import match_resume

from app.schemas.matching_request import MatchingRequest
router = APIRouter()

@router.post("/match")
def match(request: MatchingRequest):

    resume = parse_resume(request.resume_text)

    jd = parse_job_description(request.job_description)

    result = match_resume(resume, jd)

    return {
        "resume": resume,
        "job_description": jd,
        "matching": result
    }