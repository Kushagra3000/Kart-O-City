from django.shortcuts import render, redirect
from store.models.seller import Seller
from django.contrib.auth.hashers import make_password
from django.views import View


class SellerSignUp(View):
    def get(self, request):
        return render(request, 'sellerSignUp.html')
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
            print(first_name, last_name, phone, email, password)
            seller.password = make_password(seller.password)
            seller.register()
            return redirect('sellerHomepage')
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
