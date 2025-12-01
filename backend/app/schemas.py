from pydantic import BaseModel
from typing import List, Dict, Optional
from datetime import datetime

# Lecture schemas
class LectureBase(BaseModel):
    title: str
    description: Optional[str] = None
    content: str
    video_url: Optional[str] = None

class LectureCreate(LectureBase):
    pass

class LectureResponse(LectureBase):
    id: int
    
    class Config:
        from_attributes = True

# Test schemas
class TestBase(BaseModel):
    question: str
    options: List[str]
    correct_answer: int

class TestCreate(TestBase):
    lecture_id: int

class TestResponse(TestBase):
    id: int
    lecture_id: int
    
    class Config:
        from_attributes = True

# Result schemas
class ResultSubmit(BaseModel):
    name: str
    answers: Dict[str, int]  # {"1": 2, "2": 1, ...} где ключ - test_id, значение - выбранный ответ

class ResultResponse(BaseModel):
    id: int
    lecture_id: int
    user_name: str
    score: int
    total: int
    date: datetime
    
    class Config:
        from_attributes = True

