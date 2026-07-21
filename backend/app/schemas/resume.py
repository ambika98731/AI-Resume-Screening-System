from pydantic import BaseModel, EmailStr


class ResumeCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str
    resume_path: str
    extracted_text: str | None = None
    