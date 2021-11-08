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


class generateKey:
    @staticmethod
    def returnValue(phone):
        return str(phone) + str(datetime.date(datetime.now())) + "Some Random Secret Key"

class sendOTP:
    @staticmethod
    def otpsend(email,phone,otp):
        port = 465 
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



class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        lst = []
        lst.append(request.session.get('customer'))
        customer = Customer.get_customer_by_id(lst)
        email = customer.email
        # phone = customer.phone
        # cart = request.session.get('cart')
        # products = Product.get_products_by_id(list(cart.keys()))
        amount=request.POST.get('total_price')
        # client = razorpay.Client(auth=("rzp_test_NWZijDjIFaRFJk", "hqiJK5eJB3HAJpMl2ryPZXpc"))
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
        key = base64.b32encode(keygen.returnValue(phone).encode())  # Key is generated
        OTP = pyotp.TOTP(key,interval = 120)  # TOTP Model for OTP is created
        print("otp ",OTP.now())
        otpobj = sendOTP()
        otpobj.otpsend(email,phone,OTP.now())

        return render(request, 'otpcheckout.html', values)

        # payment = client.order.create({'amount': amount, 'currency': 'INR'})
        # print("payment",payment)
        # for product in products:
        #     print(cart.get(str(product.id)))
        #     order = Order(customer=Customer(id=lst[0]),
        #                   product=product,
        #                   price=product.price,
        #                   address=address,
        #                   phone=phone,
        #                   quantity=cart.get(str(product.id)))
        #     order.save()
        
        # request.session['cart'] = {}

        # return redirect('cart')