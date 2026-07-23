def calculate_overall_score(
    skill_score: float,
    education_match: bool,
    experience_match: bool,
) -> float:

    score = 0

    # Skills → 70%
    score += skill_score * 0.7

    # Education → 15%
    if education_match:
        score += 15

    # Experience → 15%
    if experience_match:
        score += 15

    return round(score, 2)