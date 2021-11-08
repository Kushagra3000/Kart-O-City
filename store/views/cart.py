from django.shortcuts import render , redirect
from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import  View
from store.models.product import  Product

class Cart(View):
    def get(self , request):
    	lst = []
    	lst.append(request.session.get('customer'))
    	customer = Customer.get_customer_by_id(lst)
    	ids = list(request.session.get('cart').keys())
    	products = Product.get_products_by_id(ids)
   
    	values = {
    	    'first_name': customer.first_name,
    	    'last_name': customer.last_name,
    	    'phone': customer.phone,
    	    'email': customer.email,
    	    'products':products
    	}
    	return render(request , 'cart.html' , values )