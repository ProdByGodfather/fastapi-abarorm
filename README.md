# FastAPI & AbarORM

This project is a simple API for managing categories and posts using FastAPI and AbarORM. AbarORM is a lightweight and efficient ORM for SQLite that makes database interaction easy.

## Features

- Manage categories and posts
- Use AbarORM for SQLite database interaction
- Quick and easy API implementation with FastAPI

## Installation

To install and set up this project, follow these steps:

1. **Clone the Repository**

   ```bash
   git clone fastapi-abarorm
   cd fastapi-abarorm
   ```
2. **Install Dependencies**
   Use pip to install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Application**
   To run the application, execute the following command:
   ```bash
   python main.py
   ```

## Usage
Once the application is running, you can access the API at [`http://localhost:8000/docs`](http:localhost:8000/docs).

## Endpoints
- Categories
   - `GET /categories/` - List all categories
   - `POST /categories/` - Create a new category
   - `GET /categories/{id}/` - Get details of a specific category
   - `PUT /categories/{id}/` - Update a category
   - `DELETE /categories/{id}/` - Delete a category
- Posts
   - `GET /posts/` - List all Posts
   - `POST /posts/` - Create a new Posts
   - `GET /posts/{id}/` - Get details of a specific Posts
   - `PUT /posts/{id}/` - Update a Posts
   - `DELETE /posts/{id}/` - Delete a Posts

## Notes
- Ensure that SQLite is installed on your system.
- To create the database, simply run the application once, and AbarORM will automatically create the database.

## Contribution
If you would like to contribute to this project, we welcome your feedback and suggestions!