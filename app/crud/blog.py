from typing import List
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.blog import Blog
from app.schemas.blog import BlogCreate, BlogUpdate

class CRUDBlog(CRUDBase[Blog, BlogCreate, BlogUpdate]):
    def get_blogs_by_author(
        self, 
        db: Session, 
        *, 
        author_id: int, 
        skip: int = 0, 
        limit: int = 100
    ) -> List[Blog]:
        return (
            db.query(Blog)
            .filter(Blog.author_id == author_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def search_blogs(
        self, 
        db: Session, 
        *, 
        query: str, 
        skip: int = 0, 
        limit: int = 100
    ) -> List[Blog]:
        return (
            db.query(Blog)
            .filter(Blog.title.contains(query))
            .offset(skip)
            .limit(limit)
            .all()
        )

blog = CRUDBlog(Blog)