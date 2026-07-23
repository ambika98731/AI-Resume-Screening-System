from app.schemas.matching_schema import MatchingSchema
from app.services.recommendation_service import generate_recommendations


matching = MatchingSchema(
    matched_skills=[
        "python",
        "fastapi",
        "docker",
    ],
    missing_skills=[
        "redis",
        "postgresql",
    ],
    skill_score=60,
    education_match=True,
    experience_match=False,
    overall_score=57,
)

result = generate_recommendations(matching)

print(result.model_dump())