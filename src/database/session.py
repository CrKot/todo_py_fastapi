from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker
from src.core.config import settings
import time


engine = create_engine(settings.DATABASE_URL, echo=True)


def create_db_engine():
    for _ in range(5):
        try:
            engine = create_engine(settings.DATABASE_URL, echo=True)
            print("tutu")
            return engine
            # engine = await create_engine(settings.DATABASE_URL, echo=True)
        except OperationalError:
            time.sleep(5)
    raise RuntimeError("Не удалось подключиться к БД")


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
