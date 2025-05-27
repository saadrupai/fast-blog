from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List, Optional

class UserBase(BaseModel):
    email: EmailStr
    username: str

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    username: Optional[str] = None
    password: Optional[str] = None

class UserResponse(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

class UserList(BaseModel):
    id: int
    username: str
    email: EmailStr
    is_active: bool
    
    class Config:
        from_attributes = True

# For User with their blogs
class UserWithBlogs(UserResponse):
    blogs: List["BlogList"] = []

# Forward reference for BlogList
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.schemas.blog import BlogList