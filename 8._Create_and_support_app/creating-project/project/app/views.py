from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from app.models import Station, Route

from django.db.models import Avg


class StationsView(View):
    def get(self, request):
        context = {}
        routes = Route.objects.all()
        context['routes'] = routes      #все маршруты
        route_number = request.GET.get('route')     #номер выбранного маршрута

        if route_number:
            current_route = get_object_or_404(Route, name=route_number)    #объект выбранного маршрута
            stations = current_route.stations.all()     #список объектов станций на данном маршруте
            context['stations'] = stations
            context['center'] = {
                'x': str(stations.aggregate(Avg('longitude'))['longitude__avg']).replace(',', '.'),
                'y': str(stations.aggregate(Avg('latitude'))['latitude__avg']).replace(',', '.')
            }
        # print(context['stations'])
        # print('\n', context['center'])

        return render(request, 'stations.html', context)