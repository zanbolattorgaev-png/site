from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import lectures, tests, results
from .db import engine, Base

app = FastAPI(title="JavaScript Course API", version="1.0.0")

# CORS настройки для работы с Vercel фронтендом
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # В продакшене указать конкретный URL Vercel
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключение роутеров
app.include_router(lectures.router, prefix="/api/lectures", tags=["lectures"])
app.include_router(tests.router, prefix="/api/tests", tags=["tests"])
app.include_router(results.router, prefix="/api/results", tags=["results"])

@app.get("/")
async def root():
    return {"message": "JavaScript Course API"}

@app.get("/api/health")
async def health():
    return {"status": "ok"}

@app.on_event("startup")
async def init_db():
    """Создание таблиц при запуске приложения"""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

