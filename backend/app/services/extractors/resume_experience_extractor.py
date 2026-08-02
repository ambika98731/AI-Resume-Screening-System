import re


def extract_resume_experience(text: str) -> int | None:
    """
    Extract years of experience from the resume.

    Examples:
        3 years
        5+ years
        2 yrs
    """

    match = re.search(
        r"(\d+)(?:\+)?\s*(?:years?|yrs?)",
        text,
        re.IGNORECASE,
    )

    if match:
        return int(match.group(1))

    return None