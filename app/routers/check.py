from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, EmailStr, Field
from app.services import VerificationService

router = APIRouter()

class VerificationRequest(BaseModel):
    email: EmailStr

class ActivationRequest(BaseModel):
    email: EmailStr
    code: str = Field(min_length=4, max_length=4)

@router.post("/send-code", status_code=200)
async def send_verification_code(request: VerificationRequest, verification_service: VerificationService = Depends()):
    await verification_service.send_code(request.email)

@router.post("/activate", status_code=200)
async def activate_user(request: ActivationRequest, verification_service: VerificationService = Depends()):
    await verification_service.activate_user(request.email, request.code)
