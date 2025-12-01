from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List
from ..db import get_db
from ..models import Lecture
from ..schemas import LectureResponse

router = APIRouter()

@router.get("/", response_model=List[LectureResponse])
async def get_lectures(db: AsyncSession = Depends(get_db)):
    """Получить список всех лекций"""
    result = await db.execute(select(Lecture))
    lectures = result.scalars().all()
    return lectures

@router.get("/{lecture_id}", response_model=LectureResponse)
async def get_lecture(lecture_id: int, db: AsyncSession = Depends(get_db)):
    """Получить конкретную лекцию по ID"""
    result = await db.execute(select(Lecture).where(Lecture.id == lecture_id))
    lecture = result.scalar_one_or_none()
    
    if not lecture:
        raise HTTPException(status_code=404, detail="Lecture not found")
    
    return lecture

