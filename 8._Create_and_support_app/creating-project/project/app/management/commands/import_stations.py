import csv
import os
from pprint import pprint

from django.core.management import BaseCommand

from project import settings
from app.models import Station, Route




class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        file = 'moscow_bus_stations.csv'
        with open(os.path.join(settings.BASE_DIR, file), 'r', encoding='cp1251') as csvfile:
            station_reader = csv.reader(csvfile, delimiter=';')
            next(station_reader)
            # count = 0
            for line in station_reader:
                # count += 1
                station = Station()
                station.name = line[1]
                station.longitude = float(line[2])
                station.latitude = float(line[3])
                station.save()
                # pprint(line)
                #
                # if count >= 5:
                #     break
                #
                # station = Station.objects.get(name=line[1])
                for route in line[7].split('; '):
                    try:
                        new_route = Route.objects.get(name=route)
                    except Route.DoesNotExist:
                        new_route = Route.objects.create(name=route)

                    station.routes.add(new_route)
                print(f'доабвлена станция {station.name}')
                    # pprint(new_route)