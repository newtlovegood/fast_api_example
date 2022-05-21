from typing import Generator

from fastapi import APIRouter

from .endpoints import posts, users, todos

api_router = APIRouter()
api_router.include_router(posts.router)
api_router.include_router(users.router)
api_router.include_router(todos.router)
