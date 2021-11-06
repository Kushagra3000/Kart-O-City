from django.shortcuts import render , redirect , HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import  View
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
import pyotp
import base64


class generateKey:
    @staticmethod
    def returnValue(phone):
        return str(phone) + str(datetime.date(datetime.now())) + "Some Random Secret Key"


def checkotp(request):
    
    
    otp = request.POST.get('otp')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    password = request.POST.get('password')
    phone = request.POST.get('phone')
    
    customer = Customer(first_name=first_name,
                        last_name=last_name,
                        phone=phone,
                        email=email,
                        password=password)
    
    keygen = generateKey()
    key = base64.b32encode(keygen.returnValue(phone).encode())  # Generating Key
    OTP = pyotp.TOTP(key,interval = 50)  # TOTP Model 
    print("Idhar otp: ",OTP.now())
    if OTP.verify(otp):  # Verifying the OTP
        # print(first_name, last_name, phone, email, password)
        customer.password = make_password(customer.password)
        customer.register()
        return redirect('homepage')
    else:
    	error_message = 'incorrect otp'
    	return render(request, 'signup.html', {'error': error_message})
