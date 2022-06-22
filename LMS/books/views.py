from django.shortcuts import render
from django.views.generic.base import View
from books.forms import BookForm
from books.models import *
from django.shortcuts import redirect
from django.urls import reverse


class studentView (View):
    def get(self, request):
        booklist = Book.objects.all()
        print(booklist)
        return render(request, "books/booklist.html", context= {'booklist': booklist})
    
    

class Add_book(View):
    def get(self, request):
        booklist= Book.objects.all()
        print(booklist)
        return render(request, "books/Add_book.html", context= {'booklist': booklist})
        
    def post(self, request):
       
            Mybook = BookForm(request.POST) 
            if Mybook.is_valid():
                Mybook.save()
                return redirect(reverse('books:studentView'))
            else:
                print(Mybook.errors)
            return render(request, "books/Add_book.html", context= { })


class update_book(View):
    def get(self, request,id):
        book_obj = Book.objects.get(pk=id)
        booklist= Book.objects.all()
        return render(request, "books/update_book.html", context= {'book_obj' : book_obj, 'booklist' : booklist})
    
    def post(self, request,id):
        obj = Book.objects.get(pk=id)
        Mybook = BookForm(request.POST, instance=obj)
        if Mybook.is_valid():
            Mybook.save()
            return redirect(reverse('books:studentView'))
          
        else:    
            print(Mybook.errors)
        return redirect(reverse('Users:userView'))

class delete_book(View):
    def get(self, request, id):
        obj = Book.objects.get(pk=id)
        obj.delete()
        return redirect(reverse('books:studentView'))
    
