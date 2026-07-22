import spacy

from app.schemas.jd_schema import JDSchema
from app.services.extractors.skill_extractor import extract_skills

from app.services.extractors.experience_extractor import extract_experience
from app.services.extractors.jd_education_extractor import extract_education_requirement
from app.services.extractors.responsibility_extractor import extract_responsibilities

nlp = spacy.load("en_core_web_sm")


def parse_job_description(text: str) -> JDSchema:
    doc = nlp(text)

    jd = JDSchema()

    # Extract Job Title
    jd.title = text.strip().split("\n")[0]

    # Extract Skills
    jd.skills = extract_skills(doc)

    # Extract Experience
    jd.experience = extract_experience(text)

    # Extract Education Requirement
    jd.education = extract_education_requirement(text)

    # Extract Responsibilities
    jd.responsibilities = extract_responsibilities(text)

    return jd