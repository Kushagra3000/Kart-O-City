from django.db import models
from django.core.validators import MinLengthValidator

class Seller(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)
    panCard = models.FileField(upload_to='uploads/', null=True)
    gstDocument = models.FileField(upload_to='uploads/', null=True)
    status = models.CharField(max_length=50,default="not verified")
    def register(self):
        self.save()

    @staticmethod
    def get_seller_by_email(email):
        try:
            return Seller.objects.get(email=email)
        except:
            return False


    def isExists(self):
        if Seller.objects.filter(email = self.email):
            return True

        return  False

    def get_customer_by_id(ids):
        return Seller.objects.get(id__in =ids)

    def handle_uploaded_file(f):  
        with open('uploads/'+f.name, 'wb+') as destination:  
            for chunk in f.chunks():  
                destination.write(chunk)  
