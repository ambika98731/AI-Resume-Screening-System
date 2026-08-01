from fastapi import APIRouter
from fastapi.responses import FileResponse

from app.services.report_service import generate_report

router = APIRouter()


@router.post("/report")
def create_report(result: dict):

    filename = "resume_report.pdf"

    generate_report(
        filename,
        result,
    )

    return FileResponse(
        path=filename,
        media_type="application/pdf",
        filename="Resume_Report.pdf",
    )