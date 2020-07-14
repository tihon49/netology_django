from django.urls import path
from django.http import HttpResponseRedirect

from .views import table_view



urlpatterns = [
    path('table/', table_view),
    path('', lambda request: HttpResponseRedirect('/table/')),
]