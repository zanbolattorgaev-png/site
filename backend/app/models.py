from sqlalchemy import Column, Integer, String, Text, ForeignKey, JSON, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from .db import Base

class Lecture(Base):
    __tablename__ = "lectures"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    content = Column(Text, nullable=False)
    video_url = Column(String(500), nullable=True)  # YouTube URL или video ID
    
    # Relationships
    tests = relationship("Test", back_populates="lecture", cascade="all, delete-orphan")
    results = relationship("Result", back_populates="lecture", cascade="all, delete-orphan")

class Test(Base):
    __tablename__ = "tests"
    
    id = Column(Integer, primary_key=True, index=True)
    lecture_id = Column(Integer, ForeignKey("lectures.id", ondelete="CASCADE"), nullable=False)
    question = Column(Text, nullable=False)
    options = Column(JSON, nullable=False)  # Массив вариантов ответа
    correct_answer = Column(Integer, nullable=False)  # Индекс правильного ответа (0-based)
    
    # Relationships
    lecture = relationship("Lecture", back_populates="tests")

class Result(Base):
    __tablename__ = "results"
    
    id = Column(Integer, primary_key=True, index=True)
    lecture_id = Column(Integer, ForeignKey("lectures.id", ondelete="CASCADE"), nullable=False)
    user_name = Column(String(255), nullable=False)
    score = Column(Integer, nullable=False)
    total = Column(Integer, nullable=False)
    date = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    # Relationships
    lecture = relationship("Lecture", back_populates="results")

