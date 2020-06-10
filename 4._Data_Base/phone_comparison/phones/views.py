from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    context = {'phones': Phone.objects.all()}
    return render(
        request,
        template,
        context
    )
