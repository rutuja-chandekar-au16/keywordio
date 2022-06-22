from django.contrib import admin
from django.urls import path, include
from books.views import *

app_name= "books"

urlpatterns = [
    path('',studentView.as_view(),name="studentView"),
    path('Add-book/',Add_book.as_view(),name="Add_book"),
    path('update-book/', update_book.as_view(),name = "update_book"),
    path('update-book/<int:id>', update_book.as_view(), name = "update_book" ),
    path('delete-book/<int:id>', delete_book.as_view(), name = "delete_book" ),
    
]