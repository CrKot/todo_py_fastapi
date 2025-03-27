from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.models import TaskModel
from src.schemas import TaskCreateSchema
from src.database.session import SessionLocal
from src.database.repositories.tasks import get_all_tasks, create_task

task_router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@task_router.get("/")
def get_task_list(db: Session = Depends(get_db)):
    return get_all_tasks(db)


@task_router.post("/tasks", response_model=TaskModel)
def post_task(user_id: int, db: Session = Depends(get_db)):
    return create_task(db, task=TaskCreateSchema, user_id=user_id)
