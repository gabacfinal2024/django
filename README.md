# Library System (Django)

Create, Read, and Delete for **Authors**, **Books**, **Members**, and **Loans** based on your ERD.

## Setup

```bash
cd c:\Users\acer\Downloads\django1
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
```

## Run

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/

## What’s included

- **Models:** `Author`, `Book`, `Member`, `Loan` (with FKs as in your ERD)
- **Create:** Add author, book, member, loan via forms
- **Read:** List pages for authors, books, members, loans
- **Delete:** Delete with confirmation for each entity
- **Admin:** http://127.0.0.1:8000/admin/ (create superuser with `python manage.py createsuperuser`)

## URLs

| Page    | URL              |
|---------|------------------|
| Home    | `/`              |
| Authors | `/authors/`      |
| Books   | `/books/`        |
| Members | `/members/`      |
| Loans   | `/loans/`        |

From each list you can use “Add …” and “Delete” for that entity.
