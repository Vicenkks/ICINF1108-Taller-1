from datetime import datetime
from pydantic import BaseModel, EmailStr


class StudentResponse(BaseModel):
    id: str
    name: str
    email: EmailStr
    age: int
    createdAt: datetime
    updatedAt: datetime