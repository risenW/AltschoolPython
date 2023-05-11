from fastapi import APIRouter, status, HTTPException, Depends
from uuid import UUID
from schema import Book, BookCreate, BookUpdate, Response
from typing import Annotated
from api.dep import oauth2_scheme

router = APIRouter()

books: dict[str, Book] = {}


@router.get("/", status_code=status.HTTP_200_OK)
def get_books(token: Annotated[str, Depends(oauth2_scheme)]):
    print(f"token: {token}")
    return books


@router.get("/{id}", status_code=status.HTTP_200_OK)
def get_book_by_id(id: UUID):
    book = books.get(str(id))
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )

    return book


@router.post("/", status_code=status.HTTP_201_CREATED)
def add_book(book_in: BookCreate):
    book = Book(
        id=str(UUID(int=len(books) + 1)),
        **book_in.dict(),
    )
    books[book.id] = book
    return Response(message="Book added successfully", data=book)


@router.put("/{id}", status_code=status.HTTP_200_OK)
def update_book(id: UUID, book_in: BookUpdate):
    book = books.get(str(id))
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )

    book.title = book_in.title
    book.pages = book_in.pages

    return Response(message="Book updated successfully", data=book)


@router.delete("/{id}")
def delete_book(id: UUID):
    book = books.get(str(id))
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )

    del books[book.id]

    return Response(message="Book deleted successfully")
