from typing_extensions import Optional
from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from starlette import status

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    published_date: int
    rating: int

    def __init__(self, id: int, title: str, author: str, description: str, published_date: int, rating: int):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.published_date: int = published_date
        self.rating = rating
        
        
class BookRequest(BaseModel):
    id: Optional[int] = Field(description="ID is not needed on create", default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    published_date: int = Field(ge=0, le=2035)
    rating: int = Field(gt=0, lt=6)
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "A New Book",
                "author": "TechThorDev",
                "description": "A new description of a book",
                "published_date": 2009,
                "rating": 5
            }
        }
    }


BOOKS = [
    Book(1, 'Computer Science Pro', 'codingwithroby', 'A very nice book', 2030, 5),
    Book(2, 'Be Fast with FastAPI', 'codingwithroby', 'A great book', 2009, 5),
    Book(3, 'Master Endpoints', 'codingwithroby', 'A awesome book', 2028, 5),
    Book(4, 'HP1', 'Author 1', 'Book Description', 2027, 2),
    Book(5, 'HP2', 'Author 2', 'Book Description', 2025, 3),
    Book(6, 'HP3', 'Author 3', 'Book Description', 2026, 1)
]


@app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOKS
    

@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def read_book(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Item not found")


@app.get("/books/publish/", status_code=status.HTTP_200_OK)
async def read_book_by_published_date(published_date: int = Query(ge=0, le=2035)):
    books_to_return = []
    for book in BOOKS:
        if book.published_date == published_date:
            books_to_return.append(book)
    return books_to_return


@app.get("/books/", status_code=status.HTTP_200_OK) 
async def read_book_by_rating(book_rating: int = Query(gt=0, lt=6)):
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return


@app.post("/create-book", status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))


def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book


@app.put("/books/update-book/", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            book_changed = True
        if not book_changed:
            raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt=0)):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            book_changed = True
            break
        if not book_changed:
            raise HTTPException(status_code=404, detail="Item not found")
