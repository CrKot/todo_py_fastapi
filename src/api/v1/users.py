from fastapi import APIRouter

user_router = APIRouter()


@user_router.get("/users")
async def get_user_list():
    return await list()
