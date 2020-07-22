from django.contrib import admin

from shop.models import Phone, SummerWear



@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    pass


@admin.register(SummerWear)
class PhoneAdmin(admin.ModelAdmin):
    pass