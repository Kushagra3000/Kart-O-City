from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.product import  Product

from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View

from store.models.product import Product
from store.models.orders import Order

from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models.product import Product
from store.models.category import Category
from django.views import View

from django.contrib.auth import logout as logouts


def Profile(request):
    return render(request, 'profile.html', {})

def logout(request):
    logouts(request)
    return redirect('login')