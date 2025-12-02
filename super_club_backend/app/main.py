from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.api.v1 import auth, users, talents, projects, events, links, content, admin
from app.core.config import settings
from app.core.database import engine
from app.core.logging import logger, setup_logger
from app.core.middleware import LoggingMiddleware, ErrorHandlingMiddleware
from app.models import Base

# 初始化日志系统
setup_logger("super_club", level="INFO", use_json=False)
logger.info("=" * 60)
logger.info("Super Club API 启动中...")
logger.info("=" * 60)

# 创建数据库表
try:
    Base.metadata.create_all(bind=engine)
    logger.info("数据库表创建/检查完成")
except Exception as e:
    logger.warning(f"数据库初始化失败，将使用演示模式: {e}")
    # 在演示模式下继续运行

# 使用 lifespan 替代 on_event（FastAPI 0.109+ 兼容）
@asynccontextmanager
async def lifespan(app: FastAPI):
    # 启动时
    logger.info("=" * 60)
    logger.info("Super Club API 启动完成")
    logger.info(f"API 文档: http://localhost:8001/docs")
    logger.info("=" * 60)
    yield
    # 关闭时
    logger.info("Super Club API 正在关闭...")

app = FastAPI(
    title="Super Club API",
    description="Super Club 后端 API 服务",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

# 添加日志中间件（最先添加，最后执行）
app.add_middleware(ErrorHandlingMiddleware)
app.add_middleware(LoggingMiddleware)

# CORS 配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 生产环境应设置具体域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logger.info("中间件配置完成")

# 注册路由
app.include_router(auth.router, prefix="/api/auth", tags=["认证"])
app.include_router(users.router, prefix="/api/user", tags=["用户"])
app.include_router(talents.router, prefix="/api/talents", tags=["人才库"])
app.include_router(projects.router, prefix="/api/projects", tags=["项目资源库"])
app.include_router(events.router, prefix="/api/events", tags=["活动管理"])
app.include_router(links.router, prefix="/api/links", tags=["社区网络"])
app.include_router(content.router, prefix="/api/content", tags=["内容库"])
app.include_router(admin.router, prefix="/api/admin", tags=["管理后台"])


@app.get("/")
async def root():
    logger.info("根路径访问")
    return {"message": "Super Club API", "version": "1.0.0"}


@app.get("/health")
async def health_check():
    logger.debug("健康检查")
    return {"status": "healthy"}

