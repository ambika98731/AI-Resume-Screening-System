from app.utils.skills import SKILLS
import re


def extract_skills(doc):
    """
    Extract both single-word and multi-word skills.
    """

    text = doc.text.lower()

    found = set()

    for skill in SKILLS:

        

        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text):
            found.add(skill)

    return sorted(found)