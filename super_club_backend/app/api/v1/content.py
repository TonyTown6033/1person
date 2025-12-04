from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from sqlalchemy import or_, func
from typing import Optional
from app.core.database import get_db
from app.core.dependencies import get_current_user, require_current_user
from app.core.logging import logger
from app.models.user import User
from app.models.content import Content, Comment
from app.models.like import Like
from app.schemas.common import ResponseModel, PaginatedResponse, PaginationInfo
import uuid
import os
from pathlib import Path

router = APIRouter()


@router.get("/cards", response_model=PaginatedResponse[dict])
async def get_content_cards(
    department: Optional[str] = Query(None),
    type: Optional[str] = Query(None),
    search: Optional[str] = Query(None),
    page: int = Query(1, ge=1),
    limit: int = Query(4, ge=1),
    db: Session = Depends(get_db)
):
    """获取内容卡片"""
    query = db.query(Content).filter(Content.is_published == True)
    
    if department:
        query = query.filter(Content.department == department)
    if type:
        query = query.filter(Content.type == type)
    if search:
        query = query.filter(
            or_(
                Content.title.ilike(f"%{search}%"),
                Content.description.ilike(f"%{search}%")
            )
        )
    
    query = query.order_by(Content.published_at.desc())
    
    total = query.count()
    items = query.offset((page - 1) * limit).limit(limit).all()
    
    card_list = []
    for content in items:
        author = db.query(User).filter(User.id == content.author_id).first()
        card_list.append({
            "id": str(content.id),
            "title": content.title,
            "description": content.description or content.excerpt,
            "image": content.image or content.cover_image,
            "type": content.type,
            "department": content.department,
            "author": {
                "id": str(author.id) if author else "",
                "name": author.name if author else "",
                "avatar": author.avatar
            },
            "stats": {
                "views": content.view_count,
                "likes": content.like_count,
                "comments": content.comment_count
            },
            "tags": content.tags or [],
            "publishedAt": content.published_at.isoformat() + "Z" if content.published_at else None,
            "readingTime": content.reading_time
        })
    
    return PaginatedResponse(
        data={
            "items": card_list,
            "pagination": PaginationInfo(
                page=page,
                limit=limit,
                total=total,
                totalPages=(total + limit - 1) // limit
            ),
            "filters": {
                "departments": ["战略部", "品牌部", "销售部", "人力部", "财法部", "技术部"],
                "types": ["文章", "视频", "课程", "案例"]
            }
        }
    )


@router.get("/articles", response_model=PaginatedResponse[dict])
async def get_articles(
    category: Optional[str] = Query(None),
    tag: Optional[str] = Query(None),
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1),
    db: Session = Depends(get_db)
):
    """获取文章列表"""
    logger.info(f"获取文章列表 - page={page}, limit={limit}, category={category}, tag={tag}")
    
    query = db.query(Content).filter(
        Content.type == "article",
        Content.is_published == True
    )
    
    if category:
        query = query.filter(Content.department == category)
    if tag:
        query = query.filter(Content.tags.contains([tag]))
    
    query = query.order_by(Content.published_at.desc())
    
    total = query.count()
    logger.debug(f"查询到 {total} 篇文章")
    
    items = query.offset((page - 1) * limit).limit(limit).all()
    
    article_list = []
    for article in items:
        author = db.query(User).filter(User.id == article.author_id).first()
        article_list.append({
            "id": str(article.id),
            "title": article.title,
            "excerpt": article.excerpt or article.description,
            "coverImage": article.cover_image,
            "author": {
                "id": str(author.id) if author else "",
                "name": author.name if author else "",
                "avatar": author.avatar
            },
            "department": article.department,
            "tags": article.tags or [],
            "stats": {
                "views": article.view_count,
                "likes": article.like_count,
                "comments": article.comment_count
            },
            "publishedAt": article.published_at.isoformat() + "Z" if article.published_at else None,
            "readingTime": article.reading_time
        })
    
    logger.info(f"返回 {len(article_list)} 篇文章")
    
    return PaginatedResponse(
        data={
            "items": article_list,
            "pagination": PaginationInfo(
                page=page,
                limit=limit,
                total=total,
                totalPages=(total + limit - 1) // limit
            )
        }
    )


def read_markdown_file(file_path: str) -> Optional[str]:
    """从文件系统读取 markdown 文件内容"""
    try:
        # 如果是相对路径，从项目根目录开始
        if not os.path.isabs(file_path):
            # 获取项目根目录（super_club_backend）
            base_dir = Path(__file__).parent.parent.parent.parent
            file_path = base_dir / file_path
        else:
            file_path = Path(file_path)
        
        logger.debug(f"尝试读取 Markdown 文件: {file_path}")
        
        if file_path.exists() and file_path.suffix.lower() in ['.md', '.markdown']:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                logger.info(f"成功读取 Markdown 文件: {file_path} ({len(content)} 字符)")
                return content
        else:
            logger.warning(f"Markdown 文件不存在或格式不正确: {file_path}")
        return None
    except Exception as e:
        logger.error(f"读取 markdown 文件失败: {file_path}, 错误: {e}", exc_info=True)
        return None


@router.post("/articles", response_model=ResponseModel[dict])
async def create_article(
    request: dict,
    current_user: User = Depends(require_current_user),
    db: Session = Depends(get_db)
):
    """创建文章"""
    from datetime import datetime
    import json as json_module
    
    # 处理 tags - 转换为 JSON 字符串存储
    tags = request.get("tags")
    if tags and isinstance(tags, list):
        tags = json_module.dumps(tags)
    
    article = Content(
        title=request["title"],
        description=request.get("description"),
        content=request["content"],  # 可以是 Markdown 文本或文件路径
        type=request.get("type", "article"),
        department=request.get("department"),
        author_id=current_user.id,
        cover_image=request.get("coverImage"),
        tags=tags,
        is_published=request.get("isPublished", False),
        published_at=datetime.now() if request.get("isPublished") else None,
        reading_time=request.get("readingTime", 5),
        view_count=0,
        like_count=0,
        comment_count=0,
        favorite_count=0
    )
    db.add(article)
    db.commit()
    db.refresh(article)
    
    return ResponseModel(
        data={
            "id": str(article.id),
            "title": article.title,
            "createdAt": article.created_at.isoformat() + "Z"
        },
        message="文章创建成功"
    )


@router.get("/articles/{article_id}", response_model=ResponseModel[dict])
async def get_article_detail(
    article_id: str,
    db: Session = Depends(get_db),
    current_user: Optional[User] = Depends(get_current_user)
):
    """获取文章详情"""
    logger.info(f"获取文章详情 - article_id={article_id}, user_id={current_user.id if current_user else None}")
    
    # 直接使用字符串ID查询（MySQL中ID是String类型）
    article = db.query(Content).filter(Content.id == article_id).first()
    
    if not article:
        logger.warning(f"文章不存在: {article_id}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="文章不存在"
        )
    
    article.view_count += 1
    db.commit()
    
    author = db.query(User).filter(User.id == article.author_id).first()
    
    is_liked = False
    is_favorited = False
    if current_user:
        like = db.query(Like).filter(
            Like.user_id == current_user.id,
            Like.resource_type == "content",
            Like.resource_id == article.id
        ).first()
        is_liked = like is not None
    
    # 处理文章内容：如果 content 字段是 markdown 文件路径，则读取文件内容
    content = article.content
    if content and (content.endswith('.md') or content.endswith('.markdown')):
        logger.info(f"检测到 Markdown 文件路径: {content}")
        # 尝试从文件系统读取
        file_content = read_markdown_file(content)
        if file_content:
            content = file_content
            logger.info(f"成功读取 Markdown 文件内容 ({len(content)} 字符)")
        else:
            logger.warning(f"无法读取 Markdown 文件: {content}")
    
    return ResponseModel(
        data={
            "id": str(article.id),
            "title": article.title,
            "content": content,
            "coverImage": article.cover_image,
            "author": {
                "id": str(author.id) if author else "",
                "name": author.name if author else "",
                "avatar": author.avatar,
                "bio": author.bio
            },
            "department": article.department,
            "tags": article.tags or [],
            "stats": {
                "views": article.view_count,
                "likes": article.like_count,
                "comments": article.comment_count,
                "favorites": article.favorite_count
            },
            "publishedAt": article.published_at.isoformat() + "Z" if article.published_at else None,
            "updatedAt": article.updated_at.isoformat() + "Z",
            "readingTime": article.reading_time,
            "relatedArticles": [],
            "isFavorited": is_favorited,
            "isLiked": is_liked
        }
    )


@router.post("/articles/{article_id}/like", response_model=ResponseModel[dict])
async def like_article(
    article_id: str,
    current_user: User = Depends(require_current_user),
    db: Session = Depends(get_db)
):
    """点赞文章"""
    article = db.query(Content).filter(Content.id == article_id).first()
    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="文章不存在"
        )
    
    # 检查是否已点赞
    existing = db.query(Like).filter(
        Like.user_id == current_user.id,
        Like.resource_type == "content",
        Like.resource_id == article.id
    ).first()
    
    if existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="已点赞过此文章"
        )
    
    like = Like(
        user_id=current_user.id,
        resource_type="content",
        resource_id=article.id
    )
    db.add(like)
    article.like_count += 1
    db.commit()
    
    return ResponseModel(
        data={
            "articleId": str(article.id),
            "isLiked": True,
            "totalLikes": article.like_count
        },
        message="点赞成功"
    )


@router.delete("/articles/{article_id}/like", response_model=ResponseModel[dict])
async def unlike_article(
    article_id: str,
    current_user: User = Depends(require_current_user),
    db: Session = Depends(get_db)
):
    """取消点赞"""
    article = db.query(Content).filter(Content.id == article_id).first()
    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="文章不存在"
        )
    
    like = db.query(Like).filter(
        Like.user_id == current_user.id,
        Like.resource_type == "content",
        Like.resource_id == article.id
    ).first()
    
    if not like:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="未点赞过此文章"
        )
    
    db.delete(like)
    article.like_count = max(0, article.like_count - 1)
    db.commit()
    
    return ResponseModel(
        data={
            "articleId": str(article.id),
            "isLiked": False,
            "totalLikes": article.like_count
        },
        message="已取消点赞"
    )


@router.post("/articles/{article_id}/comments", response_model=ResponseModel[dict])
async def create_comment(
    article_id: str,
    request: dict,
    current_user: User = Depends(require_current_user),
    db: Session = Depends(get_db)
):
    """评论文章"""
    article = db.query(Content).filter(Content.id == article_id).first()
    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="文章不存在"
        )
    
    comment = Comment(
        content_id=article.id,
        user_id=current_user.id,
        content=request["content"],
        parent_id=request.get("parentId")  # 直接使用字符串 ID
    )
    db.add(comment)
    article.comment_count += 1
    db.commit()
    db.refresh(comment)
    
    return ResponseModel(
        data={
            "id": str(comment.id),
            "content": comment.content,
            "author": {
                "id": str(current_user.id),
                "name": current_user.name,
                "avatar": current_user.avatar
            },
            "createdAt": comment.created_at.isoformat() + "Z"
        },
        message="评论成功"
    )


@router.get("/articles/{article_id}/comments", response_model=PaginatedResponse[dict])
async def get_comments(
    article_id: str,
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1),
    sort: Optional[str] = Query("latest"),
    db: Session = Depends(get_db)
):
    """获取评论列表"""
    query = db.query(Comment).filter(
        Comment.content_id == article_id,
        Comment.is_deleted == False,
        Comment.parent_id.is_(None)  # 只获取顶级评论
    )
    
    if sort == "hot":
        query = query.order_by(Comment.like_count.desc(), Comment.created_at.desc())
    else:
        query = query.order_by(Comment.created_at.desc())
    
    total = query.count()
    items = query.offset((page - 1) * limit).limit(limit).all()
    
    comment_list = []
    for comment in items:
        author = db.query(User).filter(User.id == comment.user_id).first()
        
        # 获取回复
        replies = db.query(Comment).filter(
            Comment.parent_id == comment.id,
            Comment.is_deleted == False
        ).order_by(Comment.created_at.asc()).all()
        
        reply_list = []
        for reply in replies:
            reply_author = db.query(User).filter(User.id == reply.user_id).first()
            reply_list.append({
                "id": str(reply.id),
                "content": reply.content,
                "author": {
                    "id": str(reply_author.id) if reply_author else "",
                    "name": reply_author.name if reply_author else "",
                    "avatar": reply_author.avatar
                },
                "createdAt": reply.created_at.isoformat() + "Z"
            })
        
        comment_list.append({
            "id": str(comment.id),
            "content": comment.content,
            "author": {
                "id": str(author.id) if author else "",
                "name": author.name if author else "",
                "avatar": author.avatar
            },
            "likes": comment.like_count,
            "replies": reply_list,
            "createdAt": comment.created_at.isoformat() + "Z"
        })
    
    return PaginatedResponse(
        data={
            "items": comment_list,
            "pagination": PaginationInfo(
                page=page,
                limit=limit,
                total=total,
                totalPages=(total + limit - 1) // limit
            )
        }
    )

