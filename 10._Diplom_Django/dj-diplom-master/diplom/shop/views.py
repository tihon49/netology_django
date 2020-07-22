from django.shortcuts import render
from shop.models import Phone, SummerWear



def base_view(request):
	phones = Phone.objects.all()
	summer_wear = SummerWear.objects.all()
	context = {'phones': phones,
			   'summer_wear': summer_wear}
	return render(request, 'shop/index.html', context)


def phone_view(request):
	return render(request, 'shop/phone.html')