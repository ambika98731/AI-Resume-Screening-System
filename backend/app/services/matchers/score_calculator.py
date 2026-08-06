def calculate_overall_score(
    skill_score: float,
    project_score: float,
    education_match: bool,
    experience_match: bool,
) -> float:

    score = 0

    # Skills → 50%
    score += skill_score * 0.50

    # Projects → 20%
    score += project_score * 0.20

    # Education → 15%
    if education_match:
        score += 15

    # Experience → 15%
    if experience_match:
        score += 15

    return round(score, 2)