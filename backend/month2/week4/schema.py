from uuid import UUID
from pydantic import BaseModel
from typing import Optional, Union


class Book(BaseModel):
    id: UUID
    title: str
    author: str
    year: int
    pages: int
    language: str


class BookCreate(BaseModel):
    title: str
    author: str
    year: int
    pages: int
    language: str


class BookUpdate(BaseModel):
    title: str
    pages: int


class Books(BaseModel):
    books: list[Book]


class User(BaseModel):
    id: UUID
    name: str
    email: str
    password: str


class UserCreate(BaseModel):
    name: str
    email: str
    password: str


class UserUpdate(UserCreate):
    pass


class Response(BaseModel):
    message: Optional[str] = None
    has_error: bool = False
    error_message: Optional[str] = None
    data: Union[Optional[Book | Books], Optional[User | list[User]]] = None
