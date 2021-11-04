from django import forms
from store.models import *
class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','price','description','category','image','image2','image3']
    
