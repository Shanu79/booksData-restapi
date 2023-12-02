from pydantic import BaseModel

class Book(BaseModel):
    bookId: int
    bookName: str