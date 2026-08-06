import re

from app.schemas.personal_info import PersonalInfo


def extract_personal_info(doc) -> PersonalInfo:
    """
    Extract personal information from resume.
    """

    personal_info = PersonalInfo()

    # Name (spaCy)
    for entity in doc.ents:
        if entity.label_ == "PERSON":
            personal_info.name = entity.text
            break

    # Email (Regex)
    email = re.search(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        doc.text,
    )

    if email:
        personal_info.email = email.group()

    phone = re.search(
        r"(\+?\d[\d\s-]{8,}\d)",
        doc.text,
    )

    if phone:
        personal_info.phone = phone.group()

    linkedin = re.search(
        r"https?://(www\.)?linkedin\.com/in/[^\s]+",
        doc.text,
    )

    if linkedin:
        personal_info.linkedin = linkedin.group()

    github = re.search(
        r"https?://(www\.)?github\.com/[^\s]+",
        doc.text,
    )

    if github:
        personal_info.github = github.group()

    for entity in doc.ents:
        if entity.label_ in ["GPE", "LOC"]:
            personal_info.location = entity.text
            break

    return personal_info