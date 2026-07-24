from app.schemas.resume_schema import ResumeSchema
from app.schemas.matching_schema import MatchingSchema
from app.schemas.summary_schema import SummarySchema


def generate_summary(
    resume: ResumeSchema,
    matching: MatchingSchema,
) -> SummarySchema:

    lines = []

    # -------------------------
    # Candidate
    # -------------------------

    name = resume.personal_info.name or "The candidate"

    lines.append(f"{name} has an overall resume match score of {matching.overall_score}%.")

    # -------------------------
    # Skills
    # -------------------------

    if matching.matched_skills:

        lines.append(
            "Strong skills include "
            + ", ".join(matching.matched_skills)
            + "."
        )

    if matching.missing_skills:

        lines.append(
            "The candidate is missing "
            + ", ".join(matching.missing_skills)
            + "."
        )

    # -------------------------
    # Education
    # -------------------------

    if matching.education_match:
        lines.append("The educational requirement is satisfied.")
    else:
        lines.append("The educational requirement is not satisfied.")

    # -------------------------
    # Experience
    # -------------------------

    if matching.experience_match:
        lines.append("The experience requirement is satisfied.")
    else:
        lines.append("Additional relevant work experience is recommended.")

    return SummarySchema(
        summary=" ".join(lines)
    )