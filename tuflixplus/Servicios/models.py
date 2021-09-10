from django.db import models

# Create your models here.

# Coneción CRUD de la app

class Musician(models.Model):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    salary = models.IntegerField()


class Album(models.Model):
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=180)
    genero = models.CharField(max_length=50)
    fecha_pub = models.DateField()
    caratula = models.ImageField(null=True, blank=True)


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    duaracion = models.TimeField()

class Categoria(models.Model):
    pass 
