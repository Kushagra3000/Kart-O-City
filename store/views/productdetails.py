from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.product import  Product


	
def product_details(request):
	# if request.method == "POST":
	clickedproduct = request.POST['clickedproduct']
	# 	products = Product.objects.filter(name__contains=searched)
		
	# 	return render(request, 'search_product.html', {'products':products,'searched':searched})
	# else:
	# context = {}
	# clickedproduct = request.POST.get('clickedproduct',None)
	# print(clickedproduct)
	# context['clickedproduct'] = clickedproduct
	clickedproduct = Product.get_products_by_id(clickedproduct)
	print(clickedproduct[0].image)
	return render(request, 'product_details.html', {'clickedproduct':clickedproduct})

