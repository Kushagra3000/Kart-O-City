from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from store.models.orders import Order
from django.shortcuts import render , redirect , HttpResponseRedirect,HttpResponse
from store.models.product import Product
from store.models.category import Category
from django.views import View
from django.contrib.auth import logout as logouts
from django.contrib.auth.hashers import make_password
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
        message = MIMEText("Hi there,\n\n"+otp+" is your Kart-O-City login OTP")
        message['Subject'] = 'Kart-O-City Login OTP'
        message['From'] = EMAIL_ADDR
        message['To'] = email

        server = smtplib.SMTP_SSL("smtp.gmail.com", port)
        server.login(sender_email, password)
        server.sendmail(sender_email, [receiver_email], message.as_string())
        server.quit()




def Profile(request):
	lst = []
	lst.append(request.session.get('customer'))
	customer = Customer.get_customer_by_id(lst)

	values = {
	    'first_name': customer.first_name,
	    'last_name': customer.last_name,
	    'phone': customer.phone,
	    'email': customer.email,
	}
	
	return render(request, 'profile.html', values)

def logout(request):
    logouts(request)
    return redirect('login')

def sellerlogout(request):
    logouts(request)
    return redirect('login')

def manageprofile(request):
	lst = []
	lst.append(request.session.get('customer'))
	customer = Customer.get_customer_by_id(lst)

	values = {
	    'first_name': customer.first_name,
	    'last_name': customer.last_name,
	    'phone': customer.phone,
	    'email': customer.email,
	}
	return render(request,'manageprofile.html',values)

def editprofile(request):
	first_name = request.POST.get('first_name')
	last_name = request.POST.get('last_name')
	email = request.POST.get('email')
	phone = request.POST.get('phone')
	password = request.POST.get('password')

	lst = []
	lst.append(request.session.get('customer'))
	customer = Customer.get_customer_by_id(lst)

	flag = check_password(password, customer.password)
	print("password: ",password)

	if flag:
		cust = Customer(first_name=first_name,
		                    last_name=last_name,
		                    phone=phone,
		                    email=email,
		                    password=password)
		error_message = validateCustomer(cust)
		print("error: ", error_message)
		if not error_message:

			keygen = generateKey()
			key = base64.b32encode(keygen.returnValue(phone).encode())  # Key is generated
			OTP = pyotp.TOTP(key,interval = EXPIRY_TIME)  # TOTP Model for OTP is created
			print("otp ",OTP.now())
			otpobj = sendOTP()
			otpobj.otpsend(email,phone,OTP.now())

			values = {
			    'first_name': first_name,
			    'last_name': last_name,
			    'phone': phone,
			    'email': email,
			    'emailold':customer.email,
			}
			return render(request, 'otpmanageprof.html', values)
		else:
			values = {
			    'first_name': customer.first_name,
			    'last_name': customer.last_name,
			    'phone': customer.phone,
			    'email': customer.email,
			    'error': error_message
			}
			return render(request, 'manageprofile.html', values)

	else:
		error_message = "Incorrect Password"
		print(error_message)
		values = {
		    'first_name': customer.first_name,
		    'last_name': customer.last_name,
		    'phone': customer.phone,
		    'email': customer.email,
		    'error': error_message
		}
		return render(request, 'manageprofile.html', values)


def newpass(request):
	return render(request,'changepassword.html',{})

def changepass(request):
	lst = []
	lst.append(request.session.get('customer'))
	customer = Customer.get_customer_by_id(lst)
	currentpassword = request.POST.get('currentpassword')
	newpassword = request.POST.get('newpassword')
	confirmpassword = request.POST.get('confirmpassword')
	flag = check_password(currentpassword, customer.password)

	if flag:

		if(len(newpassword)<6):
			error_message = "Minimum password length should 6!"
			return render(request, 'changepassword.html', {'error': error_message})
		if currentpassword==newpassword:
			error_message = "Current password should not be same as new password!"
			return render(request, 'changepassword.html', {'error': error_message})
		if newpassword!=confirmpassword:
			error_message = "Please confirm your password!"
			return render(request, 'changepassword.html', {'error': error_message})

		customer.password = make_password(newpassword)
		customer.register()
		confirm_msg = 'Your Password Updated Succefully!'
		return render(request, 'profile.html', {'confirm_msg':confirm_msg})
	else:
		error_message = "Incorrect Current Password"
		print(error_message)
		return render(request, 'changepassword.html', {'error': error_message})


def validateCustomer(customer):
    error_message = None;
    if (not customer.first_name):
        error_message = "First Name Required !!"
    elif len(customer.first_name) < 4:
        error_message = 'First Name must be 4 char long or more'
    elif not customer.last_name:
        error_message = 'Last Name Required'
    elif len(customer.last_name) < 4:
        error_message = 'Last Name must be 4 char long or more'
    elif not customer.phone:
        error_message = 'Phone Number required'
    elif len(customer.phone) < 10:
        error_message = 'Phone Number must be 10 char Long'
    elif len(customer.password) < 6:
        error_message = 'Password must be 6 char long'
    elif len(customer.email) < 5:
        error_message = 'Email must be 5 char long'
    # saving

    return error_message