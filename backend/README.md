# JavaScript Course Backend

Backend API для онлайн-курса по JavaScript на FastAPI.

## ⚠️ ВАЖНО: Первый запуск

Перед первым запуском обязательно инициализируйте базу данных!

### Способ 1: Автоматическое пересоздание (рекомендуется)

```bash
python reset_db.py
```

Этот скрипт:
- Удаляет старую БД (если есть)
- Создает новые таблицы
- Добавляет 10 лекций с видео и 96 тестов

### Способ 2: Просто добавление данных

```bash
python -m app.init_db
```

Этот скрипт добавляет данные только если БД пустая.

## Установка

```bash
pip install -r requirements.txt
```

## Запуск

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Переменные окружения

- `DATABASE_URL` - URL базы данных (по умолчанию: `sqlite+aiosqlite:///./db.sqlite3`)
  
  Примеры:
  - SQLite: `sqlite+aiosqlite:///./db.sqlite3`
  - PostgreSQL: `postgresql+asyncpg://user:pass@host/db`

## API Endpoints

- `GET /api/lectures` - Список всех лекций
- `GET /api/lectures/{id}` - Конкретная лекция
- `GET /api/tests/{lecture_id}` - Тесты для лекции
- `POST /api/tests/{lecture_id}/submit` - Отправить ответы на тест
- `GET /api/results/{lecture_id}` - Результаты тестов для лекции

## Структура базы данных

### lectures
- `id` - ID лекции
- `title` - Название
- `description` - Описание
- `content` - Содержимое (Markdown)
- `video_url` - URL видео с YouTube

### tests
- `id` - ID теста
- `lecture_id` - ID лекции
- `question` - Вопрос
- `options` - Варианты ответов (JSON)
- `correct_answer` - Индекс правильного ответа

### results
- `id` - ID результата
- `lecture_id` - ID лекции
- `user_name` - Имя пользователя
- `score` - Количество правильных ответов
- `total` - Всего вопросов
- `date` - Дата прохождения

## Деплой

Для деплоя на Render/Railway:

1. Установите переменную окружения `DATABASE_URL`
2. Запустите: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
3. После деплоя запустите `init_db.py` для добавления данных

## Решение проблем

### Лекции не появляются

1. Убедитесь, что запущен `python reset_db.py` или `python -m app.init_db`
2. Проверьте, что файл `db.sqlite3` существует
3. Проверьте логи backend на ошибки

### Ошибка "База данных уже содержит данные"

Если нужно пересоздать БД:
```bash
python reset_db.py
```

Или удалите `db.sqlite3` вручную и запустите `python -m app.init_db`
