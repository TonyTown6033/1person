from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class UserProfile(BaseModel):
    id: str
    email: str
    name: str
    avatar: Optional[str] = None
    phone: Optional[str] = None
    bio: Optional[str] = None
    company: Optional[str] = None
    position: Optional[str] = None
    membershipLevel: str
    membershipExpiry: Optional[datetime] = None
    stats: dict
    createdAt: datetime
    updatedAt: datetime
    
    class Config:
        from_attributes = True


class UpdateProfileRequest(BaseModel):
    name: Optional[str] = None
    bio: Optional[str] = None
    company: Optional[str] = None
    position: Optional[str] = None
    phone: Optional[str] = None


class FavoriteItem(BaseModel):
    id: str
    type: str
    resourceId: str
    resource: Optional[dict] = None
    createdAt: datetime
    
    class Config:
        from_attributes = True


class AddFavoriteRequest(BaseModel):
    type: str  # talent, project, event, content
    resourceId: str

