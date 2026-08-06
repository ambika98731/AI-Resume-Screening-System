from app.utils.skills import SKILLS


def extract_project_technologies(text: str) -> list[str]:
    """
    Extract technologies mentioned in a project description.
    """

    text = text.lower()

    found = []

    for skill in sorted(SKILLS):

        if skill.lower() in text:
            found.append(skill)

    return found