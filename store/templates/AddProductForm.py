from django import forms
from django.db.models.fields.files import ImageFieldFile
from django.forms.fields import ImageField
from django.forms.widgets import ClearableFileInput, NumberInput, Select, TextInput, Textarea
from store.models import *
class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','price','description','category','image','image2','image3']
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control form-control-sm",
                'placeholder': 'Name of Product'
                }),
            'price': NumberInput(attrs={
                'class': "form-control form-control-sm"
            }),
            'description' : TextInput(attrs={
                'class' :  "form-control form-control-sm"
            }),
            'category' : forms.Select(attrs={
                'class' : "form-group col-md-4"
            }),
            'image' : ClearableFileInput(attrs={
                'class' : "form-group col-md-6"
            }),
            'image2' : ClearableFileInput(attrs={
                'class' : "form-group col-md-6"
            }),
            'image3' : ClearableFileInput(attrs={
                'class' : "form-group col-md-6"
            })
            
        }   