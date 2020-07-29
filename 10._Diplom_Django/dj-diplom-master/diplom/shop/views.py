from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Item, Review, Category
from .forms import ReviewForm, CreateUserForm



def base_view(request):
	'''главная страница'''
	phones = Item.objects.filter(category=1)
	wear = Item.objects.filter(category=2)
	categories = Category.objects.all()
	context = {'phones': phones,
			   'wear': wear,
			   'categories': categories}
	return render(request, 'shop/index.html', context)



def item_view(request, item_id):
	'''страница обзора выбранного товара'''
	user_session = request.session.session_key
	if not user_session:
		request.session.cycle_key()
		user_session = request.session.session_key

	item = get_object_or_404(Item, id=item_id)
	form = ReviewForm() # форма добавления комментария из forms.py
	context = {'item': item}
	context['form'] = form
	context['user_session'] = user_session
	print('GET запрос:', request.session.session_key)

	# отображение отзывов, если они есть
	for review in item.reviews.all():
		if review.session_id == user_session:
			context['reviewd'] = True
			break

	# добавление комментария
	if request.method == 'POST':
		# костыль обойти ошибку при отзыве
		# без выбора количества звезд
		if request.POST.get('stars'):
			form = ReviewForm(request.POST)
			if form.is_valid:
				print('form is valid')
				print(request.POST)
				Review.objects.create(item = Item.objects.get(id=item_id),
									  name = request.POST.get('name'),
									  text = request.POST.get('text'),
									  star = request.POST.get('stars'),
									  session_id = user_session
									  )
				return redirect('item_view', item_id=item_id)
		else:
			pass
	return render(request, 'shop/item.html', context)



def registration_view(request):
	'''страница регистрации аккаунта'''
	template = 'shop/registration.html'
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, 'Создан аккаунт пользователя ' + user)
			return redirect('login')

	context = {'form': form}
	return render(request, template, context)



def login_view(request):
	'''страница авторизации'''
	template = 'shop/login.html'
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username = username, password = password)
		if user is not None:
			login(request, user)
			return redirect('base_view')
		else:
			messages.info(request, 'Логин или пароль не корректны...')

	return render(request, template)



def logout_view(request):
	logout(request)
	return redirect('login')



def empty_view(request):
	'''пустая страница'''
	template = 'shop/empty_section.html'
	return render(request, template)
