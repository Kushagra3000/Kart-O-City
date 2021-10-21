from django import forms  
class SellerForm(forms.Form):  
    file      = forms.FileField() # for creating file input