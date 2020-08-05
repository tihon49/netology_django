from pprint import pprint

from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from shop.models import Item, Category
from .models import Order, ItemInOrder, Status



def add_item_to_cart(request, item_id, user):
    '''добавление товара в заказ'''
    item = Item.objects.get(id=item_id)
    user_object = User.objects.get(username=user)

    try:
        current_order = Order.objects.get(user=user_object, is_active=True)
    except: #если заказа нет, то создаем
        current_order = Order.objects.create(user=user_object, is_active=True)

    #проверим наличие данного товара в заказе, если есть то увеличим его кол-во += 1
    try:
        current_item = ItemInOrder.objects.get(order=current_order, item=item)
        current_item.count += 1
        current_item.save()
    except:
        ItemInOrder.objects.create(order=current_order, item=item)

    return redirect('base_view')



def cart_view(request, user_name):
    '''Отображение корзины конкретного полтзователя'''
    template = 'shop/cart.html'
    current_user = User.objects.get(username=user_name)

    try:
        order = Order.objects.get(user=current_user, is_active=True)
        all_items_in_order = ItemInOrder.objects.filter(order=order)
        context = {'cart_items': all_items_in_order,
                   'cart_order': order,
                   'categories': Category.objects.all()}
    except:
        context = {'empty_cart': True}

    return render(request, template, context)



def confirm_order(request, order_id):
    '''Кнопка подтверждения заказа в корзине'''
    order = Order.objects.get(id=order_id)
    order.status = Status.objects.get(name='Выполнен')
    order.is_active = False
    order.save()
    return redirect('base_view')



def not_authenticated_user(request):
    template = 'shop/not_authenticated_user.html'
    return render(request, template)