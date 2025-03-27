from pydantic import BaseModel


class UserCreateSchema(BaseModel):
    username: str
    password: str


class UserSchema(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True


class TokenSchema(BaseModel):
    access_token: str
    token_type: str
