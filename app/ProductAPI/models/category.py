from pydantic import BaseModel
from uuid import UUID

class CategoryIn(BaseModel):
    name: str

class CategoryOut(BaseModel):
    category_id: UUID
    name: str
