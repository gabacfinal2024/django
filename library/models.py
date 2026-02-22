"""
Library models matching the ERD: Author, Book, Member, Loan.
"""
from django.db import models


class Author(models.Model):
    """Author of books. PK: author_id."""
    name = models.CharField(max_length=200)
    email = models.EmailField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Book(models.Model):
    """Book. PK: book_id, FK to Author."""
    title = models.CharField(max_length=300)
    isbn = models.CharField(max_length=20, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    published = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Member(models.Model):
    """Library member. PK: member_id."""
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    join_date = models.DateField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Loan(models.Model):
    """Book loan. PK: loan_id, FK to Book and Member."""
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='loans')
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='loans')
    loan_date = models.DateField()
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['-loan_date']

    def __str__(self):
        return f"{self.book.title} → {self.member.name}"
