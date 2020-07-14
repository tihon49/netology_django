import csv
import os

from django.shortcuts import render

from app import settings
from table.models import CSVFile, Table



def table_view(request):
    template = 'table.html'
    path = str(CSVFile.objects.first().get_path()).split('\\')[-1]
    columns = Table.objects.order_by('number')

    with open(os.path.join(settings.BASE_DIR, path), 'rt') as csv_file:
        header = []
        table = []
        table_reader = csv.reader(csv_file, delimiter=';')
        for table_row in table_reader:
            if not header:
                header = {idx: value for idx, value in enumerate(table_row)}
            else:
                row = {header.get(idx) or 'col{:03d}'.format(idx): value
                       for idx, value in enumerate(table_row)}
                table.append(row)

        context = {
            'columns': columns,
            'table': table, 
            'csv_file': path
        }

    return render(request, template, context)
