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
    posts = relationship('Post', back_populates="authors")
    todolist = relationship('ToDoList', back_populates='owner')


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    content = Column(String)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    author_id = Column(Integer, ForeignKey("users.id"))
    authors = relationship('User', back_populates='posts')


class ToDoList(Base):
    __tablename__ = 'todolists'
    
    id = Column(Integer, primary_key=True, index=True) 
    items = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship('User', back_populates='todolist')

