from curses.ascii import HT
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from starlette.templating import Jinja2Templates

from app import crud, models, schemas
from app.api import session_gen
from app.auth.endpoints.auth import get_current_active_user


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
def create_post(post_base: schemas.PostBase, 
                current_user: schemas.User = Depends(get_current_active_user),
                db: Session = Depends(session_gen.get_db)):
    
    post_in = schemas.PostCreate(**post_base.dict(), 
                                 author_id=current_user.id)
    # Some validation if needed
    # ...
    post = crud.post.create(db, post_in)
    return post


@router.delete('/posts/delete/{id}')
def delete_post(id: int, 
                current_user: schemas.User = Depends(get_current_active_user),
                db: Session = Depends(session_gen.get_db)):
    
    # if cur user is author or superuser - allow delete
    post = crud.post.get_by_id(db, id)
    if not post:
        raise HTTPException(404, 'Post not found')
    if not (post.author_id == current_user.id or current_user.is_superuser):
        raise HTTPException(403, 'Deletion is forbidden')   
    crud.post.delete(db, id)


@router.put('/posts/update/{id}')
def update_post(id: int,
                post_in: schemas.PostUpdate,
                current_user: schemas.User = Depends(get_current_active_user),
                db: Session = Depends(session_gen.get_db)):
    post = crud.post.get_by_id(db, id)
    if not post:
        raise HTTPException(404, 'Post not found')
    if not post.author_id == current_user.id:
        raise HTTPException(403, 'Editing is forbidden')
    return crud.post.update(db, id, post_in)