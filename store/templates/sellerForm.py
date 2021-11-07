from django import forms  
class SellerForm(forms.Form):
    pancard = forms.FileField(widget= forms.ClearableFileInput(attrs = {
        'class' : "form-group col-md-6"})) 
    gstDocument = forms.FileField(widget= forms.ClearableFileInput(attrs = {
        'class' : "form-group col-md-6"
    }))