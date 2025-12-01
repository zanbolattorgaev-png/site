from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List
from ..db import get_db
from ..models import Result
from ..schemas import ResultResponse

router = APIRouter()

@router.get("/{lecture_id}", response_model=List[ResultResponse])
async def get_results(lecture_id: int, db: AsyncSession = Depends(get_db)):
    """Получить все результаты для конкретной лекции"""
    result = await db.execute(
        select(Result)
        .where(Result.lecture_id == lecture_id)
        .order_by(Result.date.desc())
    )
    results = result.scalars().all()
    return results

