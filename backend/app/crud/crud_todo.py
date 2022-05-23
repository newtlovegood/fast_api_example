from sqlalchemy.orm import Session

from app.models import ToDoList
from app.schemas import ToDoListCreate

class CRUDToDoList:

    def get_or_create(self, owner_id: int, db: Session):
        todolist = db.query(ToDoList).filter(ToDoList.owner_id==owner_id).first()
        if not todolist:
            todolist = ToDoList(
            owner_id=owner_id,
            )
            db.add(todolist)
            db.commit()
            db.refresh(todolist)
        return todolist

    
    def update(self, todo_in: ToDoListCreate, items: str, db: Session):
        todolist = self.get_by_owner(todo_in.owner_id, db)
        todolist.items = items
        db.commit()
        db.refresh(todolist)
        return todolist

    def delete(self, owner_id: int, db: Session):        
        todolist = self.get_by_owner(owner_id, db) 
        db.delete(todolist)
        db.commit()
        

todolist = CRUDToDoList()