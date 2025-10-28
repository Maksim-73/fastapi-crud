from fastapi import APIRouter, HTTPException, Query

from .dictionary import users
from .schemas import *

router = APIRouter(
    prefix="/users",
    tags=["Пользователи"]
)

@router.get("/",
    summary = "Список всех пользователей",
    description = "Возвращает всех пользователей"
    )
def get_users(
    skip: int = Query(0, ge=0, description="Сколько пользователей пропустить"),
    limit: int = Query(10, ge=1, le=100, description="Сколько пользователей показать (максимум 100)"),
) -> list[UserBase]:
    result = users[skip:skip + limit]
    return result

@router.get("{user_id}", response_model=UserBase,
    summary="1 пользователь",
    description="Возвращает 1 пользователя с выбранным id"
    )
def get_user(user_id: int) -> UserBase:
    for user in users:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="Пользователь не найден")

@router.post("/", response_model=dict,
     summary="Создать пользователя",
     description="Добавляет 1 пользователя с введенными данными"
     )
def create_user(user: UserBase):
    users.append(
        {
        "id": len(users) + 1,
        "username": user.username,
        "email": user.email,
        "password": user.password,
        "phone_number": user.phone_number
         }
    )
    return {"ok": True}

@router.put("/{user_id}", response_model=dict,
    summary = "Обновить данные",
    description = "Обновляет данные пользователя"
    )
def update_user(user_id: int, user: UserUpdate):
    for us in users:
        if us["id"] == user_id:
            us.update(user)
            return {"ok": True}
    raise HTTPException(status_code=404, detail="Пользователь не найден")

@router.delete("/{user_id}", response_model=dict,
       summary="Удалить пользователя",
       description="Удаляет пользователя с выбранным id"
       )
def delete_user(user_id: int):
    for us in users:
        if us["id"] == user_id:
            users.remove(us)
            return {"ok": True}
    raise HTTPException(status_code=404, detail="Пользователь не найден")

