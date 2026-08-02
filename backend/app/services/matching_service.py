from app.schemas.resume_schema import ResumeSchema
from app.schemas.jd_schema import JDSchema
from app.schemas.matching_schema import MatchingSchema
from app.services.matchers.skill_matcher import match_skills
from app.services.matchers.education_matcher import match_education
from app.services.matchers.score_calculator import calculate_overall_score

from app.services.matchers.experience_matcher import match_experience

def match_resume(
    resume: ResumeSchema,
    jd: JDSchema,
) -> MatchingSchema:

    result = MatchingSchema()

    matched, missing, score = match_skills(
        resume.skills,
        jd.skills,
    )

    result.matched_skills = matched
    result.missing_skills = missing
    result.skill_score = score

    result.education_match =match_education(
        resume.education,
        jd.education,
    )

    result.experience_match = match_experience(
        resume.experience,
        jd.experience,
    )

    result.overall_score = calculate_overall_score(
    result.skill_score,
    result.education_match,
    result.experience_match,
)

    return result