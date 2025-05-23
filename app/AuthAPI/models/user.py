from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime

class UserIn(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    user_id: UUID
    email: EmailStr
    role: str
    created_at: datetime

class UserLogin(BaseModel):
    email: EmailStr
    password: str
