from app.services.jd_parser_service import parse_job_description

sample_jd = """
Python Backend Developer

Required Skills:
Python
FastAPI
Docker
PostgreSQL
Redis

Experience:
2+ years

Education:
Bachelor of Technology

Responsibilities:
Develop REST APIs
Design database schemas
Write unit tests
Collaborate with frontend developers
Optimize application performance
"""

result = parse_job_description(sample_jd)

print(result.model_dump())