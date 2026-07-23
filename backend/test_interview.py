from app.schemas.matching_schema import MatchingSchema
from app.services.interview_service import generate_interview_questions


matching = MatchingSchema(
    matched_skills=[
        "python",
        "fastapi",
        "docker"
    ]
)

result = generate_interview_questions(matching)

print(result.model_dump())