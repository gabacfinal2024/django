from django.contrib import admin
from .models import Author, Book, Member, Loan


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'isbn', 'author', 'published')
    list_filter = ('author',)


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'join_date')


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'member', 'loan_date', 'due_date', 'return_date')
    list_filter = ('loan_date',)
