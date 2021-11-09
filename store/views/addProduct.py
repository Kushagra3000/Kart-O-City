from django.http import HttpResponse
from django.shortcuts import render, redirect
from store.models.product import Product
from store.templates.AddProductForm import AddProductForm
from store.models.category import Category
from django.views import View

class AddProduct(View):

    def get(self,request):
    	if request.session.get('seller'):
    		context = {}
    		context['form'] = AddProductForm
    		return render(request, 'AddProduct.html',context)
    	else:
    		return redirect('sellerLogin')
    
    def post(self,request):
        form = AddProductForm(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()
            return render(request,'ProductAdded.html')
