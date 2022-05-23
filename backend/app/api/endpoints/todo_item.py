from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import session_gen
from app.auth.endpoints.auth import get_current_active_user

router = APIRouter()


@router.post('/todoitem/create', response_model=schemas.ToDoItemCreate)
def create_item(content: str,
                is_done: bool,
                current_user: schemas.User = Depends(get_current_active_user),
                db: Session = Depends(session_gen.get_db)):
    
    user_list = crud.todolist.get_or_create(current_user.id, db)
    obj_in = schemas.ToDoItemCreate(content=content, is_done=is_done, list_id=user_list.id)
    return crud.todoitem.create(obj_in ,db)

@router.put('/todoitem/update', response_model=schemas.ToDoItemCreate)
def update_item(current_user: schemas.User = Depends(get_current_active_user),
                db: Session = Depends(session_gen.get_db)):
    return crud.todoitem.update()


@router.delete('/todoitem/delete')
def delete_item(current_user: schemas.User = Depends(get_current_active_user),
                db: Session = Depends(session_gen.get_db)):
    return crud.todoitem.delete()