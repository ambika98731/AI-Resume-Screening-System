from app.schemas.personal_info import PersonalInfo
from app.schemas.resume_schema import ResumeSchema
from app.schemas.matching_schema import MatchingSchema
from app.services.summary_service import generate_summary

resume = ResumeSchema(
    personal_info=PersonalInfo(
        name="John Doe"
    )
)

matching = MatchingSchema(
    matched_skills=[
        "python",
        "fastapi",
        "docker"
    ],
    missing_skills=[
        "postgresql",
        "redis"
    ],
    skill_score=60,
    education_match=True,
    experience_match=False,
    overall_score=57
)

result = generate_summary(
    resume,
    matching
)

print(result.model_dump())