from app.schemas.project import Project


def match_projects(
    resume_projects: list[Project],
    jd_skills: list[str],
):
    """
    Match project technologies
    with required JD skills.
    """

    matched = []

    missing = []

    project_tech = set()

    for project in resume_projects:
        project_tech.update(
            tech.lower()
            for tech in project.technologies
        )

    for skill in jd_skills:

        if skill.lower() in project_tech:
            matched.append(skill)

        else:
            missing.append(skill)

    score = 0

    if jd_skills:
        score = round(
            len(matched) /
            len(jd_skills) * 100,
            2,
        )

    return matched, missing, score