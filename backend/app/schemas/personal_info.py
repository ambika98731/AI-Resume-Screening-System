from pydantic import BaseModel, EmailStr


class PersonalInfo(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    phone: str | None = None

    linkedin: str | None = None
    github: str | None = None

    location: str | None = None