from fastapi import APIRouter

import app.auth.endpoints.users as users

auth_router = APIRouter()

auth_router.include_router(users.router)