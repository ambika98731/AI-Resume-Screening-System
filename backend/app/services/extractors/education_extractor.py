import re

from app.utils.degrees import DEGREES
from app.utils.patterns import YEAR_PATTERN, CGPA_PATTERN


def normalize(text: str) -> str:
    """
    Normalize text for reliable matching.
    """
    return (
        text.lower()
            .replace("&", " ")
            .replace("/", " ")
            .replace(":", "")
            .strip()
    )


def extract_education(text: str):
    """
    Extract education details from the Education section
    of a resume.
    """

    education = []

    normalized_text = normalize(text)
    lines = text.splitlines()

    degree = None
    institution = None
    start_year = None
    end_year = None
    cgpa = None
    percentage = None
    field_of_study = None

    # ----------------------------
    # Detect Degree
    # ----------------------------
    for d in sorted(DEGREES, key=len, reverse=True):
        if normalize(d) in normalized_text:
            degree = d
            break

    # ----------------------------
    # Detect Institution
    # ----------------------------
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

    # ----------------------------
    # Detect Year
    # ----------------------------
    year_match = YEAR_PATTERN.search(text)

    if year_match:
        years = re.findall(r"\d{4}", year_match.group())

        if len(years) == 2:
            start_year = int(years[0])
            end_year = int(years[1])
        elif len(years) == 1:
            end_year = int(years[0])

    # ----------------------------
    # Detect CGPA
    # ----------------------------
    cgpa_match = CGPA_PATTERN.search(text)

    if cgpa_match:
        cgpa = float(cgpa_match.group(2))

    # ----------------------------
    # Build Output
    # ----------------------------
    if degree or institution:

        education.append(
            {
                "degree": degree,
                "field_of_study": field_of_study,
                "institution": institution,
                "start_year": start_year,
                "end_year": end_year,
                "cgpa": cgpa,
                "percentage": percentage,
            }
        )

    return education