from pydantic import BaseModel


class SummarySchema(BaseModel):
    summary: str