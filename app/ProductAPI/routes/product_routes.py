from fastapi import APIRouter
from typing import List
from models.product import *
from services.product_service import *
from uuid import UUID
router = APIRouter()

@router.post("/products")
def create_product(product: ProductIn):
    result = insert_product(product)
    return {
        "message": "Proizvod uspješno dodan.",
        "data": result
    }
    
@router.get("/products", response_model=List[ProductOut])
def read_all_products():
    return get_all_products()




@router.get("/products/by-category/{category_id}", response_model=List[ProductOut])
def get_products_by_category(category_id: UUID):
    return get_all_products(category_id=category_id)


@router.get("/products/{product_id}", response_model=ProductOut)
def read_product(product_id: UUID):
    return get_product_by_id(product_id)



@router.put("/products/{product_id}")
def update_product_route(product_id: UUID, product: ProductUpdate):
    return update_product(product_id, product)

@router.delete("/products/{product_id}")
def delete_product_route(product_id: UUID):
    return delete_product(product_id)