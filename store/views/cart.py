from django.shortcuts import render , redirect

from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import  View
from store.models.product import  Product

# class Cart(View):
#     def get(self , request):
#         ids = list(request.session.get('cart').keys())
#         products = Product.get_products_by_id(ids)
#         print(products)
#         return render(request , 'cart.html' , {'products' : products} )

class Cart(View):
    def get(self , request):
    	lst = []
    	lst.append(request.session.get('customer'))
    	customer = Customer.get_customer_by_id(lst)
    	ids = list(request.session.get('cart').keys())
    	products = Product.get_products_by_id(ids)
    	# total_price = 0
    	# for price in products:
    	# 	total_price+=(price.price)
    	# total_price = request.POST.get('total_price')
    	# print("total_price ",total_price)
    	values = {
    	    'first_name': customer.first_name,
    	    'last_name': customer.last_name,
    	    'phone': customer.phone,
    	    'email': customer.email,
    	    # 'total_price': total_price,
    	    'products':products
    	}
    	return render(request , 'cart.html' , values )