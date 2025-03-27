"""зависимости"""

from sqlalchemy import Column, Integer, String, ForeignKey
from src.database.base import Base


class TaskModel(Base):
    """Класс для тасков."""

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
