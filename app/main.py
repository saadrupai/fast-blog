# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from app.api import api_router
# from app.database import engine
# from app import models

# from app.api.endpoints.user import router as users_router
# from app.api.endpoints.blog import router as blogs_router


# # Create all tables
# models.Base.metadata.create_all(bind=engine)

# app = FastAPI(
#     title="Blog API",
#     description="A complete blog API with users and posts",
#     version="1.0.0"
# )

# # CORS middleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Configure this properly in production
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Include API routes
# # app.include_router(api_router, prefix="/api/v1")
# api_router.include_router(users_router, prefix="/users", tags=["users"])
# api_router.include_router(blogs_router, prefix="/blogs", tags=["blogs"])

# @app.get("/")
# def root():
#     return {
#         "message": "Blog API is running!",
#         "docs": "/docs",
#         "redoc": "/redoc"
#     }

# # Health check endpoint
# @app.get("/health")
# def health_check():
#     return {"status": "healthy"}

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine
from app import models

# Import routers directly - bypass api_router completely
from app.api.endpoints.users import router as users_router
from app.api.endpoints.blogs import router as blogs_router

# Create all tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Blog API", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers directly
app.include_router(users_router, prefix="/api/v1/users", tags=["users"])
app.include_router(blogs_router, prefix="/api/v1/blogs", tags=["blogs"])

@app.get("/")
def root():
    return {"message": "Blog API is running!", "docs": "/docs"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
