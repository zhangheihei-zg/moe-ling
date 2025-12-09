# backend/database.py
"""
数据库连接模块
使用 SQLAlchemy 连接 PostgreSQL + pgvector
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# 从环境变量读取 DATABASE_URL，本地开发默认值
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://moe_user:moe_secure_password_123@localhost:5432/moe_ling"
)

# 创建引擎（禁用 SQLAlchemy 2.0+ 的新风格，保持兼容）
engine = create_engine(DATABASE_URL, future=True, echo=False)

# 会话工厂
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 基类
Base = declarative_base()

def get_db():
    """
    FastAPI 依赖项：提供数据库会话
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()