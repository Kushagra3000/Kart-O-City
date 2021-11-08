from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View

from store.models.product import Product
from store.models.orders import Order
import razorpay
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
from kartocity.settings import EMAIL_ADDR
from kartocity.settings import EXPIRY_TIME

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


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        lst = []
        lst.append(request.session.get('customer'))
        customer = Customer.get_customer_by_id(lst)
        email = customer.email
        amount=request.POST.get('total_price')
        first_name = customer.first_name
        phone = customer.phone
        checkoutotp = False
        values = {'address':address,
                    'email':email,
                    'total_price':amount,
                    'first_name':first_name,
                    'phone':phone,
                    'checkoutotp':checkoutotp
                    }

        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(phone).encode())
        OTP = pyotp.TOTP(key,interval = EXPIRY_TIME)
        print("otp ",OTP.now())
        otpobj = sendOTP()
        otpobj.otpsend(email,phone,OTP.now())

        return render(request, 'otpcheckout.html', values)
