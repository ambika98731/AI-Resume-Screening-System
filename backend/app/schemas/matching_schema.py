from pydantic import BaseModel, Field


class MatchingSchema(BaseModel):

    matched_skills: list[str] = Field(default_factory=list)

    missing_skills: list[str] = Field(default_factory=list)

    skill_score: float = 0

    education_match: bool = False

    experience_match: bool = False

    overall_score: float = 0