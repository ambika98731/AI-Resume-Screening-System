from fastapi import APIRouter, Body

from app.services.parser_service import parse_resume
from app.services.jd_parser_service import parse_job_description
from app.services.matching_service import match_resume

from app.schemas.matching_request import MatchingRequest

from app.services.interview_service import generate_interview_questions
from app.services.recommendation_service import generate_recommendations

router = APIRouter()

@router.post("/match")
def match(request: MatchingRequest):

    resume = parse_resume(request.resume_text)

    jd = parse_job_description(request.job_description)

    result = match_resume(resume, jd)

    recommendation = generate_recommendations(result)

    interview = generate_interview_questions(result)

    return {
        "resume": resume,
        "job_description": jd,
        "matching": result,
        "recommendation": recommendation,
        "interview_questions": interview,
    }