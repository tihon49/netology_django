from pprint import pprint

from django.shortcuts import render



def inflation_view(request):
    template_name = 'inflation.html'

    # чтение csv-файла и заполнение контекста
    context = {}
    with open('inflation_russia.csv', encoding='utf-8') as csv_file:
        data = csv_file.readlines()
        title = data[0]
        title = title.split(";")
        body = data[1:]
        body = [i.split(';') for i in body]

        context['title'] = title
        context['body'] = body

    return render(request, f'app/{template_name}',
                  context)