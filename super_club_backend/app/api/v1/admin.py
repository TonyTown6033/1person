"""
管理后台API路由
"""
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from typing import Optional, List
from datetime import datetime, timedelta
from app.core.database import get_db
from app.core.admin_dependencies import require_admin_user, require_super_admin_user
from app.models.user import User
from app.models.project import Project
from app.models.event import Event
from app.models.content import Content
from app.models.talent import Talent
from app.models.carousel import Carousel
from app.schemas.common import ResponseModel, PaginatedResponse, PaginationInfo

router = APIRouter()


@router.get("/dashboard/stats", response_model=ResponseModel[dict])
async def get_dashboard_stats(
    current_admin: User = Depends(require_admin_user),
    db: Session = Depends(get_db)
):
    """获取仪表板统计数据"""
    
    # 用户统计
    total_users = db.query(func.count(User.id)).scalar() or 0
    active_users = db.query(func.count(User.id)).filter(User.is_active == True).scalar() or 0
    new_users_this_month = db.query(func.count(User.id)).filter(
        User.created_at >= datetime.utcnow() - timedelta(days=30)
    ).scalar() or 0
    
    # 项目统计
    total_projects = db.query(func.count(Project.id)).scalar() or 0
    active_projects = db.query(func.count(Project.id)).filter(Project.status == "active").scalar() or 0
    featured_projects = db.query(func.count(Project.id)).filter(Project.is_featured == True).scalar() or 0
    
    # 活动统计
    total_events = db.query(func.count(Event.id)).scalar() or 0
    upcoming_events = db.query(func.count(Event.id)).filter(
        Event.start_date > datetime.utcnow()
    ).scalar() or 0
    
    # 内容统计
    total_content = db.query(func.count(Content.id)).scalar() or 0
    published_content = db.query(func.count(Content.id)).filter(Content.is_published == True).scalar() or 0
    
    stats = {
        "users": {
            "total": total_users,
            "active": active_users,
            "new_this_month": new_users_this_month,
            "growth_rate": round((new_users_this_month / max(total_users - new_users_this_month, 1)) * 100, 1)
        },
        "projects": {
            "total": total_projects,
            "active": active_projects,
            "featured": featured_projects
        },
        "events": {
            "total": total_events,
            "upcoming": upcoming_events
        },
        "content": {
            "total": total_content,
            "published": published_content
        }
    }
    
    return ResponseModel(data=stats)


@router.get("/users", response_model=PaginatedResponse[dict])
async def get_admin_users(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    search: Optional[str] = Query(None),
    status: Optional[str] = Query(None),
    role: Optional[str] = Query(None),
    current_admin: User = Depends(require_admin_user),
    db: Session = Depends(get_db)
):
    """获取用户列表（管理员）"""
    
    query = db.query(User)
    
    # 搜索过滤
    if search:
        query = query.filter(
            (User.name.ilike(f"%{search}%")) |
            (User.email.ilike(f"%{search}%")) |
            (User.company.ilike(f"%{search}%"))
        )
    
    # 状态过滤
    if status:
        if status == "active":
            query = query.filter(User.is_active == True)
        elif status == "inactive":
            query = query.filter(User.is_active == False)
    
    # 角色过滤
    if role:
        query = query.filter(User.role == role)
    
    # 排序
    query = query.order_by(desc(User.created_at))
    
    # 分页
    total = query.count()
    users = query.offset((page - 1) * limit).limit(limit).all()
    
    # 格式化用户数据
    user_list = []
    for user in users:
        user_data = {
            "id": str(user.id),
            "name": user.name,
            "email": user.email,
            "phone": user.phone,
            "company": user.company,
            "position": user.position,
            "role": user.role,
            "membershipLevel": user.membership_level,
            "isActive": user.is_active,
            "verified": user.verified,
            "emailVerified": user.email_verified,
            "avatar": user.avatar,
            "createdAt": user.created_at.isoformat() + "Z",
            "updatedAt": user.updated_at.isoformat() + "Z"
        }
        user_list.append(user_data)
    
    return PaginatedResponse(
        data={
            "items": user_list,
            "pagination": {
                "page": page,
                "limit": limit,
                "total": total,
                "totalPages": (total + limit - 1) // limit
            }
        }
    )


@router.put("/users/{user_id}/status")
async def update_user_status(
    user_id: str,
    is_active: bool,
    current_admin: User = Depends(require_admin_user),
    db: Session = Depends(get_db)
):
    """更新用户状态"""
    
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="用户不存在"
        )
    
    # 防止管理员禁用自己
    if user.id == current_admin.id and not is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="不能禁用自己的账户"
        )
    
    user.is_active = is_active
    db.commit()
    
    return ResponseModel(
        data={"id": str(user.id), "isActive": user.is_active},
        message=f"用户已{'启用' if is_active else '禁用'}"
    )


@router.put("/users/{user_id}/role")
async def update_user_role(
    user_id: str,
    role: str,
    current_admin: User = Depends(require_super_admin_user),
    db: Session = Depends(get_db)
):
    """更新用户角色（仅超级管理员）"""
    
    if role not in ["user", "admin", "super_admin"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="无效的角色"
        )
    
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="用户不存在"
        )
    
    # 防止超级管理员降级自己
    if user.id == current_admin.id and role != "super_admin":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="不能降级自己的角色"
        )
    
    user.role = role
    db.commit()
    
    return ResponseModel(
        data={"id": str(user.id), "role": user.role},
        message="用户角色已更新"
    )


@router.get("/projects", response_model=PaginatedResponse[dict])
async def get_admin_projects(
    page: int = Query(1, ge=1),
    limit: int = Query(12, ge=1, le=50),
    search: Optional[str] = Query(None),
    status: Optional[str] = Query(None),
    category: Optional[str] = Query(None),
    featured: Optional[bool] = Query(None),
    current_admin: User = Depends(require_admin_user),
    db: Session = Depends(get_db)
):
    """获取项目列表（管理员）"""
    
    query = db.query(Project)
    
    # 搜索过滤
    if search:
        query = query.filter(
            (Project.name.ilike(f"%{search}%")) |
            (Project.description.ilike(f"%{search}%"))
        )
    
    # 状态过滤
    if status:
        query = query.filter(Project.status == status)
    
    # 分类过滤
    if category:
        query = query.filter(Project.category == category)
    
    # 精选过滤
    if featured is not None:
        query = query.filter(Project.is_featured == featured)
    
    # 排序
    query = query.order_by(desc(Project.created_at))
    
    # 分页
    total = query.count()
    projects = query.offset((page - 1) * limit).limit(limit).all()
    
    # 格式化项目数据
    project_list = []
    for project in projects:
        # 获取项目所有者信息
        owner = db.query(User).filter(User.id == project.owner_id).first()
        
        project_data = {
            "id": str(project.id),
            "name": project.name,
            "type": project.type,
            "description": project.description,
            "category": project.category,
            "status": project.status,
            "tags": project.tags or [],
            "isFeatured": project.is_featured,
            "viewCount": project.view_count,
            "interestCount": project.interest_count,
            "collaborationCount": project.collaboration_count,
            "ownerName": owner.name if owner else "未知用户",
            "createdAt": project.created_at.isoformat() + "Z",
            "updatedAt": project.updated_at.isoformat() + "Z"
        }
        project_list.append(project_data)
    
    return PaginatedResponse(
        data={
            "items": project_list,
            "pagination": {
                "page": page,
                "limit": limit,
                "total": total,
                "totalPages": (total + limit - 1) // limit
            }
        }
    )


@router.put("/projects/{project_id}/featured")
async def toggle_project_featured(
    project_id: str,
    is_featured: bool,
    current_admin: User = Depends(require_admin_user),
    db: Session = Depends(get_db)
):
    """切换项目精选状态"""
    
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="项目不存在"
        )
    
    project.is_featured = is_featured
    db.commit()
    
    return ResponseModel(
        data={"id": str(project.id), "isFeatured": project.is_featured},
        message=f"项目已{'设为精选' if is_featured else '取消精选'}"
    )


@router.delete("/projects/{project_id}")
async def delete_project(
    project_id: str,
    current_admin: User = Depends(require_admin_user),
    db: Session = Depends(get_db)
):
    """删除项目"""
    
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="项目不存在"
        )
    
    db.delete(project)
    db.commit()
    
    return ResponseModel(
        data={"id": str(project.id)},
        message="项目已删除"
    )


@router.get("/recent-activities")
async def get_recent_activities(
    limit: int = Query(10, ge=1, le=50),
    current_admin: User = Depends(require_admin_user),
    db: Session = Depends(get_db)
):
    """获取最近活动"""
    
    activities = []
    
    # 最近注册的用户
    recent_users = db.query(User).order_by(desc(User.created_at)).limit(limit // 2).all()
    for user in recent_users:
        activities.append({
            "id": f"user_{user.id}",
            "type": "user_register",
            "title": f"新用户注册：{user.name}",
            "icon": "👤",
            "time": user.created_at.isoformat() + "Z"
        })
    
    # 最近创建的项目
    recent_projects = db.query(Project).order_by(desc(Project.created_at)).limit(limit // 2).all()
    for project in recent_projects:
        activities.append({
            "id": f"project_{project.id}",
            "type": "project_create",
            "title": f"新项目发布：{project.name}",
            "icon": "🚀",
            "time": project.created_at.isoformat() + "Z"
        })
    
    # 按时间排序
    activities.sort(key=lambda x: x["time"], reverse=True)
    
    return ResponseModel(data=activities[:limit])


# ==================== 内容管理 API ====================

@router.get("/content", response_model=PaginatedResponse[dict])
async def get_admin_content(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    search: Optional[str] = Query(None),
    type: Optional[str] = Query(None),
    department: Optional[str] = Query(None),
    is_published: Optional[bool] = Query(None),
    current_admin: User = Depends(require_admin_user),
    db: Session = Depends(get_db)
):
    """获取内容列表（管理员）"""
    
    query = db.query(Content)
    
    # 搜索过滤
    if search:
        query = query.filter(
            (Content.title.ilike(f"%{search}%")) |
            (Content.description.ilike(f"%{search}%"))
        )
    
    # 类型过滤
    if type:
        query = query.filter(Content.type == type)
    
    # 部门/分类过滤
    if department:
        query = query.filter(Content.department == department)
    
    # 发布状态过滤
    if is_published is not None:
        query = query.filter(Content.is_published == is_published)
    
    # 排序
    query = query.order_by(desc(Content.created_at))
    
    # 分页
    total = query.count()
    contents = query.offset((page - 1) * limit).limit(limit).all()
    
    import json
    
    # 格式化内容数据
    content_list = []
    for content in contents:
        # 获取作者信息
        author = db.query(User).filter(User.id == content.author_id).first()
        
        # 解析tags（从JSON字符串转换为数组）
        tags = []
        if content.tags:
            try:
                tags = json.loads(content.tags)
            except:
                tags = []
        
        content_data = {
            "id": str(content.id),
            "title": content.title,
            "description": content.description,
            "excerpt": content.excerpt,
            "type": content.type,
            "department": content.department,
            "coverImage": content.cover_image,
            "tags": tags,
            "isPublished": content.is_published,
            "isFeatured": content.is_featured,
            "viewCount": content.view_count,
            "likeCount": content.like_count,
            "commentCount": content.comment_count,
            "readingTime": content.reading_time,
            "author": {
                "id": str(author.id) if author else None,
                "name": author.name if author else "未知作者",
                "avatar": author.avatar if author else None
            },
            "publishedAt": content.published_at.isoformat() + "Z" if content.published_at else None,
            "createdAt": content.created_at.isoformat() + "Z",
            "updatedAt": content.updated_at.isoformat() + "Z"
        }
        content_list.append(content_data)
    
    return PaginatedResponse(
        data={
            "items": content_list,
            "pagination": {
                "page": page,
                "limit": limit,
                "total": total,
                "totalPages": (total + limit - 1) // limit
            }
        }
    )


@router.post("/content", response_model=ResponseModel[dict])
async def create_admin_content(
    request: dict,
    current_admin: User = Depends(require_admin_user),
    db: Session = Depends(get_db)
):
    """创建内容（管理员）"""
    import json
    
    # 将tags数组转换为JSON字符串存储
    tags = request.get("tags", [])
    tags_str = json.dumps(tags, ensure_ascii=False) if tags else None
    
    content = Content(
        title=request.get("title"),
        description=request.get("description"),
        excerpt=request.get("excerpt"),
        content=request.get("content"),
        type=request.get("type", "article"),
        department=request.get("department"),
        cover_image=request.get("coverImage"),
        tags=tags_str,
        is_published=request.get("isPublished", False),
        is_featured=request.get("isFeatured", False),
        reading_time=request.get("readingTime", 5),
        author_id=current_admin.id,
        published_at=datetime.utcnow() if request.get("isPublished") else None,
        view_count=0,
        like_count=0,
        comment_count=0,
        favorite_count=0
    )
    
    db.add(content)
    db.commit()
    db.refresh(content)
    
    return ResponseModel(
        data={
            "id": str(content.id),
            "title": content.title,
            "createdAt": content.created_at.isoformat() + "Z"
        },
        message="内容创建成功"
    )


@router.get("/content/{content_id}", response_model=ResponseModel[dict])
async def get_admin_content_detail(
    content_id: str,
    current_admin: User = Depends(require_admin_user),
    db: Session = Depends(get_db)
):
    """获取内容详情（管理员）"""
    import json
    
    content = db.query(Content).filter(Content.id == content_id).first()
    if not content:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="内容不存在"
        )
    
    author = db.query(User).filter(User.id == content.author_id).first()
    
    # 解析tags
    tags = []
    if content.tags:
        try:
            tags = json.loads(content.tags)
        except:
            tags = []
    
    return ResponseModel(
        data={
            "id": str(content.id),
            "title": content.title,
            "description": content.description,
            "excerpt": content.excerpt,
            "content": content.content,
            "type": content.type,
            "department": content.department,
            "coverImage": content.cover_image,
            "tags": tags,
            "isPublished": content.is_published,
            "isFeatured": content.is_featured,
            "viewCount": content.view_count,
            "likeCount": content.like_count,
            "commentCount": content.comment_count,
            "readingTime": content.reading_time,
            "author": {
                "id": str(author.id) if author else None,
                "name": author.name if author else "未知作者",
                "avatar": author.avatar if author else None
            },
            "publishedAt": content.published_at.isoformat() + "Z" if content.published_at else None,
            "createdAt": content.created_at.isoformat() + "Z",
            "updatedAt": content.updated_at.isoformat() + "Z"
        }
    )


@router.put("/content/{content_id}", response_model=ResponseModel[dict])
async def update_admin_content(
    content_id: str,
    request: dict,
    current_admin: User = Depends(require_admin_user),
    db: Session = Depends(get_db)
):
    """更新内容（管理员）"""
    
    content = db.query(Content).filter(Content.id == content_id).first()
    if not content:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="内容不存在"
        )
    
    # 更新字段
    if "title" in request:
        content.title = request["title"]
    if "description" in request:
        content.description = request["description"]
    if "excerpt" in request:
        content.excerpt = request["excerpt"]
    if "content" in request:
        content.content = request["content"]
    if "type" in request:
        content.type = request["type"]
    if "department" in request:
        content.department = request["department"]
    if "coverImage" in request:
        content.cover_image = request["coverImage"]
    if "tags" in request:
        import json
        content.tags = json.dumps(request["tags"], ensure_ascii=False) if request["tags"] else None
    if "readingTime" in request:
        content.reading_time = request["readingTime"]
    if "isFeatured" in request:
        content.is_featured = request["isFeatured"]
    
    # 处理发布状态变更
    if "isPublished" in request:
        was_published = content.is_published
        content.is_published = request["isPublished"]
        if request["isPublished"] and not was_published:
            content.published_at = datetime.utcnow()
    
    db.commit()
    db.refresh(content)
    
    return ResponseModel(
        data={
            "id": str(content.id),
            "title": content.title,
            "isPublished": content.is_published,
            "updatedAt": content.updated_at.isoformat() + "Z"
        },
        message="内容更新成功"
    )


@router.put("/content/{content_id}/publish", response_model=ResponseModel[dict])
async def toggle_content_publish(
    content_id: str,
    is_published: bool = Query(...),
    current_admin: User = Depends(require_admin_user),
    db: Session = Depends(get_db)
):
    """切换内容发布状态"""
    
    content = db.query(Content).filter(Content.id == content_id).first()
    if not content:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="内容不存在"
        )
    
    content.is_published = is_published
    if is_published and not content.published_at:
        content.published_at = datetime.utcnow()
    
    db.commit()
    
    return ResponseModel(
        data={"id": str(content.id), "isPublished": content.is_published},
        message=f"内容已{'发布' if is_published else '取消发布'}"
    )


@router.put("/content/{content_id}/featured", response_model=ResponseModel[dict])
async def toggle_content_featured(
    content_id: str,
    is_featured: bool = Query(...),
    current_admin: User = Depends(require_admin_user),
    db: Session = Depends(get_db)
):
    """切换内容精选状态"""
    
    content = db.query(Content).filter(Content.id == content_id).first()
    if not content:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="内容不存在"
        )
    
    content.is_featured = is_featured
    db.commit()
    
    return ResponseModel(
        data={"id": str(content.id), "isFeatured": content.is_featured},
        message=f"内容已{'设为精选' if is_featured else '取消精选'}"
    )


@router.delete("/content/{content_id}", response_model=ResponseModel[dict])
async def delete_admin_content(
    content_id: str,
    current_admin: User = Depends(require_admin_user),
    db: Session = Depends(get_db)
):
    """删除内容（管理员）"""
    
    content = db.query(Content).filter(Content.id == content_id).first()
    if not content:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="内容不存在"
        )
    
    db.delete(content)
    db.commit()
    
    return ResponseModel(
        data={"id": content_id},
        message="内容已删除"
    )


@router.get("/content/stats/overview", response_model=ResponseModel[dict])
async def get_content_stats(
    current_admin: User = Depends(require_admin_user),
    db: Session = Depends(get_db)
):
    """获取内容统计概览"""
    
    total = db.query(func.count(Content.id)).scalar() or 0
    published = db.query(func.count(Content.id)).filter(Content.is_published == True).scalar() or 0
    draft = db.query(func.count(Content.id)).filter(Content.is_published == False).scalar() or 0
    featured = db.query(func.count(Content.id)).filter(Content.is_featured == True).scalar() or 0
    
    # 按类型统计
    type_stats = db.query(
        Content.type,
        func.count(Content.id)
    ).group_by(Content.type).all()
    
    # 按部门统计
    dept_stats = db.query(
        Content.department,
        func.count(Content.id)
    ).filter(Content.department != None).group_by(Content.department).all()
    
    # 总浏览量和互动量
    total_views = db.query(func.sum(Content.view_count)).scalar() or 0
    total_likes = db.query(func.sum(Content.like_count)).scalar() or 0
    total_comments = db.query(func.sum(Content.comment_count)).scalar() or 0
    
    return ResponseModel(
        data={
            "total": total,
            "published": published,
            "draft": draft,
            "featured": featured,
            "byType": {item[0]: item[1] for item in type_stats if item[0]},
            "byDepartment": {item[0]: item[1] for item in dept_stats if item[0]},
            "engagement": {
                "totalViews": total_views,
                "totalLikes": total_likes,
                "totalComments": total_comments
            }
        }
    )
