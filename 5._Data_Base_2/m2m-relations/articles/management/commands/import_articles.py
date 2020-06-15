import json
from pprint import pprint

from django.core.management.base import BaseCommand
from articles.models import Article
from website import settings



class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open(settings.ARTICLES, encoding='utf-8') as file:
            reader = json.load(file)

            for article in reader:
                new_article = Article(title = article['fields']['title'],
                                      text = article['fields']['text'],
                                      published_at = article['fields']['published_at'],
                                      image = article['fields']['image'])
                new_article.save()