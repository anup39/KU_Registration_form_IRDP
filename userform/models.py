from django.db import models
from django.utils import timezone



# Create your models here.
class User(models.Model):
    First_name = models.CharField( max_length=100)
    Last_name=models.CharField( max_length=100)
    Email=models.EmailField()
    Contact=models.CharField(max_length=100)
    Organization=models.CharField( max_length=100)
    Date_time = models.DateTimeField(default=timezone.now)