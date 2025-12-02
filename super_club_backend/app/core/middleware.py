"""
中间件模块 - 包含请求日志等中间件
"""
import time
import logging
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import Message

logger = logging.getLogger("super_club.api")


class LoggingMiddleware(BaseHTTPMiddleware):
    """请求日志中间件"""
    
    async def dispatch(self, request: Request, call_next):
        # 记录请求开始时间
        start_time = time.time()
        
        # 获取客户端 IP
        client_ip = request.client.host if request.client else "unknown"
        
        # 获取用户信息（如果有）
        user_id = None
        if hasattr(request.state, "user"):
            user_id = str(request.state.user.id) if request.state.user else None
        
        # 记录请求信息
        logger.info(
            f"Request: {request.method} {request.url.path}",
            extra={
                "method": request.method,
                "path": request.url.path,
                "query_params": str(request.query_params),
                "client_ip": client_ip,
                "user_id": user_id,
            }
        )
        
        # 处理请求
        try:
            response = await call_next(request)
            
            # 计算处理时间
            duration = time.time() - start_time
            
            # 记录响应信息
            status_code = response.status_code
            log_level = logging.INFO if status_code < 400 else logging.WARNING
            
            logger.log(
                log_level,
                f"Response: {request.method} {request.url.path} - {status_code} ({duration*1000:.2f}ms)",
                extra={
                    "method": request.method,
                    "path": request.url.path,
                    "status_code": status_code,
                    "duration_ms": round(duration * 1000, 2),
                    "client_ip": client_ip,
                    "user_id": user_id,
                }
            )
            
            return response
            
        except Exception as e:
            # 记录异常
            duration = time.time() - start_time
            logger.error(
                f"Exception in {request.method} {request.url.path}: {str(e)}",
                exc_info=True,
                extra={
                    "method": request.method,
                    "path": request.url.path,
                    "duration_ms": round(duration * 1000, 2),
                    "client_ip": client_ip,
                    "user_id": user_id,
                }
            )
            raise


class ErrorHandlingMiddleware(BaseHTTPMiddleware):
    """错误处理中间件"""
    
    async def dispatch(self, request: Request, call_next):
        try:
            response = await call_next(request)
            return response
        except Exception as e:
            logger.error(
                f"Unhandled exception: {type(e).__name__}: {str(e)}",
                exc_info=True,
                extra={
                    "method": request.method,
                    "path": request.url.path,
                }
            )
            # 重新抛出异常，让 FastAPI 的错误处理器处理
            raise







