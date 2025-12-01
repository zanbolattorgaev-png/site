# JavaScript Course Frontend

Frontend приложение для онлайн-курса по JavaScript на React + Vite + TypeScript.

## Установка

```bash
npm install
```

## Запуск в режиме разработки

```bash
npm run dev
```

Приложение будет доступно по адресу `http://localhost:3000`

## Переменные окружения

Создайте файл `.env`:

```
VITE_BACKEND_URL=http://localhost:8000
```

Для продакшена на Vercel укажите URL вашего бэкенда.

## Сборка для продакшена

```bash
npm run build
```

Собранные файлы будут в папке `dist/`

## Деплой на Vercel

1. Подключите репозиторий к Vercel
2. Установите переменную окружения `VITE_BACKEND_URL` (URL вашего бэкенда)
3. Build команд: `npm run build`
4. Output директория: `dist`

## Структура проекта

```
src/
├── api/          # API клиент
├── components/   # Переиспользуемые компоненты
├── pages/        # Страницы приложения
├── App.tsx       # Главный компонент с роутингом
└── main.tsx      # Точка входа
```

