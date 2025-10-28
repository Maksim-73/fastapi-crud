from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional
import re


class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, description="Имя пользователя")
    password: str = Field(..., min_length=6, description="Пароль (минимум 6 символов)")
    email: EmailStr = Field(..., description="Email пользователя")
    phone_number: str = Field(..., description="Номер телефона")

    @validator("phone_number")
    def validate_phone(cls, v):
        pattern = r"^7\d{10}$"
        if not re.match(pattern, v):
            raise ValueError("Номер должен быть в формате 7XXXXXXXXXX")
        return v


class UserUpdate(UserBase):
    password: Optional[str] = Field(None, min_length=6)
    username: Optional[str] = Field(None, min_length=3, max_length=50)
    email: Optional[EmailStr] = None
    phone_number: Optional[str] = None

    @validator("phone_number", pre=True, always=True)
    def validate_phone(cls, v):
        if v is None:
            return v
        pattern = r"^7\d{10}$"
        if not re.match(pattern, v):
            raise ValueError("Номер должен быть в формате 7XXXXXXXXXX")
        return v


class UserResponse(UserBase):
    id: int = Field(..., description="ID пользователя")

    class Config:
        from_attributes = True  # для будущей работы с ORM