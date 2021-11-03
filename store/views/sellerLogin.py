from django.shortcuts import render , redirect, HttpResponseRedirect,HttpResponse
from django.contrib.auth.hashers import  check_password
from store.models.seller import Seller
from django.views import  View
from store.templates.AddProductForm import AddProductForm

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
                request.session['seller'] = seller.id

                if Seller.return_url:
                    return HttpResponseRedirect(Seller.return_url)
                else:
                    Seller.return_url = None
                    print(seller.status == "verified")
                    context = {}
                    context['form'] = AddProductForm
                    if(seller.status == "verified"):
                        return render(request,'AddProduct.html',context)
                    elif(seller.panCard!=None and seller.gstDocument!=None):
                        return HttpResponse("Your Status is not verified")
                    else:
                        return redirect('sellerHomepage')
            else:
                error_message = 'Email or Password invalid !!'
        else:
            error_message = 'Email or Password invalid !!'

        print(email, password)
        return render(request, 'sellerLogin.html', {'error': error_message})

