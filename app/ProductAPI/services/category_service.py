from uuid import uuid4
from models.category import CategoryIn, CategoryOut
from database.database import get_session
from typing import List
from fastapi import HTTPException


def create_category(data: CategoryIn):
    session = get_session()
    result = session.execute(
        "SELECT * FROM categories WHERE name = %s ALLOW FILTERING", (data.name,)
    )
    if result.one():
        raise HTTPException(status_code=400, detail="Kategorija s tim imenom već postoji.")
    category_id = uuid4()

    session.execute("""
        INSERT INTO categories (category_id, name)
        VALUES (%s, %s)
    """, (category_id, data.name))

    return {"category_id": str(category_id), "name": data.name}

def get_all_categories() -> List[CategoryOut]:
    session = get_session()
    rows = session.execute("SELECT * FROM categories")

    return [CategoryOut(category_id=row.category_id, name=row.name) for row in rows]




def get_category_by_name(name: str) -> CategoryOut:
    session = get_session()
    
    result = session.execute(
        "SELECT * FROM categories WHERE name = %s ALLOW FILTERING", (name,)
    )
    row = result.one()

    if not row:
        raise HTTPException(status_code=404, detail="Kategorija nije pronađena.")

    return CategoryOut(category_id=row.category_id, name=row.name)
