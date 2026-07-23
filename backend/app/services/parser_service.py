import spacy

from app.schemas.resume_schema import ResumeSchema
from app.schemas.education import Education

from app.services.extractors.skill_extractor import extract_skills

from app.services.extractors.education_extractor import extract_education

from app.services.splitters.section_splitter import split_sections


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

    print("\n========== Sections ==========")

    for key, value in sections.items():
        print(f"\n[{key}]")
        print(value)

    print("==============================")

    #"text_length": len(text)

    #"num_sentences": len(list(doc.sents))

    #"num_tokens": len(doc)

    return resume

