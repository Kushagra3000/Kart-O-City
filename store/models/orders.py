from django.db import models
from .product import Product
from .customer import Customer
import datetime

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


class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)


    def save(self,*args,**kwargs):
        if self.status:
            otpobj = sendOTP()
            message = "Hi "+str(self.customer.first_name)+"\n\nYour order has been delivered.\n\nThanks for choosing Kart-O-City"
            otpobj.otpsend(self.customer.email,message)

        super().save(*args,**kwargs)


    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')

