from django.db import models
from django.utils.timezone import now
from PIL import Image
from django.utils.text import slugify
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
   name = models.CharField(max_length=50)
   phone = models.CharField(max_length=50)
   content = models.TextField()
   def __str__(self):
      return self.name
class Subject(models.Model):
   name = models.CharField(max_length=100)
   def __str__(self):
      return self.name
   
class Class_in(models.Model):
   name = models.CharField(max_length=100)
   def __str__(self):
      return self.name
   
class post(models.Model):
   CATAGORY = (
      ('Student','Student'),
      ('Teacher','Teacher'),
   )
   MEDIUM = (
      ('Bangla','Bangla'),
      ('English','English'),
      ('Hindi','Hindi'),
   )
   user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='post_set',blank=True,null=True)
   id = models.AutoField(primary_key=True)
   title = models.CharField(max_length=100)
   slug = models.CharField(max_length=50,default=title)
   email = models.EmailField(max_length=254)
   salary = models.FloatField()
   details = models.TextField()
   available = models.BooleanField()
   catagory= models.CharField(max_length=50, choices=CATAGORY)
   created_at = models.DateTimeField(default=now)
   image = models.ImageField(default='default.jpg', upload_to='tuition/images')
   medium = MultiSelectField(max_length=255,default='English',max_choices=3,choices=MEDIUM)
   subject = models.ManyToManyField(Subject,related_name='subject_set')
   class_in = models.ManyToManyField(Class_in,related_name='class_set')
   def save(self,*args, **kwargs):
      self.slug = slugify(self.title)
      super(post,self).save(*args, **kwargs)
      img = Image.open(self.image.path)
      if img.height > 300 or img.width>300:
         img_size=(300,300)
         img.thumbnail(img_size)
         img.save(self.image.path)
