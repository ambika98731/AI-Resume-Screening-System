from app.schemas.resume_schema import ResumeSchema
from app.schemas.jd_schema import JDSchema
from app.schemas.education import Education
from app.services.matching_service import match_resume


resume = ResumeSchema(
    skills=[
        "Python",
        "FastAPI",
        "Docker",
        "Git",
        "SQL",
    ],

    education=[
        Education(
            degree="Bachelor of Technology"
        )
    ]
)

jd = JDSchema(
    skills=[
        "Python",
        "FastAPI",
        "Docker",
        "Redis",
        "PostgreSQL",
    ],

    education="Bachelor of Technology"
)


result = match_resume(
    resume,
    jd
)

print(result.model_dump())