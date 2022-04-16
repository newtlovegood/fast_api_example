from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from starlette.templating import Jinja2Templates

from app import crud, models, schemas
from app.api import session_gen


router = APIRouter()

templates = Jinja2Templates(directory='app/templates')


@router.get('/users', response_class=HTMLResponse)
def get_all_users(request: Request, db: Session = Depends(session_gen.get_db)):
    users = crud.user.get_all(db)
    context = {
        'request': request,
        'users': users,

    }
    return templates.TemplateResponse('users.html', context)
