from app.schemas.resume_schema import ResumeSchema
from app.schemas.personal_info import PersonalInfo
from app.schemas.matching_schema import MatchingSchema
from app.services.improvement_service import generate_improvements


resume = ResumeSchema(
    personal_info=PersonalInfo(
        name="John Doe",
        github=None,
        linkedin=None,
    )
)

matching = MatchingSchema(
    matched_skills=[
        "python",
        "fastapi",
        "docker",
    ],
    missing_skills=[
        "postgresql",
        "redis",
    ],
    skill_score=60,
    education_match=True,
    experience_match=False,
    overall_score=57,
)

result = generate_improvements(
    resume,
    matching,
)

print(result.model_dump())