from sentence_transformers import SentenceTransformer, util

from app.schemas.semantic_matching_schema import SemanticMatchingSchema


# Load the model once when the server starts
model = SentenceTransformer("all-MiniLM-L6-v2")


def calculate_semantic_similarity(
    resume_text: str,
    job_description: str,
) -> SemanticMatchingSchema:

    resume_embedding = model.encode(
        resume_text,
        convert_to_tensor=True,
    )

    jd_embedding = model.encode(
        job_description,
        convert_to_tensor=True,
    )

    similarity = util.cos_sim(
        resume_embedding,
        jd_embedding,
    ).item()

    return SemanticMatchingSchema(
        similarity_score=round(similarity * 100, 2)
    )