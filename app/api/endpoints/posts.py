from typing import List
from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from starlette.templating import Jinja2Templates

from app import crud, models, schemas
from app.api import session_gen


router = APIRouter()

templates = Jinja2Templates(directory='app/templates')

# Example of returning response for TEMPLATES

# @router.get('/posts', response_class=HTMLResponse)
# def get_all_posts(request: Request, db: Session = Depends(session_gen.get_db)):
#     posts = crud.post.get_all(db)
#     context = {
#         'request': request,
#         'posts': posts,

#     }
#     return templates.TemplateResponse('posts.html', context)


@router.get('/posts', response_model=List[schemas.Post])
def get_all_posts(db: Session = Depends(session_gen.get_db)):
    return crud.post.get_all(db)



@router.get('/posts/{id}', response_model=schemas.Post)
def get_single_post(id: int, db: Session = Depends(session_gen.get_db)):
    return crud.post.get_by_id(db, id)


@router.post('/posts/create', response_model=schemas.Post)
def create_post(post_in: schemas.PostCreate, db: Session = Depends(session_gen.get_db)):
    post = crud.post.create(db, post_in)
    # Author ID to be taken from currrently logged in user 
    # Some validation if needed
    # ...
    return post

