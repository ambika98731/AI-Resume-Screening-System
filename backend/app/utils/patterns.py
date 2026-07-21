import re

YEAR_PATTERN = re.compile(
    r"(19|20)\d{2}\s*[-–]\s*(19|20)?\d{2}"
)

CGPA_PATTERN = re.compile(
    r"(CGPA|GPA)\s*[:\-]?\s*(\d+(\.\d+)?)",
    re.IGNORECASE
)