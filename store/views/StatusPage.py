from django.shortcuts import render, redirect
from store.models.seller import Seller
from django.views import View
from django.views import  View

class StatusPage(View):
    def get(self,request):
        if not request.session.get('seller') or request.session.get('customer'):
            return ('homepage')
        elif request.session.get('seller'):
            lst = []
            lst.append(request.session.get('seller'))
            seller = Seller.get_customer_by_id(lst)
            if(seller.status == "verified"):
                return redirect('addProduct')
            elif(seller.panCard!='' and seller.gstDocument!=''):
                return render(request,'Status.html')
            else:
                return redirect('sellerHomepage')