"""
日志配置模块
"""
import logging
import sys
from pathlib import Path
from logging.handlers import RotatingFileHandler
from datetime import datetime
import json

# 创建 logs 目录
LOG_DIR = Path(__file__).parent.parent.parent / "logs"
LOG_DIR.mkdir(exist_ok=True)

# 日志格式
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# 详细日志格式（包含文件位置）
DETAILED_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(funcName)s() - %(message)s"


class JSONFormatter(logging.Formatter):
    """JSON 格式的日志格式化器"""
    
    def format(self, record):
        log_data = {
            "timestamp": datetime.fromtimestamp(record.created).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno,
        }
        
        # 添加异常信息
        if record.exc_info:
            log_data["exception"] = self.formatException(record.exc_info)
        
        # 添加额外字段
        if hasattr(record, "user_id"):
            log_data["user_id"] = record.user_id
        if hasattr(record, "request_id"):
            log_data["request_id"] = record.request_id
        if hasattr(record, "ip_address"):
            log_data["ip_address"] = record.ip_address
        
        return json.dumps(log_data, ensure_ascii=False)


def setup_logger(name: str = "super_club", level: str = "INFO", use_json: bool = False) -> logging.Logger:
    """
    设置日志记录器
    
    Args:
        name: 日志记录器名称
        level: 日志级别 (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        use_json: 是否使用 JSON 格式
    
    Returns:
        配置好的日志记录器
    """
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, level.upper()))
    
    # 避免重复添加处理器
    if logger.handlers:
        return logger
    
    # 控制台处理器
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    if use_json:
        console_handler.setFormatter(JSONFormatter())
    else:
        console_handler.setFormatter(logging.Formatter(LOG_FORMAT, DATE_FORMAT))
    logger.addHandler(console_handler)
    
    # 文件处理器 - 所有日志
    all_log_file = LOG_DIR / "app.log"
    file_handler = RotatingFileHandler(
        all_log_file,
        maxBytes=10 * 1024 * 1024,  # 10MB
        backupCount=5,
        encoding="utf-8"
    )
    file_handler.setLevel(logging.DEBUG)
    if use_json:
        file_handler.setFormatter(JSONFormatter())
    else:
        file_handler.setFormatter(logging.Formatter(DETAILED_FORMAT, DATE_FORMAT))
    logger.addHandler(file_handler)
    
    # 错误日志文件 - 只记录 ERROR 及以上级别
    error_log_file = LOG_DIR / "error.log"
    error_handler = RotatingFileHandler(
        error_log_file,
        maxBytes=10 * 1024 * 1024,  # 10MB
        backupCount=10,
        encoding="utf-8"
    )
    error_handler.setLevel(logging.ERROR)
    if use_json:
        error_handler.setFormatter(JSONFormatter())
    else:
        error_handler.setFormatter(logging.Formatter(DETAILED_FORMAT, DATE_FORMAT))
    logger.addHandler(error_handler)
    
    # API 请求日志文件
    api_log_file = LOG_DIR / "api.log"
    api_handler = RotatingFileHandler(
        api_log_file,
        maxBytes=10 * 1024 * 1024,  # 10MB
        backupCount=5,
        encoding="utf-8"
    )
    api_handler.setLevel(logging.INFO)
    api_handler.addFilter(lambda record: hasattr(record, "is_api_request") and record.is_api_request)
    if use_json:
        api_handler.setFormatter(JSONFormatter())
    else:
        api_handler.setFormatter(logging.Formatter(LOG_FORMAT, DATE_FORMAT))
    logger.addHandler(api_handler)
    
    return logger


# 创建默认日志记录器
logger = setup_logger("super_club")

# 创建各个模块的日志记录器
api_logger = logging.getLogger("super_club.api")
db_logger = logging.getLogger("super_club.database")
auth_logger = logging.getLogger("super_club.auth")


def log_api_request(method: str, path: str, status_code: int, duration: float, 
                   user_id: str = None, ip: str = None):
    """记录 API 请求"""
    extra = {
        "is_api_request": True,
        "method": method,
        "path": path,
        "status_code": status_code,
        "duration_ms": round(duration * 1000, 2),
    }
    if user_id:
        extra["user_id"] = user_id
    if ip:
        extra["ip_address"] = ip
    
    level = logging.INFO if status_code < 400 else logging.WARNING
    api_logger.log(level, f"{method} {path} - {status_code} ({duration*1000:.2f}ms)", extra=extra)


def log_error(error: Exception, context: dict = None):
    """记录错误信息"""
    error_data = {
        "error_type": type(error).__name__,
        "error_message": str(error),
    }
    if context:
        error_data.update(context)
    
    logger.error(f"Error occurred: {error_data}", exc_info=True, extra=error_data)







