from django.shortcuts import render , redirect , HttpResponseRedirect
from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from store.models.product import Product
from store.models.seller import Seller
from store.models.orders import Order
from store.templates.captcha import MyForm
import razorpay
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
    	error_message = 'Incorrect otp'
    	return render(request, 'login.html', {'error': error_message,'form':MyForm})


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
        return render(request, 'sellerSignUp.html', {'error': error_message,'form':MyForm})


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
        error_message = 'Incorrect otp'
        return render(request, 'sellerLogin.html', {'error': error_message,'form':MyForm})


def otpcheckout(request):
    address = request.POST.get('address')
    lst = []
    lst.append(request.session.get('customer'))
    customer = Customer.get_customer_by_id(lst)
    email = customer.email
    phone = customer.phone
    cart = request.session.get('cart')
    products = Product.get_products_by_id(list(cart.keys()))
    amount=request.POST.get('total_price')
    first_name = customer.first_name
    phone = customer.phone
    

    
    keygen = generateKey()
    key = base64.b32encode(keygen.returnValue(phone).encode()) 
    OTP = pyotp.TOTP(key,interval = 120) 
    otp = request.POST.get('otp')
    amount = int(amount)*100
    print('amount',amount,type(amount))
    ids = list(request.session.get('cart').keys())
    products = Product.get_products_by_id(ids)
    if OTP.verify(otp): 
        checkoutotp = True
        values = {'address':address,
                    'email':email,
                    'total_price':amount,
                    'first_name':first_name,
                    'phone':phone,
                    'checkoutotp':checkoutotp
                    }
        return render(request, 'otpcheckout.html', values)
    else:
        error_message = "Incorrect OTP"
        values = {'address':address,
                    'email':email,
                    'total_price':amount,
                    'first_name':first_name,
                    'phone':phone,
                    'error_message':error_message,
                    'products':products
                    }
        return render(request, 'cart.html', values)

 

def otpcheckout2(request):
    address = request.POST.get('address')
    lst = []
    lst.append(request.session.get('customer'))
    customer = Customer.get_customer_by_id(lst)
    email = customer.email
    phone = customer.phone
    cart = request.session.get('cart')
    products = Product.get_products_by_id(list(cart.keys()))
    amount=request.POST.get('total_price')
    client = razorpay.Client(auth=("rzp_test_NWZijDjIFaRFJk", "hqiJK5eJB3HAJpMl2ryPZXpc"))
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
    amount = int(amount)
    payment = client.order.create({'amount': amount, 'currency': 'INR'})
    print("payment",payment)
    for product in products:
        print(cart.get(str(product.id)))
        order = Order(customer=Customer(id=lst[0]),
                      product=product,
                      price=product.price,
                      address=address,
                      phone=phone,
                      quantity=cart.get(str(product.id)))
        order.save()
    
    request.session['cart'] = {}

    confirm_msg = "Your order has been placed."
    return render(request, 'cart.html', {'confirm_msg':confirm_msg})


def checkotpforgotcustomer(request):
    email = request.POST.get('email')
    otp = request.POST.get('otp')
    customer = Customer.get_customer_by_email(email)
    phone = customer.phone
    keygen = generateKey()
    key = base64.b32encode(keygen.returnValue(phone).encode())  # Generating Key
    OTP = pyotp.TOTP(key,interval = 50)  # TOTP Model 
    print("Idhar otp: ",OTP.now())
    if OTP.verify(otp):
        return render(request, 'newpasswordcustomer.html', {'email':email}) 
    else:
        error_message = "Incorrect OTP"
        return render(request, 'forgotcustomer.html', {'error_message':error_message}) 

def checkotpforgotseller(request):
    email = request.POST.get('email')
    otp = request.POST.get('otp')
    customer = Seller.get_seller_by_email(email)
    phone = customer.phone
    keygen = generateKey()
    key = base64.b32encode(keygen.returnValue(phone).encode())  # Generating Key
    OTP = pyotp.TOTP(key,interval = 50)  # TOTP Model 
    print("Idhar otp: ",OTP.now())
    if OTP.verify(otp):
        return render(request, 'newpasswordseller.html', {'email':email}) 
    else:
        error_message = "Incorrect OTP"
        return render(request, 'forgotseller.html', {'error_message':error_message}) 
