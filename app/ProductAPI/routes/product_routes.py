from fastapi import APIRouter, Depends, HTTPException
from typing import List
from models.product import *
from services.product_service import *
from uuid import UUID
from database.auth import get_current_user

router = APIRouter()

@router.post("/products")
def create_product(product: ProductIn, user: dict = Depends(get_current_user)):
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Nemate ovlasti za dodavanje proizvoda.")
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
def update_product_route(product_id: UUID, product: ProductUpdate, user: dict = Depends(get_current_user)):
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Nemate ovlasti za uređivanje proizvoda.")
    return update_product(product_id, product)

@router.delete("/products/{product_id}")
def delete_product_route(product_id: UUID, user: dict = Depends(get_current_user)):
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Nemate ovlasti za brisanje proizvoda.")
    return delete_product(product_id)

@router.get("/products/stats")
def get_products_stats(user: dict = Depends(get_current_user)):
    return calculate_product_stats()