from typing import Optional, Generic, TypeVar, List
from pydantic import BaseModel
from datetime import datetime

T = TypeVar('T')


class ResponseModel(BaseModel, Generic[T]):
    """通用响应模型"""
    success: bool = True
    data: Optional[T] = None
    message: Optional[str] = None
    timestamp: datetime = datetime.utcnow()


class ErrorDetail(BaseModel):
    """错误详情"""
    code: str
    message: str
    details: Optional[dict] = None


class ErrorResponse(BaseModel):
    """错误响应模型"""
    success: bool = False
    error: ErrorDetail
    timestamp: datetime = datetime.utcnow()


class PaginationInfo(BaseModel):
    """分页信息"""
    page: int
    limit: int
    total: int
    totalPages: int


class PaginatedResponse(BaseModel, Generic[T]):
    """分页响应模型"""
    success: bool = True
    data: dict
    timestamp: datetime = datetime.utcnow()
    
    class Config:
        json_schema_extra = {
            "example": {
                "success": True,
                "data": {
                    "items": [],
                    "pagination": {
                        "page": 1,
                        "limit": 20,
                        "total": 100,
                        "totalPages": 5
                    }
                },
                "timestamp": "2025-11-11T12:00:00Z"
            }
        }

