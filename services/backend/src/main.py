import typing as t

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import schemas
from .db import models
from .db.database import database, engine

models.Base.metadata.create_all(bind=engine)

origins = [
    'http://localhost:8080',
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.on_event('startup')
async def startup():
    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()


@app.get('/users/', response_model=t.List[schemas.User])
async def read_users():
    query = models.users.select()
    return await database.fetch_all(query)


@app.post('/users/', response_model=schemas.User)
async def create_user(user: schemas.UserIn):
    query = models.users.insert().values(username=user.username, password=user.password)
    last_record_id = await database.execute(query)
    return {**user.dict(), 'id': last_record_id}
