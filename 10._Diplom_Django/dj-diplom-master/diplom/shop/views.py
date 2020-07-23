from django.shortcuts import render, get_object_or_404, redirect
from shop.models import Phone, SummerWear, Review
from shop.forms import ReviewForm



def base_view(request):
	'''главная страница'''
	phones = Phone.objects.all()
	summer_wear = SummerWear.objects.all()
	context = {'phones': phones,
			   'summer_wear': summer_wear}
	return render(request, 'shop/index.html', context)


def phone_view(request, item_id):
	'''обзор телефона'''
	user_session = request.session.session_key
	if not user_session:
		request.session.cycle_key()
		user_session = request.session.session_key

	phone = get_object_or_404(Phone, id=item_id)
	form = ReviewForm()
	context = {'phone': phone}
	context['form'] = form
	context['user_session'] = user_session
	print('GET запрос:', request.session.session_key)

	for review in phone.reviews.all():
		if review.session_id == user_session:
			context['reviewd'] = True
			break


	# добавление комментария
	if request.method == 'POST':
		form = ReviewForm(request.POST)
		if form.is_valid:
			print('form is valid')
			print(request.POST)
			Review.objects.create(phone = Phone.objects.get(id=item_id),
								  name = request.POST.get('name'),
								  text = request.POST.get('text'),
								  star = request.POST.get('stars'),
								  session_id = user_session
								  )
			return redirect('phone_view', item_id=item_id)
	return render(request, 'shop/phone.html', context)


def empty_view(request):
	'''пустая страница'''
	template = 'shop/empty_section.html'
	return render(request, template)
