from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from schema.schemas import list_serial

from models.booksModel import Book, BookUpdate
from db.db import collection
from bson import ObjectId
book=APIRouter()

# list books
@book.get("/api/books")
async def get_books():
    gatherData=collection.find()
    # print(gatherData)
    data=list_serial(gatherData)
    # print(data)
    return data

#post books
def is_book_uniqueName(book: Book):
    existing_bookName=collection.find_one({"bookName": book.bookName})
    return existing_bookName is None

def is_book_uniqueId(book: Book):
    existing_bookId=collection.find_one({"bookId": book.bookId})
    return existing_bookId is None

@book.post("/api/books")
async def add_book(request: Request, book: Book = Body(...)):
    try:
        if is_book_uniqueId(book): #handleing duplicate entries of book with same id
            if is_book_uniqueName(book): #handleing duplicate entries of book with same name
                result=collection.insert_one(dict(book))
                return{"status": "Book added", "book_id": str(result.inserted_id)}
        else:
            return{"status": "Book already exists"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


#put books
@book.put("/api/books/{id}")
async def put_books(id, book: Book):
    collection.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(book)
    })
