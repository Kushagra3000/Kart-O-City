from django.shortcuts import render , redirect , HttpResponseRedirect
from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from store.models.seller import Seller
from django.views import  View
from datetime import datetime
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ObjectDoesNotExist
import pyotp
import base64



class generateKey:
    @staticmethod
    def returnValue(phone):
        return str(phone) + str(datetime.date(datetime.now())) + "Some Random Secret Key"


def checkotp(request):

    # virtualkeyboard.main()
    
    email = request.POST.get('email')
    otp = request.POST.get('otp')

    customer = Customer.get_customer_by_email(email)

    phone = customer.phone
    Customer.return_url = request.GET.get('return_url')

    keygen = generateKey()
    key = base64.b32encode(keygen.returnValue(phone).encode())  # Generating Key
    OTP = pyotp.TOTP(key,interval = 50)  # TOTP Model 
    if OTP.verify(otp):  # Verifying the OTP
        request.session['customer'] = customer.id
        if Customer.return_url:
            return HttpResponseRedirect(Customer.return_url)
        else:
            Customer.return_url = None
            return redirect('homepage')
    else:
    	error_message = 'incorrect otp'
    	return render(request, 'login.html', {'error': error_message})


def checkotpmanageprofile(request):
    emailold = request.POST.get('emailold')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    # password = request.POST.get('password')
    otp = request.POST.get('otp')
    customer = Customer.get_customer_by_email(emailold)

    keygen = generateKey()
    key = base64.b32encode(keygen.returnValue(phone).encode())  # Generating Key
    OTP = pyotp.TOTP(key,interval = 50)  # TOTP Model 
    if OTP.verify(otp):  # Verifying the OTP
        customer.first_name = first_name
        customer.last_name = last_name
        customer.phone = phone
        customer.email = email
        customer.register()
        confirm_msg = "Profile Updated Succefully!"
        print(confirm_msg)
        return render(request, 'profile.html', {'confirm_msg':confirm_msg,'first_name':first_name})
    else:
        error_message = 'Incorrect OTP!'
        print(error_message)
        values = {
            'first_name': customer.first_name,
            'last_name': customer.last_name,
            'phone': customer.phone,
            'email': customer.email,
            'error': error_message
        }
        return render(request, 'manageprofile.html', values)


def checkotpsellersignup(request):
    otp = request.POST.get('otp')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    password = request.POST.get('password')
    phone = request.POST.get('phone')
    
    seller = Seller(first_name=first_name,
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
        seller.password = make_password(seller.password)
        seller.register()
        return redirect('homepage')
    else:
        error_message = 'incorrect otp'
        return render(request, 'sellerSignUp.html', {'error': error_message})


def checkotpsellerlogin(request):


    email = request.POST.get('email')
    otp = request.POST.get('otp')

    seller = Seller.get_seller_by_email(email)

    phone = seller.phone

    Seller.return_url = request.GET.get('return_url')

    keygen = generateKey()
    key = base64.b32encode(keygen.returnValue(phone).encode())  # Generating Key
    OTP = pyotp.TOTP(key,interval = 50)  # TOTP Model 

    if OTP.verify(otp): 
        request.session['seller'] = seller.id

        if Seller.return_url:
            return HttpResponseRedirect(Seller.return_url)
        else:
            Seller.return_url = None
            if(seller.status == "verified"):
                return redirect('addProduct')
            elif(seller.panCard!='' and seller.gstDocument!=''):
                return HttpResponse("Your Status is not verified")
            else:
                return redirect('sellerHomepage')
    else:
        error_message = 'incorrect otp'
        return render(request, 'sellerLogin.html', {'error': error_message})