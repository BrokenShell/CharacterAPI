"""
Character API
- Create
- Read
- Update
- Delete
"""
from typing import Dict

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.data import MongoDB

API = FastAPI(
    title="Character API",
    version="0.0.1",
    docs_url="/",
)
API.db = MongoDB()
API.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@API.get("/info")
async def info():
    return API.version


@API.post("/create")
async def create(data: Dict):
    return API.db.create("Characters", data)


@API.get("/read")
async def read():
    return API.db.read("Characters", {})


@API.patch("/update")
async def update(query: Dict, data: Dict):
    return API.db.update("Characters", query, data)


@API.delete("/delete")
async def delete(query: Dict):
    return API.db.delete("Characters", query)
