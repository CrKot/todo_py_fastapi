from pydantic import BaseModel


class Task(BaseModel):
    id: int
    description: str
    user_id: int

    class Config:
        orm_mode: True
