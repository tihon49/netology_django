from django.shortcuts import render
from phones.models import Phone



def show_catalog(request):
    template = 'catalog.html'
    context = {}
    context['response'] = []

    for p in Phone.objects.all():
        context['response'].append(p)

    if request.GET.get('sort') == 'name':
        context['response'] = Phone.objects.order_by('name')

    elif request.GET.get('sort') == 'cheap':
        context['response'] = Phone.objects.order_by('price')

    elif request.GET.get('sort') == 'expensive':
        context['response'] = Phone.objects.order_by('-price')

    return render(request, template, context)



def show_product(request, slug):
    template = 'product.html'

    for phone in Phone.objects.all():
        if phone.slug == slug:
            description = f'Some info about the current phone: {phone.name}'
            context = {'name': phone.name,
                       'price': phone.price,
                       'description': description,
                       'image': phone.image,
                       'release_date': phone.release_date,
                       'lte_exists': phone.lte_exists,
                       'slug': phone.slug
                       }

    return render(request, template, context)
