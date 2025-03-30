from fastapi import APIRouter
from typing import List
from models.category import CategoryIn, CategoryOut
from services.category_service import *

router = APIRouter()

@router.post("/categories", response_model=CategoryOut)
def add_category(payload: CategoryIn):
    return create_category(payload)

@router.get("/categories", response_model=List[CategoryOut])
def list_categories():
    return get_all_categories()

@router.get("/categories/by-name/{name}", response_model=CategoryOut)
def read_category_by_name(name: str):
    return get_category_by_name(name)