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


class generateKey:
    @staticmethod
    def returnValue(phone):
        return str(phone) + str(datetime.date(datetime.now())) + "Some Random Secret Key"

class sendOTP:
    @staticmethod
    def otpsend(email,phone,otp):
        # account_sid = 'AC40ef4acb7313454341fb58903c072b00'
        # auth_token = '2b07567ca59e4e0b61c1524a06f89068'
        # 
        # 
        # client = Client(account_sid, auth_token)
        # print('phone number ',phone)
        # message = client.messages.create(
        #                               body=f'OTP for login-{otp}',
        #                               from_='+13187319719',
        #                               to='+919773709020'
        #                           )



        port = 465  # For SSL
        password = "{k@RT-02c!2y}"
        sender_email = "kartocity.pvt.ltd@gmail.com"
        receiver_email = email
        message = MIMEText("Hi there,\n\n"+otp+" is your Kart-O-City login OTP")
        message['Subject'] = 'Kart-O-City Login OTP'
        message['From'] = 'kartocity.pvt.ltd@gmail.com'
        message['To'] = email

        server = smtplib.SMTP_SSL("smtp.gmail.com", port)
        server.login(sender_email, password)
        server.sendmail(sender_email, [receiver_email], message.as_string())
        server.quit()



class SellerLogin(View):
    return_url = None
    def get(self , request):
        form = MyForm
        Seller.return_url = request.GET.get('return_url')
        return render(request , 'sellerLogin.html',{"form":form})

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
                key = base64.b32encode(keygen.returnValue(phone).encode())  # Key is generated
                OTP = pyotp.TOTP(key,interval = 50)  # TOTP Model for OTP is created
                print("otp ",OTP.now())
                otpobj = sendOTP()

                otpobj.otpsend(email,phone,OTP.now())

                return render(request, 'otpsellerlogin.html', {'email':email,'return_url':Seller.return_url})
            else:
                error_message = 'Email or Password invalid !!'
        else:
            error_message = 'Captcha Did Not Match'
        return render(request, 'sellerLogin.html', {"form":form,'error': error_message})

