from django.shortcuts import render , redirect, HttpResponseRedirect,HttpResponse
from django.contrib.auth.hashers import  check_password
from store.models.seller import Seller
from django.views import  View
from store.templates.captcha import MyForm

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
        print(seller) #admasmoad
        error_message = None
        if seller and form1.is_valid():
            flag = check_password(password, seller.password)
            if flag:
                request.session['seller'] = seller.id

                if Seller.return_url:
                    return HttpResponseRedirect(Seller.return_url)
                else:
                    Seller.return_url = None
                    print(seller.status == "verified")
                    print(seller.panCard)
                    print(seller.panCard!='' and seller.gstDocument!='')
                    if(seller.status == "verified"):
                        return redirect('addProduct')
                    elif(seller.panCard!='' and seller.gstDocument!=''):
                        return HttpResponse("Your Status is not verified")
                    else:
                        return redirect('sellerHomepage')
            else:
                error_message = 'Email or Password invalid !!'
        else:
            error_message = 'Email or Password invalid !!'
        return render(request, 'sellerLogin.html', {'error': error_message,"form":form})

