from app.schemas.matching_schema import MatchingSchema
from app.schemas.recommendation_schema import RecommendationSchema


def generate_recommendations(
    matching: MatchingSchema,
) -> RecommendationSchema:

    result = RecommendationSchema()

    # -------------------------
    # Strengths
    # -------------------------

    for skill in matching.matched_skills:
        result.strengths.append(
            f"Strong knowledge of {skill}"
        )

    # -------------------------
    # Weaknesses
    # -------------------------

    for skill in matching.missing_skills:
        result.weaknesses.append(
            f"Missing required skill: {skill}"
        )

    # -------------------------
    # Skill Recommendations
    # -------------------------

    for skill in matching.missing_skills:
        result.recommendations.append(
            f"Learn {skill} to improve your resume."
        )

    # -------------------------
    # Education Recommendation
    # -------------------------

    if not matching.education_match:
        result.recommendations.append(
            "Consider obtaining the required educational qualification."
        )

    # -------------------------
    # Experience Recommendation
    # -------------------------

    if not matching.experience_match:
        result.recommendations.append(
            "Gain more relevant work experience."
        )

    return result