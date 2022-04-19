import random
from sqlalchemy.orm import Session

from app import crud


def create_unique_username(db: Session, username):
    while True:
        user = crud.user.get_by_username(db, username)
        if not user:
            return username
        username += str(random.randint(100, 999))