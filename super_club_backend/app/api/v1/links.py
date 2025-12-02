from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from sqlalchemy import or_, and_, func
from typing import Optional
from app.core.database import get_db
from app.core.dependencies import get_current_user, require_current_user
from app.models.user import User
from app.models.connection import Connection
from app.models.carousel import Carousel
from app.schemas.common import ResponseModel, PaginatedResponse, PaginationInfo
import uuid

router = APIRouter()


@router.get("", response_model=PaginatedResponse[dict])
async def get_links(
    category: Optional[str] = Query(None),
    search: Optional[str] = Query(None),
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1),
    current_user: Optional[User] = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """获取社区成员列表"""
    # 获取所有用户（简化实现，实际应该根据业务逻辑筛选）
    query = db.query(User).filter(User.is_active == True)
    
    if search:
        query = query.filter(
            or_(
                User.name.ilike(f"%{search}%"),
                User.company.ilike(f"%{search}%"),
                User.bio.ilike(f"%{search}%")
            )
        )
    
    total = query.count()
    items = query.offset((page - 1) * limit).limit(limit).all()
    
    link_list = []
    for user in items:
        # 统计连接数
        connection_count = db.query(func.count(Connection.id)).filter(
            ((Connection.requester_id == user.id) | (Connection.target_id == user.id)) &
            (Connection.status == "connected")
        ).scalar() or 0
        
        link_list.append({
            "id": f"link-{user.id}",
            "user": {
                "id": str(user.id),
                "name": user.name,
                "avatar": user.avatar,
                "company": user.company or "",
                "position": user.position or ""
            },
            "bio": user.bio or "",
            "tags": [],  # 可以从用户的其他字段提取
            "stats": {
                "connections": connection_count,
                "posts": 0,
                "influence": "高" if connection_count > 100 else "中"
            },
            "status": "online",  # 简化实现
            "verified": user.verified,
            "createdAt": user.created_at.isoformat() + "Z"
        })
    
    return PaginatedResponse(
        data={
            "items": link_list,
            "pagination": PaginationInfo(
                page=page,
                limit=limit,
                total=total,
                totalPages=(total + limit - 1) // limit
            ),
            "filters": {
                "categories": ["不限", "消费", "文娱", "教育", "企服", "AI", "出海", "Web3", "硬件", "本地生活", "医疗健康", "社交", "金融科技", "新能源"]
            }
        }
    )


@router.post("/connect", response_model=ResponseModel[dict])
async def connect_user(
    request: dict,
    current_user: User = Depends(require_current_user),
    db: Session = Depends(get_db)
):
    """建立连接"""
    target_user_id = uuid.UUID(request["targetUserId"])
    
    if target_user_id == current_user.id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="不能与自己建立连接"
        )
    
    # 检查是否已存在连接
    existing = db.query(Connection).filter(
        ((Connection.requester_id == current_user.id) & (Connection.target_id == target_user_id)) |
        ((Connection.requester_id == target_user_id) & (Connection.target_id == current_user.id))
    ).first()
    
    if existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="已存在连接请求或已建立连接"
        )
    
    connection = Connection(
        requester_id=current_user.id,
        target_id=target_user_id,
        message=request.get("message"),
        purpose=request.get("purpose")
    )
    db.add(connection)
    db.commit()
    db.refresh(connection)
    
    return ResponseModel(
        data={
            "connectionId": str(connection.id),
            "targetUserId": str(target_user_id),
            "status": connection.status,
            "createdAt": connection.created_at.isoformat() + "Z"
        },
        message="连接请求已发送"
    )


@router.get("/my-connections", response_model=PaginatedResponse[dict])
async def get_my_connections(
    status_filter: Optional[str] = Query(None, alias="status"),
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1),
    current_user: User = Depends(require_current_user),
    db: Session = Depends(get_db)
):
    """获取我的连接"""
    query = db.query(Connection).filter(
        (Connection.requester_id == current_user.id) | (Connection.target_id == current_user.id)
    )
    
    if status_filter == "connected":
        query = query.filter(Connection.status == "connected")
    elif status_filter == "pending":
        query = query.filter(Connection.status == "pending")
    
    total = query.count()
    items = query.order_by(Connection.created_at.desc()).offset((page - 1) * limit).limit(limit).all()
    
    connection_list = []
    for conn in items:
        # 确定对方用户
        other_user_id = conn.target_id if conn.requester_id == current_user.id else conn.requester_id
        other_user = db.query(User).filter(User.id == other_user_id).first()
        
        if other_user:
            connection_list.append({
                "connectionId": str(conn.id),
                "user": {
                    "id": str(other_user.id),
                    "name": other_user.name,
                    "avatar": other_user.avatar,
                    "company": other_user.company or "",
                    "position": other_user.position or ""
                },
                "status": conn.status,
                "connectedAt": conn.updated_at.isoformat() + "Z" if conn.status == "connected" else None,
                "mutualConnections": 0  # 简化实现
            })
    
    return PaginatedResponse(
        data={
            "items": connection_list,
            "pagination": PaginationInfo(
                page=page,
                limit=limit,
                total=total,
                totalPages=(total + limit - 1) // limit
            )
        }
    )


@router.put("/connections/{connection_id}", response_model=ResponseModel[dict])
async def update_connection(
    connection_id: str,
    request: dict,
    current_user: User = Depends(require_current_user),
    db: Session = Depends(get_db)
):
    """接受/拒绝连接请求"""
    connection = db.query(Connection).filter(Connection.id == uuid.UUID(connection_id)).first()
    if not connection:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="连接请求不存在"
        )
    
    # 检查权限（只有被请求方可以接受/拒绝）
    if connection.target_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="无权操作此连接请求"
        )
    
    action = request.get("action")
    if action == "accept":
        connection.status = "connected"
    elif action == "reject":
        connection.status = "rejected"
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="无效的操作"
        )
    
    db.commit()
    db.refresh(connection)
    
    return ResponseModel(
        data={
            "connectionId": str(connection.id),
            "status": connection.status,
            "updatedAt": connection.updated_at.isoformat() + "Z"
        },
        message="已接受连接请求" if action == "accept" else "已拒绝连接请求"
    )


@router.get("/carousel", response_model=ResponseModel[dict])
async def get_carousel(db: Session = Depends(get_db)):
    """获取轮播图"""
    carousels = db.query(Carousel).filter(
        Carousel.page == "links",
        Carousel.is_active == True
    ).order_by(Carousel.order_num.asc()).all()
    
    slides = []
    for carousel in carousels:
        slides.append({
            "id": str(carousel.id),
            "image": carousel.image,
            "title": carousel.title,
            "subtitle": carousel.subtitle,
            "link": carousel.link,
            "order": carousel.order_num
        })
    
    return ResponseModel(data={"slides": slides})

