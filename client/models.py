# Insert models here

from django.db import models

class ClientModel(models.Model):
    name = models.CharField(max_length=155,unique=True, blank=False)
    street_name = models.CharField(max_length=100, blank=True)
    suburb = models.CharField(max_length=100, blank = True)
    postcode = models.CharField(max_length=50,blank=True)
    state = models.CharField(max_length=100, blank=True)
    contact = models.CharField(max_length=100, blank = True)
    email = models.EmailField(max_length=155, unique = True, blank=False)
    phone_number = models.CharField(max_length=13, blank=False)

    def __str__(self):
        return self.name
