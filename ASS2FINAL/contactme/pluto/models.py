from pickle import TRUE
#from pickle import FALSE
import datetime
from django.db import models
class users(models.Model):
    name = models.CharField(max_length=30)
    city= models.CharField(max_length=30, blank=TRUE)
    email=models.CharField(max_length=30, blank=TRUE)
    dob=models.DateField()
    address=models.TextField(blank=TRUE)