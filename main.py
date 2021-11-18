from fastapi import FastAPI
from routes import helloWorld, users

app = FastAPI()
app.include_router(helloWorld.router)
app.include_router(users.router)
