from fastapi import FastAPI
from routers import accounts, missions, user_records, tasks
from database import Base, engine

Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(accounts.router)
app.include_router(missions.router)
app.include_router(tasks.router)
app.include_router(user_records.router)
