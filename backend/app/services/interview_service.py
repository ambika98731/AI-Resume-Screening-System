from app.schemas.matching_schema import MatchingSchema
from app.schemas.interview_schema import InterviewSchema
from app.utils.interview_questions import INTERVIEW_QUESTIONS


def generate_interview_questions(
    matching: MatchingSchema,
) -> InterviewSchema:

    result = InterviewSchema()

    for skill in matching.matched_skills:

        skill_lower = skill.lower()

        if skill_lower in INTERVIEW_QUESTIONS:

            result.questions[skill_lower] = INTERVIEW_QUESTIONS[skill_lower]

    return result