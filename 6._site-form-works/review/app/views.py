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

    context = {
        'form': form,
        'product': product,
        'product_review': product_review_list
    }

    if request.method == 'GET':
        return render(request, template, context)

    if request.method == 'POST':
        # логика для добавления отзыва
        review = Review()
        form = ReviewForm(request.POST)
        if form.is_valid():
            review.product = product
            review.text = form.cleaned_data.get("text")
            review.save()
        return redirect('main_page')
