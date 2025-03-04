from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Data(models.Model):
    date_created = models.DateField(auto_now=False, auto_now_add=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(blank=False)
    phone = PhoneNumberField(blank=False)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=10)
    
    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)