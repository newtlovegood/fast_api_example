import logging

from sqlalchemy.orm import Session
from app.db import SessionLocal, engine
from app import crud, schemas, models
from app.config import settings


logger = logging.getLogger(__name__) 


def populate(db: Session) -> None:

    # test user
    test_user_in = schemas.UserCreate(
            email=settings.EMAIL_TEST_USER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            full_name='Test Name',
            is_superuser=False,
        )
    test_user = crud.user.create(db, obj_in=test_user_in)
    
    # posts
    post_in_1 = schemas.PostCreate(
        title='CS50 AI - Intro',
        content='Introduction to course, curriculum, teachers, etc.',
        author_id=test_user.id
    )
    post_in_2 = schemas.PostCreate(
        title='CS50 AI - Search',
        content='Search algos, including Minimax, DFS, BFS, GBFS, Alpha-Beta Pruning',
        author_id=test_user.id
    )
    
    crud.post.create(db, obj_in=post_in_1)
    crud.post.create(db, obj_in=post_in_2)

    
    
    

def main() -> None:
    logger.info("Populating data")
    db = SessionLocal()
    populate(db)
    logger.info("Data created")


if __name__ == "__main__":
    main()
