from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from sqlalchemy.sql import func

from app.database.database import Base


class Analysis(Base):

    __tablename__ = "analysis"

    id = Column(Integer, primary_key=True, index=True)

    candidate_name = Column(String(200))

    email = Column(String(200))

    job_title = Column(String(250))

    overall_score = Column(Float)

    semantic_score = Column(Float)

    matched_skills = Column(Text)

    missing_skills = Column(Text)

    summary = Column(Text)

    recommendation = Column(Text)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )