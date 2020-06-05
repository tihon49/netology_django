from pprint import pprint
import csv
from django.shortcuts import render



def str_to_float(lst):
    '''
    :param lst: get a list
    :return: str items => float items
    '''
    lists_list = []
    for i in lst:
        dig_list = []
        for j in i:
            try:
                if j > 1000:
                    j = float(j)
            except:
                pass
            dig_list.append(j)
        lists_list.append(dig_list)
    return lists_list



def inflation_view(request):
    template_name = 'inflation.html'

    # чтение csv-файла и заполнение контекста
    context = {}
    with open('inflation_russia.csv', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        data = str_to_float(reader)

    context['title'] = data[0]
    context['body'] = data[1:]

    return render(request, f'app/{template_name}',
                  context)