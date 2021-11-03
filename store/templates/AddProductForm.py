from django import forms
class AddProductForm(forms.Form):
    name_of_Product = forms.CharField(max_length=100)
    price_of_Product = forms.IntegerField()
    Image1 = forms.ImageField()
    Image2 = forms.ImageField()
    Image3 = forms.ImageField()
    Category = forms.CharField(max_length=100)
