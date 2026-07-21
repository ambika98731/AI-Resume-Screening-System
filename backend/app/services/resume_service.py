from sqlalchemy.orm import Session

from app.models.resume import Resume
from app.schemas.resume import ResumeCreate


def create_resume(db: Session, resume: ResumeCreate):
    new_resume = Resume(
        name=resume.name,
        email=resume.email,
        phone=resume.phone,
        resume_path=resume.resume_path,
        extracted_text=resume.extracted_text
    )

    db.add(new_resume)
    db.commit()
    db.refresh(new_resume)

    return new_resume