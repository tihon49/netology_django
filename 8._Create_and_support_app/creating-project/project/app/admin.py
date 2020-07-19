from django.contrib import admin
from app.models import Station, Route



@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'latitude', 'longitude']
    list_display_links = ['id', 'name']
    ordering = ['id']
    search_fields = ['name']



@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    # save_on_top = True
    pass