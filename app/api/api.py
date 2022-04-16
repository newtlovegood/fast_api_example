from typing import Generator

from fastapi import APIRouter

from app.db import SessionLocal
from .endpoints import posts, users

api_router = APIRouter()
api_router.include_router(posts.router)
api_router.include_router(users.router)
