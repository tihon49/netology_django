from django.core.paginator import Paginator
from django.shortcuts import render
from books.models import Book



def home_view(request):
    template = 'books/home.html'
    return render(request, template)


def books_view(request):
    template = 'books/books_list.html'
    context = {}
    context['books'] = Book.objects.all()
    return render(request, template, context)


def date_view(request, date):
    template = 'books/book.html'
    context = {}

    for book in  Book.objects.all():
        # print(f'дата: {date} # тип: {type(date)}\nдата книги: {book.pub_date} # тип: {type(book.pub_date)}/n')
        if book.pub_date == date:
            context['book'] = book
            context['books'] = Book.objects.all()
    return render(request, template, context)
