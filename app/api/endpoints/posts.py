from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from starlette.templating import Jinja2Templates

from app import crud, models, schemas
from app.api import session_gen


router = APIRouter()

templates = Jinja2Templates(directory='app/templates')


@router.get('/posts', response_class=HTMLResponse)
def get_all_posts(request: Request, db: Session = Depends(session_gen.get_db)):
    posts = crud.post.get_all(db)
    context = {
        'request': request,
        'posts': posts,

    }
    return templates.TemplateResponse('posts.html', context)


@router.get('/posts/{id}', response_class=HTMLResponse)
def get_single_post(request: Request, id: int, db: Session = Depends(session_gen.get_db)):
    post = crud.post.get_by_id(db, id)
    context = {
        'request': request,
        'post': post,
    }
    return templates.TemplateResponse('posts.html', context)



