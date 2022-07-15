"""
Character API
- Create
- Read
- Update
- Delete

INPUT :: JSON
OUTPUT :: JSON
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.characters import Character, CharacterOptions
from app.data import MongoDB

API = FastAPI(
    title="Character API",
    version="0.0.3",
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
async def create(data: Character):
    return API.db.create("Characters", data.dict())


@API.put("/read")
async def read(query: CharacterOptions):
    return API.db.read("Characters", query.dict(exclude_none=True))


@API.patch("/update")
async def update(query: CharacterOptions, data: CharacterOptions):
    return API.db.update(
        "Characters",
        query.dict(exclude_none=True),
        data.dict(exclude_none=True),
    )


@API.delete("/delete")
async def delete(query: CharacterOptions):
    return API.db.delete("Characters", query.dict(exclude_none=True))
