from sqlalchemy import Column, String, Text, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import BaseModel

class Blog(BaseModel):
    __tablename__ = "blogs"
    
    title = Column(String(200), nullable=False)
    body = Column(Text, nullable=False)
    author_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # Relationship with User
    author = relationship("User", back_populates="blogs")