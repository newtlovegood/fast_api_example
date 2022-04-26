from tkinter import N
from typing import Optional, List
from datetime import datetime

from pydantic import BaseModel, EmailStr


class PostBase(BaseModel):
    title: str
    content: str
    
class PostUpdate(PostBase):
    pass


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


class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    username: Optional[str] = None
    password: Optional[str] = None


class User(UserBase):
    id: Optional[int] = None
    hashed_password: str
    
    class Config:
        orm_mode = True
        
        
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None



class Comment(BaseModel):
    # user
    # timestamp
    # content
    # likes
    pass
