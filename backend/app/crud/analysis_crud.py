from sqlalchemy.orm import Session

from app.models.analysis import Analysis
from app.schemas.analysis_schema import AnalysisCreate


def create_analysis(
    db: Session,
    analysis: AnalysisCreate,
):
    """
    Save a completed resume analysis
    into the database.
    """

    db_analysis = Analysis(
        candidate_name=analysis.candidate_name,
        email=analysis.email,
        job_title=analysis.job_title,
        overall_score=analysis.overall_score,
        semantic_score=analysis.semantic_score,
        matched_skills=analysis.matched_skills,
        missing_skills=analysis.missing_skills,
        summary=analysis.summary,
        recommendation=analysis.recommendation,
    )

    db.add(db_analysis)

    db.commit()

    db.refresh(db_analysis)

    return db_analysis