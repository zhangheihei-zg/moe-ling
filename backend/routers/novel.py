# backend/routers/novel.py
"""
小说创作 API 路由
- 创建小说
- 获取小说详情
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List
from backend.database import get_db
from backend.models import Novel

router = APIRouter(prefix="/api", tags=["novels"])


class NovelCreate(BaseModel):
    title: str
    content: str

    class Config:
        json_schema_extra = {
            "example": {
                "title": "星辰大海",
                "content": "在遥远的未来，人类踏上了星际殖民的征程……"
            }
        }


class NovelResponse(BaseModel):
    id: int
    title: str
    content: str

    class Config:
        from_attributes = True  # 替代旧版 orm_mode=True


@router.post(
    "/novels",
    response_model=NovelResponse,
    status_code=status.HTTP_201_CREATED,
    summary="创建新小说"
)
def create_novel(novel: NovelCreate, db: Session = Depends(get_db)):
    """
    创建一篇新小说，并保存到数据库。
    """
    db_novel = Novel(title=novel.title, content=novel.content)
    db.add(db_novel)
    db.commit()
    db.refresh(db_novel)  # 获取自增 ID
    return db_novel


@router.get(
    "/novels/{novel_id}",
    response_model=NovelResponse,
    summary="获取小说详情"
)
def read_novel(novel_id: int, db: Session = Depends(get_db)):
    """
    根据 ID 查询小说。
    """
    novel = db.query(Novel).filter(Novel.id == novel_id).first()
    if not novel:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="小说未找到"
        )
    return novel