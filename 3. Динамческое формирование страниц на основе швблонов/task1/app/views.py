from pprint import pprint

from django.shortcuts import render

def inflation_view(request):
    template_name = 'inflation.html'

    # чтение csv-файла и заполнение контекста
    context = {}
    with open('inflation_russia.csv', encoding='utf-8') as csv_file:
        data = csv_file.readlines()
        context['data'] = []

        for line in data:
            line = [i for i in line.split(';')]
            context['data'].append(line)



    return render(request, f'app/{template_name}',
                  context)