from sqlalchemy.orm import Session

from app.schemas import PostCreate
from app.models import Post


class CRUDPost:
    def get_by_id(self, db: Session, id: int):
        return db.query(Post).filter(Post.id == id).first()

    def get_multi_by_author(self, db: Session, author_id: int, limit: int = 20):
        return (
            db.query(Post)
            .filter(Post.author_id == author_id)
            .limit(limit)
            .all()
        )

    def get_all(self, db: Session):
        return db.query(Post).all()

    def create(self, db: Session, obj_in=PostCreate):
        post = Post(
            title=obj_in.title,
            content=obj_in.content,
            author_id=obj_in.author_id,

        )
        db.add(post)
        db.commit()
        db.refresh(post)
        return post

    def update(self, db: Session, id: int, content: str = None, title: str = None):
        post = self.get_by_id(db, id)
        if content:
            post.content = content
        if title:
            post.title = title
        db.commit()
        db.refresh(post)

    def delete(self, db: Session, id: int):
        post = self.get_by_id(db, id)
        db.delete(post)
        db.commit()


post = CRUDPost()
