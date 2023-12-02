from fastapi import APIRouter
from schema.schemas import list_serial

from models.booksModel import Book
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
@book.post("/api/books")
async def post_books(book: Book):
    collection.insert_one(dict(book))

#put books
@book.put("/api/books/{id}")
async def put_books(id, book: Book):
    collection.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(book)
    })
