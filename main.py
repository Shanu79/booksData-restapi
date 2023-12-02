from fastapi import FastAPI
from routes.routes import book
app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Hello World"}

app.include_router(book)

# with open('booksData.json', 'r') as f:
#     data=json.load(f)


