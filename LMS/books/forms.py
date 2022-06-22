from email.policy import default
from django import forms
from books.models import Book


class BookForm(forms.ModelForm):
    book_no = forms.IntegerField()
    name = forms.CharField(max_length=200)
    Author_name = forms.CharField(max_length=200)
    
    class Meta: 
      model = Book
      fields = '__all__' 