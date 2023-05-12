from fastapi import APIRouter

from .books import router as books_router
from .users import router as users_router

api_router = APIRouter()

api_router.include_router(books_router, prefix="/books", tags=["books"])
api_router.include_router(users_router, prefix="/users", tags=["users"])
