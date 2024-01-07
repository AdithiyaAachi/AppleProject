from django.db import models

# Create your models here.
class contactdb(models.Model):
    FirstName=models.CharField(max_length=100,null=True,blank=True)
    LastName=models.CharField(max_length=100,null=True,blank=True)
    EmailId=models.CharField(max_length=100,null=True,blank=True)
    Subject=models.CharField(max_length=100,null=True,blank=True)
    Message=models.CharField(max_length=100,null=True,blank=True)
class RegisterDb(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Mobile=models.IntegerField(null=True,blank=True)
    Email=models.CharField(max_length=100,null=True,blank=True)
    Username=models.CharField(max_length=100,null=True,blank=True)
    Password=models.CharField(max_length=100,null=True,blank=True)

class CartDb(models.Model):
    UserName=models.CharField(max_length=100,null=True,blank=True)
    BookName=models.CharField(max_length=100,null=True,blank=True)
    Quantity=models.IntegerField(null=True,blank=True)
    TotalPrice=models.IntegerField(null=True,blank=True)
    Definition=models.CharField(max_length=100,null=True,blank=True)

