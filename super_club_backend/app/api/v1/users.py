from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import Optional
from app.core.database import get_db
from app.core.dependencies import require_current_user as get_current_user
from app.models.user import User
from app.models.favorite import Favorite
from app.models.project import Project
from app.models.connection import Connection
from app.models.event import EventRegistration
from app.schemas.user import UserProfile, UpdateProfileRequest, FavoriteItem, AddFavoriteRequest
from app.schemas.common import ResponseModel, PaginatedResponse, PaginationInfo
import uuid

router = APIRouter()


@router.get("/profile", response_model=ResponseModel[UserProfile])
async def get_profile(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    """获取用户信息"""
    # 统计用户数据
    project_count = db.query(func.count(Project.id)).filter(Project.owner_id == current_user.id).scalar() or 0
    connection_count = db.query(func.count(Connection.id)).filter(
        ((Connection.requester_id == current_user.id) | (Connection.target_id == current_user.id)) &
        (Connection.status == "connected")
    ).scalar() or 0
    event_count = db.query(func.count(EventRegistration.id)).filter(EventRegistration.user_id == current_user.id).scalar() or 0
    favorite_count = db.query(func.count(Favorite.id)).filter(Favorite.user_id == current_user.id).scalar() or 0
    
    stats = {
        "projects": project_count,
        "connections": connection_count,
        "events": event_count,
        "favorites": favorite_count
    }
    
    return ResponseModel(
        data=UserProfile(
            id=str(current_user.id),
            email=current_user.email,
            name=current_user.name,
            avatar=current_user.avatar,
            phone=current_user.phone,
            bio=current_user.bio,
            company=current_user.company,
            position=current_user.position,
            membershipLevel=current_user.membership_level,
            membershipExpiry=current_user.membership_expiry,
            stats=stats,
            createdAt=current_user.created_at,
            updatedAt=current_user.updated_at
        )
    )


@router.put("/profile", response_model=ResponseModel[UserProfile])
async def update_profile(
    request: UpdateProfileRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """更新用户信息"""
    if request.name:
        current_user.name = request.name
    if request.bio is not None:
        current_user.bio = request.bio
    if request.company is not None:
        current_user.company = request.company
    if request.position is not None:
        current_user.position = request.position
    if request.phone is not None:
        current_user.phone = request.phone
    
    db.commit()
    db.refresh(current_user)
    
    return ResponseModel(
        data=UserProfile(
            id=str(current_user.id),
            email=current_user.email,
            name=current_user.name,
            avatar=current_user.avatar,
            phone=current_user.phone,
            bio=current_user.bio,
            company=current_user.company,
            position=current_user.position,
            membershipLevel=current_user.membership_level,
            membershipExpiry=current_user.membership_expiry,
            stats={},
            createdAt=current_user.created_at,
            updatedAt=current_user.updated_at
        ),
        message="信息更新成功"
    )


@router.post("/avatar", response_model=ResponseModel[dict])
async def upload_avatar(
    avatar: UploadFile = File(...),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """上传头像"""
    # 这里应该实现文件上传到存储服务（如 S3、OSS 等）
    # 目前返回一个占位 URL
    avatar_url = f"https://cdn.superclub.com/avatars/{current_user.id}.jpg"
    current_user.avatar = avatar_url
    db.commit()
    
    return ResponseModel(
        data={"avatar": avatar_url, "updatedAt": current_user.updated_at},
        message="头像上传成功"
    )


@router.get("/favorites", response_model=PaginatedResponse[FavoriteItem])
async def get_favorites(
    type: Optional[str] = None,
    page: int = 1,
    limit: int = 20,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """获取收藏列表"""
    query = db.query(Favorite).filter(Favorite.user_id == current_user.id)
    if type:
        query = query.filter(Favorite.resource_type == type)
    
    total = query.count()
    items = query.order_by(Favorite.created_at.desc()).offset((page - 1) * limit).limit(limit).all()
    
    # TODO: 根据 resource_type 和 resource_id 获取实际资源信息
    favorite_items = [
        FavoriteItem(
            id=str(item.id),
            type=item.resource_type,
            resourceId=str(item.resource_id),
            createdAt=item.created_at
        )
        for item in items
    ]
    
    return PaginatedResponse(
        data={
            "items": favorite_items,
            "pagination": PaginationInfo(
                page=page,
                limit=limit,
                total=total,
                totalPages=(total + limit - 1) // limit
            )
        }
    )


@router.post("/favorites", response_model=ResponseModel[FavoriteItem])
async def add_favorite(
    request: AddFavoriteRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """添加收藏"""
    # 检查是否已收藏（resource_id 使用字符串直接比较）
    existing = db.query(Favorite).filter(
        Favorite.user_id == current_user.id,
        Favorite.resource_type == request.type,
        Favorite.resource_id == request.resourceId
    ).first()
    
    if existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="已收藏过该资源"
        )
    
    favorite = Favorite(
        user_id=current_user.id,
        resource_type=request.type,
        resource_id=request.resourceId  # 直接使用字符串
    )
    db.add(favorite)
    db.commit()
    db.refresh(favorite)
    
    return ResponseModel(
        data=FavoriteItem(
            id=str(favorite.id),
            type=favorite.resource_type,
            resourceId=str(favorite.resource_id),
            createdAt=favorite.created_at
        ),
        message="收藏成功"
    )


@router.delete("/favorites/{favorite_id}", response_model=ResponseModel[dict])
async def delete_favorite(
    favorite_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """取消收藏"""
    favorite = db.query(Favorite).filter(
        Favorite.id == favorite_id,  # 直接使用字符串
        Favorite.user_id == current_user.id
    ).first()
    
    if not favorite:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="收藏不存在"
        )
    
    db.delete(favorite)
    db.commit()
    
    return ResponseModel(message="已取消收藏")

