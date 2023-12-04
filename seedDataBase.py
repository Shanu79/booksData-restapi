import json
from db.db import collection

def load_data_from_json(file_path):
    with open(file_path, 'r') as file:
        data=json.load(file)
    return data

def seed_db():
    collection.drop() # drop existing data

    path='booksData.json'
    data=load_data_from_json(path)

    collection.insert_many(data)

    print("Seeded database successfully")