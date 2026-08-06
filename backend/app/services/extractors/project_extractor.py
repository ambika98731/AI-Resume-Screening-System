from app.schemas.project import Project


def extract_projects(text: str):
    """
    Extract projects from the Projects section.
    """

    projects = []

    if not text.strip():
        return projects

    lines = [
        line.strip()
        for line in text.split("\n")
        if line.strip()
    ]

    current_project = None

    for line in lines:

        if current_project is None:
            current_project = Project(
                title=line
            )

        else:
            current_project.description = line
            projects.append(current_project)
            current_project = None

    if current_project:
        projects.append(current_project)

    return projects