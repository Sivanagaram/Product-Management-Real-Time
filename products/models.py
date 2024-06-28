from django.db import models
from datetime import datetime
# Create your models here.

class products(models.Model):
    image=models.ImageField(null=False,blank=False)
    name=models.CharField(max_length=200,null=False,blank=False)
    price=models.CharField(max_length=255)
    company=models.CharField(max_length=100,null=False,blank=False)
    is_available=models.BooleanField(default=True)
    description=models.TextField()
    released_on=models.DateTimeField(default=datetime.now,blank=True)


