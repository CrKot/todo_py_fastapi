from fastapi import APIRouter
from src.api.v1.tasks import task_router
from src.api.v1.users import user_router

api_router = APIRouter()
api_router.include_router(task_router)
api_router.include_router(user_router)
