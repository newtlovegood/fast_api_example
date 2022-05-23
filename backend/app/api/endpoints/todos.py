from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import session_gen
from app.auth.endpoints.auth import get_current_active_user


router = APIRouter()

@router.get('/todo', response_model=schemas.ToDoListCreate)
def get_todo(current_user: schemas.User = Depends(get_current_active_user),
             db: Session = Depends(session_gen.get_db)):
    return crud.todolist.get_or_create(current_user.id, db)

@router.post('/todo/create', response_model=schemas.ToDoListCreate)
def create_todo(todo_in: schemas.ToDoListBase,
                current_user: schemas.User = Depends(get_current_active_user),
                db: Session = Depends(session_gen.get_db)):
    obj = schemas.ToDoListCreate(items=todo_in.items, owner_id=current_user.id)
    return crud.todolist.create(obj, db)


@router.put('/todo/update', response_model=schemas.ToDoListCreate)
def update_todo(items: str,
                current_user: schemas.User = Depends(get_current_active_user),
                db: Session = Depends(session_gen.get_db)):
    todolist = crud.todolist.get_by_owner(current_user.id, db)
    if not todolist:
        raise HTTPException(404, 'Todo List not found')
    if not (todolist.author_id == current_user.id):
        raise HTTPException(403, 'Update is forbidden')   
    return crud.todolist.update(todolist, items, db)

@router.delete('/todo/delete')
def delete_todo(current_user: schemas.User = Depends(get_current_active_user),
                db: Session = Depends(session_gen.get_db)):
    
    todolist = crud.todolist.get_by_owner(current_user.id, db)
    if not todolist:
        raise HTTPException(404, 'Todo List not found')
    if not (todolist.author_id == current_user.id):
        raise HTTPException(403, 'Deletion is forbidden')   
    crud.todolist.delete(current_user.id, db)


