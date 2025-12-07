from django.db import models

# Create your models here.
class happi(models.Model):
    hid=models.IntegerField()
    hname=models.CharField(max_length=35)
    contact=models.IntegerField()
    salary=models.IntegerField()
    address=models.CharField(max_length=100)