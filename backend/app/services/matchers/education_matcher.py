def match_education(
    resume_education,
    jd_education,
) -> bool:

    if not resume_education or not jd_education:
        return False

    jd = jd_education.lower()

    for edu in resume_education:

        if not edu.degree:
            continue

        degree = edu.degree.lower()

        # Bachelor's matching
        if (
            "bachelor" in degree
            or "b.tech" in degree
            or "btech" in degree
            or "b.e" in degree
            or "be" in degree
        ):
            if "bachelor" in jd:
                return True

        # Master's matching
        if (
            "master" in degree
            or "m.tech" in degree
            or "mtech" in degree
            or "m.e" in degree
            or "me" in degree
        ):
            if "master" in jd:
                return True

        # PhD matching
        if (
            "phd" in degree
            or "doctor" in degree
        ):
            if "phd" in jd or "doctor" in jd:
                return True

    return False
