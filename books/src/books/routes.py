from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from typing import List

from src.books.books_data import books
from src.books.schemas import BookUpdateModel, Book

book_router = APIRouter()

"""
Get all books
"""
@book_router.get("/", response_model=List[Book])
async def get_all_books():
    return books
 
"""
Create new books
"""
@book_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_books(book_data: Book) -> dict:
    new_book = book_data.model_dump()
    books.append(new_book)

    return new_book
 
"""
Get book by id
"""
@book_router.get("/{book_id}")
async def get_book(book_id: int) -> dict:
    for book in books:
        if book['id'] == book_id:
            return book
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                        detail="Book not found")

"""
Update book resource
"""
@book_router.patch("/{book_id}")
async def update_book(book_id: int, book_update_data:BookUpdateModel) -> dict:
    for book in books:
        if book['id'] == book_id:
            book['title'] = book_update_data.title
            book['author'] = book_update_data.author
            book['publisher'] = book_update_data.publisher
            book['page_count'] = book_update_data.page_count
            book['language'] = book_update_data.language

            return book

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                        detail="Book not found")

"""
Delete book resource
"""
@book_router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int) -> None:
    for book in books:
        if book['id'] == book_id:
            books.remove(book)

            return
            
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                        detail="Book not found")
