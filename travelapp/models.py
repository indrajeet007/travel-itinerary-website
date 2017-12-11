from django.db import models

# Create your models here.


class RegistrationModel(models.Model):
    uname=models.CharField(max_length=20)
    email=models.EmailField()
    pwd1=models.CharField(max_length=20)
    pwd2=models.CharField(max_length=20)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)




