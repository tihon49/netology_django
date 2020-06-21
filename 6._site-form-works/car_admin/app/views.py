from django.shortcuts import render


def ckeditor_view(request):
    template = 'app/calc.html'
    context = {}

    return render(request, template, context)