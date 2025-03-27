from fastapi import FastAPI
import uvicorn
from src.api.v1.routers import api_router

app = FastAPI()
app.include_router(api_router)


if __name__ == "__main__":
    uvicorn.run("main:app")
