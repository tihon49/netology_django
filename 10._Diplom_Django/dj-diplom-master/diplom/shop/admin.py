from django.contrib import admin

from shop.models import Phone, SummerWear, Review



@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'id']
    list_display_links = ['id', 'name']
    list_filter = ['name', 'price']
    search_fields = ('name', 'price')



# TODO: переделать на отдельную модель
@admin.register(SummerWear)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'id']
    list_display_links = ['id', 'name']
    list_filter = ['name', 'price']
    search_fields = ('name', 'price')



@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass
    list_display = ['id', 'phone', 'star', 'session_id', 'name']
    list_display_links = ['id', 'phone', 'session_id', 'star', 'name']
    list_filter = ['phone', 'star', 'session_id', 'name']
    search_fields = ('name', 'session_id', 'phone')