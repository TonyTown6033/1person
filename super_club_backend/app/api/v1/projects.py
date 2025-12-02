from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from sqlalchemy import or_, func
from typing import Optional, List
from datetime import datetime
from app.core.database import get_db
from app.core.dependencies import get_current_user, require_current_user
from app.models.user import User
from app.models.project import Project, ProjectInterest
from app.schemas.common import ResponseModel, PaginatedResponse, PaginationInfo
import uuid

router = APIRouter()


@router.get("", response_model=PaginatedResponse[dict])
async def get_projects(
    category: Optional[str] = Query(None),
    search: Optional[str] = Query(None),
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1),
    sort: Optional[str] = Query("latest"),
    current_user: Optional[User] = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """获取项目列表"""
    query = db.query(Project)
    
    if category:
        query = query.filter(Project.category == category)
    if search:
        query = query.filter(
            or_(
                Project.name.ilike(f"%{search}%"),
                Project.description.ilike(f"%{search}%")
            )
        )
    
    if sort == "popular":
        query = query.order_by(Project.interest_count.desc(), Project.view_count.desc())
    else:
        query = query.order_by(Project.created_at.desc())
    
    total = query.count()
    items = query.offset((page - 1) * limit).limit(limit).all()
    
    project_list = []
    for project in items:
        owner = db.query(User).filter(User.id == project.owner_id).first()
        project_list.append({
            "id": str(project.id),
            "name": project.name,
            "type": project.type,
            "description": project.description,
            "logo": project.logo,
            "tags": project.tags or [],
            "category": project.category,
            "status": project.status,
            "owner": {
                "id": str(owner.id) if owner else "",
                "name": owner.name if owner else "",
                "company": owner.company or ""
            },
            "stats": {
                "views": project.view_count,
                "interests": project.interest_count
            },
            "createdAt": project.created_at.isoformat() + "Z",
            "updatedAt": project.updated_at.isoformat() + "Z"
        })
    
    return PaginatedResponse(
        data={
            "items": project_list,
            "pagination": PaginationInfo(
                page=page,
                limit=limit,
                total=total,
                totalPages=(total + limit - 1) // limit
            ),
            "filters": {
                "categories": ["不限", "消费", "企业服务", "文娱", "教育", "AI", "品牌", "渠道", "资本", "产业链"]
            }
        }
    )


@router.get("/{project_id}", response_model=ResponseModel[dict])
async def get_project_detail(
    project_id: str,
    current_user: Optional[User] = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """获取项目详情"""
    project = db.query(Project).filter(Project.id == uuid.UUID(project_id)).first()
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="项目不存在"
        )
    
    project.view_count += 1
    db.commit()
    
    owner = db.query(User).filter(User.id == project.owner_id).first()
    
    return ResponseModel(
        data={
            "id": str(project.id),
            "name": project.name,
            "type": project.type,
            "description": project.description,
            "fullDescription": project.full_description,
            "logo": project.logo,
            "coverImage": project.cover_image,
            "tags": project.tags or [],
            "category": project.category,
            "status": project.status,
            "owner": {
                "id": str(owner.id) if owner else "",
                "name": owner.name if owner else "",
                "avatar": owner.avatar,
                "company": owner.company or "",
                "position": owner.position or ""
            },
            "needs": project.needs or [],
            "milestones": project.milestones or [],
            "team": project.team or [],
            "stats": {
                "views": project.view_count,
                "interests": project.interest_count,
                "collaborations": project.collaboration_count
            },
            "contact": project.contact or {},
            "createdAt": project.created_at.isoformat() + "Z",
            "updatedAt": project.updated_at.isoformat() + "Z"
        }
    )


@router.post("", response_model=ResponseModel[dict])
async def create_project(
    request: dict,
    current_user: User = Depends(require_current_user),
    db: Session = Depends(get_db)
):
    """发布项目"""
    project = Project(
        owner_id=current_user.id,
        name=request["name"],
        type=request.get("type"),
        description=request["description"],
        full_description=request.get("fullDescription"),
        category=request.get("category"),
        tags=request.get("tags", []),
        needs=request.get("needs", []),
        contact=request.get("contact", {})
    )
    db.add(project)
    db.commit()
    db.refresh(project)
    
    return ResponseModel(
        data={
            "id": str(project.id),
            "name": project.name,
            "status": "pending_review",
            "createdAt": project.created_at.isoformat() + "Z"
        },
        message="项目已提交，审核通过后将展示"
    )


@router.put("/{project_id}", response_model=ResponseModel[dict])
async def update_project(
    project_id: str,
    request: dict,
    current_user: User = Depends(require_current_user),
    db: Session = Depends(get_db)
):
    """更新项目"""
    project = db.query(Project).filter(Project.id == uuid.UUID(project_id)).first()
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="项目不存在"
        )
    
    if project.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="无权修改此项目"
        )
    
    if "name" in request:
        project.name = request["name"]
    if "description" in request:
        project.description = request["description"]
    if "fullDescription" in request:
        project.full_description = request["fullDescription"]
    if "tags" in request:
        project.tags = request["tags"]
    if "needs" in request:
        project.needs = request["needs"]
    
    db.commit()
    db.refresh(project)
    
    return ResponseModel(
        data={
            "id": str(project.id),
            "name": project.name,
            "updatedAt": project.updated_at.isoformat() + "Z"
        },
        message="项目信息已更新"
    )


@router.delete("/{project_id}", response_model=ResponseModel[dict])
async def delete_project(
    project_id: str,
    current_user: User = Depends(require_current_user),
    db: Session = Depends(get_db)
):
    """删除项目"""
    project = db.query(Project).filter(Project.id == uuid.UUID(project_id)).first()
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="项目不存在"
        )
    
    if project.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="无权删除此项目"
        )
    
    db.delete(project)
    db.commit()
    
    return ResponseModel(message="项目已删除")


@router.post("/{project_id}/interest", response_model=ResponseModel[dict])
async def express_interest(
    project_id: str,
    request: dict,
    current_user: User = Depends(require_current_user),
    db: Session = Depends(get_db)
):
    """表达合作意向"""
    project = db.query(Project).filter(Project.id == uuid.UUID(project_id)).first()
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="项目不存在"
        )
    
    # 检查是否已表达过意向
    existing = db.query(ProjectInterest).filter(
        ProjectInterest.project_id == project.id,
        ProjectInterest.user_id == current_user.id
    ).first()
    
    if existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="已表达过合作意向"
        )
    
    interest = ProjectInterest(
        project_id=project.id,
        user_id=current_user.id,
        message=request.get("message"),
        capability=request.get("capability"),
        contact=request.get("contact", {})
    )
    db.add(interest)
    project.interest_count += 1
    db.commit()
    db.refresh(interest)
    
    return ResponseModel(
        data={
            "interestId": str(interest.id),
            "projectId": str(project.id),
            "status": interest.status,
            "createdAt": interest.created_at.isoformat() + "Z"
        },
        message="合作意向已提交"
    )

