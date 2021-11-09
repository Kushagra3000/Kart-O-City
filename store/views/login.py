from django.shortcuts import render , redirect , HttpResponseRedirect
from django.contrib.auth.hashers import  check_password
from django.contrib.auth.hashers import  make_password
from store.models.customer import Customer
from store.models.seller import Seller
from django.views import  View
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
import pyotp
import base64
import os
from twilio.rest import Client
import smtplib, ssl
from email.mime.text import MIMEText
from store.templates.captcha import MyForm
from kartocity.settings import EMAIL_PASSWORD
from kartocity.settings import EXPIRY_TIME
from kartocity.settings import EMAIL_ADDR


class generateKey:
    @staticmethod
    def returnValue(phone):
        return str(phone) + str(datetime.date(datetime.now())) + "Some Random Secret Key"

class sendOTP:
    @staticmethod
    def otpsend(email,phone,otp):
        port = 465 
        password = EMAIL_PASSWORD
        sender_email = EMAIL_ADDR
        receiver_email = email
        message = MIMEText("Hi there,\n\n"+otp+" is your Kart-O-City login OTP")
        message['Subject'] = 'Kart-O-City Login OTP'
        message['From'] = EMAIL_ADDR
        message['To'] = email

        server = smtplib.SMTP_SSL("smtp.gmail.com", port)
        server.login(sender_email, password)
        server.sendmail(sender_email, [receiver_email], message.as_string())
        server.quit()



class Login(View):
    return_url = None
    def get(self , request):
        if not request.session.get('customer'):
            form = MyForm
            Login.return_url = request.GET.get('return_url')
            return render(request , 'login.html',{"form":form})
        elif request.session.get('seller'):
            lst = []
            lst.append(request.session.get('seller'))
            seller = Seller.get_customer_by_id(lst)
            if(seller.status == "verified"):
                return redirect('addProduct')
            elif(seller.panCard!='' and seller.gstDocument!=''):
                return redirect('statuspage')
            else:
                return redirect('sellerHomepage')
        else:
            return redirect('homepage')

    def post(self , request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        form1 = MyForm(request.POST)
        form = MyForm
        error_message = None
        if not customer:
            error_message = 'Email or Password invalid !!'
        elif form1.is_valid():
            flag = check_password(password, customer.password)
            if flag :
                phone = customer.phone
                keygen = generateKey()
                key = base64.b32encode(keygen.returnValue(customer.password).encode()) 
                OTP = pyotp.TOTP(key,interval = EXPIRY_TIME)
                print("otp ",OTP.now(),key)
                otpobj = sendOTP()
                otpobj.otpsend(email,phone,OTP.now())
                return render(request, 'otp.html', {'email':email})

            else:
                error_message = 'Email or Password invalid !!'
        else:
            error_message = 'Captcha Did Not Match!!'

        return render(request, 'login.html', {'error': error_message,"form":form})