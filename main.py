from fastapi import FastAPI
from app.modules.user.user_controller import rounter as user_router
from contextlib import asynccontextmanager
from app.utils.database import create_db_and_tables

@asynccontextmanager
async def lifespan(app):
    create_db_and_tables()
    yield
    

app = FastAPI(title= "Attendace", lifespan= lifespan , debug= True)

app.include_router(user_router)

