from fastapi import APIRouter, Body

from app.services.parser_service import parse_resume
from app.services.jd_parser_service import parse_job_description
from app.services.matching_service import match_resume

from app.schemas.matching_request import MatchingRequest

from app.services.interview_service import generate_interview_questions
from app.services.recommendation_service import generate_recommendations

from app.services.summary_service import generate_summary

from app.services.improvement_service import generate_improvements

from app.services.semantic_matching_service import calculate_semantic_similarity

router = APIRouter()

@router.post("/match")
def match(request: MatchingRequest):

    resume = parse_resume(request.resume_text)

    jd = parse_job_description(request.job_description)

    result = match_resume(resume, jd)

    semantic_similarity = calculate_semantic_similarity(
        request.resume_text,
        request.job_description
    )

    recommendation = generate_recommendations(result)

    interview = generate_interview_questions(result)

    summary = generate_summary(resume, result)

    improvements = generate_improvements(
        resume,
        result
    )

    return {
        "resume": resume,
        "job_description": jd,
        "matching": result,
        "semantic_matching": semantic_similarity,
        "recommendation": recommendation,
        "interview_questions": interview,
        "summary": summary,
        "improvements": improvements
    }