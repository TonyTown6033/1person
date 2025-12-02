from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from sqlalchemy import or_, and_, func
from typing import Optional
from datetime import datetime
from app.core.database import get_db
from app.core.dependencies import get_current_user, require_current_user
from app.models.user import User
from app.models.event import Event, EventRegistration
from app.models.carousel import Carousel
from app.schemas.common import ResponseModel, PaginatedResponse, PaginationInfo
import uuid

router = APIRouter()


@router.get("", response_model=PaginatedResponse[dict])
async def get_events(
    status_filter: Optional[str] = Query(None, alias="status"),
    category: Optional[str] = Query(None),
    page: int = Query(1, ge=1),
    limit: int = Query(12, ge=1),
    db: Session = Depends(get_db)
):
    """获取活动列表"""
    query = db.query(Event)
    
    now = datetime.utcnow()
    if status_filter == "upcoming":
        query = query.filter(Event.start_date > now)
    elif status_filter == "past":
        query = query.filter(Event.end_date < now)
    elif status_filter == "all":
        pass
    else:
        query = query.filter(Event.start_date > now)
    
    if category:
        query = query.filter(Event.category == category)
    
    query = query.order_by(Event.start_date.asc())
    
    total = query.count()
    items = query.offset((page - 1) * limit).limit(limit).all()
    
    event_list = []
    for event in items:
        event_list.append({
            "id": str(event.id),
            "title": event.title,
            "description": event.description,
            "cover": event.cover,
            "date": event.start_date.isoformat() + "Z",
            "endDate": event.end_date.isoformat() + "Z",
            "location": event.location,
            "locationType": event.location_type,
            "category": event.category,
            "status": "upcoming" if event.start_date > now else "past",
            "capacity": event.capacity,
            "registered": event.registered_count,
            "speakers": event.speakers or [],
            "tags": event.tags or [],
            "organizer": event.organizer or {},
            "price": float(event.price) if event.price else 0,
            "createdAt": event.created_at.isoformat() + "Z"
        })
    
    return PaginatedResponse(
        data={
            "items": event_list,
            "pagination": PaginationInfo(
                page=page,
                limit=limit,
                total=total,
                totalPages=(total + limit - 1) // limit
            ),
            "stats": {
                "totalSpeakers": "200+",
                "totalFounders": "6000+",
                "upcomingEvents": db.query(func.count(Event.id)).filter(Event.start_date > now).scalar() or 0
            }
        }
    )


@router.get("/carousel", response_model=ResponseModel[dict])
async def get_carousel(db: Session = Depends(get_db)):
    """获取轮播图"""
    carousels = db.query(Carousel).filter(
        Carousel.page == "events",
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


@router.get("/my-events", response_model=PaginatedResponse[dict])
async def get_my_events(
    status_filter: Optional[str] = Query(None, alias="status"),
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1),
    current_user: User = Depends(require_current_user),
    db: Session = Depends(get_db)
):
    """获取我的活动"""
    query = db.query(EventRegistration).filter(EventRegistration.user_id == current_user.id)

    if status_filter == "upcoming":
        query = query.join(Event).filter(Event.start_date > datetime.utcnow())
    elif status_filter == "past":
        query = query.join(Event).filter(Event.end_date < datetime.utcnow())

    total = query.count()
    items = query.order_by(EventRegistration.created_at.desc()).offset((page - 1) * limit).limit(limit).all()

    event_list = []
    for reg in items:
        event = db.query(Event).filter(Event.id == reg.event_id).first()
        if event:
            event_list.append({
                "registration": {
                    "id": str(reg.id),
                    "status": reg.status,
                    "registeredAt": reg.created_at.isoformat() + "Z"
                },
                "event": {
                    "id": str(event.id),
                    "title": event.title,
                    "date": event.start_date.isoformat() + "Z",
                    "location": event.location,
                    "cover": event.cover
                }
            })

    return PaginatedResponse(
        data={
            "items": event_list,
            "pagination": PaginationInfo(
                page=page,
                limit=limit,
                total=total,
                totalPages=(total + limit - 1) // limit
            )
        }
    )


@router.get("/{event_id}", response_model=ResponseModel[dict])
async def get_event_detail(
    event_id: str,
    db: Session = Depends(get_db),
    current_user: Optional[User] = Depends(get_current_user)
):
    """获取活动详情"""
    event = db.query(Event).filter(Event.id == uuid.UUID(event_id)).first()
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="活动不存在"
        )
    
    is_registered = False
    if current_user:
        registration = db.query(EventRegistration).filter(
            EventRegistration.event_id == event.id,
            EventRegistration.user_id == current_user.id
        ).first()
        is_registered = registration is not None
    
    return ResponseModel(
        data={
            "id": str(event.id),
            "title": event.title,
            "description": event.description,
            "fullDescription": event.full_description,
            "cover": event.cover,
            "date": event.start_date.isoformat() + "Z",
            "endDate": event.end_date.isoformat() + "Z",
            "location": event.location,
            "locationType": event.location_type,
            "meetingLink": event.meeting_link,
            "category": event.category,
            "status": "upcoming" if event.start_date > datetime.utcnow() else "past",
            "capacity": event.capacity,
            "registered": event.registered_count,
            "agenda": event.agenda or [],
            "speakers": event.speakers or [],
            "tags": event.tags or [],
            "organizer": event.organizer or {},
            "price": float(event.price) if event.price else 0,
            "requirements": event.requirements,
            "benefits": event.benefits or [],
            "isRegistered": is_registered,
            "createdAt": event.created_at.isoformat() + "Z",
            "updatedAt": event.updated_at.isoformat() + "Z"
        }
    )


@router.post("/{event_id}/register", response_model=ResponseModel[dict])
async def register_event(
    event_id: str,
    request: dict,
    current_user: User = Depends(require_current_user),
    db: Session = Depends(get_db)
):
    """报名活动"""
    event = db.query(Event).filter(Event.id == uuid.UUID(event_id)).first()
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="活动不存在"
        )
    
    # 检查是否已报名
    existing = db.query(EventRegistration).filter(
        EventRegistration.event_id == event.id,
        EventRegistration.user_id == current_user.id
    ).first()
    
    if existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="已报名过此活动"
        )
    
    # 检查人数是否已满
    if event.capacity and event.registered_count >= event.capacity:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="活动人数已满"
        )
    
    registration = EventRegistration(
        event_id=event.id,
        user_id=current_user.id,
        attendee_info=request.get("attendeeInfo", {}),
        note=request.get("note"),
        questions=request.get("questions", [])
    )
    db.add(registration)
    event.registered_count += 1
    db.commit()
    db.refresh(registration)
    
    return ResponseModel(
        data={
            "registrationId": str(registration.id),
            "eventId": str(event.id),
            "status": registration.status,
            "qrCode": registration.qr_code,
            "meetingLink": event.meeting_link,
            "createdAt": registration.created_at.isoformat() + "Z"
        },
        message="报名成功！活动前将发送提醒通知"
    )


@router.delete("/{event_id}/register", response_model=ResponseModel[dict])
async def cancel_registration(
    event_id: str,
    current_user: User = Depends(require_current_user),
    db: Session = Depends(get_db)
):
    """取消报名"""
    registration = db.query(EventRegistration).filter(
        EventRegistration.event_id == uuid.UUID(event_id),
        EventRegistration.user_id == current_user.id
    ).first()
    
    if not registration:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="未报名此活动"
        )
    
    event = db.query(Event).filter(Event.id == registration.event_id).first()
    if event:
        event.registered_count = max(0, event.registered_count - 1)
    
    db.delete(registration)
    db.commit()
    
    return ResponseModel(message="已取消报名")

