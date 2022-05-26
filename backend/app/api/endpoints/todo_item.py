from curses.ascii import HT
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import session_gen
from app.auth.endpoints.auth import get_current_active_user

router = APIRouter()


@router.get('/todolist/', response_model=List[schemas.ToDoItem])
def get_todolist(current_user: schemas.User = Depends(get_current_active_user),
                 db: Session = Depends(session_gen.get_db)):
    return crud.todoitem.get_items_by_user(current_user.id, db)



@router.post('/todoitem/create', response_model=schemas.ToDoItem)
def create_item(item_in: schemas.ToDoItemBase = None,
                current_user: schemas.User = Depends(get_current_active_user),
                db: Session = Depends(session_gen.get_db)):
    
    if not item_in:
        item_in = schemas.ToDoItemBase()
    
    obj_in = schemas.ToDoItemCreate(content=item_in.content, 
                                    is_done=item_in.is_done,
                                    user_id=current_user.id)
    return crud.todoitem.create(obj_in ,db)

@router.put('/todoitem/update/{item_id}', response_model=schemas.ToDoItem)
def update_item(item_id: int,
                item_in: schemas.ToDoItemUpdate,
                current_user: schemas.User = Depends(get_current_active_user),
                db: Session = Depends(session_gen.get_db)):

    item = crud.todoitem.get_by_id(item_id, db)
    if not item:
        raise HTTPException(status_code=404, detail='Item not found')
    if not item.user_id == current_user.id:
        raise HTTPException(status_code=403, detail='Editing is forbidden')
    return crud.todoitem.update(item_id, item_in, db)


@router.delete('/todoitem/delete/{item_id}')
def delete_item(item_id: int,
                current_user: schemas.User = Depends(get_current_active_user),
                db: Session = Depends(session_gen.get_db)):
    
    # if user is owner of item - then delete
    item = crud.todoitem.get_by_id(item_id, db)
    if not item:
        raise HTTPException(status_code=404, detail='Item not found')
    if not item.user_id == current_user.id:
        raise HTTPException(status_code=403, detail='Editing is forbidden')
    return crud.todoitem.delete(item_id, db)