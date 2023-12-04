# FastAPI Book API

This is a simple FastAPI application for managing books using MongoDB.

## Prerequisites

Before running the application, make sure you have the following installed:

- Python 3.7 or higher
- MongoDB Atlas account (or a local MongoDB instance)

## Setup

1. Clone the repository:

```bash
git clone https://github.com/Shanu79/restapi-letsbloom.git
cd fastapi-book-api
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Configure MongoDB:

   - Create a MongoDB Atlas cluster or use a local MongoDB instance.
  
5. Configure the .env file:
   - create a new .env file
   - Update the `uri` variable in the `.env` file with your MongoDB connection string.
   - Update the `JSON_DATA_PATH` with your actual dummy data file is located
6. Run the application:

```bash
uvicorn main:app --reload
```

The application should now be running at [http://localhost:8000](http://localhost:8000).

## API Documentation

Visit [http://localhost:8000/docs](http://localhost:8000/docs) to access the Swagger UI for API documentation.

## Endpoints

- **GET /api/books**: List all books.

## Contributing

Feel free to contribute by opening issues or submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
