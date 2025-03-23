from fastapi import APIRouter
import uvicorn

app = APIRouter()

# app.include_router()

if __name__ == "__main__":
    uvicorn.run("main:app")

# from fastapi import FastAPI, HTTPException, Path
# from pydantic import BaseModel
# from typing import List, Optional
# import uvicorn

# # Инициализация FastAPI приложения
# app = FastAPI()


# # Модель задачи (Pydantic модель)
# class Task(BaseModel):
#     id: int
#     title: str
#     description: Optional[str] = None
#     completed: bool = False


# # База данных в памяти (список задач)
# tasks = []

# # Счетчик для генерации ID задач
# task_id_counter = 1


# # Добавление задачи
# @app.post("/tasks/", response_model=Task)
# def create_task(task: Task):
#     global task_id_counter
#     task.id = task_id_counter
#     task_id_counter += 1
#     tasks.append(task)
#     return task


# # Получение списка всех задач
# @app.get("/tasks/", response_model=List[Task])
# def get_tasks():
#     return tasks


# # Получение задачи по ID
# @app.get("/tasks/{task_id}", response_model=Task)
# def get_task(task_id: int = Path(..., description="ID задачи")):
#     for task in tasks:
#         if task.id == task_id:
#             return task
#     raise HTTPException(status_code=404, detail="Задача не найдена")


# # Обновление задачи
# @app.put("/tasks/{task_id}", response_model=Task)
# def update_task(task_id: int, updated_task: Task):
#     for task in tasks:
#         if task.id == task_id:
#             task.title = updated_task.title
#             task.description = updated_task.description
#             task.completed = updated_task.completed
#             return task
#     raise HTTPException(status_code=404, detail="Задача не найдена")


# # Удаление задачи
# @app.delete("/tasks/{task_id}", response_model=Task)
# def delete_task(task_id: int):
#     for i, task in enumerate(tasks):
#         if task.id == task_id:
#             deleted_task = tasks.pop(i)
#             return deleted_task
#     raise HTTPException(status_code=404, detail="Задача не найдена")


# Запуск сервера
# if __name__ == "__main__":
# import uvicorn
# uvicorn.run("main:app")
# uvicorn.run(app, host="0.0.0.0", port=8000)


# from fastapi import FastAPI, Depends, HTTPException, UploadFile, File
# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker, Session
# from pymongo import MongoClient
# from pydantic import BaseModel
# from passlib.context import CryptContext
# from datetime import datetime, timedelta
# from jose import JWTError, jwt

# # Database configurations
# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://user:password@localhost/todolist"
# MONGO_DB_URL = "mongodb://localhost:27017/"
# SECRET_KEY = "your_secret_key"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30

# engine = create_engine(SQLALCHEMY_DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

# client = MongoClient(MONGO_DB_URL)
# mongo_db = client.todolist

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# def get_password_hash(password):
#     return pwd_context.hash(password)

# def verify_password(plain_password, hashed_password):
#     return pwd_context.verify(plain_password, hashed_password)

# def create_access_token(data: dict, expires_delta: timedelta = None):
#     to_encode = data.copy()
#     expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
#     to_encode.update({"exp": expire})
#     return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# # User model (MySQL)
# class User(Base):
#     __tablename__ = "users"
#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String, unique=True, index=True)
#     password = Column(String)
#     role = Column(String)  # e.g., "admin", "user"

# Base.metadata.create_all(bind=engine)

# # Task model (MongoDB)
# class Task(BaseModel):
#     id: str
#     description: str
#     image: str
#     video_url: str

# # FastAPI instance
# app = FastAPI()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @app.post("/users/")
# def create_user(username: str, password: str, role: str, db: Session = Depends(get_db)):
#     hashed_password = get_password_hash(password)
#     user = User(username=username, password=hashed_password, role=role)
#     db.add(user)
#     db.commit()
#     db.refresh(user)
#     return user

# @app.post("/token")
# def login(username: str, password: str, db: Session = Depends(get_db)):
#     user = db.query(User).filter(User.username == username).first()
#     if not user or not verify_password(password, user.password):
#         raise HTTPException(status_code=401, detail="Invalid credentials")
#     access_token = create_access_token(data={"sub": user.username})
#     return {"access_token": access_token, "token_type": "bearer"}

# @app.get("/users/{user_id}")
# def get_user(user_id: int, db: Session = Depends(get_db)):
#     user = db.query(User).filter(User.id == user_id).first()
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user

# @app.post("/tasks/")
# def create_task(task: Task):
#     task_dict = task.dict()
#     mongo_db.tasks.insert_one(task_dict)
#     return task_dict

# @app.get("/tasks/{task_id}")
# def get_task(task_id: str):
#     task = mongo_db.tasks.find_one({"id": task_id})
#     if not task:
#         raise HTTPException(status_code=404, detail="Task not found")
#     return task

# @app.delete("/tasks/{task_id}")
# def delete_task(task_id: str):
#     result = mongo_db.tasks.delete_one({"id": task_id})
#     if result.deleted_count == 0:
#         raise HTTPException(status_code=404, detail="Task not found")
#     return {"message": "Task deleted"}

# @app.post("/upload-image/")
# def upload_image(file: UploadFile = File(...)):
#     file_location = f"static/{file.filename}"
#     with open(file_location, "wb") as f:
#         f.write(file.file.read())
#     return {"image_url": file_location}
