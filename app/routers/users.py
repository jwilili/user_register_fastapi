from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, EmailStr, Field
from app.services import UserService

router = APIRouter()

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6, max_length=100)

@router.post("/register", status_code=201)
async def register_user(user: UserCreate, user_service: UserService = Depends()):
    await user_service.create_user(user.email, user.password)
