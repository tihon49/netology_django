from django.core.paginator import Paginator
from django.shortcuts import render_to_response, redirect
from django.conf import settings
from django.urls import reverse


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    with open (settings.BUS_STATION_CSV, encoding='cp1251') as csv_file:
        reader = csv_file.readlines()

    stations_list = []
    # counter = 0
    for station in reader[1:]:
        name = station.split(',')[1].replace('"', '').replace('«', '').replace('»', '')
        street = station.split(',')[5]
        district = station.split(',')[7]
        stations_list.append({'Name': name,
                              'Street': street,
                              'District': district})

    paginator = Paginator(stations_list, 10)
    current_page = int(request.GET.get('page', 1))
    page_object = paginator.get_page(current_page)
    prev_page, next_page = None, None

    if page_object.has_next():
        next_page = f'?page={page_object.next_page_number()}'
    if page_object.has_previous():
        prev_page = f'?page={page_object.previous_page_number()}'

    return render_to_response('index.html', context={
        'bus_stations': page_object,
        'current_page': current_page,
        'prev_page_url': prev_page,
        'next_page_url': next_page,
    })

