from app.schemas.resume_schema import ResumeSchema
from app.schemas.matching_schema import MatchingSchema
from app.schemas.improvement_schema import ImprovementSchema


def generate_improvements(
    resume: ResumeSchema,
    matching: MatchingSchema,
) -> ImprovementSchema:

    result = ImprovementSchema()

    # ---------------------------------
    # Missing Skills
    # ---------------------------------

    for skill in matching.missing_skills:
        result.suggestions.append(
            f"Add projects or certifications demonstrating {skill}."
        )

    # ---------------------------------
    # Experience
    # ---------------------------------

    if not matching.experience_match:
        result.suggestions.append(
            "Highlight more relevant work experience or internship experience."
        )

    # ---------------------------------
    # Education
    # ---------------------------------

    if not matching.education_match:
        result.suggestions.append(
            "Include the required educational qualification if applicable."
        )

    # ---------------------------------
    # GitHub
    # ---------------------------------

    if not resume.personal_info.github:
        result.suggestions.append(
            "Add your GitHub profile to showcase your projects."
        )

    # ---------------------------------
    # LinkedIn
    # ---------------------------------

    if not resume.personal_info.linkedin:
        result.suggestions.append(
            "Include your LinkedIn profile for professional visibility."
        )

    # ---------------------------------
    # Projects
    # ---------------------------------

    result.suggestions.append(
        "Quantify project achievements using measurable results."
    )

    result.suggestions.append(
        "Use action verbs to describe your technical contributions."
    )

    return result