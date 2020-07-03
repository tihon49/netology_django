from django.contrib import admin

from .models import Car, Review
from .forms import ReviewAdminForm



class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'review_count', 'id')
    list_filter = ('brand', 'model')
    search_fields = ['brand', 'model']



class ReviewAdmin(admin.ModelAdmin):
    form = ReviewAdminForm
    list_display = ('car', 'title', 'id')
    list_filter = ('car__brand', 'car__model', 'car__id')
    search_fields = ['car__model', 'title']
    # radio_fields = {'car': admin.VERTICAL}



admin.site.register(Car, CarAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.site_title = 'Car_admin'
admin.site.site_header = 'Car administration'