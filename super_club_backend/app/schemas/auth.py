from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime


class RegisterRequest(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8)
    name: str
    phone: Optional[str] = None


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class RefreshTokenRequest(BaseModel):
    refreshToken: str


class TokenResponse(BaseModel):
    accessToken: str
    refreshToken: Optional[str] = None
    expiresIn: int


class UserInfo(BaseModel):
    id: str
    email: str
    name: str
    avatar: Optional[str] = None
    membershipLevel: Optional[str] = None
    
    class Config:
        from_attributes = True


class AuthResponse(BaseModel):
    user: UserInfo
    tokens: TokenResponse

