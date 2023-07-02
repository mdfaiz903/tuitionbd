from django.db import models
from django.utils.timezone import now
# Create your models here.
class Contact(models.Model):
   name = models.CharField(max_length=50)
   phone = models.CharField(max_length=50)
   content = models.TextField()
   def __str__(self):
      return self.name
   
class post(models.Model):
   CATAGORY = (
      ('Student','Student'),
      ('Teacher','Teacher'),
   )
   id = models.AutoField(primary_key=True)
   title = models.CharField(max_length=100)
   slug = models.CharField(max_length=50,default='title')
   email = models.EmailField(max_length=254)
   salary = models.FloatField()
   details = models.TextField()
   available = models.BooleanField()
   catagory= models.CharField(max_length=50, choices=CATAGORY)
   created_at = models.DateTimeField(default=now)