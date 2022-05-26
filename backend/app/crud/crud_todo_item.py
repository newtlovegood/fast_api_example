from sqlalchemy.orm import Session

from app.models import ToDoItem
from app.schemas import ToDoItemCreate, ToDoItemUpdate

class CRUDToDoItem:
    
    def get_by_id(self, item_id: int, db: Session):
        return db.query(ToDoItem).filter(ToDoItem.id == item_id).first()
    
    def get_items_by_user(self, user_id: int, db: Session):
        return db.query(ToDoItem).filter(ToDoItem.user_id == user_id).all()
    
    def create(self, obj_in: ToDoItemCreate, db: Session):
        todoitem = ToDoItem(
            content=obj_in.content,
            is_done=obj_in.is_done,
            user_id=obj_in.user_id,
        )
        db.add(todoitem)
        db.commit()
        db.refresh(todoitem)
        return todoitem
    
    def update(self, item_id: int, todo_in: ToDoItemUpdate, db: Session):
        
        todoitem = self.get_by_id(item_id, db)
        todoitem.content = todo_in.content
        todoitem.is_done = todo_in.is_done
        db.commit()
        db.refresh(todoitem)
        return todoitem

    def delete(self, item_id: int, db: Session):        
        todoitem = self.get_by_id(item_id, db) 
        db.delete(todoitem)
        db.commit()
        

todoitem = CRUDToDoItem()