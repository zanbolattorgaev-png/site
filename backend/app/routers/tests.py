from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List
from ..db import get_db
from ..models import Test, Result
from ..schemas import TestResponse, ResultSubmit, ResultResponse

router = APIRouter()

@router.get("/{lecture_id}", response_model=List[TestResponse])
async def get_tests(lecture_id: int, db: AsyncSession = Depends(get_db)):
    """Получить все тесты для конкретной лекции"""
    result = await db.execute(select(Test).where(Test.lecture_id == lecture_id))
    tests = result.scalars().all()
    
    if not tests:
        raise HTTPException(status_code=404, detail="Tests not found for this lecture")
    
    return tests

@router.post("/{lecture_id}/submit", response_model=ResultResponse)
async def submit_test(
    lecture_id: int,
    submission: ResultSubmit,
    db: AsyncSession = Depends(get_db)
):
    """Отправить ответы на тест и получить результат"""
    
    # Получаем все тесты для лекции
    result = await db.execute(select(Test).where(Test.lecture_id == lecture_id))
    tests = result.scalars().all()
    
    if not tests:
        raise HTTPException(status_code=404, detail="Tests not found for this lecture")
    
    # Подсчитываем правильные ответы
    score = 0
    total = len(tests)
    
    for test in tests:
        test_id_str = str(test.id)
        if test_id_str in submission.answers:
            user_answer = submission.answers[test_id_str]
            if user_answer == test.correct_answer:
                score += 1
    
    # Сохраняем результат в БД
    new_result = Result(
        lecture_id=lecture_id,
        user_name=submission.name,
        score=score,
        total=total
    )
    
    db.add(new_result)
    await db.commit()
    await db.refresh(new_result)
    
    return new_result

