from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from tinymce.models import HTMLField


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = HTMLField()
    image = models.ImageField(upload_to='pic_folder/',default='pic_folder/None/no-img.jpg')
    created_on = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now =True)
    categories = models.ManyToManyField('Category', related_name = 'posts')
    def __str__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70,blank=True, null= True, unique= True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add =True)
    post = models.ForeignKey("Post", on_delete = models.CASCADE)
    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70,blank=True, null= True, unique= True)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    message = models.TextField()
    def __str__(self):
        return self.name
