from django.shortcuts import render
from django.views.generic import ListView, DetailView

from books.models import Book


class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'book_list'


class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_details.html'
    context_object_name = 'book'
    slug_field = 'uuid'
