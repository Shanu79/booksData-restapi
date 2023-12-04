from pydantic import BaseModel, Field

class Book(BaseModel):
    bookId: str
    bookName: str=Field(...)

class BookUpdate(BaseModel):
    bookId: str
    bookName: str