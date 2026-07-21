from app.utils.degrees import DEGREES
from app.utils.patterns import YEAR_PATTERN, CGPA_PATTERN


def extract_education(text: str):
    """
    Extract education details from resume text.
    """

    education = []

    text_lower = text.lower()
    lines = text.splitlines()

    degree = None
    institution = None
    year = None
    cgpa = None

    # Detect degree
    for d in DEGREES:
        if d in text_lower:
            degree = d.upper()
            break

    # Detect institution
    for line in lines:

        clean = line.strip()

        if (
            "university" in clean.lower()
            or "college" in clean.lower()
            or "institute" in clean.lower()
            or "school" in clean.lower()
        ):
            institution = clean
            break

    # Detect year

    year_match = YEAR_PATTERN.search(text)

    if year_match:
        year = year_match.group()

    # Detect CGPA

    cgpa_match = CGPA_PATTERN.search(text)

    if cgpa_match:
        cgpa = cgpa_match.group(2)

    if degree or institution:

        education.append({

            "degree": degree,

            "institution": institution,

            "year": year,

            "cgpa": cgpa

        })

    return education