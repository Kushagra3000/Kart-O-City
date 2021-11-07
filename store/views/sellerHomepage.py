from django.forms.formsets import INITIAL_FORM_COUNT
from django.shortcuts import render , redirect, HttpResponseRedirect
from django.http import HttpResponse  
from django.views import  View

from store.models.seller import Seller
from store.templates.sellerForm import SellerForm


class SellerHomepage(View):
    def get(self,request):
        context = {}
        context['form'] = SellerForm
        return render(request,'sellerHomePage.html',context)
    def post(self,request):
        lst = []
        lst.append(request.session.get('seller'))
        sel = Seller.get_customer_by_id(lst)
        pan = SellerForm(request.POST,request.FILES)
        gst = SellerForm(request.POST,request.FILES)
        if pan.is_valid() and gst.is_valid():
            sel.panCard=request.FILES['pancard']
            sel.gstDocument=request.FILES['gstDocument']
            sel.save()
            return HttpResponse("File uploaded successfully")
        else:
            context = {}
            context['form'] = SellerForm
            return render(request,'sellerHomePage.html',context)
