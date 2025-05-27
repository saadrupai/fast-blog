# from fastapi import APIRouter
# from app.api.endpoints import users, blogs

# api_router = APIRouter()

# # api_router.include_router(users.router, prefix="/users", tags=["users"])
# # api_router.include_router(blogs.router, prefix="/blogs", tags=["blogs"])
# from app.api.endpoints.user import router as users_router
# from app.api.endpoints.blog import router as blogs_router

# api_router.include_router(users_router, prefix="/users", tags=["users"])
# api_router.include_router(blogs_router, prefix="/blogs", tags=["blogs"])

from fastapi import APIRouter
from app.api.endpoints.user import router as users_router
from app.api.endpoints.blog import router as blogs_router

api_router = APIRouter()
api_router.include_router(users_router, prefix="/users", tags=["users"])
api_router.include_router(blogs_router, prefix="/blogs", tags=["blogs"])