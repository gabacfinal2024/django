from django import forms
from .models import Author, Book, Member, Loan


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'email']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'isbn', 'author', 'published']
        widgets = {'published': forms.DateInput(attrs={'type': 'date'})}


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'email', 'phone', 'join_date']
        widgets = {'join_date': forms.DateInput(attrs={'type': 'date'})}


class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['book', 'member', 'loan_date', 'due_date', 'return_date']
        widgets = {
            'loan_date': forms.DateInput(attrs={'type': 'date'}),
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'return_date': forms.DateInput(attrs={'type': 'date'}),
        }
