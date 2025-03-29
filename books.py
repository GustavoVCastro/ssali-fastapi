from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

"""
/books GET
/books POST
/book/{book_id} PATCH
/book/{book_id} DELETE
"""

books = [
    {
        "id": 1,
        "title": "Think Python",
        "author": "Allen B. Downey",
        "publisher": "O'Reilly Media",
        "published_data": "2021-01-01",
        "page_count": 1234,
        "language": "English",
    },
    {
        "id": 2,
        "title": "Think Python",
        "author": "Allen B. Downey",
        "publisher": "O'Reilly Media",
        "published_data": "2021-01-01",
        "page_count": 1234,
        "language": "English",
    },
    {
        "id": 3,
        "title": "Think Python",
        "author": "Allen B. Downey",
        "publisher": "O'Reilly Media",
        "published_data": "2021-01-01",
        "page_count": 1234,
        "language": "English",
    },
    {
        "id": 4,
        "title": "Think Python",
        "author": "Allen B. Downey",
        "publisher": "O'Reilly Media",
        "published_data": "2021-01-01",
        "page_count": 1234,
        "language": "English",
    },
    {
        "id": 5,
        "title": "Think Python",
        "author": "Allen B. Downey",
        "publisher": "O'Reilly Media",
        "published_data": "2021-01-01",
        "page_count": 1234,
        "language": "English",
    },
]

class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_data: str
    page_count: int
    language: str


"""
Get all books
"""
@app.get("/books", response_model=Book)
async def get_all_books() -> list:
    return books
 
"""
Create new books
"""
@app.post("/books")
async def create_books() -> dict:
    pass
 
"""
Update book resource
"""
@app.patch("/books/{book_id}")
async def get_book(book_id: int) -> dict:
    pass

"""
Delete book resource
"""
@app.patch("/books/{book_id}")
async def delete_book(book_id: int) -> dict:
    pass
