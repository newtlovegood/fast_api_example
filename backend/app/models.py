from colorama import Fore
from sqlalchemy import Boolean, Integer, Column, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean(), default=False)
    posts = relationship('Post', back_populates="author")
    todoitems = relationship('ToDoItem', back_populates='user')


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    content = Column(String)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())

    author_id = Column(Integer, ForeignKey("users.id"))
    author = relationship('User', back_populates='posts')



class ToDoItem(Base):
    __tablename__ = 'todoitems'

    id = Column(Integer, primary_key=True, index=True) 
    content = Column(String, default='')
    is_done = Column(Boolean, default=False)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='todoitems')
