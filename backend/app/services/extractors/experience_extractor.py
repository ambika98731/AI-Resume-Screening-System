import re


def extract_experience(text: str) -> int | None:
    """
    Extract the minimum required years of experience.

    Examples:
        2 years  -> 2
        2+ years -> 2
        1-3 years -> 1
    """

    match = re.search(
        r"(\d+)(?:\+|\s*-\s*\d+)?\s*years?",
        text,
        re.IGNORECASE,
    )

    if match:
        return int(match.group(1))

    return None