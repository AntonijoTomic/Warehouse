from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime
from typing import Optional
class ProductIn(BaseModel):
    name: str = Field(..., example="Laptop HP")
    category: str = Field(..., example="Elektronika")
    price: float = Field(..., gt=0, example=1299.99)
    quantity: int = Field(..., ge=0, example=5)
    description: str = Field(default="", example="15.6'' ekran, SSD 512GB")


class ProductOut(BaseModel):
    product_id: UUID
    name: str
    category: str
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