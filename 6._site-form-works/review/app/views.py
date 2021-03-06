from pprint import pprint

from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from .models import Product, Review
from .forms import ReviewForm


def product_list_view(request):
    template = 'app/product_list.html'
    products = Product.objects.all()

    context = {
        'product_list': products,
    }

    return render(request, template, context)


def product_view(request, pk):
    template = 'app/product_detail.html'
    product = get_object_or_404(Product, id=pk)
    form = ReviewForm
    product_review_list = []

    for i in Review.objects.select_related('product'):
        if str(i.product.name) == str(Product.objects.all().get(name=product)):
            product_review_list.append(i.text)

    if 'commited' not in request.session:
        request.session['commited'] = []

    context = {
        'form': form,
        'product': product,
        'product_review': product_review_list,
    }

    if request.method == 'GET':
        if product.id in request.session['commited']:
            context['is_review_exist'] = True

        return render(request, template, context)

    if request.method == 'POST':
        # логика для добавления отзыва
        if product.id not in request.session['commited']:
            review = Review()
            form = ReviewForm(request.POST)

            if form.is_valid():
                review.product = product
                review.text = form.cleaned_data.get("text")
                review.save()
                request.session['commited'].append(product.id)
                request.session.save()

        return redirect(request.path)
