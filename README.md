# Library Platform

A PostgreSQL-based library management system that allows tracking of books, categories, and availability.

## Features

- Book management (add, update, delete, list)
- Category management (add, update, delete, list)
- Inventory tracking (total and available copies)
- ISBN and publication date tracking

## Technologies Used

- Python 3.10
- PostgreSQL
- psycopg2 (PostgreSQL adapter for Python)
- python-dotenv (for environment variable management)

## Setup and Installation

### Prerequisites

- Python 3.10 or higher
- PostgreSQL database
- pip (Python package manager)

### Installation Steps

1. Clone the repository:
2. Set up a virtual environment:
3. Activate the virtual environment:

- On macOS/Linux:
  ```
  source env/bin/activate
  ```
- On Windows:
  ```
  env\Scripts\activate
  ```

4. Install dependencies:

```
 pip install -r requirements.txt
```

5. Create a `.env` file in the project root with your PostgreSQL connection details:

```
PGHOST=localhost
PGPORT=5432
PGDATABASE=library_db
PGUSER=your_username 
PGPASSWORD=your_password
```

6. Create the required database tables (you may need to create the database first):
```sql
CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT
);

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    isbn VARCHAR(20),
    published_date DATE,
    total_copies INTEGER NOT NULL,
    available_copies INTEGER NOT NULL,
    category_id INTEGER REFERENCES categories(id)
);
```

7. Run the application:

```python
python [main.py](http://_vscodecontentref_/1)
```

## Running Instructions

Run the application using the command:
```python
python main.py
```

## Project Structure

config.py - Database configuration and environment variables
db.py - Database connection utility
main.py - Application entry point
models/ - Data models
book.py - Book model
category.py - Category model
resources/ - CRUD operations for models
category_resource.py - Category CRUD operations

## License

The README includes:
1. Project overview
2. Features
3. Technologies used
4. Setup and installation instructions
5. Running instructions
6. Project structure overview
7. License information

You may want to add more specific details about functionality as you develop the application further.