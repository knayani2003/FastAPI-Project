# FastAPI Blog API

A robust RESTful API built with FastAPI for managing blog posts with user authentication and PostgreSQL database integration.

## Features

- **User Authentication** using JWT (JSON Web Tokens)
- **Blog Management** - Create, Read, Update, Delete (CRUD) operations
- **PostgreSQL Database** integration using SQLAlchemy ORM
- **Password Hashing** for secure user data storage
- **Interactive API Documentation** using Swagger UI
- **Type Hints** and **Pydantic Models** for request/response validation

## Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- PassLib
- Python-Jose (JWT)
- Uvicorn

## Prerequisites

- Python 3.7+
- PostgreSQL
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/knayani2003/fastapi-blog-api.git
cd fastapi-blog-api
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure the database:
   - Create a PostgreSQL database
   - Update the database URL in `database.py`

## Running the Application

1. Start the server:
```bash
uvicorn main:app --reload
```

2. Access the API documentation:
   - Swagger UI: `http://localhost:8000/docs`
   - ReDoc: `http://localhost:8000/redoc`

## API Endpoints

### Authentication
- `POST /login/` - User login
- `POST /user/` - Create new user

### User Operations
- `GET /user/` - Get user profile
- `GET /user/blogs` - Get all blogs by user

### Blog Operations
- `POST /blog/` - Create new blog
- `GET /blog/{id}` - Get blog by ID
- `PUT /blog/{id}` - Update blog
- `DELETE /blog/{id}` - Delete blog

## Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
