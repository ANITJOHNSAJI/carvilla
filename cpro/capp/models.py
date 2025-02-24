from django.db import models

# Create your models here.
class Car(models.Model):
    year = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    body_style = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)  
    price = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='images/')
    image=models.ImageField(upload_to='images/')
    mileage=models.TextField(max_length=100)
    hp=models.TextField(max_length=100)
    type=models.TextField(max_length=100)