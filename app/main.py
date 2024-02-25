import os
from typing import Optional
from fastapi import FastAPI
from models import mongodb
from routers import users, characters, situations, chats

from starlette.middleware.cors import CORSMiddleware

app = FastAPI() # FastAPI 모듈

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router) # 다른 route파일들을 불러와 포함시킴
app.include_router(characters.router)
app.include_router(situations.router)
app.include_router(chats.router)

@app.on_event("startup")
def on_app_start():
	mongodb.connect()

@app.on_event("shutdown")
async def on_app_shutdown():
	mongodb.close()

@app.get("/") # Route Path
def index():
    return {
        "Python": "Framework",
    }