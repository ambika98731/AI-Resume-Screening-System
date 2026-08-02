def match_experience(
    resume_experience: int | None,
    jd_experience: int | None,
) -> bool:
    """
    Compare candidate experience with
    the minimum experience required
    by the Job Description.
    """

    # No experience required in JD
    if jd_experience is None:
        return True

    # Candidate has no experience
    if resume_experience is None:
        return False

    return resume_experience >= jd_experience