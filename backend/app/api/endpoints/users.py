from typing import List
import logging
import random

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from starlette.templating import Jinja2Templates

from app import crud, models, schemas
from app.api import session_gen
from app.auth.endpoints.auth import get_current_active_user


logger = logging.getLogger(__name__)

router = APIRouter()

templates = Jinja2Templates(directory='app/templates')


@router.get("/users/me")
async def reads_current_user(current_user: schemas.User = Depends(get_current_active_user)):
    return current_user

@router.get('/users', response_model=List[schemas.User])
def reads_all_users(db: Session = Depends(session_gen.get_db)):
    return crud.user.get_all(db)

@router.get('/users/{username}', response_model=schemas.User)
def reads_single_users(username: str, db: Session = Depends(session_gen.get_db)):
    return crud.user.get_by_username(db, username)

@router.post('/users/create', response_model=schemas.User)
def create_user(user_in: schemas.UserCreate, db: Session = Depends(session_gen.get_db), status_code=status.HTTP_201_CREATED):

    if not user_in.username:
        user_in.username = user_in.email.split('@')[0]

    # check if email is Unique
    if crud.user.get_by_email(db, user_in.email):
        return HTTPException(status_code=400, detail="Email is already used")
    
    while True:
        try:
            user = crud.user.create(db, user_in)
        except Exception as e:
            logger.info(e)
            db.rollback()
            user_in.username += str(random.randint(100, 999))
        else:
            break
        
    return user

@router.delete('/users/delete/{id}')
def delete_user(id: int, current_user: schemas.User = Depends(get_current_active_user),
                db: Session = Depends(session_gen.get_db)):
    # check if current user is superuser
    # check if user exists
    # use delete crud func
    user = crud.user.get_by_id(db, id)
    if not user:
        raise HTTPException(404, 'User not found')
    if not current_user.is_superuser:
        raise HTTPException(403, 'You have to be a superuser to perform this action')
    crud.user.delete(db, id)
    

@router.put('/users/update/{id}')
def update_user(id: int, 
                user_in: schemas.UserUpdate,
                current_user: schemas.User = Depends(get_current_active_user),
                db: Session = Depends(session_gen.get_db)):
    
    user = crud.user.get_by_id(db, id)
    if not user:
        raise HTTPException(404, 'User not found')
    if not current_user.id == user.id and not current_user.is_superuser:
        raise HTTPException(403, 'Editing is forbidden')
    return crud.user.update(db, id, user_in)