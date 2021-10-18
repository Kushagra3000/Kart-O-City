from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.product import Product


	
def search_products(request):
	if request.method == "POST":
		searched = request.POST['searched']
		products = Product.objects.filter(name__contains=searched)
		
		return render(request, 'search_product.html', {'products':products,'searched':searched})
	else:
		return render(request, 'search_product.html', {})

