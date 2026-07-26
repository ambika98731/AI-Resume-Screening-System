from pydantic import BaseModel


class SemanticMatchingSchema(BaseModel):
    similarity_score: float