from pydantic import BaseModel, Field


class Project(BaseModel):
    title: str | None = None
    description: str | None = None

    technologies: list[str] = Field(default_factory=list)