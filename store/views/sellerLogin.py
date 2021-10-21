from django.shortcuts import render , redirect, HttpResponseRedirect
from django.contrib.auth.hashers import  check_password
from store.models.seller import Seller
from django.views import  View

class SellerLogin(View):
    return_url = None
    def get(self , request):
        Seller.return_url = request.GET.get('return_url')
        return render(request , 'sellerLogin.html')
    def post(self , request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        seller = Seller.get_seller_by_email(email)
        error_message = None
        if seller:
            flag = check_password(password, seller.password)
            if flag:
                request.session['sellerLogin'] = seller.id

                if Seller.return_url:
                    return HttpResponseRedirect(Seller.return_url)
                else:
                    Seller.return_url = None
                    return redirect('sellerHomepage')
            else:
                error_message = 'Email or Password invalid !!'
        else:
            error_message = 'Email or Password invalid !!'

        print(email, password)
        return render(request, 'sellerLogin.html', {'error': error_message})

def logout(request):
    request.session.clear()
    return redirect('sellerLogin')