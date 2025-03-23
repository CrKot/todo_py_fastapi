from fastapi import FastAPI
import uvicorn
import src.api.v1.routers from api_router

app = FastAPI()
app.include_router(api_router)


if __name__ == "__main__":
    uvicorn.run("main:app")
