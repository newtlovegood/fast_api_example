import logging

from sqlalchemy.orm import Session
from app.db import SessionLocal, engine
from app import crud, schemas, models
from app.config import settings


logger = logging.getLogger(__name__) 


def init_db(db: Session) -> None:

    models.Base.metadata.create_all(bind=engine)

    user = crud.user.get_by_email(db, email=settings.FIRST_SUPERUSER)
    if not user:
        user_in = schemas.UserCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            full_name='Full Name',
            is_superuser=True,
        )
        user = crud.user.create(db, obj_in=user_in)


def init() -> None:
    db = SessionLocal()
    init_db(db)


def main() -> None:
    logger.info("Creating initial data")
    init()
    logger.info("Initial data created")


if __name__ == "__main__":
    main()
