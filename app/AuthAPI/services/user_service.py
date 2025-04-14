from uuid import uuid4
from datetime import datetime
from models.user import *
from database.databse import get_session
from passlib.context import CryptContext
from fastapi import HTTPException
from database.auth import create_access_token


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(data: UserIn):
    session = get_session()

  
    result = session.execute(
        "SELECT * FROM users WHERE email = %s ALLOW FILTERING", (data.email,)
    )
    if result.one():
        raise Exception("Korisnik već postoji.")

    user_id = uuid4()
    hashed_pw = pwd_context.hash(data.password)
    now = datetime.utcnow()

    session.execute("""
        INSERT INTO users (user_id, email, password, role, created_at)
        VALUES (%s, %s, %s, %s, %s)
    """, (user_id, data.email, hashed_pw, "user", now))

    return {
        "user_id": str(user_id),
        "email": data.email
    }


def verify_user(data: UserLogin):
    session = get_session()

    result = session.execute(
        "SELECT * FROM users WHERE email = %s ALLOW FILTERING", (data.email,)
    )
    row = result.one()

    if not row:
        raise HTTPException(status_code=401, detail="Neispravan email ili lozinka.")

    if not pwd_context.verify(data.password, row.password):
        raise HTTPException(status_code=401, detail="Neispravan email ili lozinka.")

    token = create_access_token({"sub": row.email}, role=row.role)

    return {"access_token": token, "token_type": "bearer"}