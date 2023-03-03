from sqlalchemy import Column, DateTime, ForeignKey, func, String, text, Text
from sqlalchemy.dialects.postgresql import UUID

from .database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(
        'id', UUID(), server_default=text('uuid_generate_v4()'),
        primary_key=True, index=True)
    username = Column('username', String(128), nullable=False, unique=True)
    password = Column('password', String(128), nullable=False)


users = User.__table__


class Plant(Base):
    __tablename__ = 'plants'

    id = Column(
        'id', UUID(), server_default=text('uuid_generate_v4()'),
        primary_key=True, index=True)
    user_id = Column('user_id', UUID(), ForeignKey('users.id'))
    description = Column('type', Text, nullable=True)


plants = Plant.__table__


class EventType(Base):
    __tablename__ = 'event_types'

    id = Column(
        'id', UUID(), server_default=text('uuid_generate_v4()'),
        primary_key=True, index=True)
    user_id = Column('user_id', UUID(), ForeignKey('users.id'))
    type = Column('type', String(512), nullable=False)


class Event(Base):
    __tablename__ = 'events'

    id = Column(
        'id', UUID(), server_default=text('uuid_generate_v4()'),
        primary_key=True, index=True)
    plant_id = Column('plant_id', UUID(), ForeignKey('plants.id'))
    event_type_id = Column('event_type_id', UUID(), ForeignKey('event_types.id'))
    date = Column('date', DateTime, default=func.now())
    comment = Column('comment', Text, nullable=True)
