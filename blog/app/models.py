from django.db import models

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name=models.CharField(max_length=40)
    email=models.CharField(max_length=100)
    content=models.TextField()

    def __str__(self):
        return self.name
    

class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    content=models.TextField()
    author=models.CharField(max_length=20)
    slug=models.CharField(max_length=200)

    def __str__(self):
        return self.titles