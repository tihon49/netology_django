from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View


def ckeditor_view(request):
    template = 'app/calc.html'
    context = {}

    return render(request, template, context)


class HomeView(View):
    def get(self, request):
        template = 'app/base.html'
        return render(request, template)