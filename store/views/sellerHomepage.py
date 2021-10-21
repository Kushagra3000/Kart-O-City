from django.shortcuts import render , redirect, HttpResponseRedirect
from django.http import HttpResponse  
from django.views import  View

from store.templates.sellerForm import SellerForm

class SellerHomepage(View):
    def get(self,request):
        return render(request,'sellerHomepage.html')
    