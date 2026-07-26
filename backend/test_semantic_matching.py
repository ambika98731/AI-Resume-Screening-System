from app.services.semantic_matching_service import calculate_semantic_similarity


resume = """
Experienced Python Backend Developer.

Skills:
Python
FastAPI
Docker
PostgreSQL
Redis

Developed scalable REST APIs and microservices.
"""


job_description = """
Python Backend Developer

Required Skills:
Python
FastAPI
Docker
PostgreSQL
Redis

Responsibilities:
Build scalable backend APIs and microservices.
"""


result = calculate_semantic_similarity(
    resume,
    job_description,
)

print(result.model_dump())