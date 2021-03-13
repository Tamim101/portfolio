from django.db import models

# Create your models here.
class blog(models.Model):
    image = models.ImageField(upload_to='Image')
    facebook = models.CharField(max_length=100,blank=True,null=False)
    instagram = models.CharField(max_length=100,blank=True,null=False)
    twitter = models.CharField(max_length=100,blank=True,null=False)
    linklind = models.CharField(max_length=100,blank=True,null=False)

    def __str__(self):
        return self.facebook


class about(models.Model):
    profisson = models.CharField(max_length=100,blank=True,null=False)
    description = models.TextField(max_length=100,blank=True,null=False)
    image = models.ImageField(upload_to='Image')

    def __str__(self):
        return self.profisson

class portfilio(models.Model):
    image1 = models.ImageField(upload_to='Image')
    image2 = models.ImageField(upload_to='Image')
    image3 = models.ImageField(upload_to='Image')

class email(models.Model):
    name = models.CharField(max_length=100,blank=True,null=False)
    email = models.EmailField(max_length=200,blank=True,null=False)
    note = models.CharField(max_length=100,blank=True,null=False)

    def __str__(self):
        return self.name
