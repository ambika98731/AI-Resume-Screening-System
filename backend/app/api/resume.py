from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Form,
    Depends,
    HTTPException,
)
from sqlalchemy.orm import Session

import os
import shutil
import uuid

from app.database.database import get_db
from app.schemas.resume import ResumeCreate
from app.services.resume_service import create_resume
from app.models.resume import Resume
from app.services.pdf_service import extract_text






router = APIRouter()

UPLOAD_FOLDER = "app/uploads"


@router.post("/resume/upload")
def upload_resume(
    name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...),
    resume: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    # Allow only PDF files
    if not resume.filename.lower().endswith(".pdf"):
        raise HTTPException(
        status_code=400,
        detail="Only PDF resumes are allowed."
    )

    # Validate MIME type
    if resume.content_type != "application/pdf":
        raise HTTPException(
        status_code=400,
        detail="Invalid file type. Only PDF files are allowed."
    )

    # Maximum file size (5 MB)
    MAX_FILE_SIZE = 5 * 1024 * 1024

    # Move pointer to the end
    resume.file.seek(0, 2)

    # Get file size
    file_size = resume.file.tell()

    # Move pointer back to the beginning
    resume.file.seek(0)

    # Reject large files
    if file_size > MAX_FILE_SIZE:
        raise HTTPException(
        status_code=400,
        detail="File size must not exceed 5 MB."
        )

    # Create uploads folder if it doesn't exist
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    # File path
    #file_path = os.path.join(UPLOAD_FOLDER, resume.filename)

    # Generate unique filename
    file_extension = os.path.splitext(resume.filename)[1]

    unique_filename = f"{uuid.uuid4()}{file_extension}"

    file_path = os.path.join(
    UPLOAD_FOLDER,
    unique_filename 
    )

    

    # Save uploaded file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(resume.file, buffer)

    text = extract_text(file_path)

    # Create schema object
    resume_data = ResumeCreate(
        name=name,
        email=email,
        phone=phone,
        resume_path=file_path,

        extracted_text=text
    )

    # Save in database
    new_resume = create_resume(db, resume_data)

    return {
        "message": "Resume uploaded successfully",
        "data": new_resume
    }