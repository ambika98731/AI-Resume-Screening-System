from pydantic import BaseModel


class Project(BaseModel):
    title: str | None = None
    description: str | None = None
    technologies: list[str] = []