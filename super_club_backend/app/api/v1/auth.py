from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import timedelta
from app.core.database import get_db
from app.core.security import verify_password, get_password_hash, create_access_token, create_refresh_token
from app.core.config import settings
from app.models.user import User
from app.schemas.auth import RegisterRequest, LoginRequest, RefreshTokenRequest, AuthResponse, TokenResponse, UserInfo
from app.schemas.common import ResponseModel
from app.core.security import decode_token

router = APIRouter()


@router.post("/register", response_model=ResponseModel[AuthResponse])
async def register(request: RegisterRequest, db: Session = Depends(get_db)):
    """用户注册"""
    # 检查邮箱是否已存在
    existing_user = db.query(User).filter(User.email == request.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="邮箱已被注册"
        )
    
    # 创建新用户
    user = User(
        email=request.email,
        password_hash=get_password_hash(request.password),
        name=request.name,
        phone=request.phone,
        avatar=f"https://api.dicebear.com/7.x/avataaars/svg?seed={request.email}"
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    
    # 生成令牌
    access_token = create_access_token(data={"sub": str(user.id)})
    refresh_token = create_refresh_token(data={"sub": str(user.id)})
    
    return ResponseModel(
        data=AuthResponse(
            user=UserInfo(
                id=str(user.id),
                email=user.email,
                name=user.name,
                avatar=user.avatar,
                membershipLevel=user.membership_level
            ),
            tokens=TokenResponse(
                accessToken=access_token,
                refreshToken=refresh_token,
                expiresIn=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60
            )
        )
    )


@router.post("/login", response_model=ResponseModel[AuthResponse])
async def login(request: LoginRequest, db: Session = Depends(get_db)):
    """用户登录"""
    user = db.query(User).filter(User.email == request.email).first()
    if not user or not verify_password(request.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="邮箱或密码错误"
        )
    
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="用户已被禁用"
        )
    
    # 生成令牌
    access_token = create_access_token(data={"sub": str(user.id)})
    refresh_token = create_refresh_token(data={"sub": str(user.id)})
    
    return ResponseModel(
        data=AuthResponse(
            user=UserInfo(
                id=str(user.id),
                email=user.email,
                name=user.name,
                avatar=user.avatar,
                membershipLevel=user.membership_level
            ),
            tokens=TokenResponse(
                accessToken=access_token,
                refreshToken=refresh_token,
                expiresIn=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60
            )
        )
    )


@router.post("/refresh", response_model=ResponseModel[TokenResponse])
async def refresh_token(request: RefreshTokenRequest):
    """刷新访问令牌"""
    payload = decode_token(request.refreshToken)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="刷新令牌无效或已过期"
        )
    
    user_id = payload.get("sub")
    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="刷新令牌无效"
        )
    
    # 生成新的访问令牌
    access_token = create_access_token(data={"sub": user_id})
    
    return ResponseModel(
        data=TokenResponse(
            accessToken=access_token,
            expiresIn=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60
        )
    )


@router.post("/logout", response_model=ResponseModel[dict])
async def logout():
    """退出登录"""
    # 在实际应用中，可以将令牌加入黑名单
    return ResponseModel(message="退出成功")

