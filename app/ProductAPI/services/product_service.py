from uuid import uuid4, UUID
from datetime import datetime
from models.product import *
from database.database import get_session
from fastapi import HTTPException, status
from typing import List, Optional


def insert_product(data: ProductIn):
    session = get_session()
    product_id = uuid4()
    now = datetime.utcnow()

    session.execute("""
        INSERT INTO products (product_id, name, category_id, price, quantity, description, created_at)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (
        product_id,
        data.name,
        str(data.category_id), 
        data.price,
        data.quantity,
        data.description,
        now
    ))


    return {
        "product_id": str(product_id),
        "created_at": now.isoformat()
    }


def get_all_products(category_id: Optional[UUID] = None) -> List[ProductOut]:
    session = get_session()

    if category_id:
        result = session.execute(
            "SELECT * FROM products WHERE category_id = %s ALLOW FILTERING", (str(category_id),)
        )
    else:
        result = session.execute("SELECT * FROM products")

    products = []
    for row in result:
        products.append(ProductOut(
            product_id=row.product_id,
            name=row.name,
            category_id=UUID(row.category_id),
            price=row.price,
            quantity=row.quantity,
            description=row.description,
            created_at=row.created_at
        ))
    return products


def get_product_by_id(product_id: UUID):
    session = get_session()
    
    result = session.execute(
        "SELECT * FROM products WHERE product_id = %s", (product_id,)
    )
    
    row = result.one()
    
    if not row:
        raise HTTPException(status_code=404, detail="Proizvod nije pronađen.")

    return ProductOut(
        product_id=row.product_id,
        name=row.name,
        category=row.category,
        price=row.price,
        quantity=row.quantity,
        description=row.description,
        created_at=row.created_at
    )
    
    
def update_product(product_id: UUID, data: ProductUpdate):
    session = get_session()
    result = session.execute(
        "SELECT * FROM products WHERE product_id = %s", (product_id,)
    )
    row = result.one()
    if not row:
        raise HTTPException(status_code=404, detail="Proizvod nije pronađen.")
    
    updated_fields = {
        "name": data.name if data.name is not None else row.name,
        "category": data.category if data.category is not None else row.category,
        "price": data.price if data.price is not None else row.price,
        "quantity": data.quantity if data.quantity is not None else row.quantity,
        "description": data.description if data.description is not None else row.description,
    }


    session.execute("""
        UPDATE products SET 
            name = %s,
            category = %s,
            price = %s,
            quantity = %s,
            description = %s
        WHERE product_id = %s
    """, (
        updated_fields["name"],
        updated_fields["category"],
        updated_fields["price"],
        updated_fields["quantity"],
        updated_fields["description"],
        product_id
    ))

    return {"message": "Proizvod ažuriran."}
    
    
def delete_product(product_id: UUID):
    session = get_session()
    result = session.execute(
        "SELECT * FROM products WHERE product_id = %s", (product_id,)
    )
    row = result.one()

    if not row:
        raise HTTPException(status_code=404, detail="Proizvod nije pronađen.")
    
    session.execute(
        "DELETE FROM products WHERE product_id = %s", (product_id,)
    )

    return {"message": "Proizvod obrisan."}
    