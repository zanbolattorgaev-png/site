# JavaScript Course - Онлайн-курс по JavaScript

Веб-платформа для изучения JavaScript с лекциями, онлайн-компилятором и тестами.

## Структура проекта

```
.
├── backend/          # FastAPI бэкенд
├── frontend/         # React + Vite фронтенд
└── README.md
```

## Технологии

### Backend
- Python FastAPI
- SQLAlchemy 2.0 (ORM)
- SQLite (по умолчанию) / PostgreSQL (Neon)
- Uvicorn

### Frontend
- React 18
- TypeScript
- Vite
- TailwindCSS
- Monaco Editor
- React Router

## Быстрый старт

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Backend будет доступен по адресу `http://localhost:8000`

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend будет доступен по адресу `http://localhost:3000`

## Настройка базы данных

По умолчанию используется SQLite. Файл базы данных создается автоматически при первом запуске.

Для использования PostgreSQL установите переменную окружения:

```bash
export DATABASE_URL="postgresql+asyncpg://user:password@host:5432/dbname"
```

## Добавление данных

Для добавления лекций и тестов в базу данных можно использовать SQL или создать скрипт инициализации.

Пример SQL для SQLite:

```sql
INSERT INTO lectures (title, description, content) VALUES 
('Введение в JavaScript', 'Основы языка JavaScript', '# Введение\n\nJavaScript - это...');

INSERT INTO tests (lecture_id, question, options, correct_answer) VALUES
(1, 'Что такое JavaScript?', '["Простой язык", "Язык программирования", "Стиль", "База данных"]', 1);
```

## Деплой

### Frontend (Vercel)

1. Подключите репозиторий к Vercel
2. Установите переменную окружения `VITE_BACKEND_URL`
3. Build команд: `npm run build`
4. Output директория: `dist`

### Backend (Render/Railway)

1. Установите переменную окружения `DATABASE_URL`
2. Команда запуска: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
3. Настройте CORS в `backend/app/main.py` (укажите URL вашего фронтенда)

## API Endpoints

- `GET /api/lectures` - Список всех лекций
- `GET /api/lectures/{id}` - Конкретная лекция
- `GET /api/tests/{lecture_id}` - Тесты для лекции
- `POST /api/tests/{lecture_id}/submit` - Отправить ответы на тест
- `GET /api/results/{lecture_id}` - Результаты тестов

## Особенности

- ✅ Онлайн-компилятор JavaScript работает полностью в браузере
- ✅ Тесты с множественным выбором
- ✅ Сохранение результатов в базе данных
- ✅ Адаптивный дизайн
- ✅ Markdown для содержимого лекций
- ✅ Поддержка SQLite и PostgreSQL

