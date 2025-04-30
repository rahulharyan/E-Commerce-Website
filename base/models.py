from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Products(models.Model):
    category=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    desc=models.CharField(max_length=100)
    price=models.IntegerField(default=0)
    p_images=models.ImageField(default='default.png',upload_to='uploads')
    p_trending=models.BooleanField(default=0)
    p_offer=models.BooleanField(default=0)

    def __str__(self):
        return self.name
    

class cartModel(models.Model):
    category=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    desc=models.CharField(max_length=100)
    price=models.IntegerField(default=0)
    p_images=models.ImageField(default='default.png',upload_to='uploads')
    p_quantity=models.IntegerField(default=1)
    totalamount=models.IntegerField(default=0)
    host=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name