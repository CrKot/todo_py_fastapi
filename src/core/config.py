import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
# from pydantic import Field

load_dotenv()


class Settings(BaseSettings):
    # MYSQL_ROOT_PASSWORD: str
    # MYSQL_DATABASE: str
    # MYSQL_USER: str
    # MYSQL_PASSWORD: str
    MYSQL_ROOT_PASSWORD: str = os.getenv("MYSQL_ROOT_PASSWORD")
    MYSQL_DATABASE: str = os.getenv("MYSQL_DATABASE")
    MYSQL_USER: str = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD: str = os.getenv("MYSQL_PASSWORD")

    # MYSQL_ROOT_PASSWORD: str = Field(..., env="MYSQL_ROOT_PASSWORD")
    # MYSQL_DATABASE: str = Field(..., env="MYSQL_DATABASE")
    # MYSQL_USER: str = Field(..., env="MYSQL_USER")
    # MYSQL_PASSWORD: str = Field(..., env="MYSQL_PASSWORD")

    # DATABASE_URL: str = (
    #     f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@127.0.0.1:3306/{MYSQL_DATABASE}"
    # )
    DATABASE_URL: str = "mysql+pymysql://root:example@127.0.0.1:3306/todo_db"

    # Другие настройки
    # SECRET_KEY: str = os.getenv("SECRET_KEY", "supersecretkey")
    # ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    # ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

    class Config:
        env_file = ".env"


settings = Settings()
# print(settings.MYSQL_USER)
# print(settings.MYSQL_DATABASE)
# print(settings.MYSQL_PASSWORD)
# print(settings.DATABASE_URL)
