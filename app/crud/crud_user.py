from sqlalchemy.orm import Session
from pydantic import EmailStr

from app.schemas import UserCreate
from app.models import User
from app.security import get_password_hash


class CRUDUser:
    def _get_by_id(self, db: Session, id: int):
        return db.query(User).filter(User.id == id).first()

    def get_by_email(self, db: Session, email: EmailStr):
        return db.query(User).filter(User.email == email).first()

    def get_by_username(self, db: Session, username: str):
        return db.query(User).filter(User.username == username).first()

    def get_all(self, db: Session):
        return db.query(User).all()

    def create(self, db: Session, obj_in: UserCreate):
        db_user = User(
            email=obj_in.email,
            hashed_password=get_password_hash(obj_in.password),
            username=obj_in.username,
            is_superuser=obj_in.is_superuser,
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    def update(self, db: Session, id: int):
        db_user = self._get_by_id(db, id)
        return db_user

    def delete(self, db: Session, id: int):
        db_user = self._get_by_id(db, id)
        db.delete(db_user)
        db.commit()


user = CRUDUser()
