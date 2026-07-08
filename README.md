# Bookstore REST API

A RESTful API built using **Django** and **Django REST Framework** that allows users to perform CRUD (Create, Read, Update, Delete) operations on a bookstore database.

The API also supports:

- CRUD operations
- Search by title and author
- Pagination
- Input validation
- ISBN uniqueness

---

# Project Overview

This project provides a REST API for managing books in a bookstore.

Each book contains:

- Title
- Author
- Price
- ISBN
- Published Date

The API is built using Django REST Framework's `ModelViewSet`, making it easy to perform all CRUD operations through REST endpoints.

---

# Technologies Used

- Python 3
- Django
- Django REST Framework (DRF)
- SQLite
- django-filter

---

# Features

- Create new books
- Retrieve all books
- Retrieve a single book
- Update book details
- Delete books
- Search books by title
- Search books by author
- Pagination (5 books per page)
- Serializer validation
- Unique ISBN enforcement

---

# Validation Rules

The API validates the following before saving data:

- Price must be greater than **0**
- ISBN must contain **exactly 13 digits**
- ISBN must be unique
- Published date cannot be a future date

---

# Installation

## 1. Clone the repository

```bash
git clone <repository-url>
```

```bash
cd BookstoreAPI
```

---

## 2. Create a virtual environment

Windows

```bash
python -m venv env
```

Activate

```bash
env\Scripts\activate
```

Linux/macOS

```bash
python3 -m venv env
source env/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

If you don't have a requirements file:

```bash
pip install django djangorestframework django-filter
```

---

## 4. Apply migrations

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

---

## 5. Run the server

```bash
python manage.py runserver
```

The API will be available at:

```
http://127.0.0.1:8000/
```

---

# API Endpoints

Base URL

```
http://127.0.0.1:8000/books/
```

---

## 1. Get All Books

**GET**

```
/books/
```

### Example Request

```
GET /books/
```

### Example Response

```json
{
  "count": 12,
  "next": "http://127.0.0.1:8000/books/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "The Great Gatsby",
      "author": "F. Scott Fitzgerald",
      "price": "12.99",
      "isbn": "9780743273565",
      "published_date": "1925-04-10"
    }
  ]
}
```

---

## 2. Get a Single Book

**GET**

```
/books/1/
```

### Example Response

```json
{
  "id": 1,
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "price": "12.99",
  "isbn": "9780743273565",
  "published_date": "1925-04-10"
}
```

---

## 3. Create a Book

**POST**

```
/books/
```

### Sample Input

```json
{
  "title": "Clean Code",
  "author": "Robert C. Martin",
  "price": 34.99,
  "isbn": "9780132350884",
  "published_date": "2008-08-01"
}
```

### Success Response

```json
{
  "id": 13,
  "title": "Clean Code",
  "author": "Robert C. Martin",
  "price": "34.99",
  "isbn": "9780132350884",
  "published_date": "2008-08-01"
}
```

---

## 4. Update a Book

**PUT**

```
/books/13/
```

### Sample Input

```json
{
  "title": "Clean Code (Updated)",
  "author": "Robert C. Martin",
  "price": 39.99,
  "isbn": "9780132350884",
  "published_date": "2008-08-01"
}
```

### Example Response

```json
{
  "id": 13,
  "title": "Clean Code (Updated)",
  "author": "Robert C. Martin",
  "price": "39.99",
  "isbn": "9780132350884",
  "published_date": "2008-08-01"
}
```

---

## 5. Delete a Book

**DELETE**

```
/books/13/
```

### Success Response

```
HTTP 204 No Content
```

---

# Search

Search by title or author.

**GET**

```
/books/?search=clean
```

Example:

```
/books/?search=martin
```

---

# Pagination

Pagination is enabled.

Default page size:

```
5 books per page
```

To access another page:

```
/books/?page=2
```

---

# Possible Validation Errors

### Invalid Price

```json
{
  "price": ["Price must be greater than zero."]
}
```

### Invalid ISBN Length

```json
{
  "isbn": ["ISBN must contain exactly 13 digits."]
}
```

### Duplicate ISBN

```json
{
  "isbn": ["book with this isbn already exists."]
}
```

### Future Published Date

```json
{
  "published_date": ["Published date cannot be in the future."]
}
```

---

# Project Structure

```
BookstoreAPI/
│
├── BookstoreAPI/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── books/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── manage.py
├── requirements.txt
└── README.md
```

---

# Author

@Rameen
Developed as a Django REST Framework CRUD API project for learning RESTful API development.
