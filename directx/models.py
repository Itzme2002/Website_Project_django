from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Students(models.Model):
    name = models.CharField(max_length=30)
    address = models.TextField()
    age = models.IntegerField()
    image = models.FileField(upload_to="documents",default='image.jpg')

class Product(models.Model):
    pro_name = models.CharField(max_length=30)
    pro_weight = models.IntegerField()
    pro_price = models.CharField(max_length=30)
    pro_image = models.FileField(upload_to="documents",default='image.jpg')

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    my_gender = models.CharField(max_length=30)
    phone_number = models.IntegerField()
    place = models.CharField(max_length=30)