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
