from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    ListFlowable,
    ListItem,
)
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
            "<b>Matched Skills</b>",
            styles["Heading2"],
        )
    )

    matched = [
        ListItem(
            Paragraph(skill, styles["BodyText"])
        )
        for skill in result["matching"]["matched_skills"]
    ]

    elements.append(
        ListFlowable(
            matched,
            bulletType="bullet",
        )
    )

    elements.append(
        Paragraph(
            "<b>Missing Skills</b>",
            styles["Heading2"],
        )
    )

    missing = [
        ListItem(
            Paragraph(skill, styles["BodyText"])
        )
        for skill in result["matching"]["missing_skills"]
    ]

    if missing:
        elements.append(
            ListFlowable(
                missing,
                bulletType="bullet",
            )
        )
    else:
        elements.append(
            Paragraph(
             "No missing skills.",
                styles["BodyText"],
            )
        )

    elements.append(
        Paragraph(
            "<b>Education Match</b>",
            styles["Heading2"],
        )
    )

    elements.append(
        Paragraph(
            "Satisfied"
            if result["matching"]["education_match"]
            else "Not Satisfied",
            styles["BodyText"],
        )
    )

    elements.append(
        Paragraph(
            "<b>Experience Match</b>",
            styles["Heading2"],
        )
    )

    elements.append(
        Paragraph(
            "Satisfied"
            if result["matching"]["experience_match"]
            else "Not Satisfied",
            styles["BodyText"],
        )
    )

    elements.append(
        Paragraph(
            "<b>Recommendations</b>",
            styles["Heading2"],
        )
    )

    recommendations = [
        ListItem(
            Paragraph(rec, styles["BodyText"])
        )
        for rec in result["recommendation"]["recommendations"]
    ]

    if recommendations:
        elements.append(
            ListFlowable(
                recommendations,
                bulletType="bullet",
            )
        )
    else:
        elements.append(
            Paragraph(
                "No recommendations.",
                styles["BodyText"],
            )
        )

    elements.append(
        Paragraph(
            "<b>Interview Questions</b>",
            styles["Heading2"],
        )
    )

    for topic, questions in result["interview_questions"]["questions"].items():

        elements.append(
            Paragraph(
                f"<b>{topic.upper()}</b>",
                styles["BodyText"],
            )
        )

        items = [
            ListItem(
                Paragraph(q, styles["BodyText"])
            )
            for q in questions
        ]

        elements.append(
            ListFlowable(
                items,
                bulletType="bullet",
            )
        )
    

    elements.append(
        Paragraph(
            f"<b>Summary:</b> {result['summary']['summary']}",
            styles["BodyText"],
        )
    )

    document.build(elements)