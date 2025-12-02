from pydantic_settings import BaseSettings
from typing import Optional
import os
from dotenv import load_dotenv


class Settings(BaseSettings):
    DATABASE_URL: str = "mysql+pymysql://root:root123456@localhost:3306/super_club"
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


# 加载 .env ，然后由 Settings 自动读取环境变量/默认值
load_dotenv()
settings = Settings()

# 强制使用MySQL配置
settings.DATABASE_URL = "mysql+pymysql://root:root123456@localhost:3306/super_club"

