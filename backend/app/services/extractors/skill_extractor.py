from app.utils.skills import SKILLS


def extract_skills(doc):
    """
    Extract both single-word and multi-word skills.
    """

    text = doc.text.lower()

    found = set()

    for skill in SKILLS:

        if skill in text:
            found.add(skill)

    return sorted(found)