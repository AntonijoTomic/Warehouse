from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime

class ProductCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    category: str = Field(..., min_length=2, max_length=50)
    price: float = Field(..., gt=0)  # Cijena mora biti veća od 0
    quantity: int = Field(..., ge=0)  # Količina ne smije biti negativna
    description: str = Field(..., min_length=5, max_length=500)

class ProductUpdate(BaseModel):
    name: str | None = None
    category: str | None = None
    price: float | None = None
    quantity: int | None = None
    description: str | None = None
    
    
class ProductResponse(BaseModel):
    product_id: UUID
    name: str
    category: str
    price: float
    quantity: int
    description: str
    created_at: datetime    
    
    
    
    class Config:
        from_attributes = True