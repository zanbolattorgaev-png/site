# Инструкция по запуску проекта

## Backend

1. Перейдите в папку `backend`:
```bash
cd backend
```

2. Создайте виртуальное окружение (рекомендуется):
```bash
python -m venv venv
```

3. Активируйте виртуальное окружение:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`

4. Установите зависимости:
```bash
pip install -r requirements.txt
```

5. (Опционально) Инициализируйте базу данных с примерами данных:
```bash
python -m app.init_db
```

6. Запустите сервер:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Backend будет доступен по адресу: `http://localhost:8000`

API документация: `http://localhost:8000/docs`

## Frontend

1. Перейдите в папку `frontend`:
```bash
cd frontend
```

2. Установите зависимости:
```bash
npm install
```

3. Создайте файл `.env` (если нужно изменить URL бэкенда):
```
VITE_BACKEND_URL=http://localhost:8000
```

4. Запустите сервер разработки:
```bash
npm run dev
```

Frontend будет доступен по адресу: `http://localhost:3000`

## Добавление данных в базу

После первого запуска база данных создастся автоматически. Для добавления примеров лекций и тестов запустите:

```bash
cd backend
python -m app.init_db
```

Это добавит 2 примера лекций и 5 тестов в базу данных.

## Структура базы данных

### Таблица `lectures`
- `id` - ID лекции
- `title` - Название лекции
- `description` - Краткое описание
- `content` - Содержимое лекции (Markdown)

### Таблица `tests`
- `id` - ID теста
- `lecture_id` - ID лекции
- `question` - Вопрос
- `options` - JSON массив вариантов ответа
- `correct_answer` - Индекс правильного ответа (0-based)

### Таблица `results`
- `id` - ID результата
- `lecture_id` - ID лекции
- `user_name` - Имя пользователя
- `score` - Количество правильных ответов
- `total` - Всего вопросов
- `date` - Дата прохождения

## Проблемы и решения

### Backend не запускается

- Убедитесь, что установлены все зависимости: `pip install -r requirements.txt`
- Проверьте, что порт 8000 свободен
- Для Windows может потребоваться установка `Microsoft Visual C++ 14.0` для некоторых пакетов

### Frontend не подключается к backend

- Проверьте, что backend запущен на порту 8000
- Убедитесь, что переменная окружения `VITE_BACKEND_URL` правильная
- В режиме разработки Vite использует прокси из `vite.config.ts`

### Ошибки с базой данных

- SQLite файл создается автоматически при первом запуске
- Убедитесь, что у приложения есть права на запись в папку `backend`
- Для PostgreSQL проверьте правильность `DATABASE_URL`

