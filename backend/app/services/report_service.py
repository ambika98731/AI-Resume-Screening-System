from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(
    filename: str,
    result: dict,
):
    """
    Generate a PDF report for
    resume analysis.
    """

    document = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            "AI Resume Screening Report",
            styles["Heading1"],
        )
    )

    elements.append(
        Paragraph(
            f"<b>Overall Score:</b> {result['matching']['overall_score']}%",
            styles["BodyText"],
        )
    )

    elements.append(
        Paragraph(
            f"<b>Semantic Score:</b> {result['semantic_matching']['similarity_score']}%",
            styles["BodyText"],
        )
    )

    elements.append(
        Paragraph(
            f"<b>Summary:</b> {result['summary']['summary']}",
            styles["BodyText"],
        )
    )

    document.build(elements)