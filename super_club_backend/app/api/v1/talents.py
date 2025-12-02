from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from sqlalchemy import func, or_
from typing import Optional
from datetime import datetime
from app.core.database import get_db
from app.core.dependencies import get_current_user, require_current_user
from app.models.user import User
from app.models.talent import Talent
from app.models.invitation import Invitation
from app.schemas.common import ResponseModel, PaginatedResponse, PaginationInfo
import uuid

router = APIRouter()


@router.get("/stats", response_model=ResponseModel[dict])
async def get_talent_stats(db: Session = Depends(get_db)):
    """获取人才统计"""
    total_talents = db.query(func.count(Talent.id)).scalar() or 0
    # PostgreSQL 数组类型的 distinct 查询需要特殊处理
    try:
        total_tracks = len(set(tag for talent in db.query(Talent.tags).all() if talent.tags for tag in talent.tags)) or 0
    except:
        total_tracks = 0
    active_invitations = db.query(func.count(Invitation.id)).filter(Invitation.status == "pending").scalar() or 0

    # 领域分布（简化实现）
    field_distribution = {
        "增长": 68,
        "品牌": 52,
        "产品": 74,
        "技术": 89,
        "销售": 45,
        "其他": 40
    }

    # 城市分布（简化实现）
    city_distribution = {
        "北京": 120,
        "上海": 98,
        "深圳": 76,
        "杭州": 42,
        "其他": 32
    }

    return ResponseModel(
        data={
            "totalTalents": total_talents,
            "totalTracks": total_tracks,
            "activeInvitations": active_invitations,
            "fieldDistribution": field_distribution,
            "cityDistribution": city_distribution
        }
    )


@router.get("/featured", response_model=ResponseModel[dict])
async def get_featured_talents(
    limit: int = Query(3, ge=1, le=10),
    db: Session = Depends(get_db)
):
    """获取精选人才"""
    talents = db.query(Talent).filter(
        Talent.verified == True,
        Talent.available == True
    ).order_by(Talent.follower_count.desc()).limit(limit).all()

    items = []
    for talent in talents:
        items.append({
            "id": str(talent.id),
            "name": talent.name,
            "role": talent.role,
            "company": talent.company,
            "location": talent.location,
            "avatar": talent.avatar,
            "description": talent.description,
            "tags": talent.tags or [],
            "stats": talent.stats or {}
        })

    return ResponseModel(data={"items": items})


@router.get("", response_model=PaginatedResponse[dict])
async def get_talents(
    field: Optional[str] = Query(None),
    city: Optional[str] = Query(None),
    search: Optional[str] = Query(None),
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
    sort: Optional[str] = Query("latest"),
    db: Session = Depends(get_db),
    current_user: Optional[User] = Depends(get_current_user)
):
    """获取人才列表"""
    query = db.query(Talent).filter(Talent.verified == True)

    if field:
        query = query.filter(Talent.tags.contains([field]))
    if city:
        query = query.filter(Talent.location == city)
    if search:
        query = query.filter(
            or_(
                Talent.name.ilike(f"%{search}%"),
                Talent.company.ilike(f"%{search}%"),
                Talent.description.ilike(f"%{search}%")
            )
        )

    # 排序
    if sort == "followers":
        query = query.order_by(Talent.follower_count.desc())
    elif sort == "experience":
        # 这里可以根据实际需求实现经验排序
        query = query.order_by(Talent.created_at.desc())
    else:
        query = query.order_by(Talent.created_at.desc())

    total = query.count()
    items = query.offset((page - 1) * limit).limit(limit).all()

    talent_list = []
    for talent in items:
        talent_list.append({
            "id": str(talent.id),
            "name": talent.name,
            "role": talent.role,
            "company": talent.company,
            "location": talent.location,
            "avatar": talent.avatar,
            "description": talent.description,
            "tags": talent.tags or [],
            "stats": talent.stats or {},
            "verified": talent.verified,
            "available": talent.available,
            "createdAt": talent.created_at.isoformat() + "Z"
        })

    return PaginatedResponse(
        data={
            "items": talent_list,
            "pagination": PaginationInfo(
                page=page,
                limit=limit,
                total=total,
                totalPages=(total + limit - 1) // limit
            ),
            "filters": {
                "availableFields": ["增长", "品牌", "产品", "销售", "技术", "运营", "财务", "人力"],
                "availableCities": ["北京", "上海", "深圳", "杭州", "广州", "成都"]
            }
        }
    )


@router.get("/{talent_id}", response_model=ResponseModel[dict])
async def get_talent_detail(
    talent_id: str,
    db: Session = Depends(get_db),
    current_user: Optional[User] = Depends(get_current_user)
):
    """获取人才详情"""
    talent = db.query(Talent).filter(Talent.id == uuid.UUID(talent_id)).first()
    if not talent:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="人才不存在"
        )

    # 增加浏览次数
    talent.view_count += 1
    db.commit()

    return ResponseModel(
        data={
            "id": str(talent.id),
            "name": talent.name,
            "role": talent.role,
            "company": talent.company,
            "location": talent.location,
            "avatar": talent.avatar,
            "bio": talent.bio or talent.description,
            "tags": talent.tags or [],
            "stats": talent.stats or {},
            "verified": talent.verified,
            "available": talent.available,
            "skills": talent.skills or [],
            "projects": [],
            "education": talent.education or [],
            "contact": talent.contact or {},
            "createdAt": talent.created_at.isoformat() + "Z",
            "updatedAt": talent.updated_at.isoformat() + "Z"
        }
    )


@router.post("/{talent_id}/invite", response_model=ResponseModel[dict])
async def invite_talent(
    talent_id: str,
    request: dict,
    current_user: User = Depends(require_current_user),
    db: Session = Depends(get_db)
):
    """邀约人才"""
    talent = db.query(Talent).filter(Talent.id == uuid.UUID(talent_id)).first()
    if not talent:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="人才不存在"
        )

    invitation = Invitation(
        talent_id=talent.id,
        user_id=current_user.id,
        message=request.get("message"),
        preferred_date=datetime.fromisoformat(request["preferredDate"].replace("Z", "+00:00")) if request.get("preferredDate") else None,
        topic=request.get("topic"),
        duration=request.get("duration", 60)
    )
    db.add(invitation)
    db.commit()
    db.refresh(invitation)

    return ResponseModel(
        data={
            "invitationId": str(invitation.id),
            "talentId": str(talent.id),
            "status": invitation.status,
            "message": invitation.message,
            "createdAt": invitation.created_at.isoformat() + "Z"
        },
        message="邀约已发送，请等待对方回复"
    )

