import json
from django.core.management.base import BaseCommand
from books.models import Book
from main import settings



class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open(settings.BOOKS, encoding='utf-8') as file:
            reader = json.load(file)

            for book in reader:
                new_book = Book(name = book['fields']['name'],
                                author = book['fields']['author'],
                                pub_date = book['fields']['pub_date'])
                new_book.save()