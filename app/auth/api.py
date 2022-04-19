from fastapi import APIRouter

import app.auth.endpoints.auth as auth

auth_router = APIRouter()

auth_router.include_router(auth.router)