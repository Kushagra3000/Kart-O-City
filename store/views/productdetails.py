from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.product import  Product
from django.shortcuts import render, redirect
from store.models.orders import Order
from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models.product import Product
from store.models.category import Category
from django.views import View


	
def product_details(request):
	if request.method == "POST":
		clickedproduct = request.POST.get('clickedproduct')
		print(clickedproduct)
		temp = []
		temp.append(clickedproduct)
		clickedproduct = Product.get_products_by_id(temp)
		return render(request, 'product_details.html', {'clickedproduct':clickedproduct})
	else:
		return redirect('store')


def product_details2(request):
	if request.method == "POST":
		product = request.POST.get('clickedproduct')
		remove = request.POST.get('remove')
		cart = request.session.get('cart')
		if cart:
		    quantity = cart.get(product)
		    if quantity:
		        if remove:
		            if quantity<=1:
		                cart.pop(product)
		            else:
		                cart[product]  = quantity-1
		        else:
		            cart[product]  = quantity+1

		    else:
		        cart[product] = 1
		else:
		    cart = {}
		    cart[product] = 1

		request.session['cart'] = cart

		clickedproduct = request.POST.get('clickedproduct')
		
		temp = []
		temp.append(clickedproduct)
		clickedproduct = Product.get_products_by_id(temp)
		
		return render(request, 'product_details.html', {'clickedproduct':clickedproduct})
	else:
		return redirect('store')
