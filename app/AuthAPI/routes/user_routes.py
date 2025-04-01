from fastapi import APIRouter, HTTPException
from models.user import *
from services.user_service import *

router = APIRouter()

@router.post("/register")
def register_user(user: UserIn):
    try:
        return create_user(user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
def login(user: UserLogin):
    return verify_user(user)