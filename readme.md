# Library System API using FastAPI

## Overview

This is a simple RESTful API built with FastAPI to manage a library system. It provides endpoints for basic CRUD operations on books.

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn

## Installation

1. Clone the repository:

    bash
    git clone 
    cd restapi-letsbloom
    

2. Create a virtual environment:

    bash
    python -m venv venv
    

3. Activate the virtual environment:

    - On Windows:

        bash
        venv\Scripts\activate
        

    - On Unix or MacOS:

        bash
        source venv/bin/activate
        

4. Install dependencies:

    bash
    pip install -r requirements.txt
    

## Database Setup

1. Make sure you have a running PostgreSQL server.

2. Create a database and update the database URI in main.py:

    python
    DATABASE_URI = "postgresql://username:password@localhost/library_db"
    

## Running the Application

1. Start the Uvicorn server:

    bash
    uvicorn main:app --reload
    

2. The API will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## API Endpoints

- *Retrieve All Books:* [http://127.0.0.1:8000/books](http://127.0.0.1:8000/books) (GET)

## Documentation

Access the Swagger documentation at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) and explore the API endpoints.

## Contributing

Feel free to contribute by submitting issues or pull requests.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to customize this README based on your specific project structure and requirements.