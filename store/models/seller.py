from django.db import models
from django.core.validators import MinLengthValidator
from kartocity.settings import EMAIL_PASSWORD
from kartocity.settings import EXPIRY_TIME
from kartocity.settings import EMAIL_ADDR
import smtplib, ssl
from email.mime.text import MIMEText

class sendOTP:
    @staticmethod
    def otpsend(email,message):
        port = 465 
        password = EMAIL_PASSWORD
        sender_email = EMAIL_ADDR
        receiver_email = email
        message = MIMEText(message)
        message['Subject'] = 'Kart-O-City Seller Verification'
        message['From'] = EMAIL_ADDR
        message['To'] = email

        server = smtplib.SMTP_SSL("smtp.gmail.com", port)
        server.login(sender_email, password)
        server.sendmail(sender_email, [receiver_email], message.as_string())
        server.quit()


class Seller(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)
    panCard = models.FileField(upload_to='Kart-O-City/uploads/userdocuments', null=True)
    gstDocument = models.FileField(upload_to='Kart-O-City/uploads/userdocuments', null=True)
    status = models.CharField(max_length=50,default="not verified")
    

    def save(self,*args,**kwargs):
        if self.status == "verified":
            otpobj = sendOTP()
            message = "Hi "+str(self.first_name)+"\n\nYour seller status on Kart-O-City has been verified.\n\nThanks from team Kart-O-City"
            otpobj.otpsend(self.email,message)
        elif self.status == "rejected":
            otpobj = sendOTP()
            message = "Hi "+str(self.first_name)+"\n\nYour seller status on Kart-O-City has been rejected due to invalid documents. You can register yourself again with correct documents.\n\nThanks from team Kart-O-City"
            otpobj.otpsend(self.email,message)
            self.delete()

        super().save(*args,**kwargs)

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

    def __str__(self):
        return self.first_name
