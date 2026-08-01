from fastapi import APIRouter, UploadFile, File

from app.services.parser_service import parse_resume
from app.services.jd_parser_service import parse_job_description
from app.services.matching_service import match_resume

from app.services.interview_service import generate_interview_questions
from app.services.recommendation_service import generate_recommendations

from app.services.summary_service import generate_summary

from app.services.improvement_service import generate_improvements

from app.services.semantic_matching_service import calculate_semantic_similarity

from app.services.pdf_extractor_service import extract_text_from_pdf
from pathlib import Path

router = APIRouter()

@router.post("/match")
def match(
    resume_file: UploadFile = File(...),
    jd_file: UploadFile = File(...)
):

    # Create upload directory if it doesn't exist
    upload_dir = Path("uploads")
    upload_dir.mkdir(exist_ok=True)

    # File paths
    resume_path = upload_dir / resume_file.filename
    jd_path = upload_dir / jd_file.filename

    # Save Resume PDF
    with open(resume_path, "wb") as buffer:
        buffer.write(resume_file.file.read())

    # Save Job Description PDF
    with open(jd_path, "wb") as buffer:
        buffer.write(jd_file.file.read())


   # Extract text from uploaded PDFs
    resume_text = extract_text_from_pdf(str(resume_path))
    jd_text = extract_text_from_pdf(str(jd_path))

    # Parse extracted text
    resume = parse_resume(resume_text)
    jd = parse_job_description(jd_text)

    print("\n===== RESUME SKILLS =====")
    print(resume.skills)

    print("\n===== JD SKILLS =====")
    print(jd.skills)

    result = match_resume(resume, jd)

    semantic_similarity = calculate_semantic_similarity(
        resume_text,
        jd_text
    )

    recommendation = generate_recommendations(result)

    interview = generate_interview_questions(result)

    summary = generate_summary(resume, result)

    improvements = generate_improvements(
        resume,
        result
    )

    return {
        "resume": resume,
        "job_description": jd,
        "matching": result,
        "semantic_matching": semantic_similarity,
        "recommendation": recommendation,
        "interview_questions": interview,
        "summary": summary,
        "improvements": improvements
    }