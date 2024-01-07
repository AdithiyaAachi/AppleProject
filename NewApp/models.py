from django.db import models

# Create your models here.
class BookDb(models.Model):
    BookName=models.CharField(max_length=100,null=True,blank=True)
    Definition=models.CharField(max_length=100,null=True,blank=True)
    BookImage=models.ImageField(upload_to="BookImage",null=True,blank=True)
class DetailsDb(models.Model):
    Genres = models.CharField(max_length=100, null=True, blank=True)
    BookName= models.CharField(max_length=100, null=True, blank=True)
    Definition= models.CharField(max_length=100, null=True, blank=True)
    Price=models.IntegerField(null=True,blank=True)
    Book_Image=models.ImageField(upload_to="Book_Image",null=True,blank=True)