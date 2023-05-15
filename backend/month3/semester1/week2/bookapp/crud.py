from schemas import BookCreate, BookUpdate, Book
from fastapi.encoders import jsonable_encoder
from database import BookDB
from bson.objectid import ObjectId


class CRUDService:
    def create_book(self, book_in: BookCreate):
        book_in_data = jsonable_encoder(book_in)
        book_id = BookDB.books.insert_one(book_in_data).inserted_id
        return str(book_id)

    def get_all_books(self):
        books = BookDB.books.find()  # This returns a cursor
        book_list = []
        for book in books:
            id = str(book.get("_id"))  # Convert ObjectId to string
            book_list.append(Book(id=id, **book))

        return book_list

    def get_book_by_id(self, book_id: str):
        book = BookDB.books.find_one({"_id": ObjectId(book_id)})
        if book:
            id = str(book.get("_id"))
            return Book(id=id, **book)

        return None

    def update_book(self, book_id: str, book_update_in: BookUpdate):
        book_update_data = book_update_in.dict(exclude_unset=True)
        BookDB.books.find_one_and_update(
            {"_id": ObjectId(book_id)}, {"$set": book_update_data}, return_document=True
        )
        return None

    def delete_book(self, book_id):
        BookDB.books.find_one_and_delete({"_id": ObjectId(book_id)})

        return None


crud_service = CRUDService()
