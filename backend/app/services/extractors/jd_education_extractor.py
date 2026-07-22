from app.utils.degrees import DEGREES


def extract_education_requirement(text: str) -> str | None:
    """
    Extract the highest education requirement
    mentioned in a Job Description.
    """

    text = text.lower()

    for degree in DEGREES:
        if degree.lower() in text:
            return degree

    return None