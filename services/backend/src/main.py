from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from .db import models
from .db.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


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
