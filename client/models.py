# Insert models here

from django.db import models

class ClientModel(models.Model):
    name = models.CharField(max_length=155,unique = True)
    street_name = models.CharField(max_length=100, null=True)
    suburb = models.CharField(max_length=100, unique = True)
    postcode = models.CharField(max_length=50,null=True)
    state = models.CharField(max_length=100, null=True)
    contact = models.CharField(max_length=100, null = True)
    email = models.EmailField(max_length=155, unique = True)
    phone_number = models.IntegerField(null=True)

    def __str__(self):
        return self.name
