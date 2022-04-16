from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from starlette.templating import Jinja2Templates

from app import crud, models, schemas
from app.api import session_gen
from app.security import verify_password, get_password_hash


router = APIRouter()


def authenticate(db: Session, username: str, password: str):
    """Check if user exists or not"""
    user = crud.user.get_by_username(db, username)
    if not user:
        return False
    if not verify_password(password, get_password_hash(password)):
        return False
    return user



# @router.get('/login')
