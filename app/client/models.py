from django.db import models
from django.utils import timezone

#Modelo Cliente
class Client(models.Model):
    first_name = models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    age = models.IntegerField
    country = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    creation_date = models.DateTimeField(default=timezone.now)
    
    def ___str___(self):
        return self.name
