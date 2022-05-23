from sqlalchemy.orm import Session

from app.models import ToDoItem
from app.schemas import ToDoItemCreate

class CRUDToDoItem:
    
    def get_by_list(self, list_id: int, db: Session):
        return db.query(ToDoItem).filter(ToDoItem.owner_id==list_id).first()
    
    def create(self, obj_in: ToDoItemCreate, db: Session):
        todoitem = ToDoItem(
            content=obj_in.content,
            is_done=obj_in.is_done,
            list_id=obj_in.list_id,
        )
        db.add(todoitem)
        db.commit()
        db.refresh(todoitem)
        return todoitem
    
    def update(self, todo_in: ToDoItemCreate, db: Session):
        todoitem = self.get_by_list(todo_in.list_id, db)
        todoitem.content = todo_in.content
        todoitem.is_done = todo_in.is_done
        db.commit()
        db.refresh(todoitem)
        return todolist

    def delete(self, list_id: int, db: Session):        
        todoitem = self.get_by_list(list_id, db) 
        db.delete(todoitem)
        db.commit()
        

todoitem = CRUDToDoItem()