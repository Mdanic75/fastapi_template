from fastapi import FastAPI
# from .auth.router import auth_router
app = FastAPI()
from .database_config.database import create_db_and_tables
# app.include_router(auth_router)


@app.get("/")
async def root():
    await create_db_and_tables()
