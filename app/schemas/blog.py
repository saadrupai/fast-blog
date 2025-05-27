from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class BlogBase(BaseModel):
    title: str
    body: str

class BlogCreate(BlogBase):
    author_id: int

class BlogUpdate(BaseModel):
    title: Optional[str] = None
    body: Optional[str] = None

class BlogResponse(BlogBase):
    id: int
    author_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

class BlogList(BaseModel):
    id: int
    title: str
    author_id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

class BlogWithAuthor(BlogResponse):
    author: "UserList"

# Forward reference
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.schemas.user import UserList