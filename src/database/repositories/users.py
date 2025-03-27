from sqlalchemy.orm import Session
from src.models import UserModel
from src.schemas import UserCreateSchema


def get_users(db: Session):
    return db.query(UserModel).all()


def get_user(db: Session, user_id: int):
    return db.query(UserModel).filter(UserModel.id == user_id).first()


async def create_user(db: Session, user: UserCreateSchema, hashed_password: str):
    db_user = UserModel(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    await db.commit()
    db.refresh(db_user)
    return db_user
