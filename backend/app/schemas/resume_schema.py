from pydantic import BaseModel, Field

from app.schemas.personal_info import PersonalInfo
from app.schemas.education import Education


class ResumeSchema(BaseModel):
    personal_info: PersonalInfo = Field(default_factory=PersonalInfo)

    education: list[Education] = Field(default_factory=list)

    skills: list[str] = Field(default_factory=list)

    experience: int | None = None