from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View

from store.models.product import Product
from store.models.orders import Order
import razorpay


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        lst = []
        lst.append(request.session.get('customer'))
        customer = Customer.get_customer_by_id(lst)
        phone = customer.phone
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        amount=request.POST.get('total_price')
        client = razorpay.Client(
            auth=("rzp_test_NWZijDjIFaRFJk", "hqiJK5eJB3HAJpMl2ryPZXpc"))

        payment = client.order.create({'amount': amount, 'currency': 'INR',})
        print("payment",payment)
        for product in products:
            print(cart.get(str(product.id)))
            order = Order(customer=Customer(id=lst[0]),
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            order.save()
        print("ordrsss::  ",order.customer,order.product,order.price,order.address,order.phone,order.quantity)
        request.session['cart'] = {}

        return redirect('cart')