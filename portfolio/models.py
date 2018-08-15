from django.db import models

# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    image=models.ImageField()
    created=models.DateTimeField(auto_now_add=True) #al atribut es guarda la data de creacio del objecte de manera automatica
    updated=models.DateTimeField(auto_now=True) #al atribut es guarda la data de la ultima modificacio del object

