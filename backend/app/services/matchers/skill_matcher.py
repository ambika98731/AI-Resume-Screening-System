def match_skills(
    resume_skills: list[str],
    jd_skills: list[str],
):
    resume_set = {
        skill.lower()
        for skill in resume_skills
    }

    jd_set = {
        skill.lower()
        for skill in jd_skills
    }

    matched = sorted(
        resume_set & jd_set
    )

    missing = sorted(
        jd_set - resume_set
    )

    score = 0

    if jd_set:
        score = round(
            len(matched)
            / len(jd_set)
            * 100,
            2,
        )

    return matched, missing, score