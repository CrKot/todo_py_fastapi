from fastapi import FastAPI
import uvicorn
from src.api.v1.routers import api_router
from alembic.config import Config
from alembic import command


def run_migraions():
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")


# run_migraions()

app = FastAPI()
app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run("main:app")

# import os
# import glob


# for pyc in glob.glob("**/*.pyc", recursive=True):
#     os.remove(pyc)
