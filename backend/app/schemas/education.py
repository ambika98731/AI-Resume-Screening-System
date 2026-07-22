from pydantic import BaseModel

class Education(BaseModel):
    degree: str | None = None
    field_of_study: str | None = None
    institution: str | None = None

    start_year: int | None = None
    end_year: int | None = None

    cgpa: float | None = None
    percentage: float | None = None