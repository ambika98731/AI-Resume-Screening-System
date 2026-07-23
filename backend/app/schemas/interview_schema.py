from pydantic import BaseModel, Field


class InterviewSchema(BaseModel):

    questions: dict[str, list[str]] = Field(default_factory=dict)