from pydantic import BaseModel


class TaskCreateSchema(BaseModel):
    id: int
    description: str
    user_id: int

    class Config:
        orm_mode: True
