from django import forms  
class SellerForm(forms.Form):
    pancard = forms.FileField() 
    gstDocument = forms.FileField()