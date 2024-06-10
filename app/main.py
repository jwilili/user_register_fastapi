from fastapi import FastAPI
from app.routers import user, verification
from app.db.database import database, create_tables

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()
    await create_tables()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(verification.router, prefix="/verification", tags=["verification"])
