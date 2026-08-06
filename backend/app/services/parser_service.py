import spacy

from app.schemas.resume_schema import ResumeSchema
from app.schemas.education import Education

from app.services.extractors.skill_extractor import extract_skills

from app.services.extractors.education_extractor import extract_education

from app.services.splitters.section_splitter import split_sections

from app.services.extractors.resume_experience_extractor import (
    extract_resume_experience,
)

from app.services.extractors.personal_info_extractor import extract_personal_info

from app.services.extractors.project_extractor import extract_projects

nlp = spacy.load("en_core_web_sm")


def parse_resume(text: str):

    doc = nlp(text)
    sections = split_sections(text)

    print("\n====== Sections ======\n")

    for section, content in sections.items():
        print(f"[{section}]")
        print(content)
        print("----------------------")

    resume = ResumeSchema()

    resume.personal_info = extract_personal_info(doc)
    

    
    #"detected_sections": list(sections.keys())

    #"sections": sections

    resume.skills = extract_skills(doc)

    education_data = extract_education(
        sections.get("education", "")
    )

    resume.education = [
        Education(**edu)
        for edu in education_data
    ]

    resume.experience = extract_resume_experience(
        sections.get("experience", "")
    )


    resume.projects = extract_projects(
    sections.get("projects", "")
    )

    print("\n===== PROJECTS =====")

    for project in resume.projects:
        print(project.title)
        print(project.technologies)

    #"text_length": len(text)

    #"num_sentences": len(list(doc.sents))

    #"num_tokens": len(doc)
    print("\n===== RESUME EXPERIENCE =====")
    print(resume.experience)
    return resume

