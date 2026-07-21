import spacy

from app.services.extractors.skill_extractor import extract_skills

from app.services.extractors.education_extractor import extract_education

from app.services.splitters.section_splitter import split_sections

nlp = spacy.load("en_core_web_sm")


def parse_resume(text: str):

    doc = nlp(text)
    sections = split_sections(text)
    

    return {
        "detected_sections": list(sections.keys()),

        "sections": sections,

        "skills": extract_skills(doc),

        "education": extract_education(
            sections.get("education", "")
        ),

        "text_length": len(text),

        "num_sentences": len(list(doc.sents)),

        "num_tokens": len(doc)

    }

