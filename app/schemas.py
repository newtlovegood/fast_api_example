from typing import Optional, List
from datetime import datetime

from pydantic import BaseModel, EmailStr


class PostBase(BaseModel):
    title: str
    content: str


class PostCreate(PostBase):
    author_id: int


class Post(PostCreate):
    id: int
    # comments
    # likes

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: EmailStr
    username: Optional[str] = None
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    posts: List[Post] = []


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    password: Optional[str] = None


class User(UserBase):
    id: Optional[int] = None
    hashed_password: str
    
    class Config:
        orm_mode = True


class Comment(BaseModel):
    # user
    # timestamp
    # content
    # likes
    pass
