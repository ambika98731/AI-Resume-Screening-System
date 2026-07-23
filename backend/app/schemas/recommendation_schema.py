from pydantic import BaseModel, Field


class RecommendationSchema(BaseModel):

    strengths: list[str] = Field(default_factory=list)

    weaknesses: list[str] = Field(default_factory=list)

    recommendations: list[str] = Field(default_factory=list) 