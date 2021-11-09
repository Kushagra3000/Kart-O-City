from django.shortcuts import render , redirect, HttpResponseRedirect,HttpResponse
from django.contrib.auth.hashers import  check_password
from store.models.seller import Seller
from django.views import  View
from store.templates.captcha import MyForm
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

class SellerLogin(View):
    return_url = None
    def get(self , request):
        if not request.session.get('seller'):
            form = MyForm
            Seller.return_url = request.GET.get('return_url')
            return render(request , 'sellerLogin.html',{"form":form})
        elif request.session.get('customer'):
            return redirect('homepage')
        else:
            lst = []
            lst.append(request.session.get('seller'))
            seller = Seller.get_customer_by_id(lst)
            if(seller.status == "verified"):
                return redirect('addProduct')
            elif(seller.panCard!='' and seller.gstDocument!=''):
                return redirect('statuspage')
            else:
                return redirect('sellerHomepage')

    def post(self , request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        form1 = MyForm(request.POST)
        seller = Seller.get_seller_by_email(email)
        form = MyForm
        Seller.return_url = request.GET.get('return_url')
        error_message = None
        if not seller:
            error_message = 'Email or Password invalid !!'
        elif form1.is_valid():
            flag = check_password(password, seller.password)
            if flag:

                phone = seller.phone
                keygen = generateKey()
                key = base64.b32encode(keygen.returnValue(seller.password).encode())  # Key is generated
                OTP = pyotp.TOTP(key,interval = EXPIRY_TIME)  # TOTP Model for OTP is created
                print("otp ",OTP.now())
                otpobj = sendOTP()

                otpobj.otpsend(email,phone,OTP.now())

                return render(request, 'otpsellerlogin.html', {'email':email,'return_url':Seller.return_url})
            else:
                error_message = 'Email or Password invalid !!'
        else:
            error_message = 'Captcha Did Not Match'
        return render(request, 'sellerLogin.html', {"form":form,'error': error_message})

