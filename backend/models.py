# backend/models.py
"""
数据模型定义
"""

from sqlalchemy import Column, Integer, String, Text, DateTime, func
from backend.database import Base

class Novel(Base):
    """
    小说主表
    """
    __tablename__ = "novels"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False, comment="小说标题")
    content = Column(Text, nullable=False, comment="小说正文")
    # 暂用 TEXT 存储 JSON 向量（如 "[0.1, -0.5, ...]"），后续升级为 VECTOR
    embedding = Column(Text, nullable=True, comment="标题/摘要的向量表示")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class KnowledgeChunk(Base):
    """
    知识切片表（用于语义检索）
    """
    __tablename__ = "knowledge_chunks"

    id = Column(Integer, primary_key=True, index=True)
    chunk_text = Column(Text, nullable=False, comment="文本片段")
    novel_id = Column(Integer, nullable=False, comment="关联的小说ID")
    embedding = Column(Text, nullable=True, comment="文本片段的向量")
    created_at = Column(DateTime(timezone=True), server_default=func.now())