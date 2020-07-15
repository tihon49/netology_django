from django.contrib import admin
from app.models import Station, Route



@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    # save_on_top = True
    pass



@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    # save_on_top = True
    pass