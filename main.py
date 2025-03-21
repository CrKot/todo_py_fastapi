from fastapi import APIRouter
import uvicorn

app = APIRouter()


if __name__ == "__main__":
    uvicorn.run("main:app")
