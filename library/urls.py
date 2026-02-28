


from django.urls import path
from .views import author_list
from . import views
from . import api_views

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
    # JSON API (for Thunder Client)
    path('api/authors/', api_views.api_author_list),
    path('api/authors/create/', api_views.api_author_create),
    path('api/authors/<int:pk>/delete/', api_views.api_author_delete),
    path('api/books/', api_views.api_book_list),
    path('api/books/create/', api_views.api_book_create),
    path('api/books/<int:pk>/delete/', api_views.api_book_delete),
    path('api/members/', api_views.api_member_list),
    path('api/members/create/', api_views.api_member_create),
    path('api/members/<int:pk>/delete/', api_views.api_member_delete),
    path('api/loans/', api_views.api_loan_list),
    path('api/loans/create/', api_views.api_loan_create),
    path('api/loans/<int:pk>/delete/', api_views.api_loan_delete),
]
