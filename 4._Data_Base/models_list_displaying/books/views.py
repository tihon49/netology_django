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
    # paginator = Paginator(list(Book.objects.order_by('pub_date')), 1)
    # page_object = paginator.get_page(date)
    # print(f'page_object: {page_object}')
    context = {}

    # if page_object.has_next():
    #     next_page = page_object.next_page_number()
    #     context['next_page'] = next_page
    # if page_object.has_previous():
    #     prev_page = page_object.previous_page_number()
    #     context['prev_page'] = prev_page

    for book in  Book.objects.all():
        # print(f'дата: {date} # тип: {type(date)}\nдата книги: {book.pub_date} # тип: {type(book.pub_date)}/n')
        if book.pub_date == date:
            context['book'] = book
            context['books'] = Book.objects.all()
    return render(request, template, context)
