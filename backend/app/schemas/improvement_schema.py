from pydantic import BaseModel, Field


class ImprovementSchema(BaseModel):

    suggestions: list[str] = Field(default_factory=list)