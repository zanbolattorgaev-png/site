from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./db.sqlite3")

# Для SQLite нужно использовать aiosqlite драйвер
if DATABASE_URL.startswith("sqlite"):
    # SQLite не поддерживает асинхронность на уровне файлов, используем aiosqlite
    if not DATABASE_URL.startswith("sqlite+aiosqlite"):
        DATABASE_URL = DATABASE_URL.replace("sqlite://", "sqlite+aiosqlite://")
elif DATABASE_URL.startswith("postgresql://"):
    # Для PostgreSQL используем async драйвер
    DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://")

engine = create_async_engine(DATABASE_URL, echo=True, future=True)
async_session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()

async def get_db():
    """Dependency для получения сессии БД"""
    async with async_session_maker() as session:
        yield session

