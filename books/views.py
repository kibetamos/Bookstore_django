from django.shortcuts import render
from django.views.generic import ListView
from .models import Book, Book
# Create your views here.

class BookListView(ListView):
  model = Book
  context_object_name = 'book_list'
  template_name = 'book/list.html'
  
  