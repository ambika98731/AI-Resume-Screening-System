from pydantic import BaseModel, Field


class JDSchema(BaseModel):
    title: str | None = None

    skills: list[str] = Field(default_factory=list)

    experience: int | None = None

    education: str | None = None

    responsibilities: list[str] = Field(default_factory=list)