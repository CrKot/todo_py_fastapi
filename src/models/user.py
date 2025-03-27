"""зависимости"""

from sqlalchemy import Column, Integer, String
from src.database.base import Base


class UserModel(Base):
    """Класс для пользователей."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    hashed_password = Column(String(150))
