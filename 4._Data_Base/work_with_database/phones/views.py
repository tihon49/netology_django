from django.shortcuts import render

from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    context = {}
    context['response'] = []

    for p in Phone.objects.all():
        context['response'].append(p)

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {
        'name': Phone.name,
    }
    return render(request, template, context)



# TODO: реализовать что-то похожее:
'''
def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    if request.GET.get('from-landing') == 'original':
        counter_click['original'] += 1
        print(counter_click)
    elif request.GET.get('from-landing') == 'test':
        counter_click['test'] += 1
        print(counter_click)
    return render_to_response('index.html')
'''