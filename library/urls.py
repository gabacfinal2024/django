from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('', views.home, name='home'),
    # Authors
    path('authors/', views.AuthorList.as_view(), name='author_list'),
    path('authors/create/', views.author_create, name='author_create'),
    path('authors/<int:pk>/delete/', views.author_delete, name='author_delete'),
    # Books
    path('books/', views.BookList.as_view(), name='book_list'),
    path('books/create/', views.book_create, name='book_create'),
    path('books/<int:pk>/delete/', views.book_delete, name='book_delete'),
    # Members
    path('members/', views.MemberList.as_view(), name='member_list'),
    path('members/create/', views.member_create, name='member_create'),
    path('members/<int:pk>/delete/', views.member_delete, name='member_delete'),
    # Loans
    path('loans/', views.LoanList.as_view(), name='loan_list'),
    path('loans/create/', views.loan_create, name='loan_create'),
    path('loans/<int:pk>/delete/', views.loan_delete, name='loan_delete'),
]
