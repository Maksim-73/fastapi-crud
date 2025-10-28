from fastapi import FastAPI
from app.users.routers import router as user_router  # Правильно!
from app.users.schemas import *

app = FastAPI()

app.include_router(user_router)

