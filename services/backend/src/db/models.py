from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from .database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column('id', UUID(as_uuid=True), primary_key=True, index=True)
    username = Column('username', String(128), nullable=False, unique=True)
    password = Column('password', String(128), nullable=False)
