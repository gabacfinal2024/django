from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Author, Book, Member, Loan
from .serializers import AuthorSerializer


from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages

from .forms import AuthorForm, BookForm, MemberForm, LoanForm


@api_view(['GET', 'POST'])
def author_list(request):

    if request.method == 'GET':
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def home(request):
    return render(request, 'library/home.html')


# ----- Authors -----
class AuthorList(ListView):
    model = Author
    context_object_name = 'authors'
    template_name = 'library/author_list.html'


def author_create(request):
    form = AuthorForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Author created.')
        return redirect('library:author_list')
    return render(request, 'library/author_form.html', {'form': form, 'title': 'Add Author'})


def author_delete(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        author.delete()
        messages.success(request, 'Author deleted.')
        return redirect('library:author_list')
    return render(request, 'library/confirm_delete.html', {'object': author, 'cancel_url': 'library:author_list'})


# ----- Books -----
class BookList(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'library/book_list.html'


def book_create(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Book created.')
        return redirect('library:book_list')
    return render(request, 'library/book_form.html', {'form': form, 'title': 'Add Book'})


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        messages.success(request, 'Book deleted.')
        return redirect('library:book_list')
    return render(request, 'library/confirm_delete.html', {'object': book, 'cancel_url': 'library:book_list'})


# ----- Members -----
class MemberList(ListView):
    model = Member
    context_object_name = 'members'
    template_name = 'library/member_list.html'


def member_create(request):
    form = MemberForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Member created.')
        return redirect('library:member_list')
    return render(request, 'library/member_form.html', {'form': form, 'title': 'Add Member'})


def member_delete(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        member.delete()
        messages.success(request, 'Member deleted.')
        return redirect('library:member_list')
    return render(request, 'library/confirm_delete.html', {'object': member, 'cancel_url': 'library:member_list'})


# ----- Loans -----
class LoanList(ListView):
    model = Loan
    context_object_name = 'loans'
    template_name = 'library/loan_list.html'


def loan_create(request):
    form = LoanForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Loan created.')
        return redirect('library:loan_list')
    return render(request, 'library/loan_form.html', {'form': form, 'title': 'Add Loan'})


def loan_delete(request, pk):
    loan = get_object_or_404(Loan, pk=pk)
    if request.method == 'POST':
        loan.delete()
        messages.success(request, 'Loan deleted.')
        return redirect('library:loan_list')
    return render(request, 'library/confirm_delete.html', {'object': loan, 'cancel_url': 'library:loan_list'})
