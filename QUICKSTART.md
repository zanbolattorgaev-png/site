# Быстрый старт

## Важно! Сначала инициализируйте базу данных

### Шаг 1: Запустите backend и инициализируйте БД

```bash
cd backend
pip install -r requirements.txt

# Пересоздать БД с лекциями (рекомендуется при первом запуске)
python reset_db.py

# ИЛИ если БД уже существует, просто добавить данные
python -m app.init_db
```

### Шаг 2: Запустите backend сервер

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Backend будет доступен на: `http://localhost:8000`

### Шаг 3: Запустите frontend

В новом терминале:

```bash
cd frontend
npm install
npm run dev
```

Frontend будет доступен на: `http://localhost:3000`

## Что будет добавлено

- ✅ 10 лекций по JavaScript
- ✅ 10 видеоуроков с YouTube
- ✅ 96 тестов (8-10 вопросов к каждой лекции)

## Решение проблем

### Лекции не отображаются

1. Убедитесь, что backend запущен
2. Проверьте, что БД инициализирована: `python reset_db.py`
3. Проверьте консоль браузера на ошибки

### Ошибка подключения к API

1. Проверьте, что backend работает: откройте `http://localhost:8000/api/health`
2. Проверьте переменную `VITE_BACKEND_URL` в `.env` файле frontend

### База данных не обновляется

Удалите файл `backend/db.sqlite3` и запустите `python reset_db.py` снова.

