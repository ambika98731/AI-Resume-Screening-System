import re


def extract_experience(text: str) -> str | None:
    """
    Extract experience requirement from a job description.

    Examples:
    - 2 years
    - 2+ years
    - 1-3 years
    """

    match = re.search(
        r"(\d+\+?\s*(?:-\s*\d+)?\s*years?)",
        text,
        re.IGNORECASE,
    )

    if match:
        return match.group(1)

    return None