from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.dependencies import get_db

router = APIRouter()

@router.post("/", response_model=schemas.BlogResponse)
def create_blog(
    *,
    db: Session = Depends(get_db),
    blog_in: schemas.BlogCreate
) -> Any:
    """Create new blog"""
    # Check if author exists
    author = crud.user.get(db=db, id=blog_in.author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    
    blog = crud.blog.create(db=db, obj_in=blog_in)
    return blog

@router.get("/", response_model=List[schemas.BlogList])
def read_blogs(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """Retrieve blogs"""
    blogs = crud.blog.get_multi(db, skip=skip, limit=limit)
    return blogs

@router.get("/{blog_id}", response_model=schemas.BlogWithAuthor)
def read_blog(
    *,
    db: Session = Depends(get_db),
    blog_id: int
) -> Any:
    """Get blog by ID with author info"""
    blog = crud.blog.get(db=db, id=blog_id)
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return blog

@router.put("/{blog_id}", response_model=schemas.BlogResponse)
def update_blog(
    *,
    db: Session = Depends(get_db),
    blog_id: int,
    blog_in: schemas.BlogUpdate
) -> Any:
    """Update blog"""
    blog = crud.blog.get(db=db, id=blog_id)
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    
    blog = crud.blog.update(db=db, db_obj=blog, obj_in=blog_in)
    return blog

@router.delete("/{blog_id}")
def delete_blog(
    *,
    db: Session = Depends(get_db),
    blog_id: int
) -> Any:
    """Delete blog"""
    blog = crud.blog.get(db=db, id=blog_id)
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    
    blog = crud.blog.delete(db=db, id=blog_id)
    return {"message": "Blog deleted successfully"}

@router.get("/user/{user_id}", response_model=List[schemas.BlogList])
def read_user_blogs(
    *,
    db: Session = Depends(get_db),
    user_id: int,
    skip: int = 0,
    limit: int = 100
) -> Any:
    """Get all blogs by a specific user"""
    # Check if user exists
    user = crud.user.get(db=db, id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    blogs = crud.blog.get_blogs_by_author(
        db, author_id=user_id, skip=skip, limit=limit
    )
    return blogs

@router.get("/search/", response_model=List[schemas.BlogList])
def search_blogs(
    *,
    db: Session = Depends(get_db),
    q: str,
    skip: int = 0,
    limit: int = 100
) -> Any:
    """Search blogs by title"""
    blogs = crud.blog.search_blogs(db, query=q, skip=skip, limit=limit)
    return blogs
