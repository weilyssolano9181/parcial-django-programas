from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    age = models.IntegerField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} {self.last_name}"

class Programa(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=150)
    estado = models.BooleanField(default=True)
    facultad = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"