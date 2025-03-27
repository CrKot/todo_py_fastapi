from fastapi import HTTPException
from starlette import status
from sqlalchemy.orm import Session
from src.models import TaskModel
from src.schemas import TaskCreateSchema


def get_all_tasks(db: Session):
    """Возвращает все таски"""
    return db.query(TaskModel).all()


def get_tasks(db: Session, user_id: int):
    """Возвращает таски по user_id"""
    return db.query(TaskModel).filter(TaskModel.user_id == user_id).all()


def get_task(db: Session, task_id: int):
    """Возвращает таску по tast_id"""
    db_task = db.query(TaskModel).filter(TaskModel.id == task_id).first()

    if db_task is None:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Задача не найдена"
        )

    return db_task


async def create_task(db: Session, task: TaskCreateSchema, user_id: int):
    """Создает таску привязанную к user_id"""
    db_task = TaskModel(description=task.description, user_id=user_id)
    db.add(db_task)
    await db.commit()
    db.refresh(db_task)
    return db_task


def delete_task(db: Session, task_id: int):
    """Удаляет таску по task_id"""
    db_task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if db_task is None:
        # return {"status": "error", "message": "Задача не найдена"}
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Задача не найдена"
        )

    db.delete(db_task)
    db.commit()
    return db_task
