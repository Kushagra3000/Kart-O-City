from django.shortcuts import render, redirect
from store.models.seller import Seller
from django.contrib.auth.hashers import make_password
from django.views import View
from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import  View
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
import pyotp
import base64
import os
import smtplib, ssl
from email.mime.text import MIMEText
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
        message = MIMEText("Hi there,\n\n"+otp+" is your Kart-O-City signup OTP")
        message['Subject'] = 'Kart-O-City Signup OTP'
        message['From'] = EMAIL_ADDR
        message['To'] = email
        server = smtplib.SMTP_SSL("smtp.gmail.com", port)
        server.login(sender_email, password)
        server.sendmail(sender_email, [receiver_email], message.as_string())
        server.quit()


class SellerSignUp(View):
    def get(self, request):
        if (not request.session.get('seller')) and (not request.session.get('customer')):
            return render(request,'sellerSignUp.html')
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
    def post(self,request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message = None
        seller = Seller(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)
        error_message = self.validateCustomer(seller)
        if not error_message:
            phone = seller.phone
            keygen = generateKey()
            key = base64.b32encode(keygen.returnValue(phone).encode())  
            OTP = pyotp.TOTP(key,interval = EXPIRY_TIME) 
            print("otp ",OTP.now())
            otpobj = sendOTP()
            otpobj.otpsend(email,phone,OTP.now())

            values = {'first_name': first_name,'last_name': last_name,'phone': phone,'email': email,'password':password}
            return render(request, 'otpsellersignup.html', values)
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'sellerSignUp.html', data)

    def validateCustomer(self, seller):
        error_message = None;
        if (not seller.first_name):
            error_message = "First Name Required !!"
        elif len(seller.first_name) < 4:
            error_message = 'First Name must be 4 char long or more'
        elif not seller.last_name:
            error_message = 'Last Name Required'
        elif len(seller.last_name) < 4:
            error_message = 'Last Name must be 4 char long or more'
        elif not seller.phone:
            error_message = 'Phone Number required'
        elif len(seller.phone) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len(seller.password) < 6:
            error_message = 'Password must be 6 char long'
        elif len(seller.email) < 5:
            error_message = 'Email must be 5 char long'
        elif seller.isExists():
            error_message = 'Email Address Already Registered..'
        # saving

        return error_message