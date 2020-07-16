from django.urls import path
from django.http import HttpResponseRedirect
from app.views import StationsView



urlpatterns = [
    path('stations/', StationsView.as_view(), name='map_stations'),
    path('', lambda request: HttpResponseRedirect('/stations/')),
]