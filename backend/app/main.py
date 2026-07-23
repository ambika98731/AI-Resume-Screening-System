from fastapi import FastAPI
from sqlalchemy import text


from app.database.database import Base, engine
from app.models.resume import Resume

from app.api.resume import router

from app.api.matching import router as matching_router

app = FastAPI(
    title="AI Resume Screening System",
    version="1.0.0"
)

app.include_router(router)
# Create tables
#Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {
        "message": "Backend Running"
    }

app.include_router(matching_router)

@app.get("/db-test")
def db_test():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version();"))
        version = result.scalar()

    return {
        "database": "Connected",
        "postgres_version": version
    }