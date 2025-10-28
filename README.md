# FastAPI CRUD — Пользователи

API для управления пользователями с валидацией и документацией.

## Эндпоинты
- `GET /users/` — список (с `?skip`, `?limit`, `?username`)
- `GET /users/{id}` — один пользователь
- `POST /users/` — создать
- `PUT /users/{id}` — обновить
- `DELETE /users/{id}` — удалить

## Запуск

### Локально

`pip install -r requirements.txt` \
`uvicorn app.main:app --reload`

### Через Docker

`bashdocker build -t fastapi-crud .` \
`docker run -p 8000:8000 fastapi-crud`