from django.contrib import admin
from table.models import Table, CSVFile


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'width', 'number')
    list_display_links = ('id', 'name')
    list_filter = ['name', 'width', 'number']



class CSVFileAdmin(admin.ModelAdmin):
    pass

admin.site.register(CSVFile, CSVFileAdmin)