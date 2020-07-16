from django.shortcuts import render
from django.views.generic import View

from app.models import Station, Route


class StationsView(View):
    def get(self, request):
        context = {}
        routes = Route.objects.all()
        context['routes'] = routes      #все маршруты
        route_number = request.GET['route']     #номер выбранного маршрута
        current_route = Route.objects.get(name=route_number)    #объект выбранного маршрута
        stations = current_route.stations.all()     #список объектов станций на данном маршруте
        context['stations'] = stations
        context['center'] = {
            'x': 55.72498684,
            'y': 37.6532731
        }
        return render(request, 'stations.html', context)