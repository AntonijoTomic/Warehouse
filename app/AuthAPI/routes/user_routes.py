from fastapi import APIRouter, HTTPException,Depends
from models.user import *
from services.user_service import *
from database.auth import *
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



@router.get("/me")
def get_me(current_user: str = Depends(get_current_user)):
    return {"email": current_user}


@router.post("/validate_token")
async def validate_token(token: str):
    payload = decode_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Token nije ispravan")
    return payload