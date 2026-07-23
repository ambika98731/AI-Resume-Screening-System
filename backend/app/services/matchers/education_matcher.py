def match_education(
    resume_education,
    jd_education,
) -> bool:

    if not resume_education or not jd_education:
        return False

    for edu in resume_education:

        if (
            edu.degree
            and
            edu.degree.lower()
            ==
            jd_education.lower()
        ):
            return True

    return False