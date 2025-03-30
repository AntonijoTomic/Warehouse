from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime
from typing import Optional

class ProductIn(BaseModel):
    name: str = Field(...)
    category_id: UUID = Field(...)
    price: float = Field(..., gt=0, example=1299.99)
    quantity: int = Field(..., ge=0, example=5)
    description: str = Field(default="")


class ProductOut(BaseModel):
    product_id: UUID
    name: str
    category_id: UUID
    price: float
    quantity: int
    description: str
    created_at: datetime
    
class ProductUpdate(BaseModel):
    name: Optional[str]
    category: Optional[str]
    price: Optional[float]
    quantity: Optional[int]
    description: Optional[str]   