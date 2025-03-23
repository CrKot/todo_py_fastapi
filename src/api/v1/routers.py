from fastapi import APIRouter
from src.api.v1.tasks import tasks
from src.api.v1.users import users

api_router = APIRouter()
api_router.include_router()
api_router.include_router()
