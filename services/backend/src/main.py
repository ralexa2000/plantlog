from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from .db import models
from .db.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

origins = [
    "http://localhost:8080",
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
def read_root():
    return {'Hello': 'World'}


@app.get('/users')
def read_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()


@app.get('/events')
def read_events(db: Session = Depends(get_db)):
    return db.query(models.Event).all()
