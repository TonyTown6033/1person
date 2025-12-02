"""
管理后台权限依赖模块
"""
from fastapi import Depends, HTTPException, status
from app.core.dependencies import require_current_user
from app.models.user import User


async def require_admin_user(
    current_user: User = Depends(require_current_user)
) -> User:
    """要求管理员权限"""
    if current_user.role not in ["admin", "super_admin"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="需要管理员权限"
        )
    return current_user


async def require_super_admin_user(
    current_user: User = Depends(require_current_user)
) -> User:
    """要求超级管理员权限"""
    if current_user.role != "super_admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="需要超级管理员权限"
        )
    return current_user
