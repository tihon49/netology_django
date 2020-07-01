import json
import os
from pprint import pprint

from django.core.management.base import BaseCommand
from app.models import Car, Review
from car_admin import settings



class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open(os.path.join(settings.BASE_DIR, 'app.json'), encoding='utf-8') as file:
            reader = json.load(file)

            for i in reader:
                if i['model']  == 'app.review':
                    new_review = Review(car = Car.objects.get(id = i['fields']['car']),
                                        title = i['fields']['title'],
                                        text = i['fields']['text'])
                    new_review.save()